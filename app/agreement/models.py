from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from django.db import models

from ..core.models import StrictTimestamp

from ..property.models import Property
from ..tenant.models import Tenant
from ..unit.models import Unit


class Agreement(StrictTimestamp):
    tenant = models.ForeignKey(Tenant, on_delete=None)
    unit = models.ForeignKey(Unit, on_delete=None)
    property = models.ForeignKey(Property, on_delete=None)
    tittle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount_regex = RegexValidator(regex=r'^\+?1?\d{1,20}$',
                                  message="Amount must be entered in the format: '10000'. Up to 20 digits allowed.")
    deposit_amount = models.CharField(validators=[amount_regex], max_length=20, blank=False)
    rent_amount = models.CharField(validators=[amount_regex], max_length=20, blank=False)
    RENT_PAYMENT_TYPE = (
        ('DY', 'Days'),
        ('MN', 'Months'),
        ('WK', 'Weeks'),
        ('YR', 'Years'),
    )
    day_to_pay_rent = models.IntegerField(blank=False)
    rent_payment_type = models.CharField(choices=RENT_PAYMENT_TYPE, blank=False, max_length=10)
    rent_start_date = models.DateField(blank=False)


    class Meta:
        verbose_name = _('agreement')
        verbose_name_plural = _('agreements')

    def __str__(self):
        return "<Agreement tittle={} tenant={} >".format (self.tittle, self.tenant)