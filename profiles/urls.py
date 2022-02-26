from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('create-profile/', views.ProfileCreateView.as_view(), name="create-profile"),
]
