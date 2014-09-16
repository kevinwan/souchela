# -*- coding:utf-8 -*-

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
