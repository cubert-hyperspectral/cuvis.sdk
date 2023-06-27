import os
import platform

import matplotlib.pyplot as plt
import numpy as np

import cuvis

### default directories and files
data_dir = None

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk",
                                             "sample_data", "set_examples"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(
        os.path.join(lib_dir, "sample_data", "set_examples"))

# default image
loc_file = os.path.join(data_dir,
                        "set0_lab",
                        "x20_calib_color.cu3s")
# default settings
loc_settings = os.path.join(data_dir, "settings")


def run_example_loadMeasurement(
        userSettingsDir=loc_settings,
        measurementLoc=loc_file):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading session...")
    session = cuvis.SessionFile(measurementLoc)

    print("loading measurement file...")
    mesu = session.getMeasurement(0)
    assert mesu.__handle__

    print("Data 1 {} t={}ms mode={}".format(mesu.Name,
                                            mesu.IntegrationTime,
                                            mesu.ProcessingMode,
                                            ))

    # TODO: use correct flags when Measurement provides them

    if isinstance(mesu.MeasurementFlags, list) and \
            len(mesu.MeasurementFlags) > 0:
        print("Flags")
        for flag in mesu.MeasurementFlags:
            print(" - {} ({})".format(flag, flag))
            # supposed to be first and second

    assert mesu.ProcessingMode == "Raw", \
        "This example requires Raw mode!"

    cube = mesu.Data.get("cube", None)
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

    userSettingsDir = input(
        "User settings directory (default: {}): ".format(loc_settings))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = loc_settings

    measurementLoc = input(
        "Measurement file (.cu3s) (default: {}): ".format(loc_file))
    if measurementLoc.strip().lower() in ["", "default"]:
        measurementLoc = loc_file

    run_example_loadMeasurement(userSettingsDir, measurementLoc)
