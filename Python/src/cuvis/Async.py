from . import cuvis_il
from .Measurement import Measurement
from .cuvis_aux import SDKException
from .cuvis_types import AsyncResult


class AsyncMesu(object):
    def __init__(self, handle):
        self.__handle__ = handle

    pass

    def get(self, timeout):
        _ptr = cuvis_il.new_p_int()
        _pmesu = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        res = cuvis_il.cuvis_async_capture_get(_ptr, int(timeout.total_seconds() * 1000), _pmesu)

        ret = {
            "state": None,
            "Measurement": None
        }

        if res == cuvis_il.status_ok:
            ret["state"] = "done"
            ret["Measurement"] = Measurement(cuvis_il.p_int_value(_pmesu))
        elif res == cuvis_il.status_deferred:
            ret["state"] = "deferred"
        elif res == cuvis_il.status_overwritten:
            ret["state"] = "overwritten"
        elif res == cuvis_il.status_timeout:
            ret["state"] = "timeout"
        else:
            raise SDKException()

        return ret

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_async_capture_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)


class Async(object):
    def __init__(self, handle):
        self.__handle__ = handle

    def get(self, timeout):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        res = cuvis_il.cuvis_async_call_get(_ptr, int(timeout.total_seconds() * 1000))

        if res == cuvis_il.status_ok:
            return AsyncResult["done"]
        elif res == cuvis_il.status_deferred:
            return AsyncResult["deferred"]
        elif res == cuvis_il.status_overwritten:
            return AsyncResult["overwritten"]
        elif res == cuvis_il.status_timeout:
            return AsyncResult["timeout"]
        else:
            raise SDKException()
        pass

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_async_call_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
