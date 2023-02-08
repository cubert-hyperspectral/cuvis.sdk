import os
import cuvis


lib_dir = os.getenv("CUVIS")
data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))


def run_example_reprocessMeasurement(userSettingsDir=os.path.join(data_dir, "settings"),
                                     measurementLoc=os.path.join(data_dir,
                                                                 "vegetation_000",
                                                                 "vegetation_000_000_snapshot.cu3"),
                                     darkLoc=os.path.join(data_dir,
                                                          "dark_000",
                                                          "dark_000_000_snapshot.cu3"),
                                     whiteLoc=os.path.join(data_dir,
                                                           "white_000",
                                                           "white_000_000_snapshot.cu3"),
                                     distanceLoc=os.path.join(data_dir,
                                                              "Calibration",
                                                              "distanceCalib__outside_000_002_snapshot16201220972486840.cu3"),
                                     factoryDir=os.path.join(data_dir, "factory"),
                                     outDir=os.path.join(os.getcwd(), "EX02")):

    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading measurement file...")
    mesu = cuvis.Measurement(measurementLoc)

    print("loading dark...")
    dark = cuvis.Measurement(darkLoc)
    print("loading white...")
    white = cuvis.Measurement(whiteLoc)
    print("loading dark...")
    distance = cuvis.Measurement(distanceLoc)

    print("Data 1 {} t={}ms mode={}".format(mesu.Name,
                                            mesu.IntegrationTime,
                                            mesu.ProcessingMode,
                                            ))

    print("loading calibration and processing context (factory)...")
    calibration = cuvis.Calibration(calibdir=factoryDir)
    processingContext = cuvis.ProcessingContext(calibration)

    print("set references...")
    processingContext.setReference(dark, "Dark")
    processingContext.setReference(white, "White")
    processingContext.setReference(distance, "Distance")

    modes = ["Raw",
             "DarkSubtract",
             "Reflectance",
             "SpectralRadiance"
             ]

    procArgs = cuvis.CubertProcessingArgs()
    saveArgs = cuvis.CubertSaveArgs(AllowOverwrite=True)

    for mode in modes:

        procArgs.ProcessingMode = mode
        isCapable = processingContext.isCapable(mesu, procArgs)

        if isCapable:
            print("processing to mode {}...".format(mode))
            processingContext.setProcessingArgs(procArgs)
            mesu = processingContext.apply(mesu)
            saveArgs.ExportDir = os.path.join(outDir, mode)
            mesu.save(saveArgs)

        else:
            print("Cannot process to {} mode!".format(mode))

    print("finished.")

    pass


if __name__ == "__main__":

    print("Example 02: Reprocess Measurement. Please provide:")

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

    def_input = os.path.join(data_dir,
                             "dark_000",
                             "dark_000_000_snapshot.cu3")
    darkLoc = input("Dark file (.cu3) (default: {}): ".format(def_input))
    if darkLoc.strip().lower() in ["", "default"]:
        darkLoc = def_input

    def_input = os.path.join(data_dir,
                             "white_000",
                             "white_000_000_snapshot.cu3")
    whiteLoc = input("White file (.cu3) (default: {}): ".format(def_input))
    if whiteLoc.strip().lower() in ["", "default"]:
        whiteLoc = def_input

    def_input = os.path.join(data_dir,
                             "Calibration",
                             "distanceCalib__outside_000_002_snapshot16201220972486840.cu3")
    distanceLoc = input("Distance file (.cu3) (default: {}): ".format(def_input))
    if distanceLoc.strip().lower() in ["", "default"]:
        distanceLoc = def_input

    def_input = os.path.join(data_dir, "factory")
    factoryDir = input("Factory directory (default: {}): ".format(def_input))
    if factoryDir.strip().lower() in ["", "default"]:
        factoryDir = def_input

    def_input = os.path.join(os.getcwd(), "EX02")
    outDir = input("Name of output directory (default: {}): ".format(def_input))
    if outDir.strip().lower() in ["", "default"]:
        outDir = def_input

    run_example_reprocessMeasurement(userSettingsDir,
                                     measurementLoc,
                                     darkLoc,
                                     whiteLoc,
                                     distanceLoc,
                                     factoryDir,
                                     outDir)
