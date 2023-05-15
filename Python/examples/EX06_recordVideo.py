import os
import platform
import sys
import time
from datetime import datetime, timedelta

import cuvis

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(
        os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(os.path.join(lib_dir, "sample_data", "set1"))


def run_example_recordVideo(userSettingsDir=os.path.join(data_dir, "settings"),
                            factoryDir=os.path.join(data_dir, "factory"),
                            recDir=os.path.join(os.getcwd(), "EX06"),
                            exposure=100,
                            autoExp=False,
                            fps=2):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading calibration (factory)...")
    calibration = cuvis.Calibration(calibdir=factoryDir)

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
        print("Component {} is {}".format(info.DisplayName,
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
                                                WorkerQueueSize=100)
    worker = cuvis.Worker(workerSettings)
    worker.setAcquisitionContext(acquisitionContext)
    worker.setProcessingContext(processingContext)
    worker.setExporter(cubeExporter)

    print("recording...! (will stop after 2 minutes)")
    start = datetime.now()
    while (datetime.now() - start) < timedelta(minutes=2):

        while 1:
            if worker.hasNextResult():
                break
            else:
                time.sleep(0.001)

        workerContainer = worker.getNextResult()
        if workerContainer["Measurement"].Data is not None:
            print("current handle index: {}".format(
                workerContainer["Measurement"].get_metadata()[
                    "session_info_sequence_no"]))
            if worker.getQueueSize() == worker.getQueueUsed():
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

    def_input = os.path.join(data_dir, "settings")
    userSettingsDir = input(
        "User settings directory (default: {}): ".format(def_input))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = def_input

    def_input = os.path.join(data_dir, "factory")
    factoryDir = input("Factory directory (default: {}): ".format(def_input))
    if factoryDir.strip().lower() in ["", "default"]:
        factoryDir = def_input

    def_input = os.path.join(os.getcwd(), "EX06")
    recDir = input(
        "Name of recording directory (default: {}): ".format(def_input))
    if recDir.strip().lower() in ["", "default"]:
        recDir = def_input

    def_input = 100
    exposure = input(
        "Exposure/Integration time [ms] (default: {}): ".format(def_input))
    if exposure.strip().lower() in ["", "default"]:
        exposure = def_input
    exposure = int(exposure)

    def_input = False
    autoExp = input(
        "Auto-exposure time [True/False] (default: {}): ".format(def_input))
    if autoExp.strip().lower() in ["", "default"]:
        autoExp = def_input

    def_input = 2
    fps = input(
        "Target frames per second (fps) (default: {}): ".format(def_input))
    if fps.strip().lower() in ["", "default"]:
        fps = def_input
    fps = int(fps)

    run_example_recordVideo(userSettingsDir, factoryDir, recDir, exposure,
                            autoExp, fps)

    while 1:
        sys.exit(0)
