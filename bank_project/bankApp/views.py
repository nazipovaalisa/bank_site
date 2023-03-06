from django.shortcuts import render
from django import views

class BaseView(views.View): #рендеринг главной страницы

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})
