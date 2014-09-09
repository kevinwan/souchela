# -*- coding: utf-8 -*-

from django.contrib import admin

from souche.apps.core.models import Province
from souche.apps.core.models import City


class CityInline(admin.TabularInline):
    model = City
    fields = ('name', 'slug', 'province', 'pinyin', 'quhao', 'priority')

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pinyin', )
    list_display_links = ('name', )
    search_fields = ['name', 'pinyin']

    inlines = (CityInline, )

admin.site.register(Province, ProvinceAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'province', 'pinyin', 'quhao', 'priority')
    list_display_links = ('name', )
    list_filter = ('province', )
    search_fields = ['name', ]

admin.site.register(City, CityAdmin)
