import base64
import io
import urllib

from django import views
from django.shortcuts import render, HttpResponseRedirect

from .fuzzy_logic import fuzzy_result, plot_credit


class BaseView(views.View): #рендеринг главной страницы

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

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
            'fio': fio
        }

        return render(request, 'index.html', context)

