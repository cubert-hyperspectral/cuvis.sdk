import os
import platform
import sys

lib_dir = os.getenv("CUVIS")
if lib_dir is None:
    print('CUVIS environmental variable is not set!')
    sys.exit(1)
if platform.system() == "Windows":
    os.add_dll_directory(lib_dir)
    add_il = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
    os.environ['PATH'] += os.pathsep + add_il
    sys.path.append(str(add_il))
elif platform.system() == 'Linux':
    os.environ['PATH'] = lib_dir + os.pathsep + os.environ['PATH']
else:
    raise NotImplementedError('Invalid operating system detected!')
    # sys.exit(1)

from .AcquisitionContext import AcquisitionContext
from .Calibration import Calibration
from .Export import CubeExporter, EnviExporter, TiffExporter, ViewExporter
from .FileWriteSettings import GeneralExportSettings, CubertSaveArgs, \
    CubertProcessingArgs, \
    EnviExportSettings, TiffExportSettings, ViewExportSettings, \
    CubertWorkerSettings
from .General import General
from .Measurement import Measurement
from .ProcessingContext import ProcessingContext
from .SessionFile import SessionFile
from .Viewer import Viewer
from .Worker import Worker
