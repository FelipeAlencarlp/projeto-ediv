from typing import Callable
from django.http import HttpRequest
from django.shortcuts import redirect

def not_authenticated(f: Callable, redirect_url: str='/'):

    def _wraper(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_url)
        return f(request, *args, **kwargs)

    return _wraper

