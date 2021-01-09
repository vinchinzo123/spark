from django.contrib import admin

# Register your models here.
from preferences.models import Preferences, StayHome, Entertainment, Dining, OutDoors

admin.site.register(Preferences)
admin.site.register(StayHome)
admin.site.register(Entertainment)
admin.site.register(Dining)
admin.site.register(OutDoors)