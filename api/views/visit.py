from api.models import Visit
from rest_framework import mixins, filters, status
from api.mixin import HospitalGenericViewSet
from api.serializers.visit import VisitCreateSerializer, VisitRetrieveSerializer, VisitUpdateSerializer, \
    VisitListSerializer, VisitRatingSerializer
from rest_framework.response import Response


class VisitView(
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
            self.action_permissions = ['view_visit']
        elif self.action == 'create':
            self.action_permissions = ['add_visit', ]
        elif self.action == 'update':
            self.action_permissions = ['change_visit', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_visit', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'update':
            return VisitUpdateSerializer
        if self.action == 'set_rating':
            return VisitRatingSerializer

    def get_queryset(self):
        return Visit.objects.all()

    def set_rating(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
