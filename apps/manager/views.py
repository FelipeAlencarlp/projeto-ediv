from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rolepermissions.decorators import has_role_decorator
from services.models import Budgets

@has_role_decorator('editor')
def list_budgets(request: HttpRequest) -> HttpResponse:
    budgets = Budgets.objects.all()
    return render(request, 'list_budgets.html', {'budgets': budgets})
