import logging
import os
import platform

from . import cuvis_il
from .cuvis_aux import SDKException
from .cuvis_types import ComponentType


class General(object):
    def __init__(self, path=""):
        log_path = "."
        FORMAT = '%(asctime)s -- %(levelname)s: %(message)s'
        if os.path.exists(path):
            log_path = path + os.sep
        elif platform.system() == "Linux":
            log_path = os.path.expanduser('~') + os.sep + ".cuvis" + os.sep
            if not os.path.exists(log_path):
                os.mkdir(log_path)
        elif platform.system() == "Windows":
            log_path = os.getenv('APPDATA') + os.sep + ".cuvis" + os.sep
            if not os.path.exists(log_path):
                os.mkdir(log_path)
                
        if os.path.exists(log_path):
            logging.basicConfig(filename=log_path + "cuvisSDK_python.log",
                                format=FORMAT,
                                encoding='utf-8',
                                level=logging.DEBUG,
                                filemode='w')
        else:
            raise SDKException(
                "path {} does not exist...".format(os.path.abspath(log_path)))
        logging.info("Logger ready.")

        if cuvis_il.status_ok != cuvis_il.cuvis_init(log_path):
            raise SDKException()
        pass

    def getVersion(self):
        return cuvis_il.cuvis_version_swig()

    def setLogLevel(self, lvl):
        lvl_dict = {"info": {"cuvis": cuvis_il.loglevel_info,
                             "logging": logging.INFO},
                    "debug": {"cuvis": cuvis_il.loglevel_debug,
                              "logging": logging.DEBUG},
                    "error": {"cuvis": cuvis_il.loglevel_error,
                              "logging": logging.ERROR},
                    "fatal": {"cuvis": cuvis_il.loglevel_fatal,
                              "logging": logging.CRITICAL},
                    "warning": {"cuvis": cuvis_il.loglevel_warning,
                                "logging": logging.WARNING},
                    }

        cuvis_il.cuvis_set_log_level(lvl_dict[lvl]["cuvis"])
        logging.basicConfig(level=lvl_dict[lvl]["logging"])


class ComponentInfo(object):
    def __init__(self, **kwargs):
        self.Type = None
        self.DisplayName = None
        self.SensorInfo = None
        self.UserField = None
        self.PixelFormat = None

        [self.__setattr__(key, kwargs.pop(key, None)) for key in self.__dict__
         if not key.startswith("__")]

        if all([getattr(self, key) is None for key in self.__dict__ if
                not key.startswith("__")]):
            if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                               cuvis_il.cuvis_component_info_t):
                ci = list(kwargs.values())[0]
                self.Type = \
                    [key for key, val in ComponentType.items() if
                     val == ci.type][0]
                self.DisplayName = ci.displayname
                self.SensorInfo = ci.sensorinfo
                self.UserField = ci.userfield
                self.PixelFormat = ci.pixelformat
            elif len(kwargs) != 0:
                raise SDKException(
                    "Could not handle every input parameter in ComponentInfo!")
        else:
            if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                               cuvis_il.cuvis_component_info_t):
                raise SDKException(
                    "Could not handle every input parameter in ComponentInfo!")
        pass

    def getInternal(self):
        ci = cuvis_il.cuvis_component_info_t()
        ci.__setattr__("type", ComponentType[self.Type])
        ci.__setattr__("displayname", self.DisplayName)
        ci.__setattr__("sensorinfo", self.SensorInfo)
        ci.__setattr__("userfield", self.UserField)
        ci.__setattr__("pixelformat", self.PixelFormat)
        return ci
