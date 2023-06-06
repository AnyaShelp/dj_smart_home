from django.contrib import admin
from .models import Sensor, Temp

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

@admin.register(Temp)
class TempAdmin(admin.ModelAdmin):
    pass

