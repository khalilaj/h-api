from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp


class Property(StrictTimestamp):
    name = models.CharField(max_length=30,blank=False)
    location = models.CharField(max_length=50,blank=False)
    year_of_completion = models.DateField(blank=False)

    class Meta:
        verbose_name = _('property')
        verbose_name_plural = _('properties')

    def __str__(self):
        return "<Property name={} location={}>".format(self.name, self.location)





