from django.contrib import admin

from .tenant.models import Tenant
from .user.models import Account
from .manager.models import Manager
from .owner.models import Owner
from .property.models import Property
from .unit.models import Unit
from .agreement.models import Agreement
from .message.models import Message

from .transaction.models import Transaction

models = [ Account,
           Tenant,
           Manager,
           Owner,
           Property,
           Unit,
           Message,
           Agreement,
           Transaction,
]

admin.site.register(models)


