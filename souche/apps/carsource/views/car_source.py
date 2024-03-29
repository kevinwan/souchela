# -*- coding: utf-8 -*-

from datetime import date

from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.views.generic import TemplateView

from souche.apps.core.mixin import AJAXResponseMixin

from souche.apps.carmodel.models import Brand
from souche.apps.carmodel.models import ConfigParameter
from souche.apps.carmodel.models import Model
from souche.apps.carmodel.rules import CLASSIFICATION
from souche.apps.carmodel.rules import TRANSMISSION
from souche.apps.carmodel.rules import CAR_PARAMETERS
from souche.apps.carmodel.rules import CAR_CONFIGURATIONS

from souche.apps.carsource.forms import OrderCarForm
from souche.apps.carsource.mixin import CarDetailInfoMixin
from souche.apps.carsource.models import CarSource
from souche.apps.carsource.tasks import record_car_source_access


from souche.apps.utils.paginator import paginate




__all__ = [
    'CarSourceDetailView',
    'SearchCarView',
    'OrderCarView',
]



class SearchCarView(TemplateView, CarDetailInfoMixin):
    ''' Search Car View.

    Request method: GET
    Parameters:
    -brand: brand slug.
    -model: model slug.
    -price: price range, e.g. 4-10, 0-5.
    -year: year range, e.g. 2011-2014.
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
        model_dic = {}
        get_param = self.request.GET.copy()
        criteria = []
        filter_conditions = []
        brand = None
        model_zh = ""
        mile_zh = ""
        min_year = ""
        max_year = date.today().year
        brand_slug = get_param.get('brand', '')
        model_slug = get_param.get('model', '')
        price = get_param.get('price', '')
        year = get_param.get('year', '')
        classification = get_param.get('category', '')
        color = get_param.get('color', '')
        mile = get_param.get('mile', '')
        control = get_param.get('control', '')
        sort = get_param.get('sort', '-time')
        page = get_param.get('page', '')

        if brand_slug:
            brand = Brand.get_brand_by_slug(brand_slug)
            if brand:
                criteria.append(Q(brand_slug=brand_slug))
                model_dic = self.get_models_of_brand(brand)
                filter_conditions.append({
                    'condition': brand.name,
                    'slug': 'brand'
                })
        if brand and model_slug:
            model = Model.get_model_by_slug(brand, model_slug)
            if model:
                criteria.append(Q(model_slug=model_slug))
                model_zh = model.name
                filter_conditions.append({
                    'condition': model_zh,
                    'slug': 'model'
                })
        if price:
            price_range = price.split('-')
            min_price, max_price = map(int, price_range)
            criteria.append(Q(price__range=(min_price, max_price)))
            filter_conditions.append({
                'condition': u'{price}万'.format(price=price),
                'slug': 'price'
            })
        if year:
            year_range = year.split('-')
            min_year, max_year = map(int, year_range)
            criteria.append(Q(year__range=(min_year, max_year)))
            filter_conditions.append({
                'condition': year,
                'slug': 'year'
            })
        classifications = CLASSIFICATION.get(classification, '')
        if classifications:
            criteria.append(Q(classification__in=classifications))
            filter_conditions.append({
                'condition': classification,
                'slug': 'category'
            })
        if color:
            criteria.append(Q(color=color))
            filter_conditions.append({
                'condition': color,
                'slug': 'color'
            })
        if mile:
            mile_range = mile.split('-')
            min_mile, max_mile = map(int, mile_range)
            criteria.append(Q(mile__range=(min_mile, max_mile)))
            filter_conditions.append({
                'condition': u'{min_mile}-{max_mile}万公里'.format(\
                            min_mile=min_mile, max_mile=max_mile),
                'slug': 'mile'
            })
            mile_zh  = u'{max_mile}万公里以内'.format(max_mile=max_mile)
        if control:
            controls = TRANSMISSION.get(control, None)
            if controls:
                criteria.append(Q(control__in=controls))
            filter_conditions.append({
                'condition': control,
                'slug': 'control'
            })
        if sort not in self.SORT_TYPE:
            sort = '-time'
        fields = ('pk', 'title', 'brand_slug', 'model_slug', 'detail_model_slug', \
                'year', 'month', 'url', 'time', 'mile', 'volume', 'control', 'price', \
                'price_bn', 'imgurls')
        cars = CarSource.objects.filter(*criteria).values(*fields).order_by(sort)
        cars = paginate(cars, page, 10, 8)
        for car in cars.object_list:
            if not car['price_bn']:
                detail_model = self.get_detail_model(car['model_slug'], \
                            car['detail_model_slug'], car['volume'], car['year'])
                car['price_bn'] = detail_model.price_bn
            car['total_cost'] = self.get_total_cost(car['price_bn'])
            car['save_money'] = self.get_save_money(car['total_cost'], car['price'])
            car['image_urls'] = car['imgurls'].split(' ')
        context.update({
            'cars': cars,
            'amount': cars.paginator.count,
            'filter_conditions': filter_conditions,
            'brand': brand,
            'model_dic': model_dic,
            'sort': sort,
            'sort_type': self.SORT_TYPE[:-2],
            'model_zh': model_zh,
            'min_year': min_year,
            'max_year': max_year,
            'mile_zh': mile_zh,
            'control': control,
        })

        return context

    def get_models_of_brand(self, brand):
        brand_slug = brand.slug if hasattr(brand, 'slug') else brand
        cache_key = brand_slug + '_models'
        model_dic = cache.get(cache_key, None)
        if model_dic is None:
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
            cache.set(cache_key, model_dic)

        return model_dic


class CarSourceDetailView(TemplateView, CarDetailInfoMixin):
    ''' Car source detail information view.

    Request method: GET
    '''

    http_method_names = ['get', ]
    template_name = 'car_info.html'

    def get_context_data(self, **kwargs):
        context = {}
        car_id = int(kwargs['car_id'])
        car = self.get_car_detail_info(car_id)
        context = {
            'car': car,
            'params': self.get_car_parameters(car.model_slug, \
                            car.detail_model.slug),
            'configs': self.get_car_configurations(car.model_slug, \
                            car.detail_model.slug),
            're_cars': self.get_recommend_cars(car),
            'EVAL_API_URL': settings.EVALUATION_API_URL,
        }
        record_car_source_access(car_id)
        return context

    def get_car_detail_info(self, car_id):
        car = get_object_or_404(CarSource, pk=car_id)
        detail_model = self.get_detail_model(car.model_slug, \
                car.detail_model_slug, car.volume, car.year)
        car.detail_model = detail_model
        car.emission_standard = car.detail_model.emission_standard
        if not car.price_bn:
            car.price_bn = detail_model.price_bn
        car.tax = self.get_purchase_tax(car.price_bn)
        car.total_cost = self.get_total_cost(car.price_bn, car.tax)
        car.save_money = self.get_save_money(car.total_cost, car.price)
        car.discount_rate = self.get_discount_rate(car.total_cost, car.price)
        car.image_urls = car.imgurls.split(' ')
        car.condition = self.get_condition(car.condition_level)
        car.age = self.get_car_age(car.year, car.month)
        car_contrast = self.request.session[settings.CAR_CONTRAST_SESSION_NAME]
        car.in_contrast = True if car.pk in car_contrast else False
        return car

    def get_car_age(self, year, month):
        today = date.today()
        buy_date = date(year, month, 1)
        age = 0
        if buy_date < today:
            months = (today - buy_date).days / 30
            age = months / 12
            months = months % 12
            if age > 0 and months >= 6:
                age += 1
                age = u'{age}年'.format(age=age)
            else:
                age = u'{month}个月'.format(month=month)
        return age

    def get_condition(self, condition_level):
        level = {
            'A': u'优秀',
            'B': u'较好',
            'C': u'一般',
        }
        return level.get(condition_level, u'较好')

    def get_car_parameters(self, model, detail_model):
        params = ConfigParameter.get_car_parameters(model, detail_model)
        param_list = self._get_config_param_list(params, CAR_PARAMETERS)
        return param_list

    def get_car_configurations(self, model, detail_model):
        configs = ConfigParameter.get_car_configurations(model, detail_model)
        config_list = self._get_config_param_list(configs, CAR_CONFIGURATIONS)
        return config_list

    def _get_config_param_list(self, cp_set, names):
        param_list = []
        for name in names:
            para_dic = {}
            for pa in cp_set:
                if pa.para_cat == name:
                    if not para_dic:
                        para_dic.update({'para_cat': name})
                    para_dic.update({pa.para_name: pa.para_value})
            if para_dic:
                param_list.append(para_dic)
        return param_list


    def get_recommend_cars(self, car):
        fields = ('title', 'year', 'month', 'mile', 'control', 'price', 'thumbnail', \
                        'price_bn', 'pk')
        re_cars = car.get_recommend_cars().values(*fields) \
                        .order_by('view_num', '-time')[:4]
        for re_car in re_cars:
            if re_car['price_bn']:
                re_car['total_cost'] = self.get_total_cost(re_car['price_bn'])
            else:
                re_car['total_cost'] = ''
        return re_cars


class OrderCarView(FormView, AJAXResponseMixin):
    ''' Order a car.

    Request method: POST
    Parameters:
    -car_id: car source id.
    -phone: mobile phone number.
    '''

    http_method_names = ['post', ]
    form_class = OrderCarForm

    def form_valid(self, form):
        form.save()
        return self.ajax_response()

    def form_invalid(self, form):
        error = form.errors.popitem()[-1][0]
        self.update_errors(error)
        return self.ajax_response()

