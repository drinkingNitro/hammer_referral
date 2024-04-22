import random
import string

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .fields import PhoneNumberField
from .managers import PhoneUserManager


class PhoneUser(AbstractBaseUser):
    password = None
    first_name = models.CharField(_("first name"), max_length=150, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)

    phone_number = PhoneNumberField(_('Phone number'), unique=True)
    personal_invite_code = models.CharField(_('Personal invite code'), max_length=6)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = PhoneUserManager()

    def __str__(self):
        return self.phone_number


    @staticmethod
    def generate_personal_invite_code(length=6):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


    def set_personal_invite_code(self):
        self.personal_invite_code = self.generate_personal_invite_code()


class ReferalLink(models.Model):
    inviter = models.ForeignKey(PhoneUser, on_delete=models.CASCADE, related_name='invited_users')
    invited = models.ForeignKey(PhoneUser, on_delete=models.CASCADE, related_name='inviter_user')

    class Meta:
        unique_together = ('inviter', 'invited')
