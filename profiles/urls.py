from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name="profile"),
    path('create-profile/', views.ProfileCreateView.as_view(), name="create-profile"),
    path('profile-detail/<pk>/', views.ProfileUpdateView.as_view(), name="profile-update"),
    path('profile-detail/<pk>/', views.ProfileDetailView.as_view(), name="profile-detail"),
    path('deleteprofile/<pk>/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]
