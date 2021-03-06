from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from preferences.models import Preferences, Dining, Entertainment, OutDoors, StayHome


class User(AbstractUser):
    """Creates a new user with username and password created through the
    AbstractUser funcitonality. Signup forms will ask for the fullname,
    email, and location.
    """

    full_name = models.CharField(blank=True, null=True, max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(blank=True, null=True, max_length=254)
    # the friends_list is setup to allow users to 'follow' one another
    # so they can add each other in the date model
    friends_list = models.ManyToManyField(
        "self", blank=True, symmetrical=False, related_name="friends"
    )
    # the date preferences model may need adjusted depending on future code
    # Instead of generic date preferences this would be 4 different fields 
    # example: dining_preferences = models.ManyToManyField("preferences.Dining")
    dining_preference = models.ManyToManyField(Dining, blank=True)
    entertainment_preference = models.ManyToManyField(
        Entertainment, blank=True
    )
    out_doors_preference = models.ManyToManyField(OutDoors, blank=True)
    stay_home_preference = models.ManyToManyField(StayHome, blank=True)
    # the location may be updated later to utilize a geolocation field
    location = models.CharField(blank=True, null=True, max_length=50)

    # upload image for user 
    picture = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'{self.full_name}'

