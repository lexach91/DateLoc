from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login_user"),
    path('home', views.logout_user, name="logout_user"),
    path('register_user', views.register_user, name="register_user"),
]