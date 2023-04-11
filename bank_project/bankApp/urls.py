from django.urls import path

from .views import FuzzyView, AssociatedView, BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('fuzzy', FuzzyView.as_view(), name='fuzzy'),
    path('apriori', AssociatedView.as_view(), name='associated')
]