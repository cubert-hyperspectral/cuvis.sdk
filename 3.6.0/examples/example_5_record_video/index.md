# Cuvis Python SDK Example 5

## Record and Show a Video using the Worker Class

This example applies principles introduced in the previous examples to set up a comprehensive real-time hyperspectral video recording and processing pipeline. The *Worker* class is introduced, which enables efficient use of the classes needed to acquire, process and save measurements.

**Used principles:**

- *SessionFile* to load a camera calibration
- *AcquisitionContext* to communicate with the camera and acquire measurments
- *ProcessingContext* to compute hyperspectral cubes
- *CubeExporter* to save measurements to disk
- *Viewer* to generate visualizations of the hyperspectral cube
- *Userplugin* to define the visualization of the hyperspectral cube
- *Worker* to tie everything together to a managed processing pipeline

**Step-by-Step outline:**

1. Import and initialize Cuvis SDK
1. Load the calibration file for your camera using *SessionFile*
1. Connect and initialize your camera using the *AcquisitionContext*
1. Set up the computation of the hyperspectral cubes using *ProcessingContext*
1. Set up saving to disk of the video using *CubeExporter*
1. Set up the visualization of the measurements using *Viewer* and *Userplugin*
1. Configure the processing and recording pipeline using *Worker*
1. Record a hyperspectral video

**Prerequisites to running this example:**

