from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'display_name': 'Display Name',
            'image': 'Image',
            'bio': 'Bio',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'job_title': 'Job Title',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
        }