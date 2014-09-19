# -*- coding: utf-8 -*-


class SetSessionIdInCookieMiddleware(object):
    ''' Set sessionid in browser's cookie.'''

    def process_request(self, request):
        request.session.set_test_cookie()
