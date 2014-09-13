# -*- coding: utf-8 -*-

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from souche.apps.carmodel.rules import CLASSIFICATION
from souche.apps.carmodel.models import Model

from souche.apps.carsource.models import CarSource



__all__ = [
    'CarSourceDetailView',
    'SearchCarView',
]



class SearchCarView(TemplateView):
    ''' Search Car View.

    Request method: GET
    Parameters:
    -brand: brand slug.
    -model: model slug.
    -price: price range, e.g. 4-10, 0-5.
    -year: year range, e.g. 2009-2012.
    -category: car category => classification.
    -color: color Chinese.
    -mile: mileage range, e.g. 0-5.
    -control: control type of car, e.g. 手动, 自动.
    -sort: sort type, e.g.
    -page: page number of pagination.
    '''

    http_method_names = ['get', ]
    template_name = 'search_car.html'
    SORT_TYPE = ('price', '-price', 'mile', '-mile', 'time', '-time')

    def get_context_data(self, **kwargs):
        context = {}
        get_param = self.request.GET.copy()
        criteria = []
        brand = get_param.get('brand', '')
        model = get_param.get('model', '')
        price = get_param.get('price', '')
        year = get_param.get('year', '')
        classification = get_param.get('category', '')
        color = get_param.get('color', '')
        mile = get_param.get('mile', '')
        control = get_param.get('control', '')
        sort = get_param.get('sort', '-time')
        page = get_param.get('page', '')

        if brand:
            criteria.append(Q(brand=brand))
        if model:
            criteria.append(Q(model=model))
        if price:
            price_range = price.split('-')
            min_price, max_price = map(int, price_range)
            criteria.append(price__range=(min_price, max_price))
        if year:
            year_range = year.split('-')
            min_year, max_year = map(int, year_range)
            criteria.append(year__range=(min_year, max_year))
        classifications = CLASSIFICATION.get(classification, '')
        if classifications:
            # TODO(jzhu): Need to refactor the classification filter and model filter.
            models = Model.get_models_by_classification(classifications)
            criteria.append()
        if color:
            criteria.append(Q(color=color))
        if mile:
            mile_range = mile.split('-')
            min_mile, max_mile = map(int, mile_range)
            criteria.append(Q(mile__range=(min_mile, max_mile)))
        if control:
            criteria.append(Q(control=control))
        if sort not in self.SORT_TYPE:
            sort = '-time'
        cars = CarSource.objects.filter(*criteria).order_by(sort)

        context.update({
            'cars': cars
        })

        return context


class CarSourceDetailView(TemplateView):
    ''' Car source detail information.'''

    http_method_names = ['get', ]
    template_name = 'car_info.html'

    def get_context_data(self, **kwargs):
        car_id = int(kwargs['car_id'])
        car = get_object_or_404(CarSource, pk=car_id)

        return {'car': car}

