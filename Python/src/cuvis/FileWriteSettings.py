from . import cuvis_il
from .cuvis_aux import SDKException
from .cuvis_types import PanSharpeningInterpolationType, \
    PanSharpeningAlgorithm, \
    TiffCompressionMode, TiffFormat, \
    OperationMode, ProcessingMode


class GeneralExportSettings(object):

    def check_kwargs(self, kwargs):
        [self.__setattr__(key, kwargs.pop(key, None)) for
         key in kwargs.copy().keys() if key in self.__dict__.keys()]
        pass

    def __init__(self, **kwargs):
        self.ExportDir = "."
        self.ChannelSelection = "all"
        self.SpectraMultiplier = 1.0
        self.PanScale = 0.0
        self.PanSharpeningInterpolationType = "Linear"
        self.PanSharpeningAlgorithmType = "CubertMacroPixel"
        self.AddPan = False
        self.AddFullscalePan = False
        self.Permissive = False

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(
                list(kwargs.values())[0],
                cuvis_il.cuvis_export_general_settings_t):
            ge = list(kwargs.values())[0]
            self.ExportDir = ge.export_dir
            self.ChannelSelection = ge.channel_selection
            self.SpectraMultiplier = ge.spectra_multiplier
            self.PanScale = ge.pan_scale0
            self.PanSharpeningInterpolationType = \
                [key for key, val in PanSharpeningInterpolationType.items() if
                 val == ge.pan_interpolation_type][0]
            self.PanSharpeningAlgorithmType = \
                [key for key, val in PanSharpeningAlgorithm.items() if
                 val == ge.pan_algorithm][0]
            self.AddPan = ge.add_pan > 0
            self.AddFullscalePan = ge.add_fullscale_pan > 0
            self.Permissive = ge.permissive > 0
        # elif len(kwargs) != 0:
        #    raise SDKException("Could not handle every
        #    input parameter in GeneralExportSettings!")

        pass

    def getInternal(self):
        ge = cuvis_il.cuvis_export_general_settings_t()
        ge.__setattr__("export_dir", self.ExportDir)
        ge.__setattr__("channel_selection", self.ChannelSelection)
        ge.__setattr__("spectra_multiplier", float(self.SpectraMultiplier))
        ge.__setattr__("pan_scale", float(self.PanScale))
        ge.__setattr__("pan_interpolation_type", PanSharpeningInterpolationType[
            self.PanSharpeningInterpolationType])
        ge.__setattr__("pan_algorithm", PanSharpeningAlgorithm[
            self.PanSharpeningAlgorithmType])
        ge.__setattr__("add_pan", int(self.AddPan))
        ge.__setattr__("add_fullscale_pan", int(self.AddFullscalePan))
        ge.__setattr__("permissive", int(self.Permissive))
        return ge


class EnviExportSettings(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def getInternal(self):
        ge = super().getInternal()
        es = None
        return ge, es


class TiffExportSettings(GeneralExportSettings):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CompressionMode = "None"
        self.Format = "MultiChannel"

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(
                list(kwargs.values())[0],
                cuvis_il.cuvis_export_tiff_settings_t):
            ts = list(kwargs.values())[0]
            self.CompressionMode = \
                [key for key, val in TiffCompressionMode.items() if
                 val == ts.compression_mode][0]
            self.Format = \
                [key for key, val in TiffFormat.items() if val == ts.format][0]
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in "
                "TiffExportSettings: {}".format(kwargs.keys()))
        pass

    def getInternal(self):
        ge = super().getInternal()
        ts = cuvis_il.cuvis_export_tiff_settings_t()
        ts.__setattr__("compression_mode",
                       TiffCompressionMode[self.CompressionMode])
        ts.__setattr__("format", TiffFormat[self.Format])
        return ge, ts


class ViewExportSettings(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Userplugin = None

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(
                list(kwargs.values())[0],
                cuvis_il.cuvis_export_view_settings_t):
            vs = list(kwargs.values())[0]
            self.Userplugin = vs.userplugin
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in ViewExportSettings: "
                "{}".format(kwargs.keys()))
        pass

        if '<userplugin xmlns=' \
           '"http://cubert-gmbh.de/user/plugin/userplugin.xsd">' not \
                in self.Userplugin:
            try:
                with open(self.Userplugin) as f:
                    userplugintmp = f.readlines()
                self.Userplugin = "".join(userplugintmp)
            except:
                raise ValueError(
                    "Could not read plugin from {}".format(self.Userplugin))

    def getInternal(self):
        ge = super().getInternal()
        vs = cuvis_il.cuvis_export_view_settings_t()
        vs.__setattr__("userplugin", self.Userplugin)
        return ge, vs


