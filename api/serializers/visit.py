from django.core.exceptions import ValidationError
from rest_framework import serializers
from api.models import Visit, Schedule


class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):

    def validate_schedule(self, value):
        visit_count = value.visits.count()
        if 3 <= visit_count:
            raise ValidationError('Превышено максимальное количество мест')
        return value

    class Meta:
        model = Visit
        fields = ['patient', 'service', 'schedule', 'status']


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['service', 'schedule']


class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Visit
        fields = ['rating']

