from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    A user profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    bio = models.TextField(max_length=500, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    job_title = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username
