from django.db import models
from dates.models import DatesNightModel

# Create your models here.
class Notification(models.Model):
    sent_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="sent_user",
        null=True,
    )
    received_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="received_user",
        null=True,
    )

    date_night = models.ForeignKey(
        "dates.DatesNightModel", null=True, on_delete=models.CASCADE
    )

    def __str__(self):
#         breakpoint()
        return f"Date: "
