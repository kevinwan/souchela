# -*- coding: utf-8 -*-

from souche.apps.carmodel.rules import CLASSIFICATION_NAMES
from souche.apps.carmodel.rules import TRANSMISSION_NAMES



def rules(request):
    context = {}
    context.update(CLASSIFICATION_NAMES)
    context.update(TRANSMISSION_NAMES)
    return context
