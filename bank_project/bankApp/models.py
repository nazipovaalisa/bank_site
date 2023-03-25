from django.db import models


# услуги.
class Service(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название услуги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Transaction(models.Model):

    date_transaction = models.DateField(verbose_name='Дата транзакции')
    services = models.ManyToManyField(Service, blank=True, related_name='related_transactions', verbose_name='Услуги')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    #все услуги в транзакции
    def services_in_transaction(self):
        return [serv.name for serv in self.services.all()]

