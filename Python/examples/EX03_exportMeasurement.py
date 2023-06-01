import os
import platform

import cuvis

### default directories and files
data_dir = None
plugin_dir = None

if platform.system() == "Windows":
    lib_dir = os.getenv("CUVIS")
    data_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk",
                                             "sample_data", "set_examples"))
    plugin_dir = os.path.normpath(os.path.join(lib_dir, os.path.pardir, "sdk",
                                               "sample_data", "set_examples",
                                               "userplugin"))

elif platform.system() == "Linux":
    lib_dir = os.getenv("CUVIS_DATA")
    data_dir = os.path.normpath(
        os.path.join(lib_dir, "sample_data", "set_examples"))
    plugin_dir = os.path.normpath(os.path.join(lib_dir, "sdk",
                                               "sample_data", "set_examples",
                                               "userplugin"))

# default images
loc_file = os.path.join(data_dir,
                        "set4_tractor",
                        "complete.cu3s")
loc_plugin = os.path.join(plugin_dir, "cai.xml")

# default settings
loc_settings = os.path.join(data_dir, "settings")

# default output
loc_output = os.path.join(os.getcwd(), "EX03_export")


def run_example_exportMeasurement(userSettingsDir=loc_settings,
                                  measurementLoc=loc_file,
                                  pluginLoc=loc_plugin,
                                  exportDir=loc_output):
    print("loading user settings...")
    settings = cuvis.General(userSettingsDir)
    settings.setLogLevel("info")

    print("loading session file...")
    session = cuvis.SessionFile(measurementLoc)
    mesu = session.getMeasurement(0)
    assert mesu.__handle__

    assert mesu.ProcessingMode != "Preview", "Wrong processing mode: {}".format(
        mesu.ProcessingMode)

    print("Export to Envi...")
    envi_settings = cuvis.EnviExportSettings(
        ExportDir=os.path.join(exportDir, "envi"))
    enviExporter = cuvis.EnviExporter(envi_settings)
    enviExporter.apply(mesu)

    print("Export to Multi-Channel Tiff...")
    multi_tiff_settings = cuvis.TiffExportSettings(
        ExportDir=os.path.join(exportDir, "multi"), Format="MultiChannel")
    multiTiffExporter = cuvis.TiffExporter(multi_tiff_settings)
    multiTiffExporter.apply(mesu)

    print("Export to separate Tiffs...")
    single_tiff_settings = cuvis.TiffExportSettings(
        ExportDir=os.path.join(exportDir, "single"), Format="Single")
    singleTiffExporter = cuvis.TiffExporter(single_tiff_settings)
    singleTiffExporter.apply(mesu)

    print("Export View to file...")

    print("load plugin...")
    with open(pluginLoc) as f:
        userpluginCai = f.readlines()
    userpluginCai = "".join(userpluginCai)

    view_export_settings = cuvis.ViewExportSettings(
        ExportDir=os.path.join(exportDir, "view"), Userplugin=userpluginCai)
    # also view_export_settings = cuvis.ViewExportSettings(ExportDir=os.path.join(exportDir, "view"),
    # Userplugin=pluginLoc) works!
    viewExporter = cuvis.ViewExporter(view_export_settings)
    viewExporter.apply(mesu)

    pass


if __name__ == "__main__":

    print("Example 03: Export Measurement. Please provide:")

    userSettingsDir = input(
        "User settings directory (default: {}): ".format(loc_settings))
    if userSettingsDir.strip().lower() in ["", "default"]:
        userSettingsDir = loc_settings

    measurementLoc = input(
        "Measurement file (.cu3) (default: {}): ".format(loc_file))
    if measurementLoc.strip().lower() in ["", "default"]:
        measurementLoc = loc_file

    pluginLoc = input(
        "User plugin file (.xml) (default: {}): ".format(loc_plugin))
    if pluginLoc.strip().lower() in ["", "default"]:
        pluginLoc = loc_plugin

    exportDir = input(
        "Name of export directory (default: {}): ".format(loc_output))
    if exportDir.strip().lower() in ["", "default"]:
        exportDir = loc_output

    run_example_exportMeasurement(userSettingsDir, measurementLoc, pluginLoc,
                                  exportDir)
