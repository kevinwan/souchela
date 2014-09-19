# -*- coding: utf-8 -*-

import re
from operator import itemgetter

from django.conf import settings

from django.views.generic import TemplateView
from django.views.generic import View

from souche.apps.carsource.mixin import CarCostDetailMixin
from souche.apps.carsource.models import CarSource

from souche.apps.core.mixin import AJAXResponseMixin



__all__ = [
    'CarContrastPreviewListView',
    'CarContrastDetailView',
    'AddCarContrastView',
    'DeleteCarContrastView',
    'EmptyCarContrastView'
]



class CarContrastPreviewListView(TemplateView):
    ''' Get abstract of compare car list.

    Request method: GET
    '''

    http_method_names = ['get', ]
    template_name = 'compare_car_preview.html'

    def get_context_data(self, **kwargs):
        car_ids = self.request.session[settings.CAR_CONTRAST_SESSION_NAME]
        fields = ('pk', 'title', 'price', 'thumbnail')
        cars = CarSource.sale_cars.filter(pk__in=car_ids).values(*fields)
        car_amount = cars.count()
        for car in cars:
            car['priority'] = car_ids.index(str(car['pk']))
        cars = sorted(cars, key=itemgetter('priority'))
        context = {
            'contrast_cars': cars,
            'empty_cars': range(car_amount+1, settings.CAR_CONTRAST_AMOUNT+1)
        }

        return context


class CarContrastDetailView(TemplateView, CarCostDetailMixin):
    ''' Compare car detail page.

    Request method: GET
    '''

    http_method_names = ['get', ]
    template_name = 'compare_car.html'

    def get_context_data(self, **kwargs):
        context = {}
        car_contrast = self.request.session[settings.CAR_CONTRAST_SESSION_NAME]
        cars = CarSource.sale_cars.filter(pk__in=car_contrast)
        context.update({'contast_cars': cars})
        return context


class AddCarContrastView(View, AJAXResponseMixin):
    ''' Add compare car view.

    Request method: POST
    Parameters:
    -car_id: car source id.
    '''

    http_method_names = ['post', ]
    err_msg = {
        'params_error': u'参数错误',
        'car_contrast_amount_limit': u'车辆对比数量达到上限',
        'car_in_contrast': u'该二手车已经在对比车辆中',
        'car_not_exist': u'该二手车不存在或已下线'
    }

    def post(self, request, *args, **kwargs):
        context = {}
        car_id = request.POST.get('car_id', '')
        car_contrast = request.session[settings.CAR_CONTRAST_SESSION_NAME]
        if not re.match(r'\d+', car_id):
            self.update_errors(self.err_msg['params_error'])
        elif len(car_contrast) >= settings.CAR_CONTRAST_AMOUNT:
            self.update_errors(self.err_msg['car_contrast_amount_limit'])
        else:
            ret = self.add_car_contrast(request, car_id)
            context.update(ret)
        return self.ajax_response(context)

    def add_car_contrast(self, request, car_id):
        context = {}
        cars = CarSource.sale_cars.filter(pk=car_id)
        car_contrast = request.session[settings.CAR_CONTRAST_SESSION_NAME]
        if cars.exists():
            if car_id in car_contrast:
                context.update({'msg': self.err_msg['car_in_contrast']})
            else:
                car_contrast.append(car_id)
                request.session[settings.CAR_CONTRAST_SESSION_NAME] = car_contrast
                context.update({
                    'car_id': car_id
                })
        else:
            self.update_errors(self.err_msg['car_not_exist'])
        return context


class DeleteCarContrastView(View, AJAXResponseMixin):
    ''' Delete compare car view.

    Request method: POST
    '''

    http_method_names = ['post', ]
    err_msg = {
        'params_error': u'参数错误',
        'car_not_in_contrast': u'该二手车不在对比车辆中'
    }

    def post(self, request, *args, **kwargs):
        car_id = request.POST.get('car_id', '')
        if not re.match(r'\d+', car_id):
            self.update_errors(self.err_msg['params_error'])
        else:
            car_contrast = request.session[settings.CAR_CONTRAST_SESSION_NAME]
            if car_id in car_contrast:
                car_contrast.remove(car_id)
                request.session[settings.CAR_CONTRAST_SESSION_NAME] = car_contrast
            else:
                self.update_errors(self.err_msg['car_not_in_contrast'])
        return self.ajax_response()


class EmptyCarContrastView(View, AJAXResponseMixin):
    ''' Empty compare car view.

    Request method: POST
    '''

    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        request.session[settings.CAR_CONTRAST_SESSION_NAME] = []
        return self.ajax_response()

