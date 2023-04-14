import os
import cuvis
import platform
import matplotlib.pyplot as plt
import numpy as np

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(os.path.join(lib_dir, "sample_data", "set1"))

def run_example_loadMeasurement(userSettingsDir=os.path.join(data_dir, "settings"),
                                measurementLoc=os.path.join(data_dir,
                                                            "vegetation_000",
                                                            "vegetation_000_000_snapshot.cu3")):

    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading measurement file...")
    mesu = cuvis.Measurement(measurementLoc)
    print("Data 1 {} t={}ms mode={}".format(mesu.Name,
                                            mesu.IntegrationTime,
                                            mesu.ProcessingMode,
                                            ))

    # TODO: use correct flags when Measurement provides them
    if not isinstance(mesu.MeasurementFlags, list):
        mesu.MeasurementFlags = [mesu.MeasurementFlags]

    if len(mesu.MeasurementFlags) > 0:
        print("Flags")
        for flag in mesu.MeasurementFlags:
            print(" - {} ({})".format(flag, flag)) # TODO: just 0/1?!

    assert mesu.ProcessingMode == "Raw", \
        "This example requires Raw mode!"

    cube = mesu.Data.pop("cube", None)
    if cube is None:
        raise Exception("Cube not found")

    x = 120
    y = 200

    assert x < cube.width, "x index exceeds cube width!"
    assert y < cube.height, "y index exceeds cube height!"

    lambda_wl = []
    raw_counts = []
    for chn in np.arange(cube.channels):
        lambda_wl.append(cube.wavelength[chn])
        raw_counts.append(cube.array[x, y, chn])

    plt.plot(lambda_wl, raw_counts)
    plt.xlabel("lambda [nm]")
    plt.ylabel("raw counts [au]")
    plt.title("Spectrum of {} for x={}, y={}".format(mesu.Name, x, y))
    plt.show()

    print("finished.")
    pass


if __name__ == "__main__":

    print("Example 01: Load Measurement. Please provide:")

    def_input = os.path.join(data_dir, "settings")
    userSettingsDir = input("User settings directory (default: {}): ".format(def_input))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = def_input

    def_input = os.path.join(data_dir,
                             "vegetation_000",
                             "vegetation_000_000_snapshot.cu3")
    measurementLoc = input("Measurement file (.cu3) (default: {}): ".format(def_input))
    if measurementLoc.strip().lower() in ["", "default"]:
        measurementLoc = def_input

    run_example_loadMeasurement(userSettingsDir, measurementLoc)
