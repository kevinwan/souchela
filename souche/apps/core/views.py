# -*- coding: utf-8 -*-

from django.views.generic import TemplateView



__all__ = [
    'IndexView',
]


class IndexView(TemplateView):
    ''' Index view for souche project.'''

    template_name = 'index.html'

