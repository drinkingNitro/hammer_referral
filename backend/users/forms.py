from django import forms
from django.utils.translation import gettext_lazy as _


class PhoneAuthenticationForm(forms.Form):
    phone_number = forms.CharField(label=_("Phone number"), max_length=20)


class VerifyAuthenticationForm(forms.Form):
    verification_code = forms.CharField(label=_("Code"), max_length=4)
