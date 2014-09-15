# -*- coding: utf-8 -*-

from souche.apps.carmodel.rules import CLASSIFICATION_NAMES
from souche.apps.carmodel.rules import TRANSMISSION_NAMES
from souche.apps.carmodel.rules import HOT_BRAND



def rules(request):
    context = {}
    context.update(CLASSIFICATION_NAMES)
    context.update(TRANSMISSION_NAMES)
    context.update(HOT_BRAND)
    return context
