from django.urls import path

from .views import (code_activate_view, login_view, logout_view, profile_view,
                    verify_view)

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('verify/', verify_view, name='verify'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('code/', code_activate_view, name='code-activate'),
    ]
