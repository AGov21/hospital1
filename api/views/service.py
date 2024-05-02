from api.models import Service
from api.serializers.service import ServiceListSerializer, ServiceCreateSerializer, ServiceRetrieveSerializer, \
    ServiceUpdateSerializer
from rest_framework import mixins, viewsets


class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()
