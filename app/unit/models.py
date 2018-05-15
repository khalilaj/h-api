from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ..core.models import StrictTimestamp

from ..property.models import Property

class Unit(StrictTimestamp):
    property = models.ForeignKey(Property, on_delete=None, blank=False)
    name = models.CharField(max_length=30, blank=False)
    no_of_bed = models.IntegerField()
    no_of_bathroom = models.IntegerField()
    status = models.BooleanField(blank=False)

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')

    def __str__(self):
        return "<Unit name={} no_of_beds={}>".format(self.name, self.no_of_bed)