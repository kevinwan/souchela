# -*- coding: utf-8 -*-

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from souche.apps.carmodel.rules import CLASSIFICATION
from souche.apps.carmodel.rules import TRANSMISSION
from souche.apps.carmodel.models import Model

from souche.apps.carsource.mixin import CarCostDetailMixin
from souche.apps.carsource.models import CarSource




__all__ = [
    'CarSourceDetailView',
    'SearchCarView',
]



class SearchCarView(TemplateView, CarCostDetailMixin):
    ''' Search Car View.

    Request method: GET
    Parameters:
    -brand: brand slug.
    -model: model slug.
    -price: price range, e.g. 4-10, 0-5.
    -min_year: year min range.
    -max_year: year max range.
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
        min_year = get_param.get('min_year', '')
        max_year = get_param.get('max_year', '')
        classification = get_param.get('category', '')
        color = get_param.get('color', '')
        mile = get_param.get('mile', '')
        control = get_param.get('control', '')
        sort = get_param.get('sort', '-time')
        page = get_param.get('page', '')

        if brand:
            criteria.append(Q(brand_slug=brand))
        if model:
            criteria.append(Q(model_slug=model))
        if price:
            price_range = price.split('-')
            min_price, max_price = map(int, price_range)
            criteria.append(price__range=(min_price, max_price))
        if min_year:
            criteria.append(year__gte=min_year)
        if max_year:
            criteria.append(year__lte=max_year)
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
            control = TRANSMISSION.get(control, None)
            if control:
                query = Q()
                for con in control:
                    query = query | Q(control__icontains=con)
                criteria.append(query)
        if sort not in self.SORT_TYPE:
            sort = '-time'
        fields = ('pk', 'title', 'brand_slug', 'model_slug', 'detail_model_slug', \
                'year', 'month', 'url', 'time', 'mile', 'volume', 'control', 'price', \
                'price_bn', 'imgurls')
        cars = CarSource.objects.filter(*criteria).values(*fields).order_by(sort)

        for car in cars:
            if not car['price_bn']:
                detail_model = self.get_detail_model(car['model_slug'], \
                            car['detail_model_slug'], car['volume'], car['year'])
                car['price_bn'] = detail_model.price_bn
            car['total_cost'] = self.get_total_cost(car['price_bn'])
            car['save_money'] = self.get_save_money(car['total_cost'], car['price'])
            car['image_urls'] = car['imgurls'].split(' ')
        context.update({
            'cars': cars
        })

        return context


class CarSourceDetailView(TemplateView, CarCostDetailMixin):
    ''' Car source detail information.'''

    http_method_names = ['get', ]
    template_name = 'car_info.html'

    def get_context_data(self, **kwargs):
        car_id = int(kwargs['car_id'])
        car = get_object_or_404(CarSource, pk=car_id)
        if not car.price_bn:
            detail_model = self.get_detail_model(car.model_slug, \
                        car.detail_model_slug, car.volume, car.year)
            car.price_bn = detail_model.price_bn
        car.tax = self.get_purchase_tax(car.price)
        car.total_cost = self.get_total_cost(car.price_bn, car.tax)
        car.save_money = self.get_save_money(car.total_cost, car.price)
        car.image_urls = car.imgurls.split(' ')
        return {'car': car}

