# -*- coding: utf-8 -*-

from souche.apps.carmodel.constants import CLASSIFICATION_NAMES



def rules(request):
    context = {}
    context.update(CLASSIFICATION_NAMES)
    return context
