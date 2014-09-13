# -*- coding: utf-8 -*-

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
    'mt': (u'手动')
}
