#!/usr/bin/python
# coding: utf-8


class StructTime(object):

    def __init__(self, hours, minutes, seconds):
        if hours < 0 or hours > 24:
            raise ValueError('hours must be in [0-24]')
        if minutes < 0 or minutes > 59:
            raise ValueError('minutes must be in [0-59]')
        if seconds < 0 or seconds > 59:
            raise ValueError('seconds must be in [0-59]')
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '%02d:%02d:%02d' % (self.hours, self.minutes, self.seconds)
