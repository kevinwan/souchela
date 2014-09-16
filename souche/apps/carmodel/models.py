# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from souche.apps.carmodel.fields import PriceField
from souche.apps.carmodel.fields import VolumeField


__all__ = [
    'Brand',
    'ConfigParameter',
    'DetailModel',
    'Model',
]

class Brand(models.Model):
    ''' Car brand data from gongpingjia.'''

    name = models.CharField(max_length=50, db_index=True, unique=True,
                        verbose_name=u'品牌中文名')
    slug = models.CharField(max_length=32, db_index=True, unique=True, 
                        verbose_name=u'品牌slug')
    logo_img = models.CharField(max_length=200, null=True, blank=True,
                        verbose_name=u'品牌logo图片')
    first_letter = models.CharField(max_length=1, verbose_name=u'首字母')
    pinyin = models.CharField(max_length=32, db_index=True,
                        verbose_name=u'品牌（拼音）')
    keywords = models.CharField(max_length=100, db_index=True,
                        verbose_name=u'搜索关键字')

    class Meta:
        db_table = 'carmodel_brand'
        verbose_name = u'汽车品牌'
        verbose_name_plural = u'汽车品牌'
        ordering=['pinyin', ]

    def __unicode__(self):
        return self.name

    @property
    def logo_img_url(self):
        img_url = settings.IMG_DOMAIN + '/img/logo/' + self.logo_img
        return img_url

    def logo_img_link(self):
        context = {
            'img_url': self.logo_img_url,
            'logo_name': self.name,
        }
        return u'<img src="{img_url}?imageView2/2/w/60" alt="{logo_name}" />'.format(**context)
    logo_img_link.short_description = u'图标'
    logo_img_link.allow_tags = True

    @classmethod
    def get_all_brands(cls):
        return cls.objects.all()

    def get_models(self):
        return self.models.all()

    @classmethod
    def get_models_by_brand_slug(cls, brand_slug):
        brand = cls.objects.get(slug=brand_slug)
        return brand.models.all().order_by('pinyin')


class Model(models.Model):
    CLASSIFICATION_CHOICE = (
        (u'微型车', u'微型车'),
        (u'小型车', u'小型车'),
        (u'紧凑型车', u'紧凑型车'),
        (u'中型车', u'中型车'),
        (u'中大型车', u'中大型车'),
        (u'豪华型车', u'豪华型车'),
        (u'小型SUV', u'小型SUV'),
        (u'紧凑型SUV', u'紧凑型SUV'),
        (u'中型SUV', u'中型SUV'),
        (u'中大型SUV', u'中大型SUV'),
        (u'全尺寸SUV', u'全尺寸SUV'),
        (u'MPV', u'MPV'),
        (u'跑车', u'跑车'),
        (u'微面', u'微面'),
        (u'微卡', u'微卡'),
        (u'轻客', u'轻客'),
        (u'皮卡', u'皮卡'),
    )

    ATTRIBUTE_CHOICE = (
        (u'合资', u'合资'),
        (u'进口', u'进口'),
        (u'国产', u'国产'),
    )

    name = models.CharField(max_length=50, db_index=True, unique=True,
                        verbose_name=u'型号中文名')
    slug = models.CharField(max_length=32, db_index=True, unique=True, 
                        verbose_name=u'型号slug')
    brand = models.ForeignKey('Brand', to_field='slug', db_column='brand',
                        related_name='models', verbose_name=u'所属品牌')
    logo_img = models.CharField(max_length=200, null=True, blank=True,
                        verbose_name=u'车型图片')
    pinyin= models.CharField(max_length=32, db_index=True, verbose_name=u'型号拼音')
    manufactor = models.CharField(max_length=32, verbose_name=u'制造厂商')
    classification = models.CharField(max_length=32, db_index=True,
                        choices=CLASSIFICATION_CHOICE, verbose_name=u'级别')
    keywords = models.CharField(max_length=100, db_index=True,
                        verbose_name=u'搜索关键字')
    attribute = models.CharField(max_length=10, db_index=True,
                        choices=ATTRIBUTE_CHOICE, verbose_name=u'属性(区分国产/进口)')

    class Meta:
        app_label = 'carmodel'
        db_table = 'carmodel_model'
        verbose_name = u'汽车型号'
        verbose_name_plural = u'汽车型号'
        ordering=['pinyin', ]

    def __unicode__(self):
        return self.name

    @classmethod
    def get_brand(cls, model_slug):
        pass

    def get_brand_name(self):
        return self.brand.name

    @classmethod
    def get_models_by_classification(cls, classification):
        if isinstance(classification, list) or isinstance(classification, tuple):
            models = cls.objects.filter(classification__in=classification)
        else:
            models = cls.objects.filter(classification=classification)
        return models


class DetailModel(models.Model):
    ''' Car detail model data from gongpingjia.'''

    name = models.CharField(max_length=50, db_index=True, verbose_name=u'详细款型中文名')
    slug = models.CharField(max_length=50, db_index=True, unique=True,
                        verbose_name=u'详细款型slug')
    model = models.ForeignKey('Model', db_column='model', to_field='slug',
                        related_name='detail_models', verbose_name=u'所属型号')
    price_bn = PriceField(verbose_name=u'新车指导价')
    year = models.IntegerField(verbose_name=u'款型年代')
    volume = VolumeField(db_index=True, verbose_name=u'排量')

    class Meta:
        app_label = 'carmodel'
        db_table = 'carmodel_detail_model'
        verbose_name = u'汽车详细款型'
        verbose_name_plural = u'汽车详细款型'

    def __unicode__(self):
        return self.name

    @classmethod
    def get_model(cls, detail_model_slug):
        pass

    def get_model_name(self):
        return self.model.name


class ConfigParameter(models.Model):
    ''' Car configuration parameters.'''
    CONFIG_KIND_CHOICES = (
        ('C', u'配置'),
        ('P', u'参数'),
    )

    para_cat = models.CharField(max_length=50, verbose_name=u'参数分类')
    para_name = models.CharField(max_length=50, blank=True, null=True,
                        verbose_name=u'参数名')
    para_value = models.CharField(max_length=50, blank=True, null=True,
                        verbose_name=u'参数值')
    isdefault = models.IntegerField(blank=True, default=0, verbose_name=u'是否默认配置')
    model = models.CharField(max_length=50, db_index=True, verbose_name=u'型号')
    detail_model = models.CharField(max_length=50, db_index=True,
                        verbose_name=u'详细款型')
    kind = models.CharField(max_length=1, choices=CONFIG_KIND_CHOICES, \
                        default='C', verbose_name=u'区分参数和配置的标志')
    # model = models.ForeignKey('Model', to_field='slug', db_column='model', db_index=True)
    # detail_model = models.ForeignKey('DetailModel', to_field='slug',
    #                     db_column='detail_model', db_index=True)

    class Meta:
        app_label = 'carmodel'
        db_table = 'carmodel_config_parameter'
        verbose_name = u'汽车配置参数'
        verbose_name_plural = u'汽车配置参数'

    def __unicode__(self):
        s = '{para_name}: {para_value}'
        return s.format(**{'para_name': self.para_name, 'para_value': self.para_value})

    @classmethod
    def get_car_parameters(cls, model, detail_model):
        criteria = {
            'model': model,
            'detail_model': detail_model,
            'kind': 'P'
        }
        parameters = cls.objects.filter(**criteria)
        return parameters

    @classmethod
    def get_car_configurations(cls, model, detail_model):
        criteria = {
            'model': model,
            'detail_model': detail_model,
            'kind': 'C'
        }
        parameters = cls.objects.filter(**criteria)
        return parameters
