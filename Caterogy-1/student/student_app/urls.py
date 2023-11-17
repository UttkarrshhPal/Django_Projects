from django.urls import path
from . import views

urlpatterns = [
    path('Student_details',views.my_view1),
]