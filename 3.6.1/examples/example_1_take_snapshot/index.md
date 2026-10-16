# Cuvis Python SDK Example 1

## Connect to camera and record a measurement

This example provides a minimal starting point to allow you to get a camera and data acquisition running.

**Used principles:**

- *AcquisitionContext* for camera control and data acquisition
- *SessionFile* as camera calibration file
- *CubeExporter* for saving measurements

**Step-by-Step outline:**

1. Import and initialize Cuvis SDK
1. Load the calibration file for your camera using *SessionFile*
1. Connect and initialize your camera using the *AcquisitionContext*
1. Acquire a measurement
1. Save the measurement to disk using the *CubeExporter*

**Prerequisites to running this example:**

- Have a camera connected *or* downloaded the provided [demo data](https://cloud.cubert-gmbh.de/s/SDKSampleData)
- Have the camera calibration file (*SN*.cu3c) ready *or* use the [demo data](https://cloud.cubert-gmbh.de/s/SDKSampleData)
- Have the Cuvis SDK installed
- Have Python and the requirements.txt installed

```
# If the import of cuvis fails, the most common cause is a mismatch between
# the _cuvis_ python package and the installed version of the Cuvis SDK.
# Try re-installing both and make sure that the version numbers match exactly
import cuvis
import time

print("Cuvis Python SDK Example 1")

# Initialize the Cuvis SDK using a settings-directory
# This is optional (all settings have defaults),
# but enables you to optimize Cuvis' performance on your system using the settings
# Your camera and the default Cuvis installation both provide these settings files
print("Initializing Cuvis")
cuvis.General.init("./settings")

# Snapshot setup / User input
# Enter your data here!
import os

snapshot_integration_time_ms = 100
save_directory = "./output" # set to a location where you want to save the data

has_camera = False  # Set to True if you have a camera connected
camera_serial_number_str = "Your camera serial here"

# If using demo data instead of a physical camera, change this to your download location:
demo_session_file = "./SDK_Training_Example_Data/WinterUlm_X20P.cu3s"
assert os.path.exists(demo_session_file), f"Demo session file not found: {demo_session_file}"

camera_calibration_file_path = F"./factory/{camera_serial_number_str}.cu3c"
```

______________________________________________________________________

#### Calibration Files (.cu3c)

This calibration file contains everything needed to connect to and process data from your camera. The **.cu3c** camera calibration file format is a special form of the SessionFile format **.cu3s**

It is thus used as a calibration file and usually contains (among other things):

- The actual encrypted camera calibration file
- A spectral radiance calibration file
- Test references (Dark and White)
- A standard camera recording configuration (framerate, integration time, etc.)

```
# Skip this if working without a physical camera
if has_camera:
    print("Load camera calibration file")
    calib = cuvis.SessionFile(camera_calibration_file_path)
```

______________________________________________________________________

#### Cube Exporter

To save measurements in the Cubert file format *SessionFile* (.cu3s), use the *CubeExporter*. Using *SessionFiles* to save measurements, is highly recommended, as it can store multiple raw measurements, reference measurements and meta-data all in one file, allowing you to re-process the measurements after the fact. This enables you to fine-tune the final product, convert the output format and even fix some mistakes made during data acquisition.

```
# Setup the Cube Exporter for saving the measurements to disk in the SessionFile format (.cu3s)
print("Create CubeExporter")
save_config = cuvis.FileWriteSettings.SaveArgs(export_dir=save_directory)
exporter = cuvis.CubeExporter(save_config)
```

______________________________________________________________________

#### Acquisition Context

The *Acquisition Context* is your interface to control the camera and all aspects of the data acquisition.

Initialize it using a *SessionFile* object, then set the recording parameters and start an acquisition. As soon as the **AcquisitionContext** is created, it will try to establish a connection with the camera.

Here, the "Software" operation mode is used to enable data acquisition using a software trigger. This is also called snapshot mode.

*Please note:* The *AcquisitionContext* will **only** connect to the **exact** camera of the same serial number matching the calibration file! All other cameras/devices are ignored.

```
# Skip this if working without a physical camera
if has_camera:
    # Create an AcquisitionContext to connect to the camera
    print("Loading Acquisition Context")
    acq = cuvis.AcquisitionContext(calib)

    # Wait for camera connection to be established
    print("Connecting with camera")
    while(not acq.ready):
        time.sleep(1)
        print(".", end="")
    print("\nCamera connected!")
    time.sleep(0.5)

    # Set camera to software trigger
    acq.operation_mode = cuvis.OperationMode.Software
    acq.integration_time = snapshot_integration_time_ms
```

______________________________________________________________________

#### Simulated Acquisition - great for testing without a camera

The *Acquisition Context* can be initialized with the **simulated** kwarg set to **True** to pretend it has a camera connected. In this mode, it will provide the measurements from a *SessionFile* as if they where received from a physically connected camera. Upon reaching the end of the file, it will loop back to the first measurement.

With this simulated camera, you can record and test your code as if a physical camera was connected. Some methods/attributes don't have any effect, as they cannot relay changes to a camera, eg. integration time, auto-exposure, gain, etc.

```
# Simulated Acquisition: Skip this if working with a physical camera
if not has_camera:
    session = cuvis.SessionFile(demo_session_file)
    # Initialize the Acquisition Context in simulated camera mode
    acq = cuvis.AcquisitionContext(session, simulate=True)

# Wait for the Acquisition Context to load the demo session file
print("Wait for Acqusition Context to be ready...")
while(not acq.ready):
    time.sleep(1)
    print(".", end="")
print("\nSimulated camera loaded!")

# Set simulated camera to software trigger
acq.operation_mode = cuvis.OperationMode.Software
```

______________________________________________________________________

#### Capturing a Measurement with Software Trigger (Single Snapshot)

Using the `capture()` method, a single measurement is initiated. Taking a snapshot requires some time, so, to prevent the call to `capture()` from blocking execution, an *AsyncMesu* is returned. To await the completion of the snapshot, use the `get()` method on the *AsyncMesu*.

```
# Optional: Name the recording
acq.session_info = cuvis.SessionData("My_Measurement", 0, 0)

# With the camera connection established, a measurement can be triggered using the capture() method.
# This returns an AsyncMesu object
async_mesu = acq.capture()

# To get the actual measurement, wait on the AsyncMesu using the get() method.
mesu, status = async_mesu.get(timeout_ms=5000)
print(F"Measurement reports: {status}")

# Export the measurement - write the data to the disk in SessionFile format using the CubeExporter
if status == cuvis.Async.AsyncResult.done:
    exporter.apply(mesu)
    print("Measurement exported!")
else:
    print("Something went wrong!")
```
