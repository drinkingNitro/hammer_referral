from .models import ReferalLink


def get_referal_data(user):
    try:
        invited_by = ReferalLink.objects.get(invited=user)
    except ReferalLink.DoesNotExist:
        invited_by = None
    invited_by_phone_number = invited_by.inviter.phone_number if invited_by else None
    try:
        invited_persons = ReferalLink.objects.filter(inviter=user)
    except ReferalLink.DoesNotExist:
        invited_by = []
    invited_list = [instance.invited.phone_number for instance in invited_persons]
    
    return invited_by_phone_number, invited_list
