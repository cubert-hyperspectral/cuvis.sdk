import os
import platform
import sys
import time
from datetime import datetime, timedelta

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
loc_output = os.path.join(os.getcwd(), "EX06_video")

# parameters
loc_exptime = 100
loc_autoexp = False
loc_fps = 2


def run_example_recordVideo(userSettingsDir=loc_settings,
                            factoryDir=loc_factory,
                            recDir=loc_output,
                            exposure=loc_exptime,
                            autoExp=loc_autoexp,
                            fps=loc_fps):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading calibration (factory)...")
    calibration = cuvis.Calibration(factoryDir)

    print("loading acquisition context...")
    acquisitionContext = cuvis.AcquisitionContext(calibration)
    session_info = {"Name": "video", "SequenceNumber": 0, "SessionNumber": 0}
    acquisitionContext.setSessionInfo(session_info)

    print("prepare saving of measurements...")
    saveArgs = cuvis.CubertSaveArgs(ExportDir=recDir,
                                    AllowOverwrite=True,
                                    AllowSessionFile=True,
                                    FPS=fps,
                                    OperationMode="Software")

    print("writing files to: {}".format(recDir))
    cubeExporter = cuvis.CubeExporter(saveArgs)

    print("prepare processing of measurements...")
    processingContext = cuvis.ProcessingContext(calibration)
    processingContext.setProcessingMode("Raw")

    print("Waiting for camera to come online...")

    while acquisitionContext.getState() == "Offline":
        print(".", end="")
        time.sleep(1)
    print("\n")

    print("Component details:")
    count = acquisitionContext.getComponentCount()
    for i in range(count):
        info = acquisitionContext.getComponentInfo(i)
        isOnline = acquisitionContext.getOnline(i)
        print("Component #{} {} is {}".format(i, info.DisplayName,
                                              "online" if isOnline else "offline"))
        print(" -- info:        {}".format(info.SensorInfo))
        print(" -- use:         {}".format(info.UserField))
        print(" -- pixelformat: {}".format(info.PixelFormat))

    print("initializing hardware...")
    acquisitionContext.setIntegrationTime(exposure)
    acquisitionContext.setOperationMode("Internal")
    acquisitionContext.setFPS(fps)
    acquisitionContext.setAutoExp(autoExp)
    acquisitionContext.setContinuous(True)

    print("configuring worker...")
    workerSettings = cuvis.CubertWorkerSettings(KeepOutOfSequence=0,
                                                PollInterval=10,
                                                WorkerCount=0,
                                                WorkerQueueHardLimit=10,
                                                WorkerQueueSoftLimit=10,
                                                CanDrop=True)
    worker = cuvis.Worker(workerSettings)
    worker.setAcquisitionContext(acquisitionContext)
    worker.setProcessingContext(processingContext)
    worker.setExporter(cubeExporter)

    worker.setQueueLimits({'hard_limit' : 100, 'soft_limit' : 90})
    print("recording...! (will stop after 2 minutes)")
    start = datetime.now()
    while (datetime.now() - start) < timedelta(minutes=2):

        while 1:
            if worker.hasNextResult():
                break
            else:
                time.sleep(0.001)

        workerContainer = worker.getNextResult(1000)
        if workerContainer["Measurement"].Data is not None:
            print("current handle index: {}".format(
                workerContainer["Measurement"].getMetadata()[
                    "session_info_sequence_no"]))
            if worker.getQueueLimits()["soft_limit"] == worker.getQueueUsed():
                print("worker queue is full! Main() loop can not keep up!")
                break
            if acquisitionContext.getQueueSize() == acquisitionContext.getQueueUsed():
                print("acquisition queue is full! Worker can not keep up!")
                break

    print("acquisition stopped...")
    acquisitionContext.setContinuous(False)
    print("finished.")

    pass


if __name__ == "__main__":
    print("Example 06: Record video file. Please provide:")

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

    autoExp = input(
        "Auto-exposure time [True/False] (default: {}): ".format(loc_autoexp))
    if autoExp.strip().lower() in ["", "default"]:
        autoExp = loc_autoexp
    autoExp = int(autoExp)

    fps = input(
        "Target frames per second (fps) (default: {}): ".format(loc_fps))
    if fps.strip().lower() in ["", "default"]:
        fps = loc_fps
    fps = int(fps)

    run_example_recordVideo(userSettingsDir, factoryDir, recDir, exposure,
                            autoExp, fps)

    while 1:
        sys.exit(0)
