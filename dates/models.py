from django.db import models

from users.models import User
from preferences.models import Preferences


class DatesNightModel(models.Model):
	users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", null=True)

	category = models.ForeignKey(Preferences, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.users}'