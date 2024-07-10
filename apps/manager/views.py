from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from services.models import Budgets

def list_budgets(request: HttpRequest) -> HttpResponse:
    budgets = Budgets.objects.all()
    return render(request, 'list_budgets.html', {'budgets': budgets})
