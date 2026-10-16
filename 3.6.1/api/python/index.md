# Python API Reference

The Python wrapper mirrors the C and C++ API concepts. Signatures shown here are derived from static analysis of the source; see the C/C++ API reference for full parameter-level documentation.

## General

## `cuvis.General`

### `init(settings_path='.', global_loglevel=logging.DEBUG, logfile_name=None)`

### `shutdown()`

### `version()`

### `set_log_level(lvl)`

## SessionFile

## `cuvis.SessionFile`

### `SessionFile`

Bases: `object`

#### `fps`

#### `hash`

#### `operation_mode`

#### `thumbnail`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__getitem__(key)`

#### `__init__(base)`

#### `__iter__()`

#### `__len__()`

#### `get_measurement(frameNo=0, itemtype=SessionItemType.no_gaps)`

#### `get_reference(frameNo, reftype)`

#### `get_size(itemtype=SessionItemType.no_gaps)`

## Measurement

## `cuvis.Measurement`

### `Measurement`

Bases: `object`

#### `assembly`

#### `averages`

#### `calibration_id`

#### `capabilities`

#### `capture_time`

Timezone-aware UTC instant; comparing it against a naive datetime raises TypeError.

#### `comment`

#### `cube`

Retrieves or processes the 'cube' data for this Measurement.

This property prioritizes convenience over strict design principles:

- Attempts to retrieve the 'cube' from `self.data`.
- Lazily initializes a `ProcessingContext` if a session is available but uninitialized.
- May trigger expensive processing and modify internal state during property access.

While functional, this approach introduces side effects and tight coupling, making it less predictable and not the cleanest solution. Suitable for specific workflows where these trade-offs are acceptable.

###### Raises

ValueError If the 'cube' is not available and processing is not possible.

###### Returns

ImageData The 'cube' data, either retrieved from `self.data` or generated through processing.

#### `data_count`

#### `distance`

#### `factory_calibration`

The calibration day, or None if the SDK reported a value datetime cannot hold.

Timezone-aware UTC, but only the day carries meaning. The SDK stores the day as midnight in the local time of the machine that wrote the file, so the time component is an artifact of that machine and the day can be off by one when the file is read in another timezone.

#### `frame_id`

#### `integration_time`

#### `measurement_flags`

#### `name`

#### `path`

#### `processing_mode`

#### `product_name`

#### `serial_number`

#### `session_info`

#### `thumbnail`

#### `__copy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

#### `__del__()`

#### `__init__(base)`

#### `clear_cube()`

#### `clear_implicit_reference(ref_type)`

#### `deepcopy()`

#### `get_cube(key='cube')`

Cube through whichever mode is active, so one call site serves both.

.. code-block:: python3

```
cube = mesu.get_cube()      # CudaImageData after cuda.enable(), else ImageData
```

With CUDA mode on (`cuvis.cuda.enable`) this is `get_cube_cuda` and raises when the device path is unavailable. There is deliberately no silent fallback to the host: a zero-copy path that quietly degrades to two copies is worse than an error, because the cost is invisible.

Parameters:

| Name  | Type  | Description                | Default  |
| ----- | ----- | -------------------------- | -------- |
| `key` | `str` | which image entry to read. | `'cube'` |

Returns:

| Type        | Description     |
| ----------- | --------------- |
| \`ImageData | CudaImageData\` |

#### `get_cube_cuda(key='cube')`

Image data as a device-resident CUDA buffer for same-process, zero-copy use.

.. code-block:: python3

```
from cuvis import cuda

if cuda.capabilities().same_process:
    cuda.enable()                       # BEFORE loading or processing
    tensor = mesu.get_cube_cuda().to_torch()
```

Returns a :class:`cuvis.CudaImageData` wrapping a CUVIS_CUDA_MEM handle; read it with `.to_torch()` (DLPack, which ties the buffer lifetime to the tensor) or through `__cuda_array_interface__` (which does not, so keep the CudaImageData alive). No host copy is made.

The cube must still be on the device, which it is only when `cuda.enable` was called before it was processed; the host fetch in `refresh` otherwise moves it to host memory and frees the device copy.

Parameters:

| Name  | Type  | Description                                                               | Default  |
| ----- | ----- | ------------------------------------------------------------------------- | -------- |
| `key` | `str` | which image entry to read, "cube" unless the measurement carries several. | `'cube'` |

Raises:

| Type                           | Description                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------- |
| `cuvis.UnavailableSDKFunction` | the installed cuvis library provides no CUDA support; call cuda.capabilities first to avoid this. |
| `cuvis.cuvis_aux.SDKException` | the image data is not device-backed.                                                              |

#### `get_cube_cuda_ipc(key='cube', backend=0)`

Image data as a shareable CUDA buffer for cross-process use.

Producer side; the consumer opens the payload with :mod:`cuvis_ipc`, which needs no SDK of its own.

.. code-block:: python3

```
cimg = mesu.get_cube_cuda_ipc()         # keep alive until the consumer is done
send(cimg.export_payload())            # descriptor + geometry, one blob

