# -*- coding: utf-8 -*-

from django.contrib import admin

from souche.apps.carmodel.models import Brand
from souche.apps.carmodel.models import Model
from souche.apps.carmodel.models import DetailModel


class ModelInline(admin.TabularInline):
    model = Model
    fields = ('name', 'slug', 'pinyin', 'manufactor', 'classification', 'keywords', 'attribute')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'logo_img_link', 'first_letter', 'pinyin')
    list_display_links = ('name', )
    list_filter = ('first_letter', )
    search_fields = ['name', 'slug']

    inlines = (ModelInline, )

admin.site.register(Brand, BrandAdmin)


class DetailModelInline(admin.TabularInline):
    model = DetailModel
    fields = ('name', 'slug', 'year', 'volume', 'price_bn')


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'brand', 'pinyin', 'manufactor', 'classification', \
                            'keywords', 'attribute')
    list_display_links = ('name', )
    list_filter = ('classification', 'attribute', )
    search_fields = ['name', 'slug']

    inlines = (DetailModelInline, )

admin.site.register(Model, ModelAdmin)


class DetailModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'model', 'year', 'volume', 'price_bn')
    list_display_links = ('name', )
    search_fields = ['name', ]

admin.site.register(DetailModel, DetailModelAdmin)
