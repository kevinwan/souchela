# -*- coding: utf-8 -*-

from django.db import models

from functools import partial


__all__ = [
    'MileageField',
    'PriceField',
    'VolumeField',
]

PRICE_MAX_DIGITS = 5
PRICE_DECIMAL_PLACES = 2
VOLUME_MAX_DIGITS = 5
VOLUME_DECIMAL_PLACES = 1
MILEAGE_MAX_DIGITS = 5
MILEAGE_DECIMAL_PLACES = 2


PriceField = partial(
        models.DecimalField,
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        help_text=u'价格最大位数为5位，最多小数为2位')


VolumeField = partial(
        models.DecimalField,
        max_digits=VOLUME_MAX_DIGITS,
        decimal_places=VOLUME_DECIMAL_PLACES,
        help_text=u'排量最大位数为5位，最多小数为1位')


MileageField = partial(
        models.DecimalField,
        max_digits=MILEAGE_MAX_DIGITS,
        decimal_places=MILEAGE_DECIMAL_PLACES,
        help_text=u'里程最大位数为5位，最多小数为1位')