# ... in the consumer process, no cuvis installed ...
import cuvis_ipc
with cuvis_ipc.open(payload) as cube:
    tensor = cube.to_torch()
```

Fetches the device buffer with `get_cube_cuda` and creates an IPC export on it, filling `.descriptor` with the transportable bytes. The returned object is the in-process pin, since legacy IPC carries no cross-process refcount: drop it and the consumer is reading freed device memory.

Parameters:

| Name      | Type  | Description                                                                                                                                                                       | Default  |
| --------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `key`     | `str` | which image entry to read.                                                                                                                                                        | `'cube'` |
| `backend` | `int` | which mechanism to export with, one of cuvis.cuda.BACKEND_NONE (auto), BACKEND_POOL, BACKEND_LEGACY or BACKEND_VMM. cuda.capabilities reports which of them this device supports. | `0`      |

Raises:

| Type                           | Description                                               |
| ------------------------------ | --------------------------------------------------------- |
| `cuvis.UnavailableSDKFunction` | the installed cuvis library provides no CUDA IPC support. |
| `cuvis.cuvis_aux.SDKException` | the requested backend is unavailable on this device.      |

#### `refresh()`

#### `save(saveargs)`

## ProcessingContext

## `cuvis.ProcessingContext`

### `ProcessingContext`

Bases: `object`

#### `calibration_id`

#### `processing_mode`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(base, load_references=True)`

#### `apply(mesu)`

#### `calc_distance(distMM)`

#### `clear_reference(refType)`

#### `get_processing_args()`

#### `get_reference(refType)`

The reference measurement, or None. Spectrum references are not measurements; for those use get_reference_spectrum.

#### `get_reference_spectrum(refType)`

The reference spectrum as an ImageData (shape 1 x 1 x channels, wavelengths in nanometres), or None when the slot is empty.

Only ReferenceType.WhiteSpectrum and ReferenceType.TargetSpectrum are spectra; other types live in get_reference. For the white spectrum the returned ImageData additionally carries the effective_bit_depth and integration_time it was set with, as plain attributes (they do not survive slicing or arithmetic).

#### `has_reference(refType)`

#### `is_capable(mesu, pa)`

#### `set_processing_args(pa)`

#### `set_reference(data, refType, *, effective_bit_depth=None, integration_time=0.0)`

Set a reference for processing.

The classic reference types take a Measurement. The two spectrum types take an ImageData carrying wavelengths, or a (wavelengths, values) pair of arrays, with wavelengths in nanometres:

- TargetSpectrum: reflectance values as fractions, 1.0 meaning 100 percent.
- WhiteSpectrum: raw sensor counts (uint16); effective_bit_depth (1 to 16) is required, integration_time [ms] describes the recording.

## AcquisitionContext

## `cuvis.AcquisitionContext`

### `AcquisitionContext`

Bases: `object`

#### `auto_exp`

#### `auto_exp_comp`

#### `average`

#### `bandwidth`

#### `component_count`

#### `dead_pixel_correction`

#### `dead_pixel_correction_available`

#### `fps`

#### `integration_time`

#### `operation_mode`

#### `queue_size`

#### `queue_used`

#### `ready`

#### `session_info`

#### `state`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(base, *, simulate=False)`

#### `capture(to_internal=False)`

#### `capture_at(timeout_ms)`

#### `components()`

Returns an iterator over all components

#### `get_next_measurement(timeout_ms)`

#### `has_next_measurement()`

#### `register_ready_callback(callback)`

#### `register_state_change_callback(callback)`

#### `reset_ready_callback()`

#### `reset_state_change_callback()`

#### `set_auto_exp_async(val)`

#### `set_auto_exp_comp_async(val)`

#### `set_average_async(avg)`

#### `set_continuous(val)`

#### `set_continuous_async(val)`

#### `set_fps_async(val)`

#### `set_integration_time_async(val)`

#### `set_operation_mode_async(val)`

### `Component`

#### `available_pixel_formats`

#### `gain`

#### `info = acq._get_component_info(idx)`

#### `integration_time_factor`

#### `online`

#### `pixel_format`

#### `temperature`

#### `__init__(acq, idx)`

