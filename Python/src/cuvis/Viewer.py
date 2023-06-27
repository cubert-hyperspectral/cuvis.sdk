from . import cuvis_il
from .Measurement import ImageData
from .cuvis_aux import SDKException
from .cuvis_types import CUVIS_imbuffer_format


class Viewer(object):
    def __init__(self, settings):
        self.__handle__ = None
        self.ViewerSettings = settings

        if isinstance(settings, int):
            self.__handle__ = settings
        if isinstance(self.ViewerSettings, cuvis_il.cuvis_viewer_settings_t):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_viewer_create(
                    _ptr, self.ViewerSettings):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        else:
            raise SDKException(
                "Could not open ViewerSettings of type {}!".format(
                    type(self.ViewerSettings)))

        pass

    def getDataCount(self, mesu):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_viewer_apply(self.__handle__,
                                                             mesu.__handle__,
                                                             _ptr):
            raise SDKException()
        currentView = cuvis_il.p_int_value(_ptr)

        countHandle = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_view_get_data_count(
                currentView, countHandle):
            raise SDKException()

        return cuvis_il.p_int_value(countHandle)

    def apply(self, mesu):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_viewer_apply(self.__handle__,
                                                             mesu.__handle__,
                                                             _ptr):
            raise SDKException()
        currentView = cuvis_il.p_int_value(_ptr)

        countHandle = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_view_get_data_count(
                currentView, countHandle):
            raise SDKException()

        dataCount = cuvis_il.p_int_value(countHandle)

        for i in range(dataCount):
            view_data = cuvis_il.cuvis_view_data_t()
            if cuvis_il.status_ok != cuvis_il.cuvis_view_get_data(
                    currentView, i, view_data):
                raise SDKException()

            if view_data.__getattribute__("data").format == \
                    CUVIS_imbuffer_format["imbuffer_format_uint8"]:
                return ImageData(img_buf=view_data.__getattribute__("data"),
                                 dformat=view_data.__getattribute__(
                                     "data").format)
            else:
                raise SDKException("Unsupported viewer bit depth!")

        pass

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_viewer_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
