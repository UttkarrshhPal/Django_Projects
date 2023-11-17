from django.urls import path
from . import views
urlpatterns = [
    path('',views.multiply),
    path('mul2no',views.compute),
]