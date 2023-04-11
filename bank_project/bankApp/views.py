import base64
import io
import urllib

from django import views
from django.shortcuts import render, HttpResponseRedirect

from .fuzzy_logic import fuzzy_result, plot_credit
from .models import Service, Transaction
from .associated_rules import recommendation_items


class BaseView(views.View):
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        context = {
            'services': services,
            'service_client': ''
        }
        return render(request, 'index.html', context=context)


class FuzzyView(views.View):

    def post(self, request, *args, **kwargs):
        try:
            fio = request.POST['fio']
            income_input = int(request.POST['income'])
            payment_input = int(request.POST['payment'])
            experience_input = int(request.POST['experience'])
            age_input = int(request.POST['age'])
            cred_sum = int(request.POST['sum_credit'])
        except Exception as E:
            print(E)
            return HttpResponseRedirect('/')

        payment_input = payment_input * 100 / cred_sum

        #нечеткий вывод
        result_approve, credit_ability_value, credit_ability, income, payment, \
        experience, age = fuzzy_result(income_input, payment_input, experience_input, age_input)
        fig = plot_credit(credit_ability, credit_ability_value)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        context = {
            'approve': result_approve,
            'plot': uri,
            'income': income,
            'payment': payment,
            'experience': experience,
            'age': age,
            'income_input': income_input,
            'experience_input': experience_input,
            'age_input': age_input,
            'payment_input': int(payment_input),
            'fio': fio,
            'services': Service.objects.all()
        }

        return render(request, 'index.html', context)


class AssociatedView(views.View):

    def post(self, request, *args, **kwargs):
        service_client = request.POST['service']
        transactions_all = Transaction.objects.all()
        transactions_list = []
        for transaction in transactions_all:
            transactions_list.append(transaction.services_in_transaction())
        result_items = recommendation_items(transactions_list, service_client)

        context = {
            # 'n': len(result_items.keys()),
            'recom_items': result_items,
            'services': Service.objects.all(),
            'service_client': service_client
        }
        return render(request, 'index.html', context=context)


