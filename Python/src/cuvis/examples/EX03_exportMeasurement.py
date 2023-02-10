import os
import cuvis
import platform

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "set1"))
    plugin_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk", "sample_data", "userplugin"))
elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(os.path.join(lib_dir, "sample_data", "set1"))
    plugin_dir = os.path.normpath(os.path.join(lib_dir, "sample_data", "userplugin"))


def run_example_exportMeasurement(userSettingsDir=os.path.join(data_dir, "settings"),
                                  measurementLoc=os.path.join(data_dir,
                                                              "vegetation_000",
                                                              "vegetation_000_000_snapshot.cu3"),
                                  pluginLoc=os.path.join(plugin_dir, "cai.xml"),
                                  exportDir=os.path.join(os.getcwd(), "EX03")):

    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading measurement file...")
    mesu = cuvis.Measurement(measurementLoc)

    assert mesu.ProcessingMode != "Preview", "Wrong processing mode: {}".format(mesu.ProcessingMode)

    print("Export to Envi...")
    envi_settings = cuvis.EnviExportSettings(ExportDir=os.path.join(exportDir, "envi"))
    enviExporter = cuvis.EnviExporter(envi_settings)
    enviExporter.apply(mesu)

    print("Export to Multi-Channel Tiff...")
    multi_tiff_settings = cuvis.TiffExportSettings(ExportDir=os.path.join(exportDir, "multi"), Format="MultiChannel")
    multiTiffExporter = cuvis.TiffExporter(multi_tiff_settings)
    multiTiffExporter.apply(mesu)

    print("Export to separate Tiffs...")
    single_tiff_settings = cuvis.TiffExportSettings(ExportDir=os.path.join(exportDir, "single"), Format="Single")
    singleTiffExporter = cuvis.TiffExporter(single_tiff_settings)
    singleTiffExporter.apply(mesu)

    print("Export View to file...")

    with open(pluginLoc) as f:
        userpluginCai = f.readlines()
    userpluginCai = "".join(userpluginCai)

    view_export_settings = cuvis.ViewExportSettings(ExportDir=os.path.join(exportDir, "view"), Userplugin=userpluginCai)
    # also view_export_settings = cuvis.ViewExportSettings(ExportDir=os.path.join(exportDir, "view"),
    # Userplugin=pluginLoc) works!
    viewExporter = cuvis.ViewExporter(view_export_settings)
    viewExporter.apply(mesu)

    pass


if __name__ == "__main__":

    print("Example 03: Export Measurement. Please provide:")

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

    def_input = os.path.join(plugin_dir, "cai.xml")
    pluginLoc = input("User plugin file (.xml) (default: {}): ".format(def_input))
    if pluginLoc.strip().lower() in ["", "default"]:
        pluginLoc = def_input

    def_input = os.path.join(os.getcwd(), "EX03")
    exportDir = input("Name of export directory (default: {}): ".format(def_input))
    if exportDir.strip().lower() in ["", "default"]:
        exportDir = def_input

    run_example_exportMeasurement(userSettingsDir, measurementLoc, pluginLoc, exportDir)
