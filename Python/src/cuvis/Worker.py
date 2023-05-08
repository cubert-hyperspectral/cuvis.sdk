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
        self.sessionSet = False

        self.__handle__ = None
        _ptr = cuvis_il.new_p_int()
        _, settings = args.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_create(_ptr, settings):
            raise SDKException()
        self.__handle__ = cuvis_il.p_int_value(_ptr)
        pass

    # Returns a tuple of: (SessionFile in progress: True / False, frames already read, total frames in session)
    def querySessionProgress(self):
        frames_read = cuvis_il.new_p_int()
        frames_total = cuvis_il.new_p_int()

        if self.sessionSet:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_query_session_progress(
                    self.__handle__, frames_read, frames_total):
                self.sessionSet = False
            else:
                self.sessionSet = True
        return (self.sessionSet, frames_read, frames_total)

    def _checkIsSessionDone(self):
        self.querySessionProgress()
        return self.sessionSet

    def setAcquisitionContext(self, base=None):
        if self._checkIsSessionDone():
            raise SDKException()

        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_acq_cont(
                    self.__handle__, base.__handle__):
                raise SDKException()
            self.acquisitionSet = True
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_acq_cont(
                    self.__handle__, 0):
                raise SDKException()
            self.acquisitionSet = False

    def setProcessingContext(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_proc_cont(
                    self.__handle__, base.__handle__):
                raise SDKException()
            self.processingSet = True
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_proc_cont(
                    self.__handle__, 0):
                raise SDKException()
            self.processingSet = False

    def setExporter(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_exporter(
                    self.__handle__, base.__handle__):
                raise SDKException()
            self.exporterSet = True
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_exporter(
                    self.__handle__, 0):
                raise SDKException()
            self.exporterSet = False

    def setViewer(self, base=None):
        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_viewer(
                    self.__handle__, base.__handle__):
                raise SDKException()
            self.viewerSet = True
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_viewer(
                    self.__handle__, 0):
                raise SDKException()
            self.viewerSet = False

    def setSession(self, base=None, skip_dropped_frames=False):
        if self._checkIsSessionDone():
            raise SDKException()

        if base is not None:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_session_file(
                    self.__handle__, base.__handle__,
                    1 if skip_dropped_frames else 0):
                raise SDKException()
            else:
                self.sessionSet = True
        else:
            if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_session_file(
                    self.__handle__, 0, 0):
                raise SDKException()

    def ingestMesu(self, base):
        if self._checkIsSessionDone():
            raise SDKException()

        if cuvis_il.status_ok != cuvis_il.cuvis_worker_ingest_mesu(
                self.__handle__, base.__handle__):
            raise SDKException()

    def hasNextResult(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_has_next_result(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val) != 0

    # Try to fetch the next result. If timeout == -1 (default), wait indefinitely, else wait 'timeout' milliseconds
    def getNextResult(self, timeout=-1):
        this_mesu = cuvis_il.new_p_int()
        this_viewer = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_next_result(
                self.__handle__, this_mesu, this_viewer, timeout):
            raise SDKException()
        mesu = Measurement(cuvis_il.p_int_value(this_mesu))
        if self.viewerSet:
            view = Viewer(cuvis_il.p_int_value(this_viewer)).apply(this_mesu)
        else:
            view = None
        return {"Measurement": mesu, "View": view}

    def getQueueLimits(self):
        hard = cuvis_il.new_p_int()
        soft = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_queue_limits(
                self.__handle__, hard, soft):
            raise SDKException()
        return (cuvis_il.p_int_value(hard), cuvis_il.p_int_value(soft))

    def setQueueLimits(self, hard, soft):
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_queue_limits(
                self.__handle__, hard, soft):
            raise SDKException()
        pass

    def getQueueUsed(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_queue_used(
                self.__handle__, val):
            raise SDKException()
        return cuvis_il.p_int_value(val)

    def setWorkerCanDrop(self, val):
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_set_drop_bahvior(
                self.__handle__, 1 if val else 0):
            raise SDKException()

    def getWorkerCanDrop(self):
        val = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_worker_get_drop_behavior(
                self.__handle__, val):
            raise SDKException()
        return bool(cuvis_il.p_int_value(val))

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_worker_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)
