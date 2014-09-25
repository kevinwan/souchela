# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.inclusion_tag('includes/pagination.html', takes_context=True)
def pagination_for(context, page):
    ''' Include the pagination template and data for persisting querystring in 
    pagination links.
    '''
    querystring = context['request'].GET.copy()
    if 'page' in querystring:
        querystring.pop('page')
    querystring = querystring.urlencode()
    context = {
        'page': page,
        'querystring': querystring
    }
    return context


@register.simple_tag(takes_context=True)
def generate_search_link(context, param, value):
    ''' Generate search link.'''

    search_params = ('brand', 'model', 'price', 'year', 'category', \
                'color', 'mile', 'control', 'sort')
    if param not in search_params:
        return ''
    querystring = context['request'].GET.copy()
    if 'page' in querystring:
        querystring.pop('page')
    if param in querystring:
        querystring.pop(param)
    querystring.update({param: value})
    if param == 'brand' and querystring.get('model'):
        querystring.pop('model')

    return ''.join(('?', querystring.urlencode()))


@register.simple_tag(takes_context=True)
def activate_filter_condition(context, param, value):
    ''' Activate filter condition.'''

    querystring = context['request'].GET.copy()
    if (param in querystring) and (value == querystring.pop(param)[0]):
        return 'class="focus"'
    return ''
