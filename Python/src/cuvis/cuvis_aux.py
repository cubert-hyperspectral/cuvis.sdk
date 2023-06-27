import inspect
import logging

from . import cuvis_il
from .cuvis_types import CUVIS_capabilities


def __fn_bits__(n):
    flaglist = []
    while n:
        b = n & (~n + 1)
        flaglist.append(b)
        n ^= b
    return flaglist


def __bit_translate__(n):
    flags = __fn_bits__(n)
    return [key for key, vald in CUVIS_capabilities.items()
            if vald in flags]


def __object_declassifier__(obj):
    res = dict()
    all_att = inspect.getmembers(obj, lambda att: not (inspect.isroutine(att)))
    [res.update({val[0]: val[1]}) for val in all_att if
     not (val[0].startswith('__') and val[0].endswith('__'))]
    return res


class SDKException(Exception):

    def __init__(self, *args):
        if len(args) == 0:
            message = cuvis_il.cuvis_get_last_error_msg_localized()
        else:
            message = args
        logging.exception(message)
        pass


class SessionData(object):
    def __init__(self, name, sessionNumber, sequenceNumber):
        self.Name = name
        self.SessionNumber = sessionNumber
        self.SequenceNumber = sequenceNumber

    def __repr__(self):
        return "'SessionFile: {}; no. {}, seq. {}'".format(self.Name,
                                                           self.SessionNumber,
                                                           self.SequenceNumber)


class GPSData(object):
    def __init__(self):
        self.longitude = None
        self.latitude = None
        self.altitude = None
        self.time = None

    def __repr__(self):
        return "'GPS: lon./lat.: {} / {}; alt. {}, time {}'".format(
            self.longitude, self.latitude, self.altitude,
            self.time)
