from django.db import models

# Create your models here.
class Notification(models.Model):
    user1 = models.ForeignKey(
        "users.User", related_name="user1", on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        "users.User", related_name="user2", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Notification: {self.pk} for {self.user1.username} and {self.user2.username}"
