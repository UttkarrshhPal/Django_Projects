from django.urls import path
from . import views

urlpatterns = [
    path("", views.sub),
    path("sub2nos", views.subtract)
]
