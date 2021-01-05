from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    '''Creates a new user with username and password created through the
    AbstractUser funcitonality. Signup forms will ask for the fullname,
    email, and location.
    '''
    full_name = models.CharField(blank=True, null=True, max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(blank=True, null=True, max_length=254)
    # the friends_list is setup to allow users to 'follow' one another
    # so they can add each other in the date model
    friends_list = models.ManyToManyField('self', symmetrical=False, related_name='friends_list')
    # the date preferences model may need adjusted depending on future code
    date_preferences = models.ManyToManyField('preferences.Preferences', symmetrical=False, related_name='date_preferences')
    # the location may be updated later to utilize a geolocation field
    location = models.CharField(blank=True, null=True, max_length=50)
    
    def __str__(self):
        return self.name