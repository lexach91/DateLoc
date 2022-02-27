from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('create-profile/', views.ProfileCreateView.as_view(), name="create-profile"),
    path('profile-detail/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile-update"),
    path('profile-detail/<int:pk>/', views.ProfileDetailView.as_view(), name="profile-detail"),
    path('deleteprofile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]
