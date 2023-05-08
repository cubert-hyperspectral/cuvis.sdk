import os

from . import cuvis_il
from .Measurement import Measurement
from .cuvis_aux import SDKException
from .cuvis_types import OperationMode


class SessionFile(object):
    def __init__(self, base):
        self.__handle__ = None
        if isinstance(base, str) and os.path.exists(base):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_session_file_load(base,
                                                                      _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        else:
            raise SDKException(
                "Could not open SessionFile File! File not found!")

    pass

    def load(self, file):
        self.__init__(file)
        pass

    def getMeasurement(self, frameNo, type='session_item_type_frames'):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_session_file_get_mesu(
                self.__handle__, frameNo, type, _ptr):
            raise SDKException()
        return Measurement(cuvis_il.p_int_value(_ptr))

    def getSize(self, type='session_item_type_frames'):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_session_file_get_size(
                self.__handle__, type, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getFPS(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_session_file_get_fps(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getOperationMode(self):
        val = cuvis_il.new_p_cuvis_operation_mode_t()
        if cuvis_il.status_ok != cuvis_il.cuvis_session_file_get_operation_mode(
                self.__handle__, val):
            raise SDKException()
        return [key for key, vald in OperationMode.items()
                if vald == cuvis_il.p_cuvis_operation_mode_t_value(val)][0]

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_session_file_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
