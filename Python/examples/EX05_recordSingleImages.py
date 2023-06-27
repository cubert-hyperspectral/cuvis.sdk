import os
import platform
import sys
import time
from datetime import timedelta

import cuvis

### default directories and files
data_dir = None
lib_dir = None

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk",
                                             "sample_data", "set_examples"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(
        os.path.join(lib_dir, "sample_data", "set_examples"))

# default factory
loc_factory = os.path.join(lib_dir, os.pardir,
                           "factory")
# default settings
loc_settings = os.path.join(data_dir, "settings")

# default output
loc_output = os.path.join(os.getcwd(), "EX05_images")

# parameters
loc_exptime = 100
loc_nimgs = 10


def run_example_recordSingleImage(
        userSettingsDir=loc_settings,
        factoryDir=loc_factory,
        recDir=loc_output,
        exposure=loc_exptime,
        nrImgs=loc_nimgs):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print(
        "loading calibration, processing and acquisition context (factory)...")
    calibration = cuvis.Calibration(factoryDir)
    processingContext = cuvis.ProcessingContext(calibration)
    acquisitionContext = cuvis.AcquisitionContext(calibration)

    saveArgs = cuvis.CubertSaveArgs(ExportDir=recDir, AllowOverwrite=True,
                                    AllowSessionFile=True)
    cubeExporter = cuvis.CubeExporter(saveArgs)

    while acquisitionContext.getState() == "Offline":
        print(".", end="")
        time.sleep(1)
    print("\n")

    print("Camera is online")
    acquisitionContext.setOperationMode("Software")
    acquisitionContext.setIntegrationTime(exposure)

    print("Start recoding now")
    for i in range(nrImgs):
        print("Record image #{}/{} ... (async)".format(i + 1, nrImgs))
        am = acquisitionContext.capture()
        res = am.get(timedelta(milliseconds=500))
        if res["Measurement"] is not None:
            mesu = res["Measurement"]

            processingContext.apply(mesu)
            cubeExporter.apply(mesu)

            print("done")

            del mesu
            del am
        else:
            print("failed")

    del processingContext
    del acquisitionContext
    del cubeExporter

    print("finished.")

    pass


if __name__ == "__main__":
    print("Example 05: Record single image. Please provide:")

    userSettingsDir = input(
        "User settings directory (default: {}): ".format(loc_settings))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = loc_settings

    factoryDir = input("Factory directory (default: {}): ".format(loc_factory))
    if factoryDir.strip().lower() in ["", "default"]:
        factoryDir = loc_factory

    recDir = input(
        "Name of recording directory (default: {}): ".format(loc_output))
    if recDir.strip().lower() in ["", "default"]:
        recDir = loc_output

    exposure = input(
        "Exposure/Integration time [ms] (default: {}): ".format(loc_exptime))
    if exposure.strip().lower() in ["", "default"]:
        exposure = loc_exptime
    exposure = int(exposure)

    nrImgs = input("Number of Images (default: {}): ".format(loc_nimgs))
    if nrImgs.strip().lower() in ["", "default"]:
        nrImgs = loc_nimgs
    nrImgs = int(nrImgs)

    run_example_recordSingleImage(userSettingsDir, factoryDir, recDir, exposure,
                                  nrImgs)

    while 1:
        sys.exit(0)
