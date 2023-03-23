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
        income_input = int(request.POST['income'])
        payment_input = int(request.POST['payment'])
        experience_input = int(request.POST['experience'])
        age_input = int(request.POST['age'])

        result_approve, credit_ability_value, credit_ability = fuzzy_result(income_input, payment_input,
                                                                            experience_input, age_input)
        fig = plot_credit(credit_ability, credit_ability_value)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        context = {
            'approve': result_approve,
            'plot': uri
        }

        return render(request, 'index.html', context)

