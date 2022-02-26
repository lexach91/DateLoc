from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class LookingFor(models.Model):
    class Meta:
        verbose_name_plural = 'Looking for'

    gender = models.CharField(max_length=254)

    def __str__(self):
        return self.gender

class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    bio = models.TextField(max_length=500, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    job_title = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    looking_for = models.ForeignKey('LookingFor', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user