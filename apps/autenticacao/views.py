from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .forms import RegisterUserForm

def register(request: HttpRequest) -> HttpResponse:
    register_form = RegisterUserForm()
    return render(request, 'register.html', {'register_form': register_form})

def validate_registration_data(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            return HttpResponse('salvo')

        return render(request, 'register.html', {'register_form': register_form})

