from django import forms


class FuzzyFrom(forms.Form):
    income = forms.CharField()
    payment = forms.IntegerField()
    experience = forms.IntegerField()
    age = forms.IntegerField()