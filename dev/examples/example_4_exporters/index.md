# Cuvis Python SDK Example 4

## Export / Convert Cubert Measurements to Different File Formats

This example provides information on the exporter classes and the file formats which they can convert measurements to.

**Used principles:**

- *SessionFile* as a source for measurements
- *CubeExporter* for saving measurements
- *TiffExporter* for exporting to TIFF format
- *EnviExporter* for exporting to ENVI format
- *ViewExporter* for exporting rendered views of the data
- *UserPlugins* to define how a view is computed

**Step-by-Step outline:**

1. Load measurements from a *SessionFile*
1. Re-export as a *SessionFile* with different settings
1. Export to TIFF
1. Export to ENVI
1. Load a *UserPlugin*
1. Export a rendered view of a measurement as described by a *UserPlugin*

**Prerequisites to running this example:**

- Have recorded a *SessionFile* (.cu3s) *or* downloaded the provided [demo data](https://cloud.cubert-gmbh.de/s/SDKSampleData)
- Have the Cuvis SDK installed
- Have Python and the requirements.txt installed

```
# If the import of cuvis fails, the most common cause is a mismatch between
# the _cuvis_ python package and the installed version of the Cuvis SDK.
# Try re-installing both and make sure that the version numbers match exactly
import cuvis
import time
from matplotlib import pyplot as plt
print("Cuvis Python SDK Example 4")

# Initialize the Cuvis SDK using a settings-directory
# This is optional (all settings have defaults),
# but enables you to optimize Cuvis' performance on your system using the settings
# Your camera and the default Cuvis installation both provide these settings files
print("Initializing Cuvis")
cuvis.General.init("./settings")

# Enter a path to the SessionFile you want to use
session_file_path = "./SDK_Training_Example_Data/WinterUlm_X20P.cu3s"
import os
assert os.path.exists(session_file_path), F"Session file '{session_file_path}' not found"

# Load the SessionFile
print(F"Loading Session File '{session_file_path}'")
session = cuvis.SessionFile(session_file_path)

# Load the first measurement of the file
mesu = session.get_measurement(0)
print(F"Loaded measurement at index 0 as {mesu.name}")
```

______________________________________________________________________

#### Cube Exporter - Settings (*SaveArgs*)

When setting up a *CubeExporter* there are many settings to fine-tune the export process and define what gets saved. The *SaveArgs* class is used to communicate the settings to the *CubeExporter*.

Here is an overview of the most important attributes of *SaveArgs*:

- `export_dir`: The directory to export the measurements to

- `allow_overwrite`: Allow overwriting files in case of a name clash

- `merge_mode`: Controls behavior regarding *SessionFile* creation. Possible values:

  - `Default`: Save measurements into a single *SessionFile*
  - `Fragmentation`: Start a new *SessionFile* for each measurement / Allow only one measurement per *SessionFile*
  - `Merge`: Save measurements into a single *SessionFile*, even if coming from different source files / sessions.

- `allow_drop`: Allow the exporter to drop measurements if it cannot write to the disk fast enough

- `allow_info_file`: Create an info file alongside the *SessionFile*. This file contains a list of all measurements in the *SessionFile* and also marks dropped measurements

- `full_export`: Include the hyperspectral cube when saving to disk. This is **FALSE** by default! *Please note:* The cube can **always be recomputed** on demand from the data stored in the *SessionFile*. Saving the cube can make sense to speed up or allow access to cube data on systems with low or insufficient processing power. It does significantly increase the size of the *SessionFiles*, usually roughly 2x. Additionally, if the cube is included, the processing mode (RAW, Reflectance, ...) is preserved.

```
# Create a CubeExporter with custom settings.
# Notably: full_export = True 
save_args_full = cuvis.SaveArgs(
    export_dir="cube_export", # Default: "."
    allow_overwrite=True,     # Default: False
    allow_drop=False,         # Default: False
    allow_info_file=True,     # Default: True
    full_export=True)         # Default: False

cube_exporter_full = cuvis.CubeExporter(save_args_full)

# First make sure, that the measurement has a cube
if mesu.processing_mode == cuvis.ProcessingMode.Preview:
    pc = cuvis.ProcessingContext(session)
    pc.processing_mode = cuvis.ProcessingMode.Raw
    pc.apply(mesu)

# Now export a measurement including the cube
cube_exporter_full.apply(mesu)
```

______________________________________________________________________

#### TIFF Exporter

The *TiffExporter* is used to export hyperspectral cubes (or parts thereof) in *.tiff* (*.tif*) format. As the TIFF format is fairly flexible, three general modes are available:

- MultiChannel: The cube is stored as a single image in a single file with each wavelength band as a seperate channel
- MultiPage: The cube is stored as multiple single channel (monochrome) images in a single file. Each wavelength band is a separate "page" within the TIFF file.
- Single: The cube is stored as a multiple single channel (monochrome) image in multiple files. Each wavelength band is a separate TIFF file.

The TIFF export mode is set via the *TiffExportSettings* class when creating the *TiffExporter*. Here is an overview of further useful settings:

- `export_dir`: The directory to export the measurements to
- `channel_selection`: Select which wavelength bands are included in the export by their wavelength [nm] value. This is set via string using a selection syntax. Here are some valid examples:
- Include only the channel at 400nm: "400"
- Include channels at 400, 410 and 620nm: "400;410;620"
- Include all channels from 400 to 500nm (both exclusive): "400-500"
- Include the channels 400 to 500nm and channel at 600nm: "400-500;600"
- Include all channels: "all"
- Include the channels between 400 and 600nm in 20nm steps: "400:20:600"
- `compression_mode`: Which compression scheme to use. To enable compression, set to `TiffCompressionMode.LZW`.
- `format`: Which TIFF export mode to use. Default: `TiffFormat.MultiChannel`

```
# Create a tiff exporter with custom settings
# Here: Export only the channels between 600nm and 800nm as separate files with compression to directory "tiff_export"
save_args_tiff = cuvis.TiffExportSettings(
    export_dir="tiff_export",                       # Default: "."
    channel_selection="600-800",                    # Default: "all"
    compression_mode=cuvis.TiffCompressionMode.LZW, # Default: TiffCompressionMode.Nothing
    format=cuvis.TiffFormat.Single)                 # Default: TiffFormat.MultiChannel

tiff_exporter = cuvis.TiffExporter(save_args_tiff)

# First make sure that the measurement has a cube
if mesu.processing_mode == cuvis.ProcessingMode.Preview:
    pc = cuvis.ProcessingContext(session)
    pc.processing_mode = cuvis.ProcessingMode.Raw
    pc.apply(mesu)

# Now export a measurement including the cube to tiff format
tiff_exporter.apply(mesu)
```

______________________________________________________________________

#### ENVI Exporter

For the *EnviExporter* only some basic settings are available. This exporter will create two files per measurement: A `.hdr` file and a data file with the same name but without a file extension. `export_dir` and `channel_selection` apply the same as for *TiffExportSettings* above.

```
# Create an ENVI exporter with custom settings
save_args_envi = cuvis.EnviExportSettings(
    export_dir="envi_export", # Default: "."
    channel_selection="all"   # Default: "all"
)

envi_exporter = cuvis.EnviExporter(save_args_envi)

# First make sure that the measurement has a cube
if mesu.processing_mode == cuvis.ProcessingMode.Preview:
    pc = cuvis.ProcessingContext(session)
    pc.processing_mode = cuvis.ProcessingMode.Raw
    pc.apply(mesu)

# Now export a measurement including the cube to envi format
envi_exporter.apply(mesu)
```

______________________________________________________________________

#### View Exporter

The *ViewExporter* enables rendering and exporting views of the cube data, ie. RGB, Color Infrared, or indices like NDVI. The views are always RGB images. How the view is rendered / computed, is described in using a *UserPlugin* - an XML file with a special syntax that describes data accesses and mathematical operations used to compute the view. These files are described in more detail below.

The *ViewExporter* is initialized with the class *ViewExportSettings*, like the other exporters. Here is an overview of some useful settings:

- `export_dir` and `channel_selection`: Same as for *TiffExportSettings* above
- `userplugin`: Either the path to the *UserPlugin* `.xml` file or a valid XML string of a *UserPlugin*
- `pan_failback`: Controls the behavior if no cube is available. If `True`, allows using the panchromatic or preview image to be used as a fallback output. Else, throws an exception instead.

#### User Plugins

The *UserPlugin* is a XML schema definition for how a hyperspectral cube is accessed and processed to compute a regular RGB image from it. You can find the XML schema in your Cuvis installation under `Cuvis/user/plugin/userplugin.xsd`

A selection of plugins is provided with your installation of Cuvis under `Cuvis/user/plugin`. The plugins differ slightly between processing modes, as some may only be applicable to, e.g. reflectance data. For further information on *UserPlugins*, their syntax and the available operators, please refer to the *Cuvis User Plug-Ins manual* PDF included with your Cuvis installation.

```
# Create a view exporter with custom settings
save_args_view = cuvis.ViewExportSettings(
    export_dir="view_export", # Default: "."
    channel_selection="all",  # Default: "all"
    pan_failback=True,        # Default: True
    # Please enter the path to your Cuvis installation below
    #userplugin="Your Cuvis Install here" + "/user/plugin/raw/00_RGB.xml") # Default: ""
    userplugin="C:/Program Files/Cuvis/user/plugin/raw/00_RGB.xml") # Default: ""

view_exporter = cuvis.ViewExporter(save_args_view)

# First make sure that the measurement has a cube
if mesu.processing_mode == cuvis.ProcessingMode.Preview:
    pc = cuvis.ProcessingContext(session)
    pc.processing_mode = cuvis.ProcessingMode.Raw
    pc.apply(mesu)

# Now export a measurement to a rendered view RGB image
view_exporter.apply(mesu)
```

______________________________________________________________________

#### View Exporter - Pansharpening

This is only applicable to cameras with a separate panchromatic sensor installed (e.g. Ultris X20P).

The process of Pan-Sharpening fuses the hyperspectral cube data (high spectral resolution) with the panchromatic image (high spatial resolution) to create a merged hyperspectral cube with much higher spatial resolution.

Pan-Sharpening can be applied with any exporter by enabling the setting `pre_pan_sharpen_cube` in their respective settings class. *Please note*: Applying Pan-Sharpening to the entire cube uses a large amount of system resources and may lead to long processing times!

When using Pan-Sharpening with the *ViewExporter*, the operation can be applied *after* the view is rendered to dramatically reduce the processing overhead. To compute a spectrally more accurate view, the setting `pre_pan_sharpen_cube` can also be used with the *ViewExporter*.

Here is an overview of the settings available that pertain to Pan-Sharpening:

- `pan_scale`: The "amount" of Pan-Sharpening to apply. 0.0 = no Pan-Sharpening. 1.0 = Pan-Sharpen to the resolution of the pan image. 0.5 = Pan-Sharpen to the resolution 50% between the spectral and pan images.
- `pan_sharpening_interpolation_type`: Which upscaling method to use for resizing operations. Uses `cuvis.PanSharpeningInterpolationType`.
- `pan_sharpening_algorithm`: Which algorithm to use for the Pan-Sharpening operation. The following are available:
- `PanSharpeningAlgorithm.None`: Only upscale, no sharpening is applied
- `PanSharpeningAlgorithm.CubertPanRatio`: Uses the pan sensors White reference for best results. Only applicable in Reflectance processing mode.
- `PanSharpeningAlgorithm.CubertMacroPixel`: Uses mean brightness information from the pan image to refine the spectral image. Works in all modes without references.
- `pre_pan_sharpen_cube`: Apply Pan-Sharpening over the entire hyperspectral data cube. *Please note*: Large performance impact!
- `add_pan`: Whether to include the pan image in the final hyperspectral data cube. It will be labeled as wavelength = 0nm.

```
# Create a view exporter with pansharpening enabled
save_args_pansharpen = cuvis.ViewExportSettings(
    export_dir="pansharpen_export",                # Default: "."
    channel_selection="all",                       # Default: "all"
    pan_scale=1.0,                                 # Default: 0.0
    pan_sharpening_interpolation_type=cuvis.PanSharpeningInterpolationType.Cubic, # Default: Linear 
    pan_sharpening_algorithm=cuvis.PanSharpeningAlgorithm.CubertPanRatio, # Default: CubertMacroPixel
    pre_pan_sharpen_cube=False,                    # Default: False 
    add_pan=False,                                 # Default: False
    pan_failback=True,                             # Default: True
    # Please enter the path to your Cuvis installation below
    #userplugin="Your Cuvis Install here" + "/user/plugin/raw/00_RGB.xml") # Default: ""
    userplugin="C:/Program Files/Cuvis/user/plugin/raw/00_RGB.xml") # Default: ""

pansharpen_exporter = cuvis.ViewExporter(save_args_pansharpen)

# First make sure that the measurement has a cube
if mesu.processing_mode == cuvis.ProcessingMode.Preview:
    pc = cuvis.ProcessingContext(session)
    pc.processing_mode = cuvis.ProcessingMode.Raw
    pc.apply(mesu)

# Now export a measurement to a pan-sharpened rendered view RGB image
pansharpen_exporter.apply(mesu)
```
