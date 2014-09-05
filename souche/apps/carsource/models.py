# -*- coding: utf-8 -*-

from django.db import models

from souche.apps.carmodel.fields import MileageField
from souche.apps.carmodel.fields import PriceField
from souche.apps.carmodel.fields import VolumeField


__all__ = [
    'CarSource',
]

class CarSource(models.Model):
    ''' Car source data.'''

    CAR_SOURCE_STATUS_CHOICE = (
        ('M', u'(M)新加入的产品或在后台被修改过'),
        ('N', u'(N)不在前台呈现'),
        ('Q', u'(Q)已售出/下线'),
        ('T', u'(T)重复记录'),
        ('W', u'(W)没有缩略图'),
        ('X', u'(X)没有联系方式'),
        ('Y', u'(Y)信息完整，优先呈现'),
    )

    title = models.CharField(max_length=200, verbose_name=u'标题')
    meta = models.TextField(blank=True, null=True, verbose_name=u'其他信息')
    brand_slug = models.CharField(max_length=32, db_index=True, \
                        verbose_name=u'品牌slug')
    model_slug = models.CharField(max_length=32, db_index=True, \
                        verbose_name=u'型号slug')
    detail_model_slug = models.CharField(blank=True, null=True, \
                        verbose_name=u'详细款型slug')
    year = models.IntegerField(verbose_name=u'首次上牌年份')
    month = models.IntegerField(verbose_name=u'首次上牌月份')
    url = models.URLField(verbose_name=u'原网站链接')
    time = models.DateTimeField(verbose_name=u'发布时间')
    mile = MileageField(verbose_name=u'行驶里程(万公里)')
    volume = VolumeField(db_index=True, verbose_name=u'排量')
    color = models.CharField(max_length=32, blank=True, null=True, db_index=True, \
                        verbose_name=u'颜色')
    control = models.CharField(max_length=32, blank=True, null=True, db_index=True, \
                        verbose_name=u'变速箱', help_text=u'手动/自动/手自一体')
    price = PriceField(db_index=True, verbose_name=u'预售价格')
    price_bn = PriceField(blank=True, null=True, verbose_name=u'新车购买价格')
    city = models.CharField(max_length=50, db_index=True, verbose_name=u'城市')
    region = models.CharField(max_length=100, blank=True, null=True, \
                        verbose_name=u'地址')
    description = models.TextField(blank=True, null=True, verbose_name=u'描述')
    thumbnail = models.CharField(max_length=200, null=True, blank=True, \
                        verbose_name=u'缩略图')
    imgurls = models.TextField(null=True, blank=True, verbose_name=u'车辆图片')
    # imgurls用来保存多对应于一部车在源网站多个图片的URL地址，用空格号分开
    # Contact info
    contact = models.CharField(max_length=64, verbose_name=u'联系人')
    phone = models.CharField(max_length=128, verbose_name=u'联系电话')
    company_name = models.CharField(max_length=128, verbose_name=u'商家名')
    company_url = models.URLField(blank=True, null=True, verbose_name=u'商家网址')
    status = models.CharField(max_length=1, default='Y', db_index=True, \
                        choices=CAR_SOURCE_STATUS_CHOICE, verbose_name=u'状态')
    # More info about car
    mandatory_insurance = models.DateTimeField(blank=True, null=True, \
                        verbose_name=u'交强险到期时间')
    business_insurance = models.DateTimeField(blank=True, null=True, \
                        verbose_name=u'商业险到期时间')
    examine_insurance = models.DateTimeField(blank=True, null=True, \
                        verbose_name=u'年审到期时间')
    transfer_owner = models.IntegerField(blank=True, null=True, \
                        verbose_name=u'过户次数', help_text=u'0表示买的新车，1以上表示买的二手车')
    condition_level = models.CharField(max_length=10, blank=True, null=True, \
                        verbose_name=u'车况等级')
    condition_detail = models.TextField(blank=True, null=True, \
                        verbose_name=u'车况介绍')
    car_application = models.CharField(blank=True, null=True, \
                        verbose_name=u'车辆用途', help_text=u'营运/非营运')
    driving_license = models.CharField(blank=True, null=True, \
                        verbose_name=u'是否有行驶证', help_text=u'是/否')
    invoice = models.CharField(blank=True, null=True, \
                        verbose_name=u'是否有购车/过户发票', help_text=u'是/否')
    maintenance_record = models.CharField(blank=True, null=True, \
                        verbose_name=u'是否有维修保养记录', help_text=u'是/否')

    class Meta:
        app_label = 'carsource'
        db_table = 'carsource_car_source'
        verbose_name = u'二手车车源'
        verbose_name_plural = u'二手车车源'

    def __unicode__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return ("subject", (), {"pid": self.id})

    @classmethod
    def get_by_pk(cls, pk):
        return cls.objects.get(pk=pk)
