from django.urls import path
from . import views

urlpatterns = [
    #/manager/list_budgets/
    path('list_budgets/', views.list_budgets, name='list_budgets'),
]
