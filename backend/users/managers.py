from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class PhoneUserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        """
        Create and save a user with the given phone_number and password. Assign personal invite code.
        """
        if not phone_number:
            raise ValueError(_("The phone_number must be set"))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_personal_invite_code()
        user.save()
        return user
