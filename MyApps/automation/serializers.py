from rest_framework import serializers
from .models import (
    AutomationSetting,
    LightingStatus,
    AlarmStatus,
    RemoteCommand,
    CommandResponse
)


class AutomationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomationSetting
        fields = '__all__'


class LightingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightingStatus
        fields = '__all__'


class AlarmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmStatus
        fields = '__all__'


class RemoteCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteCommand
        fields = '__all__'


class CommandResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandResponse
        fields = '__all__'