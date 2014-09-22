# -*- coding: utf-8 -*-

from functools import partial

from django import forms

from souche.apps.carsource.validators import validate_phone_number


__all__ = [
    'MobilePhoneField',
]


MobilePhoneField = partial(
    forms.CharField,
    max_length=20,
    validators=[validate_phone_number, ]
)

