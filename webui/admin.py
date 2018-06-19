from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Feedback, UserMaintenance

admin.site.register((Feedback, UserMaintenance))