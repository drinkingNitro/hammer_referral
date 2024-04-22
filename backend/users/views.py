from time import sleep

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import PhoneAuthenticationForm, VerifyAuthenticationForm
from .models import ReferalLink
from .services import get_referal_data


def login_view(request):
    if request.method == 'POST':
        form = PhoneAuthenticationForm(request.POST)
        if form.is_valid():
            sleep(1)  # sending sms
            request.session['phone_number'] = form.cleaned_data.get('phone_number')
            return redirect(reverse('users:verify'))
    else:
        form = PhoneAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def verify_view(request):
    if request.method == 'POST':
        form = VerifyAuthenticationForm(request.POST)
        if form.is_valid():
            phone_number = request.session.get('phone_number')
            user = authenticate(request, phone_number=phone_number)
            if user:
                login(request, user)
                # request.session.clear()
                return redirect(reverse('users:profile'))
    else:
        form = VerifyAuthenticationForm()
    return render(request, 'verify.html', {'form': form})


@login_required(login_url='/users/login')
def profile_view(request):
    user = request.user
    invited_by_phone_number, invited_list = get_referal_data(user)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, 'Profile updated successfully')
    return render(request, 'profile.html', {
        'user': user,
        'inviter': invited_by_phone_number,
        'invited': invited_list
        })


def logout_view(request):
    request.session.clear()
    return redirect('users:login')


def code_activate_view(request):
    user = request.user
    User = get_user_model()
    if request.method == 'POST':
        have_activated, _ = get_referal_data(user)
        if have_activated:
            raise ValidationError('You already have one activated invite code.')
        referral_code = request.POST.get('code')
        if referral_code == user.personal_invite_code:
            raise ValueError('Do not use your code for yourself.')
        try:
            inviter = User.objects.get(personal_invite_code=referral_code)
            if inviter:
                ReferalLink.objects.create(inviter=inviter, invited=user)
        except User.DoesNotExist:
            raise ValueError('The code is wrong. Check it and submit again.')
        return redirect('users:profile')
