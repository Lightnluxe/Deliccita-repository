from django.urls import path
from . import views

urlpatterns = [
    path('deliccita_app/', views.deliccita_app, name='deliccita_app'),
    path("register/", views.register_view, name="register")
]