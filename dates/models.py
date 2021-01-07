from django.db import models
from django.utils import timezone

from users.models import User
from preferences.models import Preferences, Dining, Entertainment, OutDoors, StayHome


class DatesNightModel(models.Model):
    # Only select one of the dating category FKs
    dining_category = models.ManyToManyField(
        Dining, null=True, blank=True
    )
    entertainment_category = models.ForeignKey(
        Entertainment, null=True, blank=True, on_delete=models.CASCADE
    )
    out_doors_category = models.ForeignKey(
        OutDoors, null=True, blank=True, on_delete=models.CASCADE
    )
    stay_home_category = models.ForeignKey(
        StayHome, null=True, blank=True, on_delete=models.CASCADE
    )

    users_one = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="one", null=True
    )

    users_two = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="two", null=True
    )

    location = models.CharField(max_length=100)

    when_date_time = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     date_activity = ""
    #     if self.dining_category != None:
    #         date_activity = "Dining - " + self.dining_category
    #     elif self.entertainment_category != None:
    #         date_activity = (
    #             "Entertainment - " + self.entertainment_category.entertainment_choices
    #         )
    #     elif self.out_doors_category != None:
    #         date_activity = "OutDoors - " + self.out_doors_category.outdoor_choices
    #     elif self.stay_home_category != None:
    #         date_activity = "StayHome - " + self.stay_home_category.stay_home_choices
    #     return f"{date_activity} with {self.users_one.username} and {self.users_two.username}"
