from django.urls import path
from . import views
urlpatterns = [
    path('',views.Addition),
    path('add2nos',views.add_logic)
]
