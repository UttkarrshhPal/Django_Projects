from django.urls import path
from . import views

urlpatterns = [
    path("", views.div),
    path("div2nos", views.division)
]
