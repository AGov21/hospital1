from api.models import Schedule
from rest_framework import mixins, filters
from api.mixin import HospitalGenericViewSet
from api.serializers import ScheduleListSerializer, ScheduleRetrieveSerializer, ScheduleCreateSerializer, \
    ScheduleUpdateSerializer


class ScheduleView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin
):
    lookup_field = 'id'

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_schedule']
        elif self.action == 'create':
            self.action_permissions = ['add_schedule', ]
        elif self.action == 'update':
            self.action_permissions = ['change_schedule', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_schedule', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        if self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        if self.action == 'create':
            return ScheduleCreateSerializer
        if self.action == 'update':
            return ScheduleUpdateSerializer

    def get_queryset(self):
        return Schedule.objects.all()
