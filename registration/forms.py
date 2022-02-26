from django import forms
from .models import UserRegistration, LookingFor


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
