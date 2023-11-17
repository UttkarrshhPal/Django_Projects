from django.urls import path
from . import views

urlpatterns = [
    path("", views.add),
    path("add2nos", views.addition)
]
