from django.contrib import admin

from .models import *


class ElevatorAdmin(admin.AdminSite):
    model = Elevator


class ElevatorBlockAdmin(admin.ModelAdmin):
    model = ElevatorBlock


admin.site.register(ElevatorBlock, ElevatorBlockAdmin)
