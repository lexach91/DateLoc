from django.db import models
from django.contrib.auth.models import User

from profiles.models import UserProfile


class Locations(models.Model):
    name = models.CharField(max_length=254)
    liked_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Location_Match(models.Model):
    """
    Model to match users location
    """
    match = models.ManyToManyField('self')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='match')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='matched')
    location = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='location')

    def __str__(self):
        return self.match
