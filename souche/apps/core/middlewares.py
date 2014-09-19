# -*- coding: utf-8 -*-

from django.conf import settings



class SoucheSessionMiddleware(object):
    ''' Process souche session includes car contrast.'''

    def process_request(self, request):
        if settings.CAR_CONTRAST_SESSION_NAME not in request.session:
            request.session[settings.CAR_CONTRAST_SESSION_NAME] = []
