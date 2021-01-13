from django.db import models
from dates.models import DatesNightModel

# Create your models here.
class Notification(models.Model):
    date_night = models.ForeignKey(
        "dates.DatesNightModel", null=True, on_delete=models.CASCADE
    )
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
    STATUS_CHOICES = [
        ("Sent", "Sent"),
        ("Confirmed", "Confirmed"),
        ("Declined", "Declined"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Sent")

    def __str__(self):
        return f"Notification for: {self.date_night.__str__()} "
