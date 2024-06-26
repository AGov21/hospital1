import datetime

from api.models import Visit


def get_upcoming_visits_count():
    return Visit.objects.filter(
        schedule__timestamp_start__gte=datetime.datetime.now()
    ).coun