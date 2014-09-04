# -*- coding: utf-8 -*-

from django.db import models


__all__ = [
    'City',
    'Province',
]


class Province(models.Model):
    ''' Province data.'''

    name = models.CharField(max_length=50, db_index=True, unique=True,
                                verbose_name=u'省份名')
    slug = models.CharField(max_length=32, db_index=True, unique=True,
                                verbose_name=u'省份slug')
    pinyin = models.CharField(max_length=32, blank=True, null=True, db_index=True,
                                verbose_name=u'省份拼音')

    class Meta:
        app_label = 'core'
        db_table = 'souche_province'
        verbose_name = u'省份'
        verbose_name_plural = u'省份'

    def __unicode__(self):
        return self.name

    def get_city_list(self):
        ''' get city list in the province.'''

        return self.cities


class City(models.Model):
    ''' City data.'''

    name = models.CharField(max_length=50, db_index=True, unique=True,
                                verbose_name=u'城市名')
    slug = models.CharField(max_length=32, db_index=True, unique=True,
                                verbose_name=u'城市slug')
    province = models.ForeignKey('Province', db_column='province', to_field='name',
                                related_name='cities', verbose_name=u'所属省份')
    pinyin = models.CharField(max_length=32, blank=True, null=True, db_index=True,
                                verbose_name=u'城市拼音')
    quhao = models.CharField(max_length=32, blank=True, null=True, db_index=True,
                                verbose_name=u'城市区号')
    priority = models.IntegerField(null=True, verbose_name=u'优先级')
    longitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True,
                                null=True, verbose_name=u'经度')
    latitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True,
                                null=True, verbose_name=u'纬度')

    class Meta:
        app_label = 'core'
        db_table = 'souche_city'
        verbose_name = u'城市'
        verbose_name_plural = u'城市'

    def __unicode__(self):
        return self.name

    def get_province_name(self):
        return self.province.name

    @classmethod
    def get_province(cls, city):
        return cls.objects.get(name=city)
