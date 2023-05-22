import os
from pathlib import Path

from . import cuvis_il
from .SessionFile import SessionFile
from .cuvis_aux import SDKException
from .cuvis_types import OperationMode


class Calibration(object):

    def __init__(self, base, **kwargs):
        self.__handle__ = None

        if isinstance(Path(base), Path) and os.path.exists(Path(base)):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_calib_create_from_path(
                    base, _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        elif isinstance(base, SessionFile):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != \
                    cuvis_il.cuvis_calib_create_from_session_file(
                        base.__handle__, _ptr):
                raise SDKException()
        else:
            raise SDKException(
                "Could not interpret input of type {}.".format(type(base)))
        pass

    def getCapabilities(self):
        All_Modes = {}
        # All_Modes.update(ProcessingMode)
        All_Modes.update(OperationMode)
        Usable_Modes = []
        _ptr = cuvis_il.new_p_int()
        for k, v in All_Modes.items():
            try:
                if cuvis_il.status_ok != cuvis_il.cuvis_calib_get_capabilities(
                        self.__handle__, v, _ptr):
                    raise SDKException()
                else:
                    Usable_Modes.append(k)
            except SDKException:
                raise SDKException()
        return Usable_Modes  # __bit_translate__(cuvis_il.p_int_value(_ptr))

    def getID(self):
        _id = cuvis_il.cuvis_calib_get_id_swig(self.__handle__)
        return _id

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_calib_free(_ptr)
        pass
