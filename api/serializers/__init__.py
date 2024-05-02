from .doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorUpdateSerializer, DoctorCreateSerializer
from .patient import PatientListSerializer, PatientDetailedSerializer, PatientCreateOrUpdateSerializer
from .service import ServiceUpdateSerializer, ServiceCreateSerializer, ServiceRetrieveSerializer, ServiceListSerializer
from .visit import VisitCreateSerializer, VisitRetrieveSerializer, VisitUpdateSerializer, VisitListSerializer
from .schedule import ScheduleCreateSerializer, ScheduleListSerializer, ScheduleUpdateSerializer, \
    ScheduleRetrieveSerializer

