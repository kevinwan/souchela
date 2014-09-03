# -*- coding: utf-8 -*-

from django.views.generic import TemplateView



__all__ = [
    'IndexView',
    'SearchCarView',
]


class IndexView(TemplateView):
    ''' Index view for souche project.'''

    template_name = 'index.html'

class SearchCarView(TemplateView):
    template_name = 'search_car.html'
