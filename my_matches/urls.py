from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_matches, name="my_matches"),
]