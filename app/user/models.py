from __future__ import unicode_literals
from datetime import datetime ,timedelta
import jwt
import json

from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from ..core.models import StrictTimestamp


class AcountManager(BaseUserManager):

    def create_user(self, username, email, password, user_type, **kwargs):

        if username is None:
            raise ValueError("Username has not been provided")
        if email is None:
            raise ValueError("Username has not been provided")

        account = self.model(username=username, email=self.normalize_email(email),**kwargs)
        account.set_password(password)
        account.user_type = user_type
        account.save()
        print(account.id)
        return account

    def create_superuser(self, username, email, password):
       account = self.create_user(username, email, password, 'AD')

       if password is None:
           raise ValueError("Superuser must have a password")

       account.is_superuser = True
       account.is_staff = True
       account.save()


class Account(AbstractBaseUser,PermissionsMixin, StrictTimestamp):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True)

    firstname = models.CharField( max_length=30, blank=False)
    lastname = models.CharField( max_length=30, blank=False)
    national_id_regex = RegexValidator(regex=r'^\+?1?\d{8,8}$',
                                 message="National id must be entered in the format: '33335501'. Up to 8 digits allowed ")
    national_id = models.CharField(validators=[national_id_regex], max_length=8, blank=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                                 message="Phone number must be entered in the format: '07123456789'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)

    dob = models.DateField(blank=True, null=True)

    USER_TYPE = (
        ('TN', 'tenant'),
        ('MN', 'manager'),
        ('AD', 'admin'),

    )

    user_type = models.CharField(choices=USER_TYPE, blank=False, max_length=10)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=False)

    objects = AcountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __str__(self):
        return "<User firstname={} user_type={}>".format(self.firstname, self.user_type)

    def json(self):
        return json.dumps({"username": self.username,"email":self.email, "active": self.is_active})

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        fullname = '%s %s' % (self.firstname, self.lastname)
        return fullname.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.firstname

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def token(self):
        return self._tokenize()

    def _tokenize(self):
        stamp = datetime.utcnow() + timedelta(days=60)

        token = jwt.encode({
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'exp': stamp,
            'iat': datetime.utcnow()
        }, settings.SECRET_KEY, algorithm='HS256')


        return token

