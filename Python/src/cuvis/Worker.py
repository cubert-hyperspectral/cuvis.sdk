from . import cuvis_il
from .Measurement import Measurement
from .Viewer import Viewer
from .cuvis_aux import SDKException


class Worker(object):
    def __init__(self, args):
        self.exporterSet = False
        self.acquisitionSet = False
        self.processingSet = False
        self.viewerSet = False

        self.__handle__ = None
        _ptr = cuvis_il.new_p_int()
        _, settings = args.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_create(_ptr, settings):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass

    def setAcquisitionContext(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_acq_cont(self.__handle__, base.__handle__):
                raise SDKException()
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_acq_cont(self.__handle__, 0):
                raise SDKException()
        self.acquisitionSet = True
        pass

    def setProcessingContext(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_proc_cont(self.__handle__, base.__handle__):
                raise SDKException()
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_proc_cont(self.__handle__, 0):
                raise SDKException()
        self.processingSet = True
        pass

    def setExporter(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_exporter(self.__handle__, base.__handle__):
                raise SDKException()
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_exporter(self.__handle__, 0):
                raise SDKException()
        self.exporterSet = True
        pass

    def setViewer(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_viewer(self.__handle__, base.__handle__):
                raise SDKException()
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_viewer(self.__handle__, 0):
                raise SDKException()
        self.viewerSet = True
        pass

    def hasNextResult(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_has_next_result(self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val) != 0

    def getNextResult(self):
        this_mesu = cuvis_il.new_p_int()
        this_viewer = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_next_result(self.__handle__, this_mesu, this_viewer):
            raise SDKException()
        mesu = Measurement(cuvis_il.p_int_value(this_mesu))
        if self.viewerSet:
            view = Viewer(cuvis_il.p_int_value(this_viewer)).apply(this_mesu)
        else:
            view = None
        return {"Measurement": mesu, "View": view}
        # return mesu

    def getQueueSize(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_queue_limit(self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setQueueSize(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_queue_limit(self.__handle__, val):
            raise SDKException()
        pass

    def getQueueUsed(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_queue_used(self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_worker_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
