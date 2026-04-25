from rest_framework import serializers
from .models import IoTNode, Sensor, Actuator


class IoTNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTNode
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = '__all__'