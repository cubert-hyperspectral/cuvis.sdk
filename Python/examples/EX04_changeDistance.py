import os
import platform

import cuvis

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(
        os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(os.path.join(lib_dir, "sample_data", "set1"))


def run_example_changeDistance(
        userSettingsDir=os.path.join(data_dir, "settings"),
        measurementLoc=os.path.join(data_dir,
                                    "vegetation_000",
                                    "vegetation_000_000_snapshot.cu3"),
        factoryDir=os.path.join(data_dir, "factory"),
        distance=1000,
        exportDir=os.path.join(os.getcwd(), "EX04")):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading measurement file...")
    mesu = cuvis.Measurement(measurementLoc)

    print("Data 1 {} t={}ms mode={}".format(mesu.Name,
                                            mesu.IntegrationTime,
                                            mesu.ProcessingMode,
                                            ))

    print("loading calibration and processing context (factory)...")
    calibration = cuvis.Calibration(calibdir=factoryDir)
    processingContext = cuvis.ProcessingContext(calibration)

    print("setting distance...")
    processingContext.calcDistance(1000)

    processingContext.setProcessingMode("Raw")

    saveArgs = cuvis.CubertSaveArgs(ExportDir=exportDir, AllowOverwrite=True)

    assert processingContext.isCapable(mesu,
                                       processingContext.getProcessingArgs())

    print("changing distance...")
    print("original distance...")
    print(mesu.get_metadata()["distance"])
    processingContext.apply(mesu)
    print("new distance...")
    print(mesu.get_metadata()["distance"])
    print("saving...")
    mesu.save(saveArgs)
    print("finished.")

    pass


if __name__ == "__main__":

    print("Example 04: Change distance. Please provide:")

    def_input = os.path.join(data_dir, "settings")
    userSettingsDir = input(
        "User settings directory (default: {}): ".format(def_input))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = def_input

    def_input = os.path.join(data_dir,
                             "vegetation_000",
                             "vegetation_000_000_snapshot.cu3")
    measurementLoc = input(
        "Measurement file (.cu3) (default: {}): ".format(def_input))
    if measurementLoc.strip().lower() in ["", "default"]:
        measurementLoc = def_input

    def_input = os.path.join(data_dir, "factory")
    factoryDir = input("Factory directory (default: {}): ".format(def_input))
    if factoryDir.strip().lower() in ["", "default"]:
        factoryDir = def_input

    def_input = 1000
    distance = input("New distance [mm] (default: {}): ".format(def_input))
    if distance.strip().lower() in ["", "default"]:
        distance = def_input
    distance = float(distance)

    def_input = os.path.join(os.getcwd(), "EX04")
    exportDir = input(
        "Name of export directory (default: {}): ".format(def_input))
    if exportDir.strip().lower() in ["", "default"]:
        exportDir = def_input

    run_example_changeDistance(userSettingsDir, measurementLoc, factoryDir,
                               distance, exportDir)
