from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp
from django.db.models.signals import post_save
from ..user.models import Account


class Manager(StrictTimestamp):
    account = models.OneToOneField('Account', blank=False)
    dob = models.DateField(blank=True, null=True)

    def create_manager(sender,weak=False,**kwargs):
        if kwargs['created']:
            user_type = kwargs['instance'].user_type
            if user_type == 'MN':
                manager = Manager.objects.create(account=kwargs['instance'])

    post_save.connect(create_manager, sender=Account,)

    class Meta:
        verbose_name = _('manager')
        verbose_name_plural = _('managers')

    def __str__(self):
        return "<Manager firstname={} lastname={}>".format(self.account.firstname, self.account.lastname)