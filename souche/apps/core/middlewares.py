# -*- coding: utf-8 -*-

from django.conf import settings

from django.middleware.csrf import get_token


__all__ = [
	'SoucheSessionMiddleware',
	'EnsureCsrfCookieMiddleware',
]



class SoucheSessionMiddleware(object):
    ''' Process souche session includes car contrast.'''

    def process_request(self, request):
        if settings.CAR_CONTRAST_SESSION_NAME not in request.session:
            request.session[settings.CAR_CONTRAST_SESSION_NAME] = []


class EnsureCsrfCookieMiddleware(object):
	''' Ensure the csrf_token is in the cookie.'''

	def process_view(self, request, callback, callback_args, callback_kwargs):
		get_token(request)
		return None
