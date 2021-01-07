from django.db import models
from django.utils import timezone

from users.models import User
from preferences.models import Preferences


class DatesNightModel(models.Model):
	category = models.ForeignKey(Preferences, on_delete=models.CASCADE)

	users_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="one", null=True)

	users_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="two", null=True)

	location = models.CharField(max_length=100)

	when_date_time = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f'{self.category}'