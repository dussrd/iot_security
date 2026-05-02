from rest_framework import serializers
from .models import (
    CITY_NEIGHBORHOODS,
    Home,
    HomeZone,
    SensorReading,
    MotionEvent,
    SystemAlert,
)


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        read_only_fields = ("country",)

    def validate(self, attrs):
        city = attrs.get("city", getattr(self.instance, "city", None))
        barrio = attrs.get("barrio", getattr(self.instance, "barrio", None))
        valid_neighborhoods = {
            neighborhood_key
            for neighborhood_key, _ in CITY_NEIGHBORHOODS.get(
                city,
                {"barrios": []},
            )["barrios"]
        }

        if barrio not in valid_neighborhoods:
            raise serializers.ValidationError(
                {"barrio": "El barrio seleccionado no pertenece a la ciudad."}
            )

        attrs["country"] = "Colombia"
        return attrs


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