## Worker

## `cuvis.Worker`

### `Worker`

Bases: `object`

#### `can_drop_results`

#### `can_skip_measurements`

#### `can_skip_supplementary`

#### `input_queue_limit`

#### `is_processing`

#### `is_processing_mandatory`

#### `mandatory_queue_limit`

#### `output_queue_limit`

#### `query_session_progress`

#### `queue_used`

#### `state`

#### `supplementary_queue_limit`

#### `threads_busy`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(args)`

#### `drop_all_queued()`

#### `get_next_result(timeout)`

#### `get_next_result_async(timeout)`

Wait for the next result without polling for it.

The SDK's own wait is blocking and releases the GIL, so it runs in a worker thread while the event loop carries on. Unlike the polling version this raises `SDKException` when the timeout passes rather than returning a result built from handles the SDK never filled in.

#### `has_next_result()`

#### `ingest_mesu(mesu)`

#### `ingest_session_file(session, frame_selection='all')`

#### `register_worker_callback(callback)`

#### `reset_worker_callback()`

#### `set_acquisition_context(base=None)`

#### `set_exporter(base=None)`

#### `set_processing_context(base=None)`

#### `set_viewer(base=None)`

#### `start_processing()`

#### `stop_processing()`

### `WorkerResult`

#### `mesu`

#### `view`

#### `__init__(mesu, view)`

## Viewer

## `cuvis.Viewer`

### `Viewer`

Bases: `object`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(settings)`

#### `apply(mesu)`

## Calibration

## `cuvis.Calibration`

### `Calibration`

Bases: `object`

#### `id`

#### `info`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(base)`

#### `get_capabilities(operation_mode)`

## Export

## `cuvis.Export`

### `CubeExporter`

Bases: `Exporter`

#### `__init__(fs)`

### `EnviExporter`

Bases: `Exporter`

#### `__init__(ge)`

### `Exporter`

Bases: `object`

