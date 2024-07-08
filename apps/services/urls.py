from django.urls import path
from . import views

urlpatterns = [
    #/services/request_budget/
    path('request_budget/', views.request_budget, name='request_budget'),
]
