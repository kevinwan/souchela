# -*- coding: utf-8 -*-

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage


__all__ = [
    'paginate',
]


def paginate(objects, page_num, per_page, max_paging_links):
    ''' Return a paginated page for the given objects.'''
    paginator = Paginator(objects, per_page)
    try:
        page_num = int(page_num)
    except ValueError:
        page_num = 1
    try:
        objects = paginator.page(page_num)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)
    page_range = objects.paginator.page_range
    if len(page_range) > max_paging_links:
        start = min(objects.paginator.num_pages - max_paging_links, \
                max(0, objects.number - (max_paging_links / 2) - 1))
        page_range = page_range[start: start + max_paging_links]
    objects.visible_page_range = page_range
    return objects
