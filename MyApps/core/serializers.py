from rest_framework import serializers
from .models import Home, HomeZone, SensorReading, MotionEvent, SystemAlert


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class HomeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeZone
        fields = '__all__'


class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'


class MotionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionEvent
        fields = '__all__'


class SystemAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAlert
        fields = '__all__'