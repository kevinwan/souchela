# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.inclusion_tag('includes/car_source_images.html', takes_context=False)
def show_car_source_images(img_urls):
	image_urls = img_urls.split(' ')
	print image_urls
	context = {
		'image_urls': image_urls
	}
	return context
