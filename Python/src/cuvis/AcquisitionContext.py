from . import cuvis_il
from .Async import Async, AsyncMesu
from .Calibration import Calibration
from .General import ComponentInfo
from .Measurement import Measurement
from .SessionFile import SessionFile
from .cuvis_aux import SDKException, SessionData
from .cuvis_types import HardwareState, OperationMode


class AcquisitionContext(object):
    def __init__(self, base, **kwargs):
        self.__handle__ = None
        __simulate__ = kwargs.get("simulate", False)

        if isinstance(base, Calibration):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_create_from_calib(
                    base.__handle__, _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        if isinstance(base, SessionFile):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != \
                    cuvis_il.cuvis_acq_cont_create_from_session_file(
                        base.__handle__, __simulate__, _ptr):
                raise SDKException()
        else:
            raise SDKException(
                "Could not interpret input of type {}.".format(type(base)))
        pass

    def getState(self):
        val = cuvis_il.new_p_cuvis_hardware_state_t()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_get_state(
                self.__handle__, val):
            raise SDKException()
        return [key for key, vald in HardwareState.items()
                if vald == cuvis_il.p_cuvis_hardware_state_t_value(val)][0]

    def getComponentCount(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_get_component_count(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getComponentInfo(self, idref):
        ci = cuvis_il.cuvis_component_info_t()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_get_component_info(
                self.__handle__, idref, ci):
            raise SDKException()
        return ComponentInfo(info=ci)

    def getQueueSize(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_queue_size_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setQueueSize(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_queue_size_set(
                self.__handle__, val):
            raise SDKException()
        pass

    def getOnline(self, idref):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_online_get(self.__handle__,
                                                                idref, val):
            raise SDKException()
        return cuvis_il.p_int_value(val) == 1

    def getGain(self, idref):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_gain_get(self.__handle__,
                                                              idref, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setGain(self, idref, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_gain_set(self.__handle__,
                                                              idref, val):
            raise SDKException()
        pass

    def setGainAsync(self, idref, val):
        _pAsync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_gain_set_async(
                self.__handle__, idref, _pAsync, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pAsync))

    def setOperationMode(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_operation_mode_set(
                self.__handle__, OperationMode[val]):
            raise SDKException()
        pass

    def setOperationModeAsync(self, val):
        _pAsync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_acq_cont_operation_mode_set_async(
                    self.__handle__, _pAsync,
                    OperationMode[val]):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pAsync))

    def getOperationMode(self):
        val = cuvis_il.new_p_cuvis_operation_mode_t()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_operation_mode_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_cuvis_operation_mode_t_value(val)

    def setIntegrationTime(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_integration_time_set(
                self.__handle__, val):
            raise SDKException()
        pass

    def setIntegrationTimeAsync(self, val):
        _pAsync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_acq_cont_integration_time_set_async(
                    self.__handle__, _pAsync, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pAsync))

    def getIntegrationTimeFactor(self, idref):
        val = cuvis_il.new_p_double()
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_comp_integration_time_factor_get(
                    self.__handle__, idref, val):
            raise SDKException()
        return cuvis_il.p_double_value(val)

    def setIntegrationTimeFactor(self, idref, val):
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_comp_integration_time_factor_set(
                    self.__handle__, idref, val):
            raise SDKException()
        pass

    def setIntegrationTimeFactorAsync(self, idref, val):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_comp_integration_time_factor_set_async(
                    self.__handle__, idref, _pasync, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def getIntegrationTime(self):
        val = cuvis_il.new_p_double()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_integration_time_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_double_value(val)

    def capture(self):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_capture_async(
                self.__handle__, _pasync):
            raise SDKException()
        return AsyncMesu(cuvis_il.p_int_value(_pasync))

    def captureAt(self, timeout_ms):
        this_mesu = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_capture(
                self.__handle__, this_mesu, timeout_ms):
            raise SDKException()
        return Measurement(cuvis_il.p_int_value(this_mesu))

    def setFPS(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_fps_set(
                self.__handle__, val):
            raise SDKException()
        pass

    def setFPSAsync(self, val):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_fps_set_async(
                self.__handle__, _pasync, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def getFPS(self):
        val = cuvis_il.new_p_double()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_fps_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_double_value(val)

    def hasNextMeasurement(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_has_next_measurement(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val) != 0

    def getNextMeasurement(self, timeout_ms):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_get_next_measurement(
                self.__handle__, val, timeout_ms):
            raise SDKException()
        return Measurement(cuvis_il.p_int_value(val))

    def setSessionInfo(self, val):
        session = cuvis_il.cuvis_session_info_t()
        try:
            session.__setattr__("name", val["Name"])
            session.__setattr__("sequence_no", val["SequenceNumber"])
            session.__setattr__("session_no", val["SessionNumber"])
        except KeyError as e:
            raise ValueError(
                "Missing {} in SessionFile Info dictionary.".format(e))
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_set_session_info(
                self.__handle__, session):
            raise SDKException()
        pass

    def getSessionInfo(self):
        session = cuvis_il.cuvis_session_info_t()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_get_session_info(
                self.__handle__, session):
            raise SDKException()
        return SessionData(session.__getattribute__("name"),
                           session.__getattribute__("session_no"),
                           session.__getattribute__("sequence_no"))

    def getQueueUsed(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_queue_used_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getDriverQueueUsed(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_driver_queue_used_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getHardwareQueueUsed(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_hardware_queue_used_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getDriverQueueSize(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_driver_queue_size_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getHardwareQueueSize(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_hardware_queue_size_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def getTemperature(self, idref):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_comp_temperature_get(
                self.__handle__, idref, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setAverage(self, avg):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_average_set(
                self.__handle__, avg):
            raise SDKException()
        pass

    def getAverage(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_average_get(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setAverageAsync(self, avg):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_average_set_async(
                self.__handle__, _pasync, avg):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def setContinuous(self, val):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_continuous_set_async(
                self.__handle__, _pasync, int(val)):
            raise SDKException()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_continuous_set(
                self.__handle__, int(val)):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def getBandwidth(self):
        _ptr = cuvis_il.new_p_double()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_bandwidth_get(
                self.__handle__, _ptr):
            raise SDKException()
        return cuvis_il.p_double_value(_ptr)

    def getAutoExp(self):
        _ptr = cuvis_il.new_p_double()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_auto_exp_get(
                self.__handle__, _ptr):
            raise SDKException()
        return cuvis_il.p_double_value(_ptr)

    def setAutoExp(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_auto_exp_set(
                self.__handle__, val):
            raise SDKException()
        pass

    def setAutoExpAsync(self, val):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_auto_exp_set_async(
                self.__handle__, _pasync, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def getPreviewMode(self):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_preview_mode_get(
                self.__handle__, _ptr):
            raise SDKException()
        return bool(cuvis_il.p_int_value(_ptr))

    def setPreviewMode(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_preview_mode_set(
                self.__handle__, val):
            raise SDKException()
        return

    def setPreviewModeAsync(self, val):
        _pasync = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_acq_cont_preview_mode_set_async(
                self.__handle__, val):
            raise SDKException()
        return Async(cuvis_il.p_int_value(_pasync))

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_acq_cont_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
