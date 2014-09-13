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
