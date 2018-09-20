#!/usr/bin/python
# coding: utf-8


class PyTimeCampError(Exception):
    def __init__(self, message, code):
        super(PyTimeCampError, self).__init__(message)
        self.code = code
