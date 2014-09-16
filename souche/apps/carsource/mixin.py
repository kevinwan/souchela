# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404

from souche.apps.carmodel.models import Model




__all__ = [
    'CarCostDetailMixin'
]



class CarCostDetailMixin(object):
    ''' Get car cost detail information.'''

    def get_detail_model(self, model, detail_model=None, volume=None, year=None):
        if not isinstance(model, Model):
            model = get_object_or_404(Model, slug=model)
        if detail_model:
            detail_model = model.detail_models.get(slug=detail_model)
        elif volume and year:
            year_range = range(year-2, year+2)
            detail_models = model.detail_models.filter(volume=volume, \
                            year__in=year_range).order_by('price_bn')
            if detail_models.exists():
                detail_model = detail_models[0]
            else:
                raise Http404
        else:
            raise Http404

        return detail_model

    def get_purchase_tax(self, new_car_price):
        ''' 购置税＝购车款/(1+17%)×购置税率(10%)'''
        tax = float(new_car_price) / 11.7
        return round(tax, 2)

    def get_total_cost(self, new_car_price, tax=None):
        if tax:
            cost = float(new_car_price) + tax
        else:
            cost = float(new_car_price) + self.get_purchase_tax(new_car_price)
        return round(cost, 2)

    def get_save_money(self, total_cost, list_price):
        save_money = float(total_cost) - float(list_price)
        return round(save_money, 2)

    def get_discount_rate(self, total_cost, list_price):
        ''' 折价率=售价/新车总成本 * 100%'''
        discount_rate = float(list_price) / float(total_cost)
        discount_rate *= 100
        return round(discount_rate, 2)
