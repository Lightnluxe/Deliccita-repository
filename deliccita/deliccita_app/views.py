from django.shortcuts import render
from .models import Pizza

def deliccita_app (request):
    pizzas = Pizza.objects.all()
    return render(request, "myfirst.html", {"pizzas": pizzas})

# Create your views here.