from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp

from ..tenant.models import Tenant
from ..property.models import Property


class Message(StrictTimestamp):
    tenant = models.ForeignKey(Tenant, on_delete=None, default=None)
    property = models.ForeignKey(Property, on_delete=None, blank=False)
    tittle = models.CharField(max_length=100)
    message = models.TextField(max_length=500,blank=False)
    response = models.TextField(max_length=500,blank=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('message')

    def __str__(self):
        return "<Message tittle={} >".format(self.tittle)
