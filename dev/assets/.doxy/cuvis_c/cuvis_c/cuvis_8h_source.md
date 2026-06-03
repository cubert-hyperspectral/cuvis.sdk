

# File cuvis.h

[**File List**](files.md) **>** [**\_api\_sources**](dir_461ad87a78e7eefd7882d4ef5ca214ae.md) **>** [**cuvis.h**](cuvis_8h.md)

[Go to the documentation of this file](cuvis_8h.md)


```C++

#ifndef CUVIS_SDK_C_H
#define CUVIS_SDK_C_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Supress security warnings */
#ifndef _CRT_SECURE_NO_WARNINGS
  #define _CRT_SECURE_NO_WARNINGS
#endif
/* API MACROS */

#ifdef _WIN32
  #ifdef CUVIS_SDK_CLIBRARY_EXPORTS
    #define SDK_CAPI __declspec(dllexport)
  #else
    #define SDK_CAPI __declspec(dllimport)
  #endif

  #ifdef __cplusplus
    #define SDK_CCALL __cdecl
  #else
    #define SDK_CCALL
  #endif
#else
  #define SDK_CAPI
  #define SDK_CCALL
#endif

/* FUNCTION MACROS */

#define ALLOCATE_AND_FREE(DATATYPE, NAME)                     \
                      \
  SDK_CAPI DATATYPE* SDK_CCALL cuvis_##NAME##_allocate(void); \
                           \
  SDK_CAPI void SDK_CCALL cuvis_##NAME##_free(DATATYPE* ptr);

#define ACQ_GET_SINGLE_VALUE(NAME, TYPE, COMMENT)                            \
 \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_get(CUVIS_ACQ_CONT i_acqCont, TYPE* o_pvalue);

#define ACQ_SET_SINGLE_VALUE(NAME, TYPE, UNIT_STR)                                            \
                               \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set(CUVIS_ACQ_CONT i_acqCont, TYPE value);           \
 \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, TYPE value);

#define COMP_GET_SINGLE_VALUE(NAME, TYPE, COMMENT)                           \
 \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, TYPE* o_pvalue);

#define COMP_SET_SINGLE_VALUE(NAME, TYPE, UNIT_STR)                                                 \
                                     \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, TYPE value); \
       \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, TYPE value);

/* SIMPLE TYPES */

#define CUVIS_INT int32_t

#define CUVIS_SIZE uint64_t

#define CUVIS_HANDLE CUVIS_INT

#define CUVIS_HANDLE_NULL CUVIS_HANDLE(0)

#define CUVIS_MISC_PTR void*

#define CUVIS_CHAR char

#define CUVIS_WCHAR wchar_t

#define CUVIS_MAXBUF 256

#define CUVIS_STRING CUVIS_CHAR[CUVIS_MAXBUF]

#define CUVIS_FLAGS uint32_t

#define CUVIS_TIMESTAMP uint64_t

#define CUVIS_MESU CUVIS_HANDLE

#define CUVIS_SESSION_FILE CUVIS_HANDLE

#define CUVIS_CALIB CUVIS_HANDLE

#define CUVIS_ACQ_CONT CUVIS_HANDLE

#define CUVIS_PROC_CONT CUVIS_HANDLE

#define CUVIS_EXPORTER CUVIS_HANDLE

#define CUVIS_VIEWER CUVIS_HANDLE

#define CUVIS_VIEW CUVIS_HANDLE

#define CUVIS_WORKER CUVIS_HANDLE

#define CUVIS_ASYNC_CALL_RESULT CUVIS_HANDLE

#define CUVIS_ASYNC_CAPTURE_RESULT CUVIS_HANDLE

#define CUVIS_MODE_CAPABILITIES CUVIS_INT

/* CONSTANTS AND FLAGS */

/* TODO add documentation */
#define CUVIS_MODE_CAPABILITY_ACQUISITION_CAPTURE 1
#define CUVIS_MODE_CAPABILITY_ACQUISITION_TIMELAPSE 2
#define CUVIS_MODE_CAPABILITY_ACQUISITION_CONTINUOUS 4
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SNAPSHOT 8
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SETINTEGRATIONTIME 16
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SETGAIN 32
#define CUVIS_MODE_CAPABILITY_ACQUISITION_AVERAGING 64
#define CUVIS_MODE_CAPABILITY_PROCESSING_SENSOR_RAW 128
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_RAW 256
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_REF 512
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_DARKSUBTRACT 1024
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_FLATFIELDING 2048
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_SPECTRALRADIANCE 4096
#define CUVIS_MODE_CAPABILITY_PROCESSING_SAVE_FILE 8192
#define CUVIS_MODE_CAPABILITY_PROCESSING_CLEAR_RAW 16384
#define CUVIS_MODE_CAPABILITY_PROCESSING_CALC_LIVE 32768
#define CUVIS_MODE_CAPABILITY_PROCESSING_AUTOEXPOSURE 65536
#define CUVIS_MODE_CAPABILITY_PROCESSING_ORIENTATION 131072
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_WHITE 262144
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DARK 524288
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_SPRADCALIB 1048576
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCECALIB 2097152
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCE_VALUE 4194304
#define CUVIS_MODE_CAPABILITY_PROCESSING_USE_DARK_SPRADCALIB 8388608
#define CUVIS_MODE_CAPABILITY_PROCESSING_USE_WHITE_SPRADCALIB 16777216
#define CUVIS_MODE_CAPABILITY_PROCESSING_REQUIRE_WHITEDARK_REFLECTANCE 33554432

//todo documentation
enum cuvis_capabilities_t
{
  AcquisitionCapture = 1,
  AcquisitionTimelapse = 2,
  AcquisitionContinuous = 4,
  AcquisitionSnapshot = 8,
  AcquisitionSetIntegrationtime = 16,
  AcquisitionSetGain = 32,
  AcquisitionAveraging = 64,
  ProcessingSensorRaw = 128,
  ProcessingCubeRaw = 256,
  ProcessingCubeRef = 512,
  ProcessingCubeDarkSubtract = 1024,
  ProcessingCubeFlatFielding = 2048,
  ProcessingCubeSpectralRadiance = 4096,
  ProcessingSaveFile = 8192,
  ProcessingClearRaw = 16384,
  ProcessingCalcLive = 32768,
  ProcessingAutoExposure = 65536,
  ProcessingOrientation = 131072,
  ProcessingSetWhite = 262144,
  ProcessingSetDark = 524288,
  ProcessingSetSprad = 1048576,
  ProcessingSetDistanceCalib = 2097152,
  ProcessingSetDistanceValue = 4194304,
  ProcessingUseDarkSpradcalib = 8388608,
  ProcessingUseWhiteSpradCalib = 16777216,
  ProcessingRequireWhiteDarkReflectance = 33554432
};

#define CUVIS_MESU_FLAG_OVERILLUMINATED 1

#define CUVIS_MESU_FLAG_POOR_REFERENCE 2

#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING 4

#define CUVIS_MESU_FLAG_DARK_INTTIME 8

#define CUVIS_MESU_FLAG_DARK_TEMP 16

#define CUVIS_MESU_FLAG_WHITE_INTTIME 32

#define CUVIS_MESU_FLAG_WHITE_TEMP 64

#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME 128

#define CUVIS_MESU_FLAG_WHITEDARK_TEMP 256

#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED 512

#define CUVIS_MESU_CUBE_KEY "cube"

#define CUVIS_MESU_PAN_KEY "pan"

#define CUVIS_MESU_GPS_KEY "GPS_data"

#define CUVIS_MESU_PREVIEW_KEY "preview"

#define CUVIS_MESU_DARKREF_KEY "dark_ref"

#define CUVIS_MESU_WHITEREF_KEY "white_ref"

#define CUVIS_MESU_WHITEDARKREF_KEY "white_dark_ref"

#define CUVIS_MESU_FLAG_OVERILLUMINATED_KEY "Flag_DataIsOverilluminated"

#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED_KEY "Flag_PanDataIsOverilluminated"

#define CUVIS_MESU_FLAG_POOR_REFERENCE_KEY "Flag_DataUsesPoorReference"

#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY "Flag_PoorWhiteBalancingData"

#define CUVIS_MESU_FLAG_DARK_INTTIME_KEY "Flag_IntegrationTimeMismatchDark"

#define CUVIS_MESU_FLAG_DARK_TEMP_KEY "Flag_TemperatureMismatchDark"

#define CUVIS_MESU_FLAG_WHITE_INTTIME_KEY "Flag_IntegrationTimeMismatchWhite"

#define CUVIS_MESU_FLAG_WHITE_TEMP_KEY "Flag_TemperatureMismatchWhite"

#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY "Flag_IntegrationTimeMismatchWhiteDark"

#define CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY "Flag_TemperatureMismatchWhiteDark"
#define CUVIS_MESU_CUBE_INFO_KEY "cube_info_layer"

#define CUVIS_MESU_PAN_INFO_KEY "pan_info_layer"

#define CUVIS_MESU_INFO_OK 0

#define CUVIS_MESU_INFO_OVERILLUMINATED 1

#define CUVIS_MESU_INFO_BAD_PIXEL 2

#define CUVIS_MESU_INFO_OVERILLUMINATED_REFERENCE 4

#define CUVIS_MESU_INFO_UNDERFLOW_MEASUREMENT_MIN_DARK 8

#define CUVIS_MESU_INFO_UNDERFLOW_WHITE_MIN_DARK 16

#define CUVIS_MESU_INFO_REFERENCE_CALC_OVERFLOW 32

#define CUVIS_MESU_INFO_INCOMPLETE 64

//todo capabilites binary flags

/* ENUMERATIONS */

enum cuvis_status_t
{
  status_ok = 1,
  status_error = -1,
  status_deferred = -10,

  status_overwritten = -11,

  status_timeout = -12,

  status_no_measurement = -20,

  status_not_available = -30,

  status_not_processed = -41,

  status_not_stored = -42,

  status_no_view = -43

};

enum cuvis_hardware_state_t
{
  hardware_state_offline = 0,
  hardware_state_partially_online = 1,
  hardware_state_online = 2
};


enum cuvis_loglevel_t
{
  loglevel_fatal = 0,

  loglevel_error = 1,

  loglevel_warning = 2,

  loglevel_info = 3,

  loglevel_debug = 4,
};

enum cuvis_imbuffer_format_t
{
  imbuffer_format_uint8 = 1,

  imbuffer_format_uint16 = 2,

  imbuffer_format_uint32 = 3,

  imbuffer_format_float = 4,
};

#define CUVIS_IMBUFFER struct cuvis_imbuffer_t



enum cuvis_session_item_type_t
{
  session_item_type_frames = 0,
  session_item_type_frames_no_gaps = 1,
  session_item_type_references = 2
};


enum cuvis_data_type_t
{
  data_type_unsupported = 0,

  data_type_image = 1,

  data_type_gps = 2,

  data_type_string = 3,

  data_type_sensor_info = 4,
};

enum cuvis_processing_mode_t
{
  Cube_Raw = 0,

  Cube_DarkSubtract = 1,

  Cube_Reflectance = 2,

  Cube_SpectralRadiance = 3,

  Preview = 5
};

enum cuvis_reference_type_t
{
  Reference_Dark = 0,

  Reference_White = 1,

  Reference_WhiteDark = 2,

  Reference_SpRad = 3,

  Reference_Distance = 4
};

enum cuvis_operation_mode_t
{
  OperationMode_Software = 1,
  OperationMode_Internal = 2,
  OperationMode_External = 3,
  OperationMode_Undefined = 4
};

enum cuvis_pan_sharpening_interpolation_type_t
{
  pan_sharpening_interpolation_type_NearestNeighbor = 0,
  pan_sharpening_interpolation_type_Linear = 1,
  pan_sharpening_interpolation_type_Cubic = 2,
  pan_sharpening_interpolation_type_Lanczos = 4
};

enum cuvis_pan_sharpening_algorithm_t
{
  pan_sharpening_algorithm_Noop = 0,

  pan_sharpening_algorithm_CubertMacroPixel = 1,

  pan_sharpening_algorithm_CubertPanRatio = 2,

  pan_sharpening_algorithm_PCAFusion = 3,
};

enum cuvis_tiff_compression_mode_t
{
  tiff_compression_mode_None = 0,

  tiff_compression_mode_LZW = 1
};

enum cuvis_tiff_format_t
{
  tiff_format_Single = 0,

  tiff_format_MultiChannel = 1,

  tiff_format_MultiPage = 2,
};

enum cuvis_view_category_t
{
  view_category_image = 0,

  view_category_data = 1,
};

enum cuvis_component_type_t
{
  component_type_image_sensor = 0,
  component_type_misc_sensor = 1,
};

enum cuvis_session_merge_mode_t
{
  session_merge_mode_Default = 0,

  session_merge_mode_Fragmentation = 1,

  session_merge_mode_Merge = 2
};

/* TYPE DEFINITIONS */

#define CUVIS_STATUS enum cuvis_status_t
#define CUVIS_LOGLEVEL enum cuvis_loglevel_t
#define CUVIS_IMBUFFER_FORMAT enum cuvis_imbuffer_format_t
#define CUVIS_DATA_TYPE enum cuvis_data_type_t
#define CUVIS_PROCESSING_MODE enum cuvis_processing_mode_t
#define CUVIS_OPERATION_MODE enum cuvis_operation_mode_t
#define CUVIS_HARDWARE_STATE enum cuvis_hardware_state_t
#define CUVIS_REFERENCE_TYPE enum cuvis_reference_type_t
#define CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE enum cuvis_pan_sharpening_interpolation_type_t
#define CUVIS_PAN_SHAPRENING_ALGORITHM_TYPE enum cuvis_pan_sharpening_algorithm_t
#define CUVIS_TIFF_COMPRESSION_MODE enum cuvis_tiff_compression_mode_t
#define CUVIS_TIFF_FORMAT enum cuvis_tiff_format_t
#define CUVIS_VIEW_CATEGORY enum cuvis_view_category_t
#define CUVIS_COMPONENT_TYPE enum cuvis_component_type_t
#define CUVIS_SESSION_ITEM_TYPE enum cuvis_session_item_type_t
#define CUVIS_SESSION_MERGE_MODE enum cuvis_session_merge_mode_t



#define CUVIS_PANSHARPENING_SETTINGS struct cuvis_pansharpening_settings_t
/*  DATA STRUCUTRES */

struct cuvis_imbuffer_t
{
  uint8_t const* raw;
  uint32_t bytes;
  uint32_t length;
  uint32_t width;
  uint32_t height;

  uint16_t channels;

  CUVIS_IMBUFFER_FORMAT format;

  uint32_t const* wavelength;
};

struct cuvis_sensor_info_t
{
  uint32_t averages;

  double temperature;

  double gain;

  CUVIS_TIMESTAMP readout_time;

  uint32_t width;
  uint32_t height;

  CUVIS_SIZE raw_frame_id;

  CUVIS_CHAR pixel_format[CUVIS_MAXBUF];

  double integration_time;
};

struct cuvis_gps_t
{
  double longitude;

  double latitude;

  double altitude;

  CUVIS_TIMESTAMP time;
};

struct cuvis_session_info_t
{
  CUVIS_CHAR name[CUVIS_MAXBUF];

  CUVIS_INT session_no;

  CUVIS_INT sequence_no;
};
#define CUVIS_SESSION_INFO struct cuvis_session_info_t

struct cuvis_calibration_info_t
{
  CUVIS_CHAR model_name[CUVIS_MAXBUF];

  CUVIS_CHAR serial_no[CUVIS_MAXBUF];

  CUVIS_TIMESTAMP calibration_date;

  CUVIS_CHAR annotation_name[CUVIS_MAXBUF];

  CUVIS_CHAR unique_id[CUVIS_MAXBUF];

  CUVIS_CHAR file_path[CUVIS_MAXBUF];

  uint32_t cube_width;

  uint32_t cube_height;

  uint32_t cube_channels;

  uint32_t const* cube_wavelengths;
};
#define CUVIS_CALIBRATION_INFO struct cuvis_calibration_info_t

struct cuvis_mesu_metadata_t
{
  CUVIS_CHAR name[CUVIS_MAXBUF];

  CUVIS_CHAR path[CUVIS_MAXBUF];

  CUVIS_CHAR comment[CUVIS_MAXBUF];

  CUVIS_TIMESTAMP capture_time;

  CUVIS_TIMESTAMP factory_calibration;

  CUVIS_CHAR product_name[CUVIS_MAXBUF];

  CUVIS_CHAR serial_number[CUVIS_MAXBUF];

  CUVIS_CHAR assembly[CUVIS_MAXBUF];

  double integration_time;

  CUVIS_INT averages;

  double distance;

  CUVIS_CHAR session_info_name[CUVIS_MAXBUF];

  CUVIS_INT session_info_session_no;

  CUVIS_INT session_info_sequence_no;

  CUVIS_PROCESSING_MODE processing_mode;

  CUVIS_PROCESSING_MODE processing_mode_at_capture;

  CUVIS_FLAGS measurement_flags;

  CUVIS_SIZE measurement_frame_id;
};

struct cuvis_save_args_t
{
  CUVIS_SESSION_MERGE_MODE merge_mode;

  CUVIS_INT allow_overwrite;

  CUVIS_INT allow_drop;

  CUVIS_INT allow_session_file;

  CUVIS_INT allow_info_file;

  CUVIS_OPERATION_MODE operation_mode;

  double fps;

  CUVIS_INT soft_limit;

  CUVIS_INT hard_limit;

  CUVIS_INT max_buftime;

  CUVIS_INT full_export;
};

struct cuvis_proc_args_t
{
  CUVIS_PROCESSING_MODE processing_mode;

  CUVIS_INT allow_recalib;
};


struct cuvis_pansharpening_settings_t
{
  CUVIS_CHAR channel_selection[CUVIS_MAXBUF];

  float spectra_multiplier;

  double pan_scale;

  CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE pan_interpolation_type;

  CUVIS_PAN_SHAPRENING_ALGORITHM_TYPE pan_algorithm;

  CUVIS_INT pre_pan_sharpen_cube;

  CUVIS_INT add_pan;
};


struct cuvis_export_general_settings_t
{
  CUVIS_CHAR export_dir[CUVIS_MAXBUF];

  CUVIS_INT add_fullscale_pan;

  CUVIS_INT permissive;

  CUVIS_PANSHARPENING_SETTINGS pansharpening_settings;
};

struct cuvis_export_view_settings_t
{
  CUVIS_CHAR const* userplugin;

  CUVIS_INT complete;

  CUVIS_INT pan_failback;
};

struct cuvis_export_tiff_settings_t
{
  CUVIS_TIFF_COMPRESSION_MODE compression_mode;

  CUVIS_TIFF_FORMAT format;
};

struct cuvis_viewer_settings_t
{
  CUVIS_CHAR const* userplugin;

  CUVIS_INT complete;

  CUVIS_INT pan_failback;

  CUVIS_PANSHARPENING_SETTINGS pansharpening_settings;
};

struct cuvis_view_data_t
{
  CUVIS_CHAR id[CUVIS_MAXBUF];

  CUVIS_VIEW_CATEGORY category;

  CUVIS_IMBUFFER data;

  CUVIS_INT show;
};

struct cuvis_component_info_t
{
  CUVIS_COMPONENT_TYPE type;

  CUVIS_CHAR displayname[CUVIS_MAXBUF];

  CUVIS_CHAR sensorinfo[CUVIS_MAXBUF];

  CUVIS_CHAR userfield[CUVIS_MAXBUF];

  CUVIS_CHAR pixelformat[CUVIS_MAXBUF];
};

#define CUVIS_EVENT_BASE_DATA struct cuvis_event_base_data_t
#define CUVIS_EVENT_ACQUISITION_DATA struct cuvis_event_acquisition_data_t
#define CUVIS_EVENT_PROCESSING_DATA struct cuvis_event_processing_event_t
#define CUVIS_EVENT_QUALITY_DATA struct cuvis_event_quality_event_t
#define CUVIS_EVENT_COMPONENT_DATA struct cuvis_event_component_data_t

struct cuvis_event_base_data_t
{
  CUVIS_INT event_id;
};

struct cuvis_event_acquisition_data_t
{
  CUVIS_ACQ_CONT source;
};

struct cuvis_event_processing_event_t
{
  CUVIS_PROC_CONT source;
};

struct cuvis_event_quality_event_t
{
  CUVIS_HANDLE source;
};

struct cuvis_event_component_data_t
{
  CUVIS_HANDLE compent_id;
};

struct cuvis_worker_settings_t
{
  CUVIS_SIZE input_queue_size;

  CUVIS_SIZE mandatory_queue_size;

  CUVIS_SIZE supplementary_queue_size;

  CUVIS_SIZE output_queue_size;

  CUVIS_INT can_skip_measurements;

  CUVIS_INT can_skip_supplementary_steps;

  CUVIS_INT can_drop_results;
};

struct cuvis_worker_state_t
{
  CUVIS_SIZE measurementsInQueue;

  CUVIS_SIZE sessionFilesInQueue;

  CUVIS_SIZE framesInQueue;

  CUVIS_SIZE measurementsBeingProcessed;

  CUVIS_SIZE resultsInQueue;

  CUVIS_INT hasAcquisitionContext;

  CUVIS_INT isProcessing;
};

/*  ADDITIONAL DEFINITIONS */
#define CUVIS_GPS struct cuvis_gps_t
#define CUVIS_MESU_METADATA struct cuvis_mesu_metadata_t
#define CUVIS_SAVE_ARGS struct cuvis_save_args_t
#define CUVIS_PROC_ARGS struct cuvis_proc_args_t
#define CUVIS_EXPORT_GENERAL_SETTINGS struct cuvis_export_general_settings_t
#define CUVIS_EXPORT_CUBE_SETTINGS struct cuvis_save_args_t
#define CUVIS_EXPORT_VIEW_SETTINGS struct cuvis_export_view_settings_t
#define CUVIS_EXPORT_TIFF_SETTINGS struct cuvis_export_tiff_settings_t
#define CUVIS_VIEWER_SETTINGS struct cuvis_viewer_settings_t
#define CUVIS_VIEW_DATA struct cuvis_view_data_t
#define CUVIS_COMPONENT_INFO struct cuvis_component_info_t
#define CUVIS_SENSOR_INFO struct cuvis_sensor_info_t
#define CUVIS_WORKER_SETTINGS struct cuvis_worker_settings_t
#define CUVIS_WORKER_STATE struct cuvis_worker_state_t

#ifndef MATLAB

typedef void(SDK_CCALL* log_callback)(const char* msg, CUVIS_INT level);
typedef void(SDK_CCALL* log_callback_localized)(const CUVIS_WCHAR* msg, CUVIS_INT level);

#endif

#ifndef MATLAB

  /* EVENT TYPEDEFS */
  /*enum cuvis_event_handler_t
{
  base_event,
  acquisition_event,
  processing_event,
  quality_event,
  component_event,
  /* TODO Add more eventhandler
}; */

  //                                        mmmmxxxxssss

  /*
  #define CUVIS_EVENT_ACQUISTION         0b000100000000
  #define CUVIS_EVENT_COMPONENT        0b000100010000
  #define CUVIS_EVENT_TRIGGER_SKIPPED  0b000100010001
  */

  #define CUVIS_EVENT_PROCESSING (2 << 8)

  #define CUVIS_EVENT_ACQUISTION (1 << 8)

  #define CUVIS_EVENT_COMPONENT (CUVIS_EVENT_ACQUISTION | (1 << 4))

  #define CUVIS_EVENT_TRIGGER_SKIPPED (CUVIS_EVENT_COMPONENT | 1)

  #define CUVIS_EVENT CUVIS_HANDLE

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_event_get_acquisition_data(CUVIS_EVENT i_event, CUVIS_EVENT_ACQUISITION_DATA* o_p_acquisition_data);

/* EVENT CALLBACKS */

typedef void(SDK_CCALL* external_event_callback)(CUVIS_INT i_handler_id, CUVIS_EVENT i_event);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_register_external_event_callback(external_event_callback i_callback, CUVIS_INT i_type, CUVIS_INT* o_p_handler_id);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_unregister_event_callback(CUVIS_INT i_handler_id);

#endif

SDK_CAPI const CUVIS_CHAR* SDK_CCALL cuvis_get_last_error_msg(void);

SDK_CAPI const CUVIS_STATUS SDK_CCALL cuvis_set_last_error_locale(CUVIS_CHAR const* i_locale_id);

SDK_CAPI const CUVIS_WCHAR* SDK_CCALL cuvis_get_last_error_msg_localized(void);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_set_log_level(CUVIS_INT level);

#ifndef MATLAB

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_register_log_callback(log_callback i_callback, CUVIS_INT i_min_level);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_reset_log_callback();

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_register_log_callback_localized(log_callback_localized i_callback_localized, CUVIS_INT i_min_level, CUVIS_CHAR const* i_locale_id);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_reset_log_callback_localized();

#endif

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_init(CUVIS_CHAR const* i_settings_path, CUVIS_INT i_global_loglevel, CUVIS_CHAR const* i_logfile_name);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_shutdown();


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_version(CUVIS_CHAR* o_pVersion);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_get_userplugin_engine_version(CUVIS_CHAR* o_pVersion);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_get(CUVIS_ASYNC_CALL_RESULT* io_pAsyncResult, CUVIS_INT timeout_ms);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_free(CUVIS_ASYNC_CAPTURE_RESULT* io_pAsyncResult);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_free(CUVIS_ASYNC_CALL_RESULT* io_pAsyncResult);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_status(CUVIS_ASYNC_CALL_RESULT i_pAsyncResult, CUVIS_STATUS* io_pStatusResult);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_status(CUVIS_ASYNC_CAPTURE_RESULT i_pAsyncResult, CUVIS_STATUS* io_pStatusResult);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_capture(CUVIS_ACQ_CONT i_acqCont, CUVIS_MESU* o_pMesu, CUVIS_INT timeout_ms);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_capture_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CAPTURE_RESULT* o_pAsyncResult);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_get(CUVIS_ASYNC_CAPTURE_RESULT* io_pAsyncResult, CUVIS_INT timeout_ms, CUVIS_MESU* o_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_copy_handle(CUVIS_MESU i_mesu, CUVIS_MESU* o_pMesu);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_load(const CUVIS_CHAR* i_path, CUVIS_MESU* o_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_deep_copy(CUVIS_MESU i_mesu, CUVIS_MESU* o_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_clear_cube(CUVIS_PROC_CONT i_mesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_clear_implicit_reference(CUVIS_PROC_CONT i_mesu, CUVIS_REFERENCE_TYPE i_type);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_copy_handle(CUVIS_SESSION_FILE i_sess, CUVIS_SESSION_FILE* o_pSess);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_load(const CUVIS_CHAR* i_path, CUVIS_SESSION_FILE* o_pSess);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_free(CUVIS_SESSION_FILE* o_pSess);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_session_file_get_mesu(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_frameNo, CUVIS_SESSION_ITEM_TYPE i_type, CUVIS_MESU* o_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_session_file_get_reference_mesu(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_frameNo, CUVIS_REFERENCE_TYPE i_type, CUVIS_MESU* o_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_size(CUVIS_SESSION_FILE i_sess, CUVIS_SESSION_ITEM_TYPE i_type, CUVIS_INT* o_pSize);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_thumbnail(CUVIS_SESSION_FILE i_sess, CUVIS_IMBUFFER* o_pThumbnail);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_fps(CUVIS_SESSION_FILE i_sess, double* o_pFps);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_hash(CUVIS_SESSION_FILE i_sess, CUVIS_CHAR* o_pHash);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_operation_mode(CUVIS_SESSION_FILE i_sess, CUVIS_OPERATION_MODE* o_pMode);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_next_measurement(CUVIS_ACQ_CONT i_acqCont, CUVIS_MESU* o_pMesu, CUVIS_INT timeout_ms);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_has_next_measurement(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pHasNext);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_save(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_path, CUVIS_SAVE_ARGS args);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_set_name(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_name);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_set_comment(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_comment);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_free(CUVIS_MESU* io_pMesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_metadata(CUVIS_MESU i_mesu, CUVIS_MESU_METADATA* o_pMetaData);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_image(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_IMBUFFER* o_pBuf);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_measurement_get_data_string(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SIZE i_outBufferlength, CUVIS_CHAR* o_pValue);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_string_length(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SIZE* o_pLength);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_sensor_info(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SENSOR_INFO* o_pValue);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_gps(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_GPS* o_pGps);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_info(CUVIS_MESU i_mesu, CUVIS_CHAR* o_pKey, CUVIS_DATA_TYPE* o_pType, CUVIS_INT i_id);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_count(CUVIS_MESU i_mesu, CUVIS_INT* o_pCount);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_copy_handle(CUVIS_CALIB i_calibration, CUVIS_CALIB* o_pCalibration);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_create_from_path(const CUVIS_CHAR* i_factoryDir, CUVIS_CALIB* o_pCalibration);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_create_from_session_file(const CUVIS_SESSION_FILE i_sess, CUVIS_CALIB* o_pCalibration);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_free(CUVIS_CALIB* io_pCalibration);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_copy_handle(CUVIS_ACQ_CONT i_acqCont, CUVIS_ACQ_CONT* o_pAcqCont);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_create_from_calib(CUVIS_CALIB i_calib, CUVIS_ACQ_CONT* o_pAcqCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_create_from_session_file(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_simulate, CUVIS_ACQ_CONT* o_pAcqCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_state(CUVIS_ACQ_CONT i_acqCont, CUVIS_HARDWARE_STATE* o_pState);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_ready_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pIsReady);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_session_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_SESSION_INFO* o_pSessionInfo);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_set_session_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_SESSION_INFO const* i_pSessionInfo);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_queue_size_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_size);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_available_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_is_available);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_is_enabled);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT o_set_enabled);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_free(CUVIS_ACQ_CONT* io_pAcqCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_component_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_COMPONENT_INFO* o_pCompInfo);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_component_count(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pCount);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_pixel_format_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_CHAR const* i_pPixelFormat);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_comp_pixel_format_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, CUVIS_INT i_id, CUVIS_CHAR const* i_pPixelFormat);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_pixel_format_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_CHAR* o_pPixelFormat);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_available_pixel_format_count_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_INT* o_pCount);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_available_pixel_format_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_INT i_index, CUVIS_CHAR* o_pPixelFormat);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_copy_handle(CUVIS_PROC_CONT i_procCont, CUVIS_PROC_CONT* o_pProcCont);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_calib(CUVIS_CALIB i_calib, CUVIS_PROC_CONT* o_pProcCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_mesu(CUVIS_MESU i_mesu, CUVIS_INT i_loadReferences, CUVIS_PROC_CONT* o_pProcCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_session_file(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_loadReferences, CUVIS_PROC_CONT* o_pProcCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_get_reference(CUVIS_PROC_CONT i_procCont, CUVIS_MESU* o_pMesu, CUVIS_REFERENCE_TYPE i_type);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_set_reference(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu, CUVIS_REFERENCE_TYPE i_type);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_clear_reference(CUVIS_PROC_CONT i_procCont, CUVIS_REFERENCE_TYPE i_type);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_calc_distance(CUVIS_PROC_CONT i_procCont, double i_distanceMM);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_has_reference(CUVIS_PROC_CONT i_procCont, CUVIS_REFERENCE_TYPE i_type, CUVIS_INT* o_pHasReference);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_is_capable(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu, CUVIS_PROC_ARGS i_args, CUVIS_INT* o_pIsCapable);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_apply(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_set_args(CUVIS_PROC_CONT i_procCont, CUVIS_PROC_ARGS i_args);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_free(CUVIS_PROC_CONT* io_pProcCont);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_cube(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_CUBE_SETTINGS formatSettings);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_tiff(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_TIFF_SETTINGS formatSettings);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_create_envi(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings);

SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_view(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_VIEW_SETTINGS formatSettings);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_apply(CUVIS_EXPORTER i_exporter, CUVIS_MESU i_mesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_flush(CUVIS_EXPORTER i_exporter);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_get_queue_used(CUVIS_EXPORTER i_exporter, CUVIS_INT* o_pQueueUsed);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_free(CUVIS_EXPORTER* io_pExporter);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_copy_handle(CUVIS_VIEWER i_viewer, CUVIS_VIEWER* o_pViewer);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_create(CUVIS_VIEWER* o_pViewer, CUVIS_VIEWER_SETTINGS viewerSettings);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_apply(CUVIS_VIEWER i_viewer, CUVIS_MESU i_mesu, CUVIS_VIEW* o_pView);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_free(CUVIS_VIEWER* io_pViewer);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_get_data_count(CUVIS_VIEW i_view, CUVIS_INT* o_pCount);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_get_data(CUVIS_VIEW i_view, CUVIS_INT i_index, CUVIS_VIEW_DATA* o_pData);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_free(CUVIS_VIEWER* io_pView); //VIEWER or VIEW???

/*  MISC. */

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_capabilities(CUVIS_CALIB i_calibration, CUVIS_OPERATION_MODE i_mode, CUVIS_INT* o_pCapabilities);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_capabilities(CUVIS_MESU i_mesu, CUVIS_INT* o_pCapabilities);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_calib_id(CUVIS_MESU i_mesu, CUVIS_CHAR* o_pCalibId);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_id(CUVIS_CALIB i_calib, CUVIS_CHAR* o_pCalibId);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_info(CUVIS_CALIB i_calib, CUVIS_CALIBRATION_INFO* o_pCalibInfo);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_component_info(CUVIS_CALIB i_calib, CUVIS_INT i_id, CUVIS_COMPONENT_INFO* o_pCompInfo);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_component_count(CUVIS_CALIB i_calib, CUVIS_INT* o_pCount);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_get_calib_id(CUVIS_PROC_CONT i_procCont, CUVIS_CHAR* o_pCalibId);


SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_create(CUVIS_WORKER* o_pWorker, CUVIS_WORKER_SETTINGS worker_settings);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_free(CUVIS_WORKER* io_pWorker);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_acq_cont(CUVIS_WORKER i_worker, CUVIS_ACQ_CONT i_acq_cont);
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_proc_cont(CUVIS_WORKER i_worker, CUVIS_PROC_CONT i_proc_cont);
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_exporter(CUVIS_WORKER i_worker, CUVIS_EXPORTER i_exporter);
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_viewer(CUVIS_WORKER i_worker, CUVIS_VIEWER i_viewer);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_query_session_progress(CUVIS_WORKER i_worker, double* o_frames_read);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_ingest_session_file(CUVIS_WORKER i_worker, CUVIS_SESSION_FILE i_session_file, const char* i_frame_selection);
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_ingest_mesu(CUVIS_WORKER i_worker, CUVIS_MESU i_mesu);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_next_result(CUVIS_WORKER i_worker, CUVIS_MESU* o_pMesu, CUVIS_VIEW* o_pView, CUVIS_SIZE i_Timeout_ms);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_has_next_result(CUVIS_WORKER i_worker, CUVIS_INT* o_pHasNext);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_input_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pInputQueueLimit);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_mandatory_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pMandatoryLimit);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_supplementary_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pSupplementaryLimit);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_output_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pOutputQueueLimit);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_queue_used(CUVIS_WORKER i_worker, CUVIS_INT* o_pQueueUsed);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_drop_results(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanDrop);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_skip_measurements(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanSkip);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_skip_supplementary(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanSkip);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_is_processing_mandatory(CUVIS_WORKER i_worker, CUVIS_INT* o_pProcessingMandatory);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_start(CUVIS_WORKER i_worker);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_stop(CUVIS_WORKER i_worker);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_drop_all_queued(CUVIS_WORKER i_worker);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_is_processing(CUVIS_WORKER i_worker, CUVIS_INT* o_pIsProcessing);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_threads_busy(CUVIS_WORKER i_worker, CUVIS_INT* o_pThreadsBusy);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_state(CUVIS_WORKER i_worker, CUVIS_WORKER_STATE* o_pWorkerState);

SDK_CAPI
CUVIS_STATUS SDK_CCALL cuvis_set_special(const char*);

/* (DE-) ALLOCATORS FOR WRAPPERS TO OTHER LANGAUGES (E.G. MATLAB) */

ALLOCATE_AND_FREE(CUVIS_IMBUFFER, imbuffer);
ALLOCATE_AND_FREE(CUVIS_GPS, gps);
ALLOCATE_AND_FREE(CUVIS_SENSOR_INFO, sensor_info);
ALLOCATE_AND_FREE(CUVIS_SESSION_INFO, session_info);
ALLOCATE_AND_FREE(CUVIS_MESU_METADATA, mesu_metadata);
ALLOCATE_AND_FREE(CUVIS_SAVE_ARGS, save_args);
ALLOCATE_AND_FREE(CUVIS_PROC_ARGS, proc_args);
ALLOCATE_AND_FREE(CUVIS_EXPORT_GENERAL_SETTINGS, export_general_settings);
ALLOCATE_AND_FREE(CUVIS_EXPORT_CUBE_SETTINGS, export_cube_settings);
ALLOCATE_AND_FREE(CUVIS_EXPORT_VIEW_SETTINGS, export_view_settings);
ALLOCATE_AND_FREE(CUVIS_EXPORT_TIFF_SETTINGS, export_tiff_settings);
ALLOCATE_AND_FREE(CUVIS_VIEWER_SETTINGS, viewer_settings);
ALLOCATE_AND_FREE(CUVIS_VIEW_DATA, view_data);
ALLOCATE_AND_FREE(CUVIS_COMPONENT_INFO, component_info);
ALLOCATE_AND_FREE(CUVIS_WORKER_SETTINGS, worker_settings);
ALLOCATE_AND_FREE(CUVIS_WORKER_STATE, worker_state);
ALLOCATE_AND_FREE(CUVIS_CALIBRATION_INFO, calibration_info);

/* GETTER AND SETTER STUB GENERATION */


ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_fps, double, "Frames per second");
ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_fps, double, "Frames per second");
ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_average, CUVIS_INT, "Number of averages");
ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_average, CUVIS_INT, "Number of averages");
ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_integration_time, double, "Integration time in milliseconds");
ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_integration_time, double, "Integration time in milliseconds");
ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_auto_exp, CUVIS_INT, "get_auto_exp");
ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_auto_exp, CUVIS_INT, "set_auto_exp");

ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_auto_exp_comp, double, "get auto exposure compensation");
ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_auto_exp_comp, double, "set auto exposure compensation");

ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_operation_mode, CUVIS_OPERATION_MODE, "enumeration value");

ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_operation_mode, CUVIS_OPERATION_MODE, "enumeration value");

ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_continuous, CUVIS_INT, "0 = stop, 1 = run");

ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_bandwidth, CUVIS_INT, "bandwidth in MBit/s");

ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_queue_size, CUVIS_INT, "size of measurement queue");

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_queue_size_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_size);

ACQ_GET_SINGLE_VALUE(cuvis_acq_cont_queue_used, CUVIS_INT, "used part of measurement queue");

COMP_GET_SINGLE_VALUE(cuvis_comp_online, CUVIS_INT, "0 = false, 1 = true");

COMP_GET_SINGLE_VALUE(cuvis_comp_temperature, double, "temperature in degrees celsius");

COMP_GET_SINGLE_VALUE(cuvis_comp_bandwidth, CUVIS_INT, "bandwidth in MBit/s");

COMP_GET_SINGLE_VALUE(cuvis_comp_driver_queue_size, CUVIS_INT, "driver's internal receiving queue size");
COMP_GET_SINGLE_VALUE(cuvis_comp_driver_queue_used, CUVIS_INT, "driver's internal receiving queue used");
COMP_GET_SINGLE_VALUE(cuvis_comp_hardware_queue_size, CUVIS_INT, "internal hardware buffer size (if supported)");
COMP_GET_SINGLE_VALUE(cuvis_comp_hardware_queue_used, CUVIS_INT, "internal hardware buffer used (if supported)");

COMP_GET_SINGLE_VALUE(cuvis_comp_gain, double, "a.u.");

COMP_SET_SINGLE_VALUE(cuvis_comp_gain, double, "a.u.");

COMP_GET_SINGLE_VALUE(cuvis_comp_integration_time_factor, double, "factor to main integration time");

COMP_SET_SINGLE_VALUE(cuvis_comp_integration_time_factor, double, "factor to main integration time");

#define CUVIS_CHECK(code)                                    \
  if (status_ok != (code))                                   \
  {                                                          \
    printf("Call failed. %s\n", cuvis_get_last_error_msg()); \
    return -1;                                               \
  }
;

#define IMBUFFER_GET(ptr, x, y, chn, imbuf) ptr[((y) * (imbuf).width + (x)) * (imbuf).channels + (chn)]

#ifdef __cplusplus
}
#endif

#undef ALLOCATE_AND_FREE
#undef ACQ_GET_SINGLE_VALUE
#undef ACQ_SET_SINGLE_VALUE
#undef COMP_GET_SINGLE_VALUE
#undef COMP_SET_SINGLE_VALUE

#endif
```