- Have a camera connected *or* downloaded the provided [demo data](https://cloud.cubert-gmbh.de/s/SDKSampleData)
- Have the camera calibration file (*SN*.cu3c) ready *or* use the [demo data](https://cloud.cubert-gmbh.de/s/SDKSampleData)
- Have the Cuvis SDK installed
- Have Python and the requirements.txt installed

```
#%matplotlib widget
# If the import of cuvis fails, the most common cause is a mismatch between
# the _cuvis_ python package and the installed version of the Cuvis SDK.
# Try re-installing both and make sure that the version numbers match exactly
import cuvis
import time
import io
import os
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from PIL import Image as PILImage
print("Cuvis Python SDK Example 5")

# Initialize the Cuvis SDK using a settings-directory
# This is optional (all settings have defaults),
# but enables you to optimize Cuvis' performance on your system using the settings
# Your camera and the default Cuvis installation both provide these settings files
print("Initializing Cuvis")
cuvis.General.init("./settings")

# Video recording setup / User input
# Enter your data here!
video_integration_time_ms = 100
video_fps = 2
video_number = 1 # For naming the video files
video_processing_mode = cuvis.ProcessingMode.Raw
visualization_user_plugin_path = "./plugins/00_RGB.xml"
enable_pansharpening = True
save_directory = "./output/" # directory to save the measurements to here

video_filename = "MyHyperspectralVideo"
camera_serial_number_str = "Your Cameras Serial Number"

# If using demo data instead of a physical camera, change this to your download location:
has_camera = False

demo_session_file = "./SDK_Training_Example_Data/WinterUlm_X20P.cu3s"
import os
assert os.path.exists(demo_session_file), F"Demo session file not found: {demo_session_file}"

camera_calibration_file_path = F"./factory/{camera_serial_number_str}.cu3c"
```

______________________________________________________________________

#### Set up Camera

- Load calibration file
- Initialize *AcquisitionContext*
- Wait for camera to report **ready**
- Parametrize *AcquisitionContext* with recording parameters

```
# If working with a physical camera, use these two lines
if has_camera:
    calib = cuvis.SessionFile(camera_calibration_file_path)
    acq_cont = cuvis.AcquisitionContext(calib)

# If you don't have a physical camera and want to simulate one, use these two lines. Uncomment the above
else:
    calib = cuvis.SessionFile(demo_session_file)
    acq_cont = cuvis.AcquisitionContext(calib, simulate=True)

# Wait for camera connection to be established
print("Connecting with camera")
while(not acq_cont.ready):
    time.sleep(1)
    print(".", end="")
print("\nCamera connected!")
time.sleep(0.5)
# Set up recording parameters
acq_cont.operation_mode = cuvis.OperationMode.Internal
acq_cont.set_continuous(False)  # Pause video stream for now
acq_cont.integration_time = video_integration_time_ms
acq_cont.fps = video_fps
print("Camera ready!")
```

______________________________________________________________________

#### Set up ProcessingContext and Export

- Initialize and configure *ProcessingContext*
- Create and configure *CubeExporter*

```
# Create ProcessingContext
print("Loading processing context...")
proc_cont = cuvis.ProcessingContext(calib)
proc_cont.processing_mode = video_processing_mode
print("Done!")

# Create CubeExporter
save_args = cuvis.SaveArgs(
    export_dir=save_directory,
    allow_overwrite=True,
    full_export=False,
    allow_drop=True)
cube_exporter = cuvis.CubeExporter(save_args)
```

______________________________________________________________________

#### Viewer

This class uses a *Userplugin* file to compute visualizations (RGB images) of hyperspectral input data (cubes). The *Viewer* is almost the same thing as the *ViewExporter* introduced in **Example 04 - Exporters**. The only real difference is: The *ViewExporter* immediately writes the generated visualizations to disk as `.tiff` files while the *Viewer* returns these images in memory for immediate use in your application. The results are returned using the class *ImageData*. *ImageData* contains the following attributes:

- `width`, `height` and `channels`, define the image's dimensions
- `array` points to the actual data as a **numpy** array
- `wavelength` is a list that maps the image's channels to a physical wavelength, if applicable

The *Viewer* is configured similarly to the *ViewExporter* with some differences. Here is an overview of some useful settings:

- `userplugin`: Either the path to the *UserPlugin* `.xml` file or a valid XML string of a *UserPlugin*
- `pan_failback`: Controls the behavior if no cube is available. If `True`, allows using the panchromatic or preview image to be used as a fallback output. Else, throws an exception instead.
- Pan Sharpening Settings (`pan_scale`, `pan_sharpening_interpolation_type`, `pan_sharpening_algorithm`, `pre_pan_sharpen_cube`): See Example 4

```
# Create Viewer
view_args = cuvis.ViewerSettings(
    userplugin=visualization_user_plugin_path,
    pan_scale=1.0 if enable_pansharpening else 0.0)
viewer = cuvis.Viewer(view_args)
```

______________________________________________________________________

#### Worker

The *Worker* is a class that implements a processing and/or recording pipeline. It manages the acquisition of measurements from the *AcquisitionContext* and manages handing them to further processing and/or exporting steps as you define them. This allows your application code to avoid dealing with asynchronous processing and resource management (compute, threads). Using settings files and parameters in its constructor, you can define some characteristics of the *Worker*, eg. how many threads it will occupy at maximum.

A typical *Worker* setup looks like this:

Worker`[AcquisitionContext -> CubeExporter -> ProcessingContext -> Viewer]`-> View Results

Alternatively, measurements can be "manually" inserted into the *Worker*. For this to work, the *Worker* must not have an *AcquisitionContext* set and the `input_queue_size` must be set to larger than zero.

The following settings are available for the *Worker*:

- `input_queue_size`: When not using an *AcquisitionContext* as the source of measurements, you can also **ingest** measurements directly into the *Worker*. This parameter defines the size of the input queue for "manually" inserted measurements.
- `mandatory_queue_size`: Defines the number of measurements that can be processed at the same time. This "work pool" handles the "mandatory" steps, like exporting and computing the hyperspectral cube.
- `supplementary_queue_size`: Generally should be set to the same value as `mandatory_queue_size`. This "work pool" handles the "supplementary" steps, such as view generation and computing the hyperspectral cube, if the cube is not required for the export step.
- `output_queue_size`: The number of measurements that the *Worker* will hold onto in its output buffer, before dropping or stalling. Should at least be `mandatory_queue_size` + `supplementary_queue_size` + 1.
- `can_skip_measurements`: Whether incoming measurements can be dropped if the input queue is full.
- `can_skip_supplementary_steps`: Whether measurements can be dropped after they have been exported if the system is overloaded.
- `can_drop_results`: Whether results (processed measurements) can be dropped if the output buffer is full.

```
# Create a Worker
worker_args = cuvis.WorkerSettings(
    input_queue_size=0,                # Default: 0
    mandatory_queue_size=2,            # Default: 4
    supplementary_queue_size=2,        # Default: 4
    output_queue_size=10,              # Default: 10
    can_skip_measurements=True,        # Default: False
    can_skip_supplementary_steps=True, # Default: True
    can_drop_results=True)             # Default: True
worker = cuvis.Worker(worker_args)

# Configure the worker
worker.set_acquisition_context(acq_cont)
worker.set_processing_context(proc_cont)
worker.set_exporter(cube_exporter)
worker.set_viewer(viewer)

# Helper Function
def show_next_frame(frame, fmt='jpeg', jpeg_quality=85):
    arr = np.asarray(frame)
    if arr.ndim == 2:
        arr = np.repeat(arr[..., None], 3, axis=2)
    if arr.shape[-1] == 4:
        arr = arr[..., :3]
    if arr.dtype != np.uint8:
        arr = np.clip(arr, 0, 255).astype(np.uint8)

    buf = io.BytesIO()
    if fmt == 'jpeg':
        PILImage.fromarray(arr).save(buf, format='JPEG', quality=jpeg_quality)
    else:
        PILImage.fromarray(arr).save(buf, format='PNG')
    img.value = buf.getvalue()
```

______________________________________________________________________

#### Run Worker Pipeline

To start/stop the worker pipeline, a simple procedure should be followed to avoid measurements being stuck in buffers or queues.

Starting the pipeline:

1. Start the *Worker*
1. Start the video stream of the camera

Stopping the pipeline:

1. Stop the video stream of the camera
1. Stop the *Worker*
1. Clear all measurements from the *Worker*

```
# Video duration in seconds
video_duration_s = 10

print("Starting pipeline...")
worker.start_processing()
# Name the video
acq_cont.session_info = cuvis.SessionData(video_filename, video_number, 0)
acq_cont.set_continuous(True)

# Show image in notebook
img = widgets.Image(format='jpeg')  # or 'png'
img.layout = widgets.Layout(border='1px solid #ddd', width='auto')
display(img)

print("Acquiring...")
# Run recording for video_duration_s seconds
start_time_ns = time.time_ns()
end_time_ns = start_time_ns + video_duration_s * 1e9 # convert to ns
while time.time_ns() < end_time_ns:
    # Check if worker has a result
    if worker.has_next_result():
        # Fetch and display it 
        result = worker.get_next_result(timeout=100) # timeout is in ms
        show_next_frame(result.view.array)
    else:
        time.sleep(0.1)

print("Stopping pipeline...")
acq_cont.set_continuous(False)
worker.stop_processing()
worker.drop_all_queued()

# Check recorded file
filepath = os.path.join(save_directory, video_filename + F"_{video_number:03}.cu3s")
video_number += 1
if not os.path.exists(filepath):
    print("Video file not found...")
else:
    sess = cuvis.SessionFile(filepath)
    print(F"Recorded {sess.get_size()} measurements in file: {filepath}")
```
