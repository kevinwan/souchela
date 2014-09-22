# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator



__all__ = [
    'validate_phone_number',
]


PHONE_REGEX = r'^(13[0-9]|15[0-9]|18[0-9]|14[3579]|17[067])\d{8}$'


validate_phone_number = RegexValidator(
    regex=PHONE_REGEX,
    message=u'手机号码格式错误',
    code='invalid')
