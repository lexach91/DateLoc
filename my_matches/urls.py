from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_matches, name="my_matches"),
    path('my_matches_in_location/<int:location_id>/', views.my_matches_in_location, name="my_matches_in_location")
]