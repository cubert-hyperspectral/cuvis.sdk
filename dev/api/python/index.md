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

### `base_datetime = datetime.datetime(1970, 1, 1)`

### `Measurement`

Bases: `object`

#### `assembly`

#### `averages`

#### `calibration_id`

#### `capabilities`

#### `capture_time`

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

#### `has_reference(refType)`

#### `is_capable(mesu, pa)`

#### `set_processing_args(pa)`

#### `set_reference(mesu, refType)`

## AcquisitionContext

## `cuvis.AcquisitionContext`

### `AcquisitionContext`

Bases: `object`

#### `auto_exp`

#### `auto_exp_comp`

#### `average`

#### `bandwidth`

#### `component_count`

Get the number of components

The acquisition hardware is build from one or more components. Get the component count.

#### `dead_pixel_correction`

Query whether the dead pixel correction is enabled

Returns whether the Cuvis built-in dead pixel correction algorithm is currently enabled

#### `dead_pixel_correction_available`

Query whether the dead pixel correction is available

Returns whether dead pixel correction information is available in the camera's calibration file.

#### `fps`

#### `integration_time`

#### `operation_mode`

#### `queue_size`

#### `queue_used`

#### `ready`

get initialization state of the acquisition context

#### `session_info`

get the acquisition session_info

Get the acquisition session_info settings. Also use this function to get the current sequence number.

#### `state`

get the online state of the hardware

Hardware can be used, when at least it's required components are online.

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(base, *, simulate=False)`

#### `capture(to_interal=False)`

Capture a measurement async

This function is only available in operation mode "Software". The function executes a software trigger asynchronously. The recorded measurement can be obtained by the function 'cuvis_async_capture_get'.

If o_pAsyncResult is set to NULL, the measurement is added to the Acqusition Context's internal queue. Retrieve it with 'cuvis_acq_cont_get_next_measurement' or via the worker (if used) 'cuvis_worker_get_next_result'

#### `capture_at(timeout_ms)`

Capture a measurement

This function is only available in operation mode "Software". The function executes a software trigger synchronously.

#### `components()`

Returns an iterator over all components

#### `get_next_measurement(timeout_ms)`

Get measurement from internal cache

This function is only available in operation mode "Internal" or "External". The function obtains the image from the internal memory, if available.

#### `has_next_measurement()`

check if any measurements are available in the buffer

This function is only available in operation mode "Internal" or "External".

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

Query current drop behavior

#### `can_skip_measurements`

Query current skip behavior

#### `can_skip_supplementary`

Query current skip behavior

#### `input_queue_limit`

Query the maximum queue size of the input queue

#### `is_processing`

Query wether the worker is currently allowed to process measurements - wether it is running.

#### `is_processing_mandatory`

Query wether the processing step is currently mandatory The result is only valid, if a processing context is assigned to the worker. If no processing context is assigned, will always return 0 (false)

#### `mandatory_queue_limit`

Query the maximum queue size of the mandatory queue

#### `output_queue_limit`

Query the maximum queue size of the output queue

#### `query_session_progress`

Get the current percentage of frames done of the current session. -1.0 if no session file is currently being processed.

#### `queue_used`

Query the number of items currently in the result queue.

#### `state`

Query multiple attributes of the worker at once, see cuvis_worker_state_t

#### `supplementary_queue_limit`

Query the maximum queue size of the supplementary queue

#### `threads_busy`

Query how many measurements the worker is processing right now

#### `__copy__()`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__deepcopy__(memo)`

This functions is not permitted due to the class only keeping a handle, that is managed by the cuvis sdk.

#### `__del__()`

#### `__init__(args)`

#### `drop_all_queued()`

Command the worker to discard all measurements it is currently processing and empty the result queue.

#### `get_next_result(timeout)`

Get the next result in order

The measurement will be readyly recorded, processed (if set), stored (if set) and have a view (if set).

#### `get_next_result_async(timeout)`

#### `has_next_result()`

Check, if a new worker result is available

#### `ingest_mesu(mesu)`

Push a mesurement into the worker to process. Worker must have neither a session file nor an acquisition context.

#### `ingest_session_file(session, frame_selection='all')`

set a session file for the worker to process (read access only). Give CUVIS_HANDLE_NULL to clear. Set parameter SkipDroppedFrames to 1 to skip any dropped frames contained in the session - 0 will insert empty frames.

#### `register_worker_callback(callback)`

#### `reset_worker_callback()`

#### `set_acquisition_context(base=None)`

set the acquistion context for the worker. Give CUVIS_HANDLE_NULL to clear

#### `set_exporter(base=None)`

set the exporter for the worker. Give CUVIS_HANDLE_NULL to clear

#### `set_processing_context(base=None)`

set the processing context for the worker. Give CUVIS_HANDLE_NULL to clear

#### `set_viewer(base=None)`

set the viewer for the worker. Give CUVIS_HANDLE_NULL to clear

#### `start_processing()`

Start the worker

#### `stop_processing()`

Pause the worker

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

### `__CuvisReferenceType__ = {ReferenceType.Dark: cuvis_il.Reference_Dark, ReferenceType.White: cuvis_il.Reference_White, ReferenceType.WhiteDark: cuvis_il.Reference_WhiteDark, ReferenceType.SpRad: cuvis_il.Reference_SpRad, ReferenceType.Distance: cuvis_il.Reference_Distance}`

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

#### `White = 2`

#### `WhiteDark = 3`

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
