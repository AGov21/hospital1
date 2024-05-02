from api.mixin import HospitalGenericViewSet
from api.models import Doctor, Patient
from api.serializers.doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorUpdateSerializer, \
    DoctorCreateSerializer
from api.serializers.patient import PatientListSerializer
from rest_framework import mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import DoctorFilterSet


class DoctorView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor']
        elif self.action == 'list_patient':
            self.action_permissions = ['vies_patient']
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.prefetch_related(
                'visits'
            ).all()

        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)
