# -*- coding: utf-8 -*-

from souche.apps.carmodel.rules import CLASSIFICATION_NAMES



def rules(request):
    context = {}
    context.update(CLASSIFICATION_NAMES)
    return context
