# -*- coding: utf-8 -*-

from django import forms

from souche.apps.carsource.fields import MobilePhoneField

from souche.apps.carsource.models import CarOrderRecord
from souche.apps.carsource.models import CarSource


__all__ = [
    'OrderCarForm',
]


class OrderCarForm(forms.Form):
    ''' Order car form.'''

    error_messages = {
        'car_not_exist': u'该车源不存在或已下线',
        'car_not_object': u'车源不存在',
        'order_already_exist': u'您已预约过该车源,请耐心等候，客服会尽快联系您！'
    }

    car_id = forms.IntegerField(required=True, \
                error_messages={'required': u'车源为空'})
    phone = MobilePhoneField(required=True, \
                error_messages={
                    'max_length': u'手机号码长度错误',
                    'required': u'手机号码为空',
                    'invalid': u'手机格式错误'
                })

    def clean_car_id(self):
        car_id = self.cleaned_data['car_id']
        car = CarSource.sale_cars.filter(pk=car_id)
        if car.exists():
            return car[0]
        raise forms.ValidationError(self.error_messages['car_not_exist'])

    def clean(self):
        car = self.cleaned_data.pop('car_id')
        phone = self.cleaned_data['phone']
        if not isinstance(car, CarSource):
            raise forms.ValidationError(self.error_messages['car_not_object'])
        car_order = CarOrderRecord.objects.filter(car=car, phone=phone)
        if car_order.exists():
            raise forms.ValidationError(self.error_messages['order_already_exist'])

        self.cleaned_data.update({'car': car})
        return self.cleaned_data
        
    def save(self, commit=True):
        car_order = CarOrderRecord(**self.cleaned_data)
        if commit:
            car_order.save()
        return car_order
