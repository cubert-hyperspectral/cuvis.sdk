from . import cuvis_il
from .cuvis_aux import SDKException


class Exporter(object):
    def __init__(self):
        self.__handle__ = None
        pass

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_exporter_free(_ptr)
        pass

    def apply(self, mesu):
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_apply(self.__handle__,
                                                               mesu.__handle__):
            raise SDKException()
        mesu.refresh()
        return mesu

    def getQueueUsed(self):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_get_queue_used(
                self.__handle__, _ptr):
            raise SDKException()
        return cuvis_il.p_int_value(_ptr)


class CubeExporter(Exporter):
    def __init__(self, fs):
        super().__init__()
        _ptr = cuvis_il.new_p_int()
        ge, fs = fs.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_create_cube(_ptr, ge,
                                                                     fs):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass


class TiffExporter(Exporter):
    def __init__(self, fs):
        super().__init__()
        _ptr = cuvis_il.new_p_int()
        ge, fs = fs.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_create_tiff(_ptr, ge,
                                                                     fs):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass


class EnviExporter(Exporter):
    def __init__(self, ge):
        super().__init__()
        _ptr = cuvis_il.new_p_int()
        ge, _ = ge.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_create_envi(_ptr, ge):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass


class ViewExporter(Exporter):
    def __init__(self, fs):
        super().__init__()
        _ptr = cuvis_il.new_p_int()
        ge, fs = fs.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_exporter_create_view(_ptr, ge,
                                                                     fs):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass
