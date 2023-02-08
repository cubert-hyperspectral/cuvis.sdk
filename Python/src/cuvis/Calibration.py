from . import cuvis_il
from .cuvis_aux import SDKException, __bit_translate__
from .cuvis_types import ProcessingMode, OperationMode


class Calibration(object):
    def __init__(self, calibdir=None):
        self.__handle__ = None
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_calib_create_from_path(calibdir, _ptr):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass

    def getCapabilities(self):
        All_Modes = {}
        # All_Modes.update(ProcessingMode)
        All_Modes.update(OperationMode)
        Usable_Modes = []
        _ptr = cuvis_il.new_p_int()
        for k, v in All_Modes.items():
            try:
                if cuvis_il.status_ok != cuvis_il.cuvis_calib_get_capabilities(self.__handle__, v, _ptr):
                    raise SDKException()
                else:
                    Usable_Modes.append(k)
            except SDKException:
                raise SDKException()
        return Usable_Modes  # __bit_translate__(cuvis_il.p_int_value(_ptr))

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_calib_free(_ptr)
        pass
