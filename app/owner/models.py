from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp
from ..property.models import Property


class Owner(StrictTimestamp):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=True)
    national_id_regex = RegexValidator(regex=r'^\+?1?\d{8,8}$',
                                       message="National id must be entered in the format: '33335501'. Up to 8 digits allowed ")
    national_id = models.CharField(validators=[national_id_regex], max_length=8, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$',
                                 message="Phone number must be entered in the format: '07123456789'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    dob = models.DateField(blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=None, blank=False)

    class Meta:
        verbose_name = _('owner')
        verbose_name_plural = _('owners')

    def __str__(self):
        return "<Owner firstname={} lastname={}>".format(self.firstname, self.lastname)



