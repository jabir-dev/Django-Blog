from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanici ve ya Parola yanlisdi")
            return render(request, "login.html", context)
        
        messages.success(request, "Basasri ile Giris yapdiniz")
        login(request, user)
        return HttpResponseRedirect("/articles/dashboard/")
    
    return render(request, "login.html", context)
