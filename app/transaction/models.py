from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from django.db import models

from ..tenant.models import Tenant
from ..property.models import Property
from ..unit.models import Unit
from ..core.models import StrictTimestamp


class Transaction(StrictTimestamp):
    name = models.CharField(max_length=100, blank=False)
    date_paid = models.DateField(blank=True)
    payer = models.ForeignKey(Tenant , on_delete=None, blank=False)
    amount_regex = RegexValidator(regex=r'^\+?1?\d{1,20}$',
                                  message="Amount must be entered in the format: '10000'. Up to 20 digits allowed.")
    amount_due = models.CharField(validators=[amount_regex], max_length=20, blank=False)
    amount_paid = models.CharField(validators=[amount_regex], max_length=20, blank=True, default=0)
    TRANSACTION_TYPE = (
        ('RN', 'rent'),
        ('SC', 'service charge'),
        ('DP', 'deposit'),
        ('MT', 'maintenance')
    )
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=20, blank=True)

    TRANSACTION_STATUS = (
        ('P', 'paid'),
        ('UN', 'unpaid')
    )
    transaction_status = models.CharField(choices=TRANSACTION_STATUS, max_length=20, blank=False)
    date_paid = models.CharField(blank=True, max_length=100)
    date_due = models.DateField(blank=False)
    property = models.ForeignKey(Property, blank=True, default=None, on_delete=None)
    unit = models.ForeignKey(Unit, blank=True, default=None, on_delete=None)

    class Meta:
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')

    def __str__(self):
        return "<Transaction name={} amount_paid={}>".format(self.name , self.payer)


