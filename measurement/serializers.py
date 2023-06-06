from rest_framework import serializers
from .models import Sensor, Temp

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name', 'description', 'measurements']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ['sensor', 'temperature']
