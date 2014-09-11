# -*- coding: utf-8 -*-

from django import forms


__all__ = [
    'BaseForm'
]



class BaseForm(forms.Form):

    _cleaned_prefix = 'cleaned_'

    def __getattr__(self, name):
        ''' Using cleaned_XXX to get field rather than cleaned_data '''

        if name.startswith(self._cleaned_prefix):
            field_name = name.replace(self._cleaned_prefix, '')
            value = self.cleaned_data.get(field_name, None)
            if value is not None:
                return value
        return getattr(super(BaseForm, self), name)
