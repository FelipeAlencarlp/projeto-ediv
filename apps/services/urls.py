from django.urls import path
from . import views

urlpatterns = [
    #/services/request_budget/
    path('request_budget/', views.BudgetRequestView.as_view(), name='request_budget'),
]
