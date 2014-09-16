# -*- coding: utf-8 -*-

from django.db import models



__all__ = [
    'SaleCarManager',
]


class SaleCarManager(models.Manager):
    ''' Manage query in CarSource, filter car that is on sale.'''

    def get_query_set(self):
        query_set = super(self.__class__, self).get_query_set() \
                        .filter(status__in=('Y', 'U'))

        return query_set
