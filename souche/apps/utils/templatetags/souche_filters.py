# -*- coding:utf-8 -*-

from datetime import date

from django import template


register = template.Library()


@register.filter
def car_config_css(value):
    config_values_css = {
        u'●': 'b-lake-blue f-white',
        u'○': 'b-orange f-white',
        '-': 'f-gray',
    }
    return config_values_css.get(value, 'f-gray')


@register.filter
def car_config_value(value):
    config_values = {
        u'●': u'标配',
        u'○': u'选配',
        '-': u'——',
    }
    return config_values.get(value, value)


@register.filter
def year_month_zh(value):
    if isinstance(value, date):
        return u'{year}年{month}月'.format(year=value.year, month=value.month)
    return ''
