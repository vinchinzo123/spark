from django.contrib import admin

from dates.models import DatesNightModel, ActivityModel

admin.site.register(DatesNightModel)
admin.site.register(ActivityModel)