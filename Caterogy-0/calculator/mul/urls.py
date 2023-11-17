from django.urls import path
from . import views

urlpatterns = [
    path("", views.mul),
    path("mul2nos", views.multiplication)
]
