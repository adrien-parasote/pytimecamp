#!/usr/bin/python
# coding: utf-8
from pytimecamp.constantes import ALLOWED_RESPONSE_FORMAT, ALLOWED_APIS
from pytimecamp.manager import Manager


class PyTimeCamp(object):

    def __init__(self,  token, response_format='json', user_agent=None):

        if response_format.lower() not in ALLOWED_RESPONSE_FORMAT:
            raise ValueError('Format %s is not allowed' % response_format)

        for api_name, methods in ALLOWED_APIS.iteritems():
            setattr(self, api_name.lower(), Manager(token, api_name, methods, response_format, user_agent))
