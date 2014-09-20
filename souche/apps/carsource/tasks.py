# -*- coding: utf-8 -*-

from django.db.models import F

from souche.apps.carsource.models import CarSource
from souche.apps.utils.decorators import async


__all__ = [
    'record_car_source_access',
]


@async
def record_car_source_access(car_id):
    CarSource.objects.filter(pk=car_id).update(view_num=F('view_num')+1)


@async
def record_car_source_contrast(car_ids):
    if not (isinstance(car_ids, tuple) and isinstance(car_ids, list)):
        car_ids = (car_ids, )
    CarSource.objects.filter(pk__in=car_ids) \
                    .update(compare_num=F('compare_num')+1)
