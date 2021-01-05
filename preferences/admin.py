from django.contrib import admin

# Register your models here.
from preferences.models import Preferences

admin.site.register(Preferences)