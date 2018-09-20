#!/usr/bin/python
# coding: utf-8
from datetime import date, datetime

import requests

from pytimecamp.constantes import API_BASE_URL, POST_DATA, GROUP_SETTINGS, QUERY_FIELDS, PUT_DATA
from pytimecamp.errors import PyTimeCampError
from pytimecamp.structtime import StructTime
from . import __version__ as VERSION


class BaseManager(object):

    def __init__(self, token, api_name, response_format='json', user_agent=None):
        self._header = {
            'Authorization': token,
            'User-Agent': 'pytimecamp/%s ' % VERSION + requests.utils.default_user_agent() if user_agent is None else user_agent
        }
        self._api_name = api_name
        self._format = response_format.lower()
        self._url = '%s/%s/format/%s' % (API_BASE_URL, api_name, response_format)

    def _get_data(self, func):
        def wrapper(*args, **kwargs):
            uri, params, method, headers, data = func(*args, **kwargs)
            response = getattr(requests, method)(uri, headers=headers, params=params, data=data)
            if response.status_code not in [200, 201]:
                error = response.json()
                print error
                if isinstance(error, list):
                    error = {'message': ''}
                error.update({'code': response.status_code})
                raise PyTimeCampError(**error)
            if self._format == 'json':
                return response.json()
            else:
                return response.text
        return wrapper

    def _get_api_setting_keys(self):
        data = POST_DATA.get(self._api_name, {})
        return data.get('optional', {}).keys() + data.get('mandatory', {}).keys()

    @staticmethod
    def _check_settings(**kwargs):
        data = {}
        if not kwargs:
            raise ValueError('No settings to update')
        if len(kwargs) != 1:
            raise ValueError('Settings must be updated one by one')

        for key, value in kwargs.iteritems():
            if key not in GROUP_SETTINGS.keys():
                raise ValueError('Key %s is not allowed' % key)
            if value not in GROUP_SETTINGS.get(key):
                raise ValueError('Value %s is not allowed for %s : %s' % (value, key, GROUP_SETTINGS.get(key)))
            data = {'name': key, 'value': value}
        return data

    def _get_settings(self, entity_id):
        return (
            '%s/%s/%s/setting/format/%s' % (API_BASE_URL, self._api_name, entity_id, self._format),
            {'name[]': GROUP_SETTINGS.keys()},
            'get',
            self._header,
            None
        )

    def _set_settings(self, entity_id, **kwargs):
        return (
            '%s/%s/%s/setting/format/%s' % (API_BASE_URL, self._api_name, entity_id, self._format),
            {},
            'put',
            self._header,
            self._check_settings(**kwargs)
        )

    def _get_current(self):
        return '%s/me/format/%s' % (API_BASE_URL, self._format), {}, 'get', self._header, None

    def _list(self):
        return self._url, {}, 'get', self._header, None

    def _filter(self, **kwargs):
        return self._url, self._prepare_data(QUERY_FIELDS, **kwargs), 'get', self._header, None

    def _add(self, **kwargs):
        self._header.update({'content-type': 'application/x-www-form-urlencoded'})
        verb = 'post' if self._api_name == 'tasks' else 'put'  # because timecamp dev sucks :P
        return self._url, {}, verb, self._header, self._prepare_data(POST_DATA, **kwargs)

    def _update(self, **kwargs):
        self._header.update({'content-type': 'application/x-www-form-urlencoded'})
        verb = 'put' if self._api_name == 'tasks' else 'post'  # because timecamp dev sucks :P
        return self._url, {}, verb, self._header, self._prepare_data(PUT_DATA, **kwargs)

    def _delete(self, id):
        return self._url, {'%s_id' % self._api_name: id}, 'delete', self._header, None

    @staticmethod
    def _build_date_format(date):
        return date.strftime('%Y-%m-%d')

    @staticmethod
    def _change_date_keyword(keyword):
        if keyword == 'date_to':
            return 'to'
        if keyword == 'date_from':
            return 'from'
        return keyword

    def _check_params(self, query_field_types, kwargs):
        params = {}
        for field, field_types in query_field_types.iteritems():
            if field in kwargs.keys():
                if not isinstance(kwargs.get(field), field_types):
                    raise ValueError(
                        'Wrong value %s type for key %s (need %s)' % (
                            kwargs.get(field),
                            field,
                            ' or '.join([str(t) for t in field_types])
                        )
                    )
                else:
                    if isinstance(kwargs.get(field), (date, datetime)):
                        params.update({self._change_date_keyword(field): self._build_date_format(kwargs.get(field))})
                    elif isinstance(kwargs.get(field), list):
                        params.update({field: ','.join([str(k) for k in kwargs.get(field)])})
                    elif isinstance(kwargs.get(field), StructTime):
                        params.update({field: str(kwargs.get(field))})
                    else:
                        params.update({field: kwargs.get(field)})

        return params

    def _prepare_data(self, data, **kwargs):
        fields = data.get(self._api_name, {})
        prepared_data = {}
        mandatory = fields.get('mandatory', {})
        if len(mandatory) > 0 and not kwargs:
            raise ValueError('Following fields are mandatory : %s' % ' and '.join(mandatory.keys()))
        if kwargs:
            # Check mandatory
            prepared_data.update(self._check_params(mandatory, kwargs))
            if len(prepared_data) != len(mandatory):
                raise ValueError(
                    'Following fields are mandatory : %s' % list(
                        set(prepared_data.keys()).symmetric_difference(mandatory.keys())
                    )
                )
            # Check optional
            prepared_data.update(self._check_params(fields.get('optional', {}), kwargs))
        return prepared_data


class Manager(BaseManager):

    def __init__(self, token, api_name, methods=[], response_format='json', user_agent=None):
        super(Manager, self).__init__(token, api_name, response_format, user_agent)
        for method_name in methods:
            method = getattr(self, '_%s' % method_name)
            setattr(self, method_name, self._get_data(method))