#### `queue_used`

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__()`

#### `apply(mesu)`

#### `flush()`

### `TiffExporter`

Bases: `Exporter`

#### `__init__(fs)`

### `ViewExporter`

Bases: `Exporter`

#### `__init__(fs)`

## Types & Enums

## `cuvis.cuvis_types`

### `CUVIS_imbuffer_format = dict({('imbuffer_format_uint8', cuvis_il.imbuffer_format_uint8), ('imbuffer_format_uint16', cuvis_il.imbuffer_format_uint16), ('imbuffer_format_uint32', cuvis_il.imbuffer_format_uint32), ('imbuffer_format_float', cuvis_il.imbuffer_format_float)})`

### `DataFormat = dict({(1, np.uint8), (2, np.uint16), (3, np.uint32), (4, np.float32)})`

### `__Capabilities__ = __inverseTranslationDict(__CuvisCapabilities__)`

### `__ComponentType__ = __inverseTranslationDict(__CuvisComponentType__)`

### `__CuvisCapabilities__ = {'AcquisitionCapture': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_CAPTURE, 'AcquisitionTimelapse': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_TIMELAPSE, 'AcquisitionContinuous': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_CONTINUOUS, 'AcquisitionSnapshot': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SNAPSHOT, 'AcquisitionSetIntegrationtime': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SETINTEGRATIONTIME, 'AcquisitionSetGain': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SETGAIN, 'AcquisitionAveraging': cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_AVERAGING, 'ProcessingSensorRaw': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SENSOR_RAW, 'ProcessingCubeRaw': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_RAW, 'ProcessingCubeRef': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_REF, 'ProcessingCubeDarkSubtract': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_DARKSUBTRACT, 'ProcessingCubeFlatFielding': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_FLATFIELDING, 'ProcessingCubeSpectralRadiance': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_SPECTRALRADIANCE, 'ProcessingSaveFile': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SAVE_FILE, 'ProcessingClearRaw': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CLEAR_RAW, 'ProcessingCalcLive': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CALC_LIVE, 'ProcessingAutoExposure': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_AUTOEXPOSURE, 'ProcessingOrientation': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_ORIENTATION, 'ProcessingSetWhite': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_WHITE, 'ProcessingSetDark': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DARK, 'ProcessingSetSprad': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_SPRADCALIB, 'ProcessingSetDistanceCalib': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCECALIB, 'ProcessingSetDistanceValue': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCE_VALUE, 'ProcessingUseDarkSpradcalib': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_USE_DARK_SPRADCALIB, 'ProcessingUseWhiteSpradCalib': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_USE_WHITE_SPRADCALIB, 'ProcessingRequireWhiteDarkReflectance': cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_REQUIRE_WHITEDARK_REFLECTANCE, 'UNDEFINED': 2 ** 26}`

### `__CuvisComponentType__ = {ComponentType.ImageSensor: cuvis_il.component_type_image_sensor, ComponentType.MiscSensor: cuvis_il.component_type_misc_sensor}`

### `__CuvisHardwareState__ = {HardwareState.Online: cuvis_il.hardware_state_online, HardwareState.PartiallyOnline: cuvis_il.hardware_state_partially_online, HardwareState.Offline: cuvis_il.hardware_state_offline}`

### `__CuvisLoglevel__ = {logging.DEBUG: cuvis_il.loglevel_debug, logging.INFO: cuvis_il.loglevel_info, logging.WARNING: cuvis_il.loglevel_warning, logging.ERROR: cuvis_il.loglevel_error, logging.FATAL: cuvis_il.loglevel_fatal, logging.CRITICAL: cuvis_il.loglevel_fatal}`

### `__CuvisMeasurementFlag__ = {'POOR_REFERENCE': cuvis_il.CUVIS_MESU_FLAG_POOR_REFERENCE, 'OVERILLUMINATED': cuvis_il.CUVIS_MESU_FLAG_OVERILLUMINATED, 'PAN_OVERILLUMINATED': cuvis_il.CUVIS_MESU_FLAG_PAN_OVERILLUMINATED, 'POOR_WHITE_BALANCING': cuvis_il.CUVIS_MESU_FLAG_POOR_WHITE_BALANCING, 'DARK_INTTIME': cuvis_il.CUVIS_MESU_FLAG_DARK_INTTIME, 'DARK_TEMP': cuvis_il.CUVIS_MESU_FLAG_DARK_TEMP, 'WHITE_INTTIME': cuvis_il.CUVIS_MESU_FLAG_WHITE_INTTIME, 'WHITE_TEMP': cuvis_il.CUVIS_MESU_FLAG_WHITE_TEMP, 'WHITEDARK_INTTIME': cuvis_il.CUVIS_MESU_FLAG_WHITEDARK_INTTIME, 'WHITEDARK_TEMP': cuvis_il.CUVIS_MESU_FLAG_WHITEDARK_TEMP}`

### `__CuvisOperationMode__ = {OperationMode.External: cuvis_il.OperationMode_External, OperationMode.Internal: cuvis_il.OperationMode_Internal, OperationMode.Software: cuvis_il.OperationMode_Software, OperationMode.UNDEFINED: cuvis_il.OperationMode_Undefined}`

### `__CuvisPanSharpeningAlgorithm__ = {PanSharpeningAlgorithm.Noop: cuvis_il.pan_sharpening_algorithm_Noop, PanSharpeningAlgorithm.CubertMacroPixel: cuvis_il.pan_sharpening_algorithm_CubertMacroPixel, PanSharpeningAlgorithm.CubertPanRatio: cuvis_il.pan_sharpening_algorithm_CubertPanRatio, PanSharpeningAlgorithm.PCAFusion: cuvis_il.pan_sharpening_algorithm_PCAFusion}`

### `__CuvisPanSharpeningInterpolationType__ = {PanSharpeningInterpolationType.NearestNeighbour: cuvis_il.pan_sharpening_interpolation_type_NearestNeighbor, PanSharpeningInterpolationType.Linear: cuvis_il.pan_sharpening_interpolation_type_Linear, PanSharpeningInterpolationType.Cubic: cuvis_il.pan_sharpening_interpolation_type_Cubic, PanSharpeningInterpolationType.Lanczos: cuvis_il.pan_sharpening_interpolation_type_Lanczos}`

### `__CuvisProcessingMode__ = {ProcessingMode.Preview: cuvis_il.Preview, ProcessingMode.Raw: cuvis_il.Cube_Raw, ProcessingMode.DarkSubtract: cuvis_il.Cube_DarkSubtract, ProcessingMode.Reflectance: cuvis_il.Cube_Reflectance, ProcessingMode.SpectralRadiance: cuvis_il.Cube_SpectralRadiance}`

### `__CuvisReferenceType__ = {ReferenceType.Dark: cuvis_il.Reference_Dark, ReferenceType.White: cuvis_il.Reference_White, ReferenceType.WhiteDark: cuvis_il.Reference_WhiteDark, ReferenceType.SpRad: cuvis_il.Reference_SpRad, ReferenceType.Distance: cuvis_il.Reference_Distance, ReferenceType.WhiteSpectrum: cuvis_il.Reference_WhiteSpectrum, ReferenceType.TargetSpectrum: cuvis_il.Reference_TargetSpectrum}`

### `__CuvisSessionItemType__ = {SessionItemType.all_frames: cuvis_il.session_item_type_frames, SessionItemType.no_gaps: cuvis_il.session_item_type_frames_no_gaps, SessionItemType.references: cuvis_il.session_item_type_references}`

### `__CuvisSessionMergeMode__ = {SessionMergeMode.Default: cuvis_il.session_merge_mode_Default, SessionMergeMode.Fragmentation: cuvis_il.session_merge_mode_Fragmentation, SessionMergeMode.Merge: cuvis_il.session_merge_mode_Merge}`

### `__CuvisTiffCompressionMode__ = {TiffCompressionMode.Nothing: cuvis_il.tiff_compression_mode_None, TiffCompressionMode.LZW: cuvis_il.tiff_compression_mode_LZW}`

### `__CuvisTiffFormat__ = {TiffFormat.Single: cuvis_il.tiff_format_Single, TiffFormat.MultiChannel: cuvis_il.tiff_format_MultiChannel, TiffFormat.MultiPage: cuvis_il.tiff_format_MultiPage}`

### `__HardwareState__ = __inverseTranslationDict(__CuvisHardwareState__)`

### `__MeasurementFlag__ = __inverseTranslationDict(__CuvisMeasurementFlag__)`

### `__OperationMode__ = __inverseTranslationDict(__CuvisOperationMode__)`

### `__PanSharpeningAlgorithm__ = __inverseTranslationDict(__CuvisPanSharpeningAlgorithm__)`

### `__PanSharpeningInterpolationType__ = __inverseTranslationDict(__CuvisPanSharpeningInterpolationType__)`

### `__ProcessingMode__ = __inverseTranslationDict(__CuvisProcessingMode__)`

### `__ReferenceType__ = __inverseTranslationDict(__CuvisReferenceType__)`

### `__SessionMergeMode__ = __inverseTranslationDict(__CuvisSessionMergeMode__)`

### `__TiffCompressionMode__ = __inverseTranslationDict(__CuvisTiffCompressionMode__)`

### `__TiffFormat__ = __inverseTranslationDict(__CuvisTiffFormat__)`

### `__strToLogLevel__ = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR, 'critical': logging.CRITICAL, 'fatal': logging.FATAL}`

### `AsyncResult`

Bases: `Enum`

#### `deferred = 3`

#### `done = 0`

#### `overwritten = 2`

#### `timeout = 1`

### `ComponentType`

Bases: `Enum`

#### `ImageSensor = 1`

#### `MiscSensor = 2`

### `DataType`

Bases: `Enum`

#### `data_type_gps = 3`

#### `data_type_image = 2`

#### `data_type_sensor_info = 5`

#### `data_type_string = 4`

#### `data_type_unsupported = 1`

### `HardwareState`

Bases: `Enum`

#### `Offline = 3`

#### `Online = 1`

#### `PartiallyOnline = 2`

### `OperationMode`

Bases: `Enum`

#### `External = 1`

#### `Internal = 2`

#### `Software = 3`

#### `UNDEFINED = 4`

### `PanSharpeningAlgorithm`

Bases: `Enum`

#### `CubertMacroPixel = 2`

#### `CubertPanRatio = 3`

#### `Noop = 1`

#### `PCAFusion = 4`

### `PanSharpeningInterpolationType`

Bases: `Enum`

#### `Cubic = 3`

#### `Lanczos = 4`

#### `Linear = 2`

#### `NearestNeighbour = 1`

### `ProcessingMode`

Bases: `Enum`

#### `DarkSubtract = 3`

#### `Preview = 1`

#### `Raw = 2`

#### `Reflectance = 4`

#### `SpectralRadiance = 5`

### `ReferenceType`

Bases: `Enum`

#### `Dark = 1`

#### `Distance = 5`

#### `SpRad = 4`

#### `TargetSpectrum = 7`

#### `White = 2`

#### `WhiteDark = 3`

#### `WhiteSpectrum = 6`

### `SessionItemType`

Bases: `Enum`

#### `all_frames = 1`

#### `no_gaps = 2`

#### `references = 3`

### `SessionMergeMode`

Bases: `Enum`

#### `Default = 0`

#### `Fragmentation = 1`

#### `Merge = 2`

### `TiffCompressionMode`

Bases: `Enum`

#### `LZW = 2`

#### `Nothing = 1`

### `TiffFormat`

Bases: `Enum`

#### `MultiChannel = 2`

#### `MultiPage = 3`

#### `Single = 1`

### `__generateTranslationDict(enum_cls)`

### `__inverseTranslationDict(translationDict)`
