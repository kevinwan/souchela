# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson



__all__ = [
    'JSONResponseMixin',
    'AJAXResponseMixin'
]


class JSONResponseMixin(object):

    status = 'success'
    error_msg = 'message'

    def update_errors(self, msg, errors=None):
        self.status = 'error'
        if errors is not None:
            self.error_msg = errors
        else:
            self.error_msg = msg

    def render_to_json(self, data):
        context = {
            'status': self.status,
            'msg': self.error_msg,
        }
        context.update(data)

        return HttpResponse(simplejson.dumps(context),
                            mimetype='application/json')

    def json_response(self, context=None, **kwargs):
        if context is None:
            context = {}
        if not isinstance(context, dict):
            context = {'data': context}
        context.update(**kwargs)

        return self.render_to_json(context)


class AJAXResponseMixin(JSONResponseMixin):

    def ajax_response(self, context=None, **kwargs):
        return super(AJAXResponseMixin, self).json_response(context, **kwargs)