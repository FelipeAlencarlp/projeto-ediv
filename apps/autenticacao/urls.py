from django.urls import path
from . import views

urlpatterns = [
    #/auth/register/
    path('register/', views.register, name='register'),
    #/auth/validate_registration_data/
    path('validate_registration_data/', views.validate_registration_data, name='validate_registration_data'),
    #/auth/active_account/xyz/xyz...
    path('active_account/<uidb4>/<token>/', views.active_account, name='active_account'),
    #/auth/login/
    path('login/', views.login, name='login'),
]
