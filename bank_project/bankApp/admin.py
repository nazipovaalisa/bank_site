from django.contrib import admin
from django import forms
from .models import *


class ServicesInLine(admin.TabularInline):

    model = Transaction.services.through


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    inlines = [ServicesInLine]
    exclude = ('services', )
    list_display = ('id', 'date_transaction')
    list_filter = ('date_transaction', )
    ordering = ('date_transaction', )


admin.site.register(Service)



