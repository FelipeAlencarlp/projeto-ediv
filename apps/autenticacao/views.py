from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model, login as login_auth, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from .forms import RegisterUserForm, AuthUserForm
from .decorators import not_authenticated

def register(request: HttpRequest) -> HttpResponse:
    register_form = RegisterUserForm()
    return render(request, 'register.html', {'register_form': register_form})

def validate_registration_data(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)

        if register_form.is_valid():
            new_form = register_form.save(commit=False)
            new_form.is_active = False
            new_form.save()

            messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso! Entre no seu e-mail e ative sua conta para acessar.')
            return redirect(reverse('login'))
        
        messages.add_message(request, messages.ERROR, 'Dados incorretos! Verifique e tente novamente.')
        return render(request, 'register.html', {'register_form': register_form})

def active_account(request: HttpRequest, uidb4, token):
    UserModel = get_user_model()
    uid = force_str(urlsafe_base64_decode(uidb4))
    user = UserModel.objects.filter(pk=uid)

    if (user := user.first()) and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        login_auth(request, user)
        messages.add_message(request, messages.SUCCESS, 'Sua conta foi ativa com sucesso.')
        return redirect(reverse('login'))
    
    messages.add_message(request, messages.ERROR, 'A url acessada não é valida!')
    return redirect(reverse('login'))

@not_authenticated
def login(request: HttpRequest):
    auth_form = AuthUserForm()
    return render(request, 'login.html', {'auth_form': auth_form})

def validate_login_data(request: HttpRequest):
    if request.method == 'POST':
        auth_form = AuthUserForm(request.POST)

        if auth_form.is_valid():
            if auth_form.log_into(request):
                return redirect('/')

        return render(request, 'login.html', {'auth_form': auth_form})

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Você saiu do sistema, para acessar novamente entre com suas credências.')
    return redirect(reverse('login'))

