# -*- coding: utf-8 -*-

from django import template

from souche.apps.carmodel.models import Brand



register = template.Library()

@register.inclusion_tag('includes/models_of_brand.html', takes_context=False)
def show_models_of_brand(brand):
    if isinstance(brand, Brand):
        models = brand.get_models()
    else:
        models = Brand.get_models_by_brand_slug(brand)
    model_dic = {}
    for m in models:
        if m.manufactor in model_dic:
            model_dic[m.manufactor].append(m)
        else:
            model_dic[m.manufactor] = [m, ]

    return {'model_dic': model_dic}
