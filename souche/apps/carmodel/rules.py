# -*- coding: utf-8 -*-

CLASSIFICATION_NAMES_ZH = {
    'SMALL_CAR': u'微小型车',
    'COMPACT_CAR': u'紧凑型车',
    'MID_CAR': u'中型车',
    'LARGE_CAR': u'中大型车',
    'SUV': u'SUV',
    'MPV': u'MPV',
    'SPORTS_CAR': u'跑车',
    'COMMERCIAL_CAR': u'商用车',
}

CLASSIFICATION_NAMES = {
    'SMALL_CAR': 'small_car',
    'COMPACT_CAR': 'compact_car',
    'MID_CAR': 'mid_car',
    'LARGE_CAR': 'large_car',
    'SUV': 'suv',
    'MPV': 'mpv',
    'SPORTS_CAR': 'sports_car',
    'COMMERCIAL_CAR': 'commercial_car',
}

CLASSIFICATION = {
    'small_car': (u'微型车', u'小型车'),  # 微小型车
    'compact_car': (u'紧凑型车', ),  # 紧凑型车
    'mid_car': (u'中型车', ),  # 中型车
    'large_car': (u'中大型车', u'豪华型车'),  # 中大型车
    'suv': (u'小型SUV', u'紧凑型SUV', u'中型SUV', u'中大型SUV', u'全尺寸SUV'),  #SUV
    'mpv': (u'MPV', ),  # MPV
    'sports_car': (u'跑车', ),  # 跑车
    'commercial_car': (u'微面', u'微卡', u'轻客', u'皮卡')  # 商用车
}

# TRANSMISSION TYPE
TRANSMISSION_NAMES = {
    'AUTO_TRANSMISSION': 'at',
    'MANUAL_TRANSMISSION': 'mt'
}

TRANSMISSION = {
    'at': (u'自动', u'手自一体'),
    'mt': (u'手动', )
}

HOT_BRAND = {
    'DAZHONG': 'dazhong',
    'BENCHI': 'benz',
    'AODI': 'audi',
    'BAOMA': 'bmw',
    'BENTIAN': 'hongda',
    'FENGTIAN': 'toyota',
    'RICHAN': 'richan',
    'MAZIDA': 'mazda',
    'XIANDAI': 'hyundai',
    'LINGMU': 'suzuki',
    'BIAOZHI': 'biaozhi',
    'XUETIELONG': 'citroen'
}

CAR_PARAMETERS = (u'主要参数', u'基本参数', u'基本信息', u'车辆基本信息', u'发动机/变速箱', \
    u'发动机', u'燃油&发动机', u'变速器', u'变速箱', u'基本性能', u'内部尺寸', u'外部尺寸', \
    u'底盘/车轮制动', u'底盘操控', u'底盘转向', u'电动机', u'越野性能', u'车型结构', u'车身', \
    u'车轮制动', u'轮胎轮毂')

CAR_CONFIGURATIONS = (u'操控配置', u'安全性能', u'安全装备', u'安全配置', u'车身功能', \
    u'车身结构', u'悬架', u'内部配置', u'内饰', u'外部配置', u'外饰装备', u'座椅', u'座椅配置', \
    u'控制台', u'方向盘', u'影音空调', u'多媒体配置', u'娱乐设备', u'灯光配置', u'玻璃/后视镜', \
    u'空调/冰箱', u'车内功能', u'车内电控', u'车窗及后视镜', u'便利功能', u'通讯系统', \
    u'防盗配置', u'高科技配置')
