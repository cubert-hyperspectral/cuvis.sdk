import cuvis
import time
import os
from datetime import timedelta
import sys

lib_dir = os.getenv("CUVIS")
data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))


def run_example_recordSingleImage(userSettingsDir=os.path.join(data_dir, "settings"),
                                  factoryDir=os.path.join(data_dir, "factory"),
                                  recDir=os.path.join(os.getcwd(), "EX05"),
                                  exposure=100,
                                  nrImgs=10):

    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading calibration, processing and acquisition context (factory)...")
    calibration = cuvis.Calibration(calibdir=factoryDir)
    processingContext = cuvis.ProcessingContext(calibration)
    acquisitionContext = cuvis.AcquisitionContext(calibration)

    saveArgs = cuvis.CubertSaveArgs(ExportDir=recDir, AllowOverwrite=True, AllowSessionFile=False)
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

    def_input = os.path.join(data_dir, "settings")
    userSettingsDir = input("User settings directory (default: {}): ".format(def_input))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = def_input

    def_input = os.path.join(data_dir, "factory")
    factoryDir = input("Factory directory (default: {}): ".format(def_input))
    if factoryDir.strip().lower() in ["", "default"]:
        factoryDir = def_input

    def_input = os.path.join(os.getcwd(), "EX05")
    recDir = input("Name of recording directory (default: {}): ".format(def_input))
    if recDir.strip().lower() in ["", "default"]:
        recDir = def_input

    def_input = 100
    exposure = input("Exposure/Integration time [ms] (default: {}): ".format(def_input))
    if exposure.strip().lower() in ["", "default"]:
        exposure = def_input
    exposure = int(exposure)

    def_input = 10
    nrImgs = input("Number of Images (default: {}): ".format(def_input))
    if nrImgs.strip().lower() in ["", "default"]:
        nrImgs = def_input
    nrImgs = int(nrImgs)

    run_example_recordSingleImage(userSettingsDir, factoryDir, recDir, exposure, nrImgs)

    while 1:
        sys.exit(0)
