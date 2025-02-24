from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Pizza

def deliccita_app (request):
    pizzas = Pizza.objects.all()
    return render(request, "myfirst.html", {"pizzas": pizzas})

def register_view (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('deliccita_app')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'deliccita_app/login.html', {'form': form})


# Create your views here.