class CubertSaveArgs(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.AllowOverwrite = False
        self.AllowFragmentation = False
        self.AllowDrop = False
        self.AllowSessionFile = True
        self.AllowInfoFile = True
        self.OperationMode = "Software"
        self.FPS = 0
        self.SoftLimit = 20
        self.HardLimit = 100
        self.MaxBuftime = 10000

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                           cuvis_il.cuvis_save_args_t):
            sa = list(kwargs.values())[0]
            self.AllowOverwrite = sa.allow_overwrite > 0
            self.AllowFragmentation = sa.allow_fragmentation > 0
            self.AllowDrop = sa.allow_drop > 0
            self.AllowSessionFile = sa.allow_session_file > 0
            self.AllowInfoFile = sa.allow_info_file > 0
            self.OperationMode = \
                [k for k, v in OperationMode.items() if v == sa.operation_mode][
                    0]
            self.FPS = sa.fps
            self.SoftLimit = sa.soft_limit
            self.HardLimit = sa.hard_limit
            self.MaxBuftime = sa.max_buftime
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in CubertSaveArgs: "
                "{}".format(kwargs.keys()))

        pass

    def getInternal(self):
        ge = super().getInternal()
        sa = cuvis_il.cuvis_save_args_t()
        sa.__setattr__("allow_overwrite", int(self.AllowOverwrite))
        sa.__setattr__("allow_fragmentation", int(self.AllowFragmentation))
        sa.__setattr__("allow_drop", int(self.AllowDrop))
        sa.__setattr__("allow_session_file", int(self.AllowSessionFile))
        sa.__setattr__("allow_info_file", int(self.AllowInfoFile))
        sa.__setattr__("operation_mode", OperationMode[self.OperationMode])
        sa.__setattr__("fps", int(self.FPS))
        sa.__setattr__("soft_limit", int(self.SoftLimit))
        sa.__setattr__("hard_limit", int(self.HardLimit))
        sa.__setattr__("max_buftime", int(self.MaxBuftime))
        return ge, sa


class CubertProcessingArgs(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.AllowRecalib = False
        self.ProcessingMode = "Raw"

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                           cuvis_il.cuvis_proc_args_t):
            pa = list(kwargs.values())[0]
            self.AllowRecalib = pa.allow_recalib > 0
            self.ProcessingMode = \
                [k for k, v in ProcessingMode.items() if
                 v == pa.processing_mode][0]
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in CubertProcessingArgs: "
                "{}".format(kwargs.keys()))
        pass

    def getInternal(self):
        ge = super().getInternal()
        pa = cuvis_il.cuvis_proc_args_t()
        pa.__setattr__("allow_recalib", int(self.AllowRecalib))
        pa.__setattr__("processing_mode",
                       int(ProcessingMode[self.ProcessingMode]))
        return ge, pa


class CubertWorkerSettings(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.WorkerCount = 0
        self.PollInterval = 10
        self.KeepOutOfSequence = False
        self.WorkerQueueHardLimit = 10
        self.WorkerQueueSoftLimit = 10
        self.CanDrop = True

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                           cuvis_il.cuvis_worker_settings_t):
            wa = list(kwargs.values())[0]
            self.WorkerCount = wa.worker_count
            self.PollInterval = wa.poll_interval
            self.KeepOutOfSequence = wa.keep_out_of_sequence > 0
            self.WorkerQueueHardLimit = wa.hard_limit
            self.WorkerQueueSoftLimit = wa.soft_limit
            self.CanDrop = wa.can_drop == 1
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in CubertWorkerArgs: "
                "{}".format(kwargs.keys()))

        pass

    def getInternal(self):
        ge = super().getInternal()
        wa = cuvis_il.cuvis_worker_settings_t()
        wa.__setattr__("worker_count", int(self.WorkerCount))
        wa.__setattr__("poll_interval", int(self.PollInterval))
        wa.__setattr__("keep_out_of_sequence", int(self.KeepOutOfSequence))
        wa.__setattr__("hard_limit", int(self.WorkerQueueHardLimit))
        wa.__setattr__("soft_limit", int(self.WorkerQueueSoftLimit))
        wa.__setattr__("can_drop", int(self.CanDrop))
        return ge, wa

class CubertViewerSettings(GeneralExportSettings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.WorkerCount = 0
        self.PollInterval = 10
        self.KeepOutOfSequence = False
        self.WorkerQueueHardLimit = 10
        self.WorkerQueueSoftLimit = 10
        self.CanDrop = True

        self.check_kwargs(kwargs)

        if len(kwargs) == 1 and isinstance(list(kwargs.values())[0],
                                           cuvis_il.cuvis_viewer_settings_t):
            wa = list(kwargs.values())[0]
            self.WorkerCount = wa.worker_count
            self.PollInterval = wa.poll_interval
            self.KeepOutOfSequence = wa.keep_out_of_sequence > 0
            self.WorkerQueueHardLimit = wa.hard_limit
            self.WorkerQueueSoftLimit = wa.soft_limit
            self.CanDrop = wa.can_drop == 1
        elif len(kwargs) != 0:
            raise SDKException(
                "Could not handle input parameter(s) in CubertWorkerArgs: "
                "{}".format(kwargs.keys()))

        pass

    def getInternal(self):
        ge = super().getInternal()
        wa = cuvis_il.cuvis_worker_settings_t()
        wa.__setattr__("worker_count", int(self.WorkerCount))
        wa.__setattr__("poll_interval", int(self.PollInterval))
        wa.__setattr__("keep_out_of_sequence", int(self.KeepOutOfSequence))
        wa.__setattr__("hard_limit", int(self.WorkerQueueHardLimit))
        wa.__setattr__("soft_limit", int(self.WorkerQueueSoftLimit))
        wa.__setattr__("can_drop", int(self.CanDrop))
        return ge, wa

