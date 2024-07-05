from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('validate_registration_data/', views.validate_registration_data, name="validate_registration_data"),
]
