import os
import platform

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

# default images
loc_file = os.path.join(data_dir,
                        "set4_tractor",
                        "raw.cu3s")
loc_dark = os.path.join(data_dir,
                        "set4_tractor",
                        "dark.cu3s")
loc_white = os.path.join(data_dir,
                         "set4_tractor",
                         "white.cu3s")
loc_distance = os.path.join(data_dir,
                            "set4_tractor",
                            "distance.cu3s")

# default settings
loc_settings = os.path.join(data_dir, "settings")

# default output
loc_output = os.path.join(os.getcwd(), "EX02_reprocessed")


def run_example_reprocessMeasurement(
        userSettingsDir=loc_settings,
        measurementLoc=loc_file,
        darkLoc=loc_dark,
        whiteLoc=loc_white,
        distanceLoc=loc_distance,
        outDir=loc_output):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading measurement file...")
    sessionM = cuvis.SessionFile(measurementLoc)
    mesu = sessionM.getMeasurement(0)
    assert mesu.__handle__

    print("loading dark...")
    sessionDk = cuvis.SessionFile(darkLoc)
    dark = sessionDk.getMeasurement(0)
    assert dark.__handle__

    print("loading white...")
    sessionWt = cuvis.SessionFile(whiteLoc)
    white = sessionWt.getMeasurement(0)
    assert white.__handle__

    print("loading distance...")
    sessionDc = cuvis.SessionFile(distanceLoc)
    distance = sessionDc.getMeasurement(0)
    assert distance.__handle__

    print("Data 1 {} t={}ms mode={}".format(mesu.Name,
                                            mesu.IntegrationTime,
                                            mesu.ProcessingMode,
                                            ))

    print("loading processing context...")
    processingContext = cuvis.ProcessingContext(sessionM)

    print("set references...")
    processingContext.setReference(dark, "Dark")
    processingContext.setReference(white, "White")
    processingContext.setReference(distance, "Distance")

    procArgs = cuvis.CubertProcessingArgs()
    saveArgs = cuvis.CubertSaveArgs(AllowOverwrite=True,
                                    AllowSessionFile=True,
                                    AllowInfoFile=False)

    modes = ["Raw",
             "DarkSubtract",
             "Reflectance",
             "SpectralRadiance"
             ]

    for mode in modes:

        procArgs.ProcessingMode = mode

        if processingContext.isCapable(mesu, procArgs):
            print("processing to mode {}...".format(mode))
            processingContext.setProcessingArgs(procArgs)
            mesu = processingContext.apply(mesu)
            mesu.setName(mode)
            saveArgs.ExportDir = os.path.join(outDir, mode)
            exporter = cuvis.Export.CubeExporter(saveArgs)
            exporter.apply(mesu)

        else:
            print("Cannot process to {} mode!".format(mode))

    print("finished.")

    pass


if __name__ == "__main__":

    print("Example 02: Reprocess Measurement. Please provide:")

    userSettingsDir = input(
        "User settings directory (default: {}): ".format(loc_settings))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = loc_settings

    measurementLoc = input(
        "Measurement file (.cu3s) (default: {}): ".format(loc_file))
    if measurementLoc.strip().lower() in ["", "default"]:
        measurementLoc = loc_file

    darkLoc = input("Dark file (.cu3s) (default: {}): ".format(loc_dark))
    if darkLoc.strip().lower() in ["", "default"]:
        darkLoc = loc_dark

    whiteLoc = input("White file (.cu3s) (default: {}): ".format(loc_white))
    if whiteLoc.strip().lower() in ["", "default"]:
        whiteLoc = loc_white

    distanceLoc = input(
        "Distance file (.cu3s) (default: {}): ".format(loc_distance))
    if distanceLoc.strip().lower() in ["", "default"]:
        distanceLoc = loc_distance

    outDir = input(
        "Name of output directory (default: {}): ".format(loc_output))
    if outDir.strip().lower() in ["", "default"]:
        outDir = loc_output

    run_example_reprocessMeasurement(userSettingsDir,
                                     measurementLoc,
                                     darkLoc,
                                     whiteLoc,
                                     distanceLoc,
                                     outDir)
