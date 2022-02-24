from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_match, name="location_match"),
]
