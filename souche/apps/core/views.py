# -*- coding: utf-8 -*-

from django.views.generic import TemplateView



__all__ = [
    'IndexView',
    'SearchCarView',
    'CarInfoView',
]


class IndexView(TemplateView):
    ''' Index view for souche project.'''

    template_name = 'index.html'

class SearchCarView(TemplateView):
    template_name = 'search_car.html'
    
class CarInfoView(TemplateView):
    template_name = 'car_info.html'