# -*- coding: utf-8 -*-

from django.core.cache import cache
from django.views.generic import View

from souche.apps.carmodel.models import Brand

from souche.apps.core.mixin import JSONResponseMixin


__all__ = [
    'BrandDataView',
]


class BrandDataView(View, JSONResponseMixin):
    ''' Get brand data.

    Request method: GET
    Parameters: None
    '''

    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        brands = cache.get('all_brands', None)
        if brands is None:
            brands = Brand.get_all_brands() \
                            .order_by('first_letter') \
                            .values('name', 'slug', 'first_letter')
            brands = list(brands)
            cache.set('all_brands', brands)
        return self.json_response({'data': brands})
