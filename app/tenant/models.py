from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from ..core.models import StrictTimestamp
from django.db.models.signals import post_save
from ..user.models import Account



class Tenant(StrictTimestamp):
    account = models.OneToOneField(Account, blank=False)

    def create_tenant(sender,weak=False,**kwargs):
        if kwargs['created']:
            user_type = kwargs['instance'].user_type
            if user_type == 'TN':
                tenant = Tenant.objects.create(account=kwargs['instance'])

    post_save.connect(create_tenant, sender=Account,)

    class Meta:
        verbose_name = _('tenant')
        verbose_name_plural = _('tenant')

    def __str__(self):
        return "<Tenant firstname={} lastname={}>".format(self.account.firstname, self.account.lastname)