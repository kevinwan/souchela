# -*- coding: utf-8 -*-

from django.conf import settings as sys_settings

from souche.apps.carmodel.rules import CLASSIFICATION_NAMES
from souche.apps.carmodel.rules import TRANSMISSION_NAMES
from souche.apps.carmodel.rules import HOT_BRAND




def rules(request):
    context = {}
    context.update(CLASSIFICATION_NAMES)
    context.update(TRANSMISSION_NAMES)
    context.update(HOT_BRAND)
    return context


def settings(request):
    context = {
        'IMG_URL': sys_settings.IMG_URL,
        'SITE_INFO': sys_settings.SITE_INFO,
    }
    return context
