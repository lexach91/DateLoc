from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_match, name="location_match"),
    path('<int:location_id>/', views.liked_location, name='liked_location'),
]
