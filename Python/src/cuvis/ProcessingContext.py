from . import cuvis_il
from .Calibration import Calibration
from .FileWriteSettings import CubertProcessingArgs
from .Measurement import Measurement
from .SessionFile import SessionFile
from .cuvis_aux import SDKException
from .cuvis_types import ReferenceType, ProcessingMode


class ProcessingContext(object):
    def __init__(self, base):
        self.__handle__ = None
        self.__modeArgs__ = cuvis_il.cuvis_proc_args_t()

        if isinstance(base, Calibration):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_create_from_calib(
                    base.__handle__, _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        elif isinstance(base, SessionFile):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != \
                    cuvis_il.cuvis_proc_cont_create_from_session_file(
                        base.__handle__, _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        elif isinstance(base, Measurement):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_create_from_mesu(
                    base.__handle__, _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        else:
            raise SDKException(
                "could not interpret input of type {}.".format(type(base)))
        pass

    def apply(self, mesu):
        if isinstance(mesu, Measurement):
            if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_apply(
                    self.__handle__, mesu.__handle__):
                raise SDKException()
            mesu.refresh()
            return mesu
        else:
            raise SDKException(
                "Can only apply ProcessingContext to Measurement!")
        pass

    def setReference(self, mesu, refType):
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_set_reference(
                self.__handle__, mesu.__handle__,
                ReferenceType[refType]):
            raise SDKException()
        pass

    def clearReference(self, refType):
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_clear_reference(
                self.__handle__, ReferenceType[refType]):
            raise SDKException()
        pass

    def getReference(self, refType):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_get_reference(
                self.__handle__, _ptr,
                ReferenceType[refType]):
            raise SDKException()
        return Measurement(cuvis_il.p_int_value(_ptr))

    def hasReference(self, refType):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_has_reference(
                self.__handle__, ReferenceType[refType],
                _ptr):
            raise SDKException()
        return cuvis_il.p_int_value(_ptr) == 1

    def setProcessingMode(self, pMode):
        self.__modeArgs__.__setattr__("processing_mode", ProcessingMode[pMode])
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_set_args(
                self.__handle__, self.__modeArgs__):
            raise SDKException()
        pass

    def getProcessingMode(self):
        return [key for key, val in ProcessingMode.items() if
                val == self.__modeArgs__.__getattribute__("processing_mode")][0]

    def setProcessingArgs(self, pa):
        _, self.__modeArgs__ = pa.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_set_args(
                self.__handle__, self.__modeArgs__):
            raise SDKException()

    pass

    def getProcessingArgs(self):
        return CubertProcessingArgs(args=self.__modeArgs__)

    def isCapable(self, mesu, pa):
        _, args = pa.getInternal()
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_is_capable(
                self.__handle__, mesu.__handle__, args, _ptr):
            raise SDKException()
        return cuvis_il.p_int_value(_ptr) == 1

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_proc_cont_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass

    def calcDistance(self, distMM):
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_calc_distance(
                self.__handle__, distMM):
            raise SDKException()
        return True

    def setRecalib(self, val):
        self.__modeArgs__.__setattr__("allow_recalib", int(val))
        if cuvis_il.status_ok != cuvis_il.cuvis_proc_cont_set_args(
                self.__handle__, self.__modeArgs__):
            raise SDKException()
        pass

    def getCalibrationID(self):
        _id = cuvis_il.cuvis_proc_cont_get_calib_id_swig(self.__handle__)
        return _id

    def getRecalib(self):
        return self.__modeArgs__.__getattribute__("allow_recalib") != 0
