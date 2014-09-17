# -*- coding: utf-8 -*-

from django.db.models import F

from souche.apps.carsouce.models import CarSource
from souche.apps.utils.decorators import async


__all__ = [
    'record_car_source_access',
]


@async
def record_car_source_access(car_id):
    CarSource.objects.filter(pk=car_id).update(F('view_num') + 1)
