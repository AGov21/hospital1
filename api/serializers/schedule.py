from rest_framework import serializers

from api.models import Schedule
from rest_framework.exceptions import ValidationError


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleCreateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_start
        ).exists

        if exists:
            raise ValidationError('У нас есть накладка')

    class Meta:
        model = Schedule
        fields = ['day_of_week', 'timestamp_start', 'timestamp_end']


class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day_of_week', 'timestamp_start', 'timestamp_end']
