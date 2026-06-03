
/**
 @file cuvis.h
 SDK calls for cuvis C SDK. This header defines all public C SDK functions and data types
 */


/**
 \addtogroup c_examples Examples

 There are several examples delivered with the SDK

 # Overview

  Under Windows you can find the examples in your installation directory (Default: "C:\Program Files\Cuvis\sdk\cuvis_c\examples" or "C:\Program Files\Cuvis\sdk\cuvis_cpp\examples"),
  under Linux they can be found in "/lib/cuvis/cuvis_c/examples" or "/lib/cuvis/cuvis_cpp/examples" .
  Each Example comes with the precompiled binary, a short .sh-script to run the application and the source code file. The .sh-script requires the bash console. Under windows we recommend to use Git Bash.

  Examples 01-04 and 07 require the "sample_data" folder to be present in the installation directory ( Windows: "C:\Program Files\Cuvis\sdk\sample_data" , Linux: "/lib/cuvis/sample_data").
  Examples 05-06 require a camera to be installed and connected.

 # Compiling examples
  Instead of using the precompiled examples, you can use the provided source code to compile it yourself. Under Linux this is quite simple.

 ```
 sudo apt install gcc
 sudo gcc -o 0X_example main.c  -L/lib/cuvis -lcuvis
 ```

 or

 ```
 sudo apt install g++
 sudo g++ -o 0X_example main.cpp  -L/lib/cuvis -lcuvis -std=c++17
 ```
 */

/**
* \addtogroup c_examples Examples
* @{
*/

/**
* Example_1_Take_Snapshot
* \example 01/main.c
* Connect to camera and record a measurement.
* */

/**
* Example_2_Load_Measurement
* \example 02/main.c
* Load and analyse a recorded measurement.
* */

/**
* Example_3_Reprocess
* \example 03/main.c
* Load and reprocess a recorded measurement.
* */

/**
* Example_4_Exporters
* \example 04/main.c
* Expot / Convert Cubert Measurements to different file formats.
* */

/**
* Example_5_Record_Video
* \example 05/main.c
* Record a Video using the Worker Class.
* */

/**
* Example_6_Record_Video_From_SessionFile
* \example 06/main.c
* Record Video From Session File.
* */

/**
* Example_7_Change_Distance
* \example 07/main.c
* Load and change a measurement.
* */

/** @} */

/** \addtogroup cuvis_handle Handles
*
* @brief The SDK is handle-based, i.e to access an internal data object you will require a handle.
*
* The main concepts of the SDK which use handles are the \ref cuvis_mesu, the \ref cuvis_calib, the \ref cuvis_session, the \ref cuvis_acq, the \ref cuvis_proc, the \ref cuvis_viewer, the \ref cuvis_exporter and the \ref cuvis_worker.
* On how to obtain a handle of the individual components of the SDK, see the respective Pages for the individual components.
* 
* For example, a handle wich represents a \ref cuvis_mesu can be obtained by either loading (\ref cuvis_measurement_load)
* or by recording (\ref cuvis_acq_cont_capture or \ref cuvis_acq_cont_get_next_measurement) a measurement. \n
* A measurement is equivalent to a data-cube and would be called a frame in a traditional Camera-Setup.
* The handle then refers to measurement in the SDK context.
*
* Each handle should be freed after it is no longer needed. This can be done via the respective free function.
* Calling the free-function does not necessarily free up the used memory immediately, because there could be multiple handles referring to the same object.
*
*
*/

#ifndef CUVIS_SDK_C_H
#define CUVIS_SDK_C_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
/** The cuvis namespace contains all SDK functions. */
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

/** macro for creating allocate and free functions for c data structures*/
#define ALLOCATE_AND_FREE(DATATYPE, NAME)                     \
  /** Allocate function for DATATYPE. */                      \
  SDK_CAPI DATATYPE* SDK_CCALL cuvis_##NAME##_allocate(void); \
  /** Free function for DATATYPE */                           \
  SDK_CAPI void SDK_CCALL cuvis_##NAME##_free(DATATYPE* ptr);

/** macro for creating acquisition getter functions */
#define ACQ_GET_SINGLE_VALUE(NAME, TYPE, COMMENT)                            \
  /** Get NAME function. Details: COMMENT\n Result is written to o_pvalue */ \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_get(CUVIS_ACQ_CONT i_acqCont, TYPE* o_pvalue);

/** macro for creating stubs of sync and async acquisition setter functions */
#define ACQ_SET_SINGLE_VALUE(NAME, TYPE, UNIT_STR)                                            \
  /** set NAME. Unit: UNIT_STR\n Block until done or failed  */                               \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set(CUVIS_ACQ_CONT i_acqCont, TYPE value);           \
  /** set NAME asynchronously. Unit: UNIT_STR\n Use @ref cuvis_async_call_get to sync again*/ \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, TYPE value);

/** macro for creating acquisition-component getter functions */
#define COMP_GET_SINGLE_VALUE(NAME, TYPE, COMMENT)                           \
  /** Get NAME function. Details: COMMENT\n Result is written to o_pvalue */ \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, TYPE* o_pvalue);

/** macro for creating stubs of sync and async acquisition-component setter functions */
#define COMP_SET_SINGLE_VALUE(NAME, TYPE, UNIT_STR)                                                 \
  /** set NAME. Unit: UNIT_STR\n Block until done or failed  */                                     \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, TYPE value); \
  /** set NAME asynchronously. Unit: UNIT_STR\n Use @ref cuvis_async_call_get to sync again*/       \
  SDK_CAPI CUVIS_STATUS SDK_CCALL NAME##_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, TYPE value);

/* SIMPLE TYPES */

/** */
#define CUVIS_INT int32_t

#define CUVIS_SIZE uint64_t

/** handle */
#define CUVIS_HANDLE CUVIS_INT

/** handle value of 0 is reserved for invalid handles */
#define CUVIS_HANDLE_NULL CUVIS_HANDLE(0)

/** placeholder data type*/
#define CUVIS_MISC_PTR void*

/** */
#define CUVIS_CHAR char

/** */
#define CUVIS_WCHAR wchar_t

/** max string buffer length (e.g. for paths) */
#define CUVIS_MAXBUF 256

/** cstring data type definition */
#define CUVIS_STRING CUVIS_CHAR[CUVIS_MAXBUF]

/** field for binary flags */
#define CUVIS_FLAGS uint32_t

/** time since epoch in millisecond steps */
#define CUVIS_TIMESTAMP uint64_t

/** measurement handle */
#define CUVIS_MESU CUVIS_HANDLE

/** measurement session_info file handle */
#define CUVIS_SESSION_FILE CUVIS_HANDLE

/** calibration handle */
#define CUVIS_CALIB CUVIS_HANDLE

/** acquisition context handle */
#define CUVIS_ACQ_CONT CUVIS_HANDLE

/** processing context handle */
#define CUVIS_PROC_CONT CUVIS_HANDLE

/** exporter handle (all exporter types) */
#define CUVIS_EXPORTER CUVIS_HANDLE

/** data viewer handle */
#define CUVIS_VIEWER CUVIS_HANDLE

/** data viewer result handle (view) */
#define CUVIS_VIEW CUVIS_HANDLE

/** worker handle */
#define CUVIS_WORKER CUVIS_HANDLE

/** @brief handle to an async function call result.

A handle can be checked by the function @ref cuvis_async_call_get */
#define CUVIS_ASYNC_CALL_RESULT CUVIS_HANDLE

/** @brief handle to an async capture result.

A handle can be checked by the function @ref cuvis_async_capture_get */
#define CUVIS_ASYNC_CAPTURE_RESULT CUVIS_HANDLE

/** @brief holds capabilities for operation mode as flags
*/
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

/** @brief the measurement was over-illuminated

    One of the devices sensor data points were over-saturated while recording
    This may not be directly visible in the data cube, as the sensor data needs
    extensive processing.
    @note only the spectral data is checked. The pan image's saturation is not checked.

    If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_OVERILLUMINATED_KEY
    */
#define CUVIS_MESU_FLAG_OVERILLUMINATED 1

/** @brief A reference measurement used has poor quality

One or more of the reference measurements used had a poor data quality.
This may lead to invalid results.

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_POOR_REFERENCE_KEY
*/
#define CUVIS_MESU_FLAG_POOR_REFERENCE 2

/** @brief the white balancing detected bad data

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY
*/
#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING 4

/** the dark's integration time does not match the measurement

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_DARK_INTTIME_KEY
*/
#define CUVIS_MESU_FLAG_DARK_INTTIME 8

/** the sensor temperature at dark's recording does not match measurement's recording device temperature

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_DARK_TEMP_KEY
*/
#define CUVIS_MESU_FLAG_DARK_TEMP 16

/** the white's integration time does not match the measurement

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_WHITE_INTTIME_KEY
*/
#define CUVIS_MESU_FLAG_WHITE_INTTIME 32

/** the sensor temperature at white's recording does not match measurement's recording device temperature

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_WHITE_TEMP_KEY
*/
#define CUVIS_MESU_FLAG_WHITE_TEMP 64

/** the white's dark integration time does not match the measurement

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY
*/
#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME 128

/** the sensor temperature at white's dark recording does not match measurement's recording device temperature

If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY
*/
#define CUVIS_MESU_FLAG_WHITEDARK_TEMP 256

/** @brief the measurements pan image was over-illuminated

    One of the devices pan sensor data points were over-saturated while recording
    This may not be directly visible in the data cube, as the sensor data needs
    extensive processing.
    @note only the pan data is checked. The spectral image's saturation is not checked.

    If this flag is set, additional information can retrieved by calling
@ref cuvis_measurement_get_data_sensor_info with the key @ref CUVIS_MESU_FLAG_PAN_OVERILLUMINATED_KEY
    */
#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED 512

/** \addtogroup cuvis_reserved_keys Reserved Keys
 *  @{
*/

/** name of the data field for the hyperspectral cube (in all modes except @ref Preview) */
#define CUVIS_MESU_CUBE_KEY "cube"

/** name of the pan image (pixels registered to  @ref CUVIS_MESU_CUBE_KEY)*/
#define CUVIS_MESU_PAN_KEY "pan"

/** name of the GPS data field, if available */
#define CUVIS_MESU_GPS_KEY "GPS_data"

/** name of the generate preview image, if available. The preview will be generated by the @ref cuvis_proc_cont_apply function*/
#define CUVIS_MESU_PREVIEW_KEY "preview"

/** @brief If this field is present, a dark was set while recording the measurement.
  * This is the dark that is implicitly loaded when a processing context is created
  * with the current measurement and used, if a dark is needed (unless overwritten by
  * @ref cuvis_proc_cont_set_reference )
  * The reference file should be located in ../Calibration/<reference-name>.cu3 or the
  * precise path defined by the string value of the data tag
  */
#define CUVIS_MESU_DARKREF_KEY "dark_ref"

/** @brief If this field is present, a white was set while recording the measurement.
  * This is the white that is implicitly loaded when a processing context is created
  * with the current measurement and used, if a dark is needed (unless overwritten by
  * @ref cuvis_proc_cont_set_reference )
  * The reference file should be located in ../Calibration/<reference-name>.cu3 or the
  * precise path defined by the string value of the data tag
  */
#define CUVIS_MESU_WHITEREF_KEY "white_ref"

/** @brief If this field is present, a white's dark was set while recording the measurement.
  * This is the white' dark that is implicitly loaded when a processing context is created
  * with the current measurement and used, if a dark is needed (unless overwritten by
  * @ref cuvis_proc_cont_set_reference )
  * The reference file should be located in ../Calibration/<reference-name>.cu3 or the
  * precise path defined by the string value of the data tag
  */
#define CUVIS_MESU_WHITEDARKREF_KEY "white_dark_ref"

/** see @ref CUVIS_MESU_FLAG_OVERILLUMINATED */
#define CUVIS_MESU_FLAG_OVERILLUMINATED_KEY "Flag_DataIsOverilluminated"

/** see @ref CUVIS_MESU_FLAG_OVERILLUMINATED */
#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED_KEY "Flag_PanDataIsOverilluminated"

/** see @ref CUVIS_MESU_FLAG_POOR_REFERENCE */
#define CUVIS_MESU_FLAG_POOR_REFERENCE_KEY "Flag_DataUsesPoorReference"

/** see @ref CUVIS_MESU_FLAG_POOR_WHITE_BALANCING */
#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY "Flag_PoorWhiteBalancingData"

/** see @ref CUVIS_MESU_FLAG_DARK_INTTIME */
#define CUVIS_MESU_FLAG_DARK_INTTIME_KEY "Flag_IntegrationTimeMismatchDark"

/** see @ref CUVIS_MESU_FLAG_DARK_TEMP */
#define CUVIS_MESU_FLAG_DARK_TEMP_KEY "Flag_TemperatureMismatchDark"

/** see @ref CUVIS_MESU_FLAG_WHITE_INTTIME */
#define CUVIS_MESU_FLAG_WHITE_INTTIME_KEY "Flag_IntegrationTimeMismatchWhite"

/** see @ref CUVIS_MESU_FLAG_WHITE_TEMP */
#define CUVIS_MESU_FLAG_WHITE_TEMP_KEY "Flag_TemperatureMismatchWhite"

/** see @ref CUVIS_MESU_FLAG_WHITEDARK_INTTIME */
#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY "Flag_IntegrationTimeMismatchWhiteDark"

/** see @ref CUVIS_MESU_FLAG_WHITEDARK_TEMP */
#define CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY "Flag_TemperatureMismatchWhiteDark"
/** @}*/

/** \addtogroup cuvis_info_layer The info layer
  *
  * The info layer can be retrieved with the function @ref cuvis_measurement_get_data_image
  * Though is appears to be an image and will also be exported and fragmented as an image
  * it is actually a set of flags. Each position of the a info-layer pixel represents a data
  * flag for a respective cube (or pan image).
  *
  * E.g. if a cube (@ref CUVIS_MESU_CUBE_KEY) has the size of 410x410x164 (W x H x Chn), the
  * respective info layer (@ref CUVIS_MESU_CUBE_INFO_KEY) will have a size of 410x410. The info_layer
  * value at position x,y contains the flags for the whole spectrum at position x,y in the cube.
  *
  * The same is true for the pan-chromatic image ((@ref CUVIS_MESU_CUBE_INFO_KEY) and @ref CUVIS_MESU_CUBE_INFO_KEY, respectively)
  *
  * The info layer pixel value is retrieved by binary operation.
  *
  * @note The info layer may not be available on all devices.
  *
  *Example:
  *
  * @code
  * // mesu is a measurement already loaded
  * // load the info channel to cube_info_layer_buffer
  * CUVIS_IMBUFFER cube_info_layer_buffer;
  * cuvis_measurement_get_data_image(mesu, CUVIS_MESU_CUBE_INFO_KEY, &cube_info_layer_buffer);
  * //now load pixel x=15, y=17' s flag information
  * int x = 15, y = 17;
  * uint16_t info_ptr = (const uint16_t*)(cube_info_layer_buffer.raw);
  * cube_info_layer_buffer pixel_info = IMBUFFER_GET(info_ptr, x, y, 0, imbuf);
  * //check if the pixel is ok
  * if (pixel_info == CUVIS_MESU_INFO_OK)
  *     printf("pixel 15|17 ok \n");
  * else
  * {
  *     // multiple flags can be set
  *     if ((pixel_info  & CUVIS_MESU_INFO_BAD_PIXEL) != 0)
  *         printf("pixel 15|17 is over-illuminated \n");
  *
  *     if ((pixel_info  & CUVIS_MESU_INFO_OVERILLUMINATED) != 0)
  *         printf("pixel 15|17 is a bad pixel \n");
  *     // ...
  * }
  * @endcode
  *  @{
  */

/** name of the info channel of its respective cube.*/
#define CUVIS_MESU_CUBE_INFO_KEY "cube_info_layer"

/** name of the info channel of its respective pan image.*/
#define CUVIS_MESU_PAN_INFO_KEY "pan_info_layer"

/** no flag set, only valid, if pixel value is equal 0 */
#define CUVIS_MESU_INFO_OK 0

/** one or more channels of the spectrum are over-exposed / the pan image is over-exposed at this position*/
#define CUVIS_MESU_INFO_OVERILLUMINATED 1

/** the pixel is marked bad, eg. a pixel of the respective spectrum is dead */
#define CUVIS_MESU_INFO_BAD_PIXEL 2

/** one or more channels of the spectrum of the white reference that was used to calculate this position was over-exposed*/
#define CUVIS_MESU_INFO_OVERILLUMINATED_REFERENCE 4

/** the meausurement was darker then the dark reference at this position (underflow) */
#define CUVIS_MESU_INFO_UNDERFLOW_MEASUREMENT_MIN_DARK 8

/** the white reference was darker then the dark reference at this position (underflow) */
#define CUVIS_MESU_INFO_UNDERFLOW_WHITE_MIN_DARK 16

/** the reflectance value exceeded the maximum value possible by the data format (i.e. the value reflectance reached or exceeded 655.35% (uint16 value of 65535) */
#define CUVIS_MESU_INFO_REFERENCE_CALC_OVERFLOW 32

/** the spectrum at this position is incomplete, e.g by a bad / too close distance calibration */
#define CUVIS_MESU_INFO_INCOMPLETE 64

/** @} */

//todo capabilites binary flags

/* ENUMERATIONS */

/** \addtogroup cuvis_returns Return Values of SDK Functions
 *  @{
*/

/** @brief return state of any SDK function */
enum cuvis_status_t
{
  /** the function encountered no problems */
  status_ok = 1,
  /** the function failed for some reason. Call cuvis_get_last_error_msg for details */
  status_error = -1,
  /** a async function has not been started yet */
  status_deferred = -10,

  /** the async call was overwritten by another async call to the same internal values */
  status_overwritten = -11,

  /** obtaining a async function result has timed out. Call again later */
  status_timeout = -12,

  /** polling a measurement returned no result / frame was dropped */
  status_no_measurement = -20,

  /** retrieving a value is (currently) not possible */
  status_not_available = -30,

  /** processing the measurement with the worker failed, raw data is available */
  status_not_processed = -41,

  /** storing the measurement with the worker/exporter failed */
  status_not_stored = -42,

  /** obtaining the measurement's view with the worker failed, raw data is available */
  status_no_view = -43

};

/** @} */

/** the state of the hardware */
enum cuvis_hardware_state_t
{
  /** at least one required components is offline */
  hardware_state_offline = 0,
  /** all required components are online, at least one optional component is offline */
  hardware_state_partially_online = 1,
  /** all components are online */
  hardware_state_online = 2
};


/**
* \addtogroup cuvis_log Logging
* @{
*/

/** @brief The available log levels. */
enum cuvis_loglevel_t
{
  /** only report error not recoverable */
  loglevel_fatal = 0,

  /** report errors and @ref loglevel_fatal messages */
  loglevel_error = 1,

  /** report warnings and @ref loglevel_error messages.  */
  loglevel_warning = 2,

  /** report status information and @ref loglevel_warning messages.  */
  loglevel_info = 3,

  /** report all messages, including debug messages  */
  loglevel_debug = 4,
};

/** @}*/

/** @brief supported image buffer formats */
enum cuvis_imbuffer_format_t
{
  /** 8 bit, unsigned */
  imbuffer_format_uint8 = 1,

  /** 16 bit, unsigned */
  imbuffer_format_uint16 = 2,

  /** 32 bit, unsigned */
  imbuffer_format_uint32 = 3,

  /** IEEE 754 single-precision (32 bit) floating-point value (a.k.a float) */
  imbuffer_format_float = 4,
};

#define CUVIS_IMBUFFER struct cuvis_imbuffer_t



/** The session file item type */
enum cuvis_session_item_type_t
{
  /** all regular measurements, also list dropped frames */
  session_item_type_frames = 0,
  /** all regular measurements, excluding dropped frames (i.e. actual images) */
  session_item_type_frames_no_gaps = 1,
  /** all reference measurements */
  session_item_type_references = 2
};


/** @brief the data field's type */
enum cuvis_data_type_t
{
  /** the data type is unsupported or unknown by the SDK */
  data_type_unsupported = 0,

  /** data type is image, retrieve with @ref cuvis_measurement_get_data_image */
  data_type_image = 1,

  /** data type is gps, retrieve with @ref cuvis_measurement_get_data_gps */
  data_type_gps = 2,

  /** data type is string, retrieve with @ref cuvis_measurement_get_data_string */
  data_type_string = 3,

  /** data type is sensor info, retrieve with @ref cuvis_measurement_get_data_sensor_info */
  data_type_sensor_info = 4,
};

/** @brief The processing mode (a.k.a. capture mode) of a measurement. */
enum cuvis_processing_mode_t
{
  /** @brief processed as cube, but without reference

         The measurement is processed into a cube. Effects of
         sensor temperature, vignetting,
         missing flat-fielding, etc. are not
         corrected.

          */
  Cube_Raw = 0,

  /** @brief processed as cube, with dark subtract as reference.

         Subtracts the dark from the raw measurement.
         I_DS = I_RAW - I_DARK
          */
  Cube_DarkSubtract = 1,

  /** @brief processed as cube, with dark subtract and white as reference

           Calculates the reflectance as follows:

           I_REF = 10000(I_RAW - I_DARK) / (I_WHITE - I_WHITEDARK)

           Depending on the camera, I_WHITEDARK will be substituted
           I_DARK, is missing. Note the factor of 10000.
           A value of 100% corresponds to 10000 counts.

            */
  Cube_Reflectance = 2,

  /** @brief processed as cube, with spectral radiance calibration

             The spectral radiance calibration is camera-dependent.
             It's value is given in the units of W m^{-2} sr^{-1} um^{-1}

              */
  Cube_SpectralRadiance = 3,

  /** unprocessed (no cube), only preview image */
  Preview = 5
};

/** @brief The type of a reference */
enum cuvis_reference_type_t
{
  /** a dark reference for dark subtract/reflectance/sp. rad */
  Reference_Dark = 0,

  /** white reference measurement, brightness defined as 100% */
  Reference_White = 1,

  /** the dark corresponding to the white reference measurement*/
  Reference_WhiteDark = 2,

  /** spectral sprad measurement object (spectral fields) */
  Reference_SpRad = 3,

  /** spectral distance reference (spectral fields). If normal mesu.
         is used, measurement is calculated from it */
  Reference_Distance = 4
};

/**
* @addtogroup cuvis_acq Acquisition Context
* @{
*/

/** @brief Operation mode of a camera. */
enum cuvis_operation_mode_t
{
  /** software trigger, aka "single shot mode" or "software mode". */
  OperationMode_Software = 1,
  /** triggered by internal clock, aka "video mode". */
  OperationMode_Internal = 2,
  /** triggered by external trigger, aka "trigger mode". */
  OperationMode_External = 3,
  /** undefiend (e.g. changing) */
  OperationMode_Undefined = 4
};

/**@}*/

/** @brief the pan sharpening interpolation type for scaling up the cube before applying the pan image's weights */
enum cuvis_pan_sharpening_interpolation_type_t
{
  /// nearest neighbor interpolation
  pan_sharpening_interpolation_type_NearestNeighbor = 0,
  /// bilinear interpolation (recommended)
  pan_sharpening_interpolation_type_Linear = 1,
  /// bicubic interpolation
  pan_sharpening_interpolation_type_Cubic = 2,
  ///Lanczos (8x8)
  pan_sharpening_interpolation_type_Lanczos = 4
};

/** @brief the pan-sharpening algorithm for calculating the pan image's weights */
enum cuvis_pan_sharpening_algorithm_t
{
  /** Interpolate @ref CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE but no operation
       * is applied to apply the pan image information to the data. This mode is
       * recommended together with NearestNeighbor interpolation.
       */
  pan_sharpening_algorithm_Noop = 0,

  /** @brief cuvis macro pixel algorithm
      * @author Dr. Rene Heine
      *
      * Weights spectral "macro pixel" with local pan image gradient
      */
  pan_sharpening_algorithm_CubertMacroPixel = 1,

  /** @brief cuvis pan ratio algorithm
      * @author Arnd Brandes
      *
      * Relative pan-image brighness (white refernce and current image) is used as weight for specral image
      */
  pan_sharpening_algorithm_CubertPanRatio = 2,

  /** @brief cuvis pan overlay algorithm
      * @author Philip Manke
      *
      * Mode used viewing classifier results with the pan image as an overlay. ONLY works with images from viewer
      */
  pan_sharpening_algorithm_PCAFusion = 3,
};

/** @brief the tiff compression options */
enum cuvis_tiff_compression_mode_t
{
  /** do not compress data */
  tiff_compression_mode_None = 0,

  /** compress LZW. */
  tiff_compression_mode_LZW = 1
};

/** @brief the tiff export format. */
enum cuvis_tiff_format_t
{
  /** Export each channel as separate files */
  tiff_format_Single = 0,

  /** Create a multi-channel tiff (recommended format) */
  tiff_format_MultiChannel = 1,

  /** Create a multi-page tiff, i.e. each channel is a "sub-image" within the tiff.  */
  tiff_format_MultiPage = 2,
};

/** image data types for view data */
enum cuvis_view_category_t
{
  /** data is process as an image for displaying. Pan-sharpening may have been applied. The bit depth is always 8 per channel*/
  view_category_image = 0,

  /** data contains calculation results. The format is always single precision floating point. */
  view_category_data = 1,
};

/** the component types */
enum cuvis_component_type_t
{
  /** the component is an image sensor (camera) */
  component_type_image_sensor = 0,
  /** the component is a non-camera, e.g. GPS */
  component_type_misc_sensor = 1,
};

/** @brief merge mode for the cube exporter */
enum cuvis_session_merge_mode_t
{
  /** Default behaviour, on export keep filestructure intact */
  session_merge_mode_Default = 0,

  /** On export run in fragmentation mode, meaning for session files write each measurement in a separate file, for legacy export write data containers in separate tiff files*/
  session_merge_mode_Fragmentation = 1,

  /** On export run in merging mode, meaning try to write all measurements into a single file. for legacy export this does nothing. */
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

/** @brief image buffer data structure with meta-data
    *
    * The image buffer data structure holds a anonymous
    * raw data pointer, that can be interpreted to give
    * a meaningful data array with the help of the other
    * members:
    * The \ref format gives the information of the data type,
    * the \ref width, \ref length, and \ref channels give the
    * number of elements in the array.
    *
    * The \ref wavelength property is only set for hyperspectral cubes
    * but not for normal images. If it exists, it is an array with the number
    * of channels
    *
    * Example:
    * @code
    * // format = CUVIS_IMBUFFER_FORMAT_UINT16
    * // x in [0, width)
    * // y in [0,   height)
    * // chn in [0, channels)
    * unsigned index = (y * width + x) * channels + chn;
    * uint16_t value = ((uint16_t*) raw)[index];
    * unsigned lambda = cube.wavelength[chn];
    * @endcode
    *
    * see also: \ref IMBUFFER_GET
    */
struct cuvis_imbuffer_t
{
  /** the memory reference of the cube.
                 Valid as long as the parent element (e.g. measurement)
                 is valid and unchanged. */
  uint8_t const* raw;
  /** number of bytes per data element */
  uint32_t bytes;
  /**  total number of bytes in array */
  uint32_t length;
  /** width of buffer */
  uint32_t width;
  /** height of buffer */
  uint32_t height;

  /** number of channels */
  uint16_t channels;

  /** @brief the buffer format
      *
      * The buffer format defines what the member \ref raw can be casted into.
      */
  CUVIS_IMBUFFER_FORMAT format;

  /** @brief the wavelength vector
      *
      * If the \ref cuvis_imbuffer_t is not a hyperspectral cube, the value will be nullptr
      * For cubes this is an array of length channels, the elements define the
      * cube's wavelength in nanometers.
      */
  uint32_t const* wavelength;
};

struct cuvis_sensor_info_t
{
  /** number of averages used*/
  uint32_t averages;

  /** the sensors's temperature while readout (0 if not applicable) */
  double temperature;

  /** gain value while recording */
  double gain;

  /** the timestamp (UTC) of the image readout (senor's hardware clock )*/
  CUVIS_TIMESTAMP readout_time;

  /** width of buffer */
  uint32_t width;
  /** height of buffer */
  uint32_t height;

  /** ID given to this measurement by the device hardware or driver */
  CUVIS_SIZE raw_frame_id;

  /** The sensor read-out pixel format used by this device. Informs how many bits per pixel are available. */
  CUVIS_CHAR pixel_format[CUVIS_MAXBUF];

  /** The real integration time of the sensor (exposure time) in ms */
  double integration_time;
};

/** @brief The gps data structure */
struct cuvis_gps_t
{
  /** gps longitude in decimal degrees */
  double longitude;

  /** gps latitude in decimal degrees */
  double latitude;

  /** gps altitude in meters*/
  double altitude;

  /** the timestamp (UTC) while recoding the gps.*/
  CUVIS_TIMESTAMP time;
};

/** internal session_info info of acquisition context */
struct cuvis_session_info_t
{
  /** session_info name */
  CUVIS_CHAR name[CUVIS_MAXBUF];

  /** SessionFile number. Will be increased by stopping & starting recording */
  CUVIS_INT session_no;

  /** Sequence number. Increases with each recorded frame. Reset, if session_no changes */
  CUVIS_INT sequence_no;
};
#define CUVIS_SESSION_INFO struct cuvis_session_info_t

/** internal info/data of calibration */
struct cuvis_calibration_info_t
{
  /** camera model name */
  CUVIS_CHAR model_name[CUVIS_MAXBUF];

  /** camera serial number */
  CUVIS_CHAR serial_no[CUVIS_MAXBUF];

  /** timestamp (UTC) of calibration date*/
  CUVIS_TIMESTAMP calibration_date;

  /** calibration annotation name */
  CUVIS_CHAR annotation_name[CUVIS_MAXBUF];

  /** calibration unique ID */
  CUVIS_CHAR unique_id[CUVIS_MAXBUF];

  /** calibration file path */
  CUVIS_CHAR file_path[CUVIS_MAXBUF];

  /** cube width, -1 if unknown */
  uint32_t cube_width;

  /** cube height, -1 if unknown */
  uint32_t cube_height;

  /** cube number of channels, -1 if unknown */
  uint32_t cube_channels;

  /** cubes wavelengths (nm) vector, contains 'cube_channels' values, can be nullptr if wavelengths are unknown */
  uint32_t const* cube_wavelengths;
};
#define CUVIS_CALIBRATION_INFO struct cuvis_calibration_info_t

/** @brief The measurement meta structure */
struct cuvis_mesu_metadata_t
{
  /** The name of the measurement */
  CUVIS_CHAR name[CUVIS_MAXBUF];

  /** The output file path */
  CUVIS_CHAR path[CUVIS_MAXBUF];

  /** The User Comment linked to the measurement */
  CUVIS_CHAR comment[CUVIS_MAXBUF];

  /** The Capture Time of the Measurement */
  CUVIS_TIMESTAMP capture_time;

  /** The factory calibration date of the device */
  CUVIS_TIMESTAMP factory_calibration;

  /** The name of the device, which took the measurement */
  CUVIS_CHAR product_name[CUVIS_MAXBUF];

  /** The serial number of the device, which took the measurement */
  CUVIS_CHAR serial_number[CUVIS_MAXBUF];

  /** The Assembly Data of the device */
  CUVIS_CHAR assembly[CUVIS_MAXBUF];

  /** The integration time of the measurement (exposure time) in ms */
  double integration_time;

  /** Number of averaging taken */
  CUVIS_INT averages;

  /** Distance, the measurement was recorded in mm. If not provided, value is -1 */
  double distance;

  /** session_info name */
  CUVIS_CHAR session_info_name[CUVIS_MAXBUF];

  /** SessionFile number. Will be increased by stopping & starting recording */
  CUVIS_INT session_info_session_no;

  /** Sequence number. Increases with each recorded frame. Reset, if session_no changes */
  CUVIS_INT session_info_sequence_no;

  /** The current processing mode of the cube */
  CUVIS_PROCESSING_MODE processing_mode;

  /** The processing mode at the time of the cube was recorded */
  CUVIS_PROCESSING_MODE processing_mode_at_capture;

  /** measurement flags */
  CUVIS_FLAGS measurement_flags;

  /** The frame ID assigned by cuvis to this measurement */
  CUVIS_SIZE measurement_frame_id;
};

/**
* @addtogroup cuvis_exporter Export API
* @{
*/

/** @brief options for saving as cu3/cu3s files
  *
  * The cube exporter works asynchronically. For 
  *
  * # offline saving to session file
  * When processing sesion files (@ref allow_session_file=true) offline, the option @ref allow_drop should be set to false. 
  * In this case measurements are added to the internal buffer until the size given by @ref hard_limit 
  * is reached.   
  * In this mode, the options @ref soft_limit and @ref max_buftime are ignroed.
  * 
  * # online saving to session file
  * When recording sesion files (@ref allow_session_file=true) live, the options @ref allow_drop should be set to true. 
  *
  * When a new measurement is added to the cube exporter, the following strategy is applied:
  * 
  * 1. The internal buffer has a total limit of size @ref hard_limit. If the buffer is full, 
  * it will be dropped (end).
  * 
  * 2. If the buffer is not full, the @ref soft_limit is checked. If it is reachd, the ordering of the frame numbers is ignored 
  * and the measurement with the lowest sequence nubmer is stored to the disk directly. (This can mess up the order of the frames
  * set @ref soft_limit = @ref hard_limit to disable this behaviour)
  * 
  * 3. All meausurements in the internal buffer are checked: If they are held in the buffer for longer then the time given by 
  * @ref max_buftime, they are saved to disk directly. (This can mess up the order of the frames
  * set @ref max_buftime to a higher value allow for longer hold time intervals.)
  */
struct cuvis_save_args_t
{
  /** allow to split file to multiple files. 
    *
    * When exporting to a cu3s file (@ref allow_session_file=true) the merge mode (previous allow_fragmentation flag) controlles 
    * if all measurements (of the same session name) are written as they are present in the input directory (set to 0) or 
    * if each measurement is saved to a separate cu3s file (set to 1). The latter option generates substantial 
    * overhead. If the merge mode is merging (set to 2)all measurements are written to one file even if they are present as multiple files on the disk.
    * Different references will still result in additional session files being written.
    * 
    * When exporting to a (legacy) cu3 file (@ref allow_session_file=false), the merge mode fragmentation (previous allow_fragmentation flag) will lead
    * to multiple files exported: a <name>.cu3 file, followed by <name>_<postfix>.tiff files. These come as a tuple
    * and must be kept together, else the file will be corrupted. This export option is intended for legacy programs
    * that were deisnged to read raw data with the previous software verison 2.x. 
    * 
    */
  CUVIS_SESSION_MERGE_MODE merge_mode;

  /** allow to overwrite an existing file.  
    *
    * This option anables to allow to ovewrite files on the disk, if they exist. 
    *
    * @note When exporting to legacy format of version 2.x (@ref allow_session_file=false and @ref allow_fragmentation=true),
    * only the existance of the *.cu3 file is checked, existing *.tiff files are neither cleaned up nor checked if they exist
    * prior overwriting.
    */
  CUVIS_INT allow_overwrite;

  /** allow to drop files, if output buffers are full
    *
    * This options controlls the export behaviour. If internal write buffers are full, 
    * new measurements are either dropped or kept. 
    * 
    * The policy to drop measurements on full buffer (allow_drop=true) is recommended for online opration. The 
    * idea is to rather drop measurements and thus allow the acquisition to continue without slowing down. 
    * When this policy is set, the @ref soft_limit and the @ref max_buftime options are also used (see there). 
    * 
    * If new measurements are forced to be kept (allow_drop=true), the exporter will wait until the measurement can be written.
    * This polocy is recommended for batch-processing measurements (offline). The options @ref soft_limit and @ref max_buftime 
    * are ignored.
    * 
    * @note This option only applies, if @ref allow_session_file=true.
    * */
  CUVIS_INT allow_drop;

  /** save files of same session number to a single cu3s file. If @ref allow_fragmentation is set, cu3s fill be split by measurement. Default in Wrappers: True */
  CUVIS_INT allow_session_file;

  /** save additional info file.
    * 
    * The info file is written to the same path as the export files. 
    * It is a plain text file and consits of the a header showing the recoridng FPS and mode and 
    * a body, where each frame number from 0 till the last frame written is shown by their name. 
    * Missing frames are noted as "dropped".
    * 
    * @note The output of this file is not flushed until the exporter writes to a different file or is closed. Thus, it is not 
    * suited to be used as a way to monitor frame drops during live acquisiton.
    *
    * This option is ignored, when @ref allow_session_file is set to false.
    */
  CUVIS_INT allow_info_file;

  /** give the current operation mode. 
    *
    * Save the operation mode used while recording.
    * Only used if @ref allow_session_file is set.
    * */
  CUVIS_OPERATION_MODE operation_mode;

  /** the fps used in operation_mode video
    *
    * only used if @ref allow_session_file=true and @ref operation_mode=Internal. 
    * */
  double fps;

  /** Out-of-order frames are sorted within the cache, as long as the cache useage is below this limit. 
    *
    * The soft limit is only used if @ref allow_drop=true and @ref allow_session_file=true.
    *
    * The internal chache may hold up to @ref soft_limit number of frames that are out of sequence.
    *
    * For example: Let the the seqence number of the measurement written last be #14, and let the internal 
    * cache hold the frames  #16,#17,...#24 (9 images in chache) and let the soft limit be 10
    * If we assume the next frame to be #25, the 10 images in cache reached the soft limit, forcing
    * the first frame with the lowest nubmer (#16) to be written (#15 is makred as 'dropped'). 
    * If the next image actually is #15, this image is then written out of sequence, resulting in the
    * order #14, #16, #15. 
    * 
    * Theese are the states of the example avove.
    * 
    * > write to disk: #14
    * 
    * > cache: #16,#17,...#24 [soft limit: 10]
    * 
    * > insert: #25
    * 
    * > write to disk: #16
    * 
    * > cache: #17,...#24, #25 [soft limit: 10]
    * 
    * > insert: #15
    * 
    * > write to disk: #15
    * 
    * > cache: #17,...#24, #25 [soft limit: 10]
    * 
    * This behaviour is a compromise between keeping the seuqence in order and at the same time
    * not storing too many images if a frame was acutally dropped. 
    * Increase the soft_limit to a value same or grater the @ref hard_limit to disable this behaviour.
    */
  CUVIS_INT soft_limit;

  /** Maximum number of elements in output cache 
    *
    * The hard limit is only used if @ref allow_session_file=true.
    * 
    * The output cache has a maximum size of @ref hard_limit. If more measurements
    * are added, adding another measurment is not possible. 
    * Adding a measurement will lock the calling function if @ref allow_drop is set to false.
    * If @ref allow_drop is set to true, the added frame is directrly dropped and not stored.
    *
    * @note This behaviour also applies when using the exproter within a worker.
    * 
    */
  CUVIS_INT hard_limit;

  /** Any frame is forced to be written after this time (in ms), latest. 
    *
    * The maximum buffer time option is only used if @ref allow_drop=true and 
    * @ref allow_session_file=true.
    * 
    * The time a buffer is held in the exporter's cache is tracked. If the time given
    * by the max_buftime is exceeded, a measuremnt is written to disk. 
    *
    * This option also helps to guarantee a measurements to be serialized to a permanent
    * storage and avoid data loss upon power or abnormal program termination.
    * 
    * This option will overwrite the @ref soft_limit for this frame, if needed. 
    * 
    * */
  CUVIS_INT max_buftime;

  /** Whether processing results are also saved in the export.
    *
    * If enabled, all cube data and accompanying meta-data are stored in the exported file as well.
    * This vastly increases file size and the time and processing resources needed for the export.
    * 
    * If disabled, only the raw image from the camera and raw data from any additional devices are stored.
    * This in turn requires the data to be reprocessed when loading it again.
    * */
  CUVIS_INT full_export;
};

/** @}*/

/** @brief processing arguments */
struct cuvis_proc_args_t
{
  /** the processing mode to be used.
      *
      * use @ref cuvis_proc_cont_is_capable to check,
      * if the mode is currently possible of a specific measurement
      */
  CUVIS_PROCESSING_MODE processing_mode;

  /** allow to use different calibration (expert option)
      *
      * This options allows to process raw data with a different calibration.
      * this is, however, limited to the same hardware.
      *
      * If the hardware was mechanically changed, results may be poor or not usable
      * at all. Unless the accuracy of the result can be verified, this option is
      * not recommended.
      * */
  CUVIS_INT allow_recalib;
};


/**
* @addtogroup cuvis_exporter Export API
* @{
*/


/** @brief general export settings */
struct cuvis_pansharpening_settings_t
{
  /** The export channel selection  
   *
   * Use "all" or "full" for all available channels
   *
   * Use ranges for wavelength range start-end or start:end or start:step:end ;
   * All values in Nanometers.
   * Examples: 450:10:550 or 450-550
   */
  CUVIS_CHAR channel_selection[CUVIS_MAXBUF];

  /** multiply spectrum by fixed factor before exporting 
  *
  * This is most usefull for bitshifting the data - especially when the pan image is also added to the export.
  */
  float spectra_multiplier;

  /** amount of pan-sharpening
      *
      * The value is relative to the pan image size, give a value between 0 and 1 */
  double pan_scale;

  /** for pansharpening use this interpolation type to scale up the cube before adjusting the weights 
  *
  * As a first step to pan-sharpening the spectral data needs to be re-sampled to the target resolution
  * This parameter determines the method for this resampling. 
  */
  CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE pan_interpolation_type;

  /** method for calculating the weights */
  CUVIS_PAN_SHAPRENING_ALGORITHM_TYPE pan_algorithm;

  /** pansharpen cube before calculating user plugin
  *
  * Normally pan sharpening is applied after calculating the user plugin. Prepansharpening can be used to get
  * a pansharpened cube when no real userplugin shall be applied. Prepansharpening is calculated on the whole
  * spectral cube which is heavy on performance.
  */
  CUVIS_INT pre_pan_sharpen_cube;

  /** add pan to exported image / cube.
  *
  * If applicable, the pan image is scaled to target pan-sharpening resolution. 
  */
  CUVIS_INT add_pan;
};


/** @brief general export settings */
struct cuvis_export_general_settings_t
{
  /** The export directory */
  CUVIS_CHAR export_dir[CUVIS_MAXBUF];

  /** add full-resolution pan to the export. 
  * The pan image is exported seperately
  */
  CUVIS_INT add_fullscale_pan;

  /** Set exporter to "permisive mode" 
  * 
  * If set, errors will be skipped and alternative values assumed, wherever possible. 
  *
  * E.g., if @ref add_pan is selected but there is no panchromatic image avaialbe, the export is not possible. 
  * In permissive mode, however, the add_pan option is de-activated and an exprot without pan image is conducted
  * instead.
  * 
  * @note This mode may lead to unexpected behaviour and should be used with caution.
  */
  CUVIS_INT permissive;

  /** Settings regarding pansharpening and channel selection
  */
  CUVIS_PANSHARPENING_SETTINGS pansharpening_settings;
};

/** @brief Additional settings for exporting to a userplugin view. See also \ref cuvis_export_general_settings_t */
struct cuvis_export_view_settings_t
{
  /** The userplugin xml string. See userplugin manual. */
  CUVIS_CHAR const* userplugin;

  /** When using View Exporter: export all output elements of the user plugin, even if they're not marked as "show" */
  CUVIS_INT complete;

  /** failback to pan image if cube is not available */
  CUVIS_INT pan_failback;
};

/** @brief Additional settings for exporting tiff. See also \ref cuvis_export_general_settings_t */
struct cuvis_export_tiff_settings_t
{
  /** the compression mode for tiff export */
  CUVIS_TIFF_COMPRESSION_MODE compression_mode;

  /** the tiff export mode / format */
  CUVIS_TIFF_FORMAT format;
};

/**@}*/

/** @brief viewer settings */
struct cuvis_viewer_settings_t
{
  /** The userplugin xml string. See userplugin manual. */
  CUVIS_CHAR const* userplugin;

  /** also include parts that were not marked as "show". */
  CUVIS_INT complete;

  /** failback to pan image if cube is not available */
  CUVIS_INT pan_failback;

  /** Settings regarding pansharpening and channel selection
  */
  CUVIS_PANSHARPENING_SETTINGS pansharpening_settings;
};

/** @brief The view meta structure */
struct cuvis_view_data_t
{
  /** The id of the view*/
  CUVIS_CHAR id[CUVIS_MAXBUF];

  /** the type of view data*/
  CUVIS_VIEW_CATEGORY category;

  /** the actual data. View data is always 8 bit, i.e. imbuffer bytes = 1 */
  CUVIS_IMBUFFER data;

  /** 1 if dataset is intended for showing, 0 else */
  CUVIS_INT show;
};

/** Information about components */
struct cuvis_component_info_t
{
  /** type of the component */
  CUVIS_COMPONENT_TYPE type;

  /** the name that can be displayed human-readable */
  CUVIS_CHAR displayname[CUVIS_MAXBUF];

  /** the sensor's meta-informaiton */
  CUVIS_CHAR sensorinfo[CUVIS_MAXBUF];

  /** additional sensor informaiton */
  CUVIS_CHAR userfield[CUVIS_MAXBUF];

  /** additional sensor informaiton */
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

/** settings for the worker */
struct cuvis_worker_settings_t
{
  /** @brief Size of the input queue for measurements and session files
  * 
  * The worker has an input queue that accepts measurements and entire session files.
  * To limit the memory usage, the queue is bounded by this value
  */
  CUVIS_SIZE input_queue_size;

  /** @brief Number of threads working on mandatory processing steps
  * 
  * Set the number of processing slots / threads / queue size for mandatory processing steps in the worker
  * Mandatory steps always include exporting the measurement, if an exporter is set in the worker.
  * If the measurement needs to be processed before it can be exported, the processing is also a mandatory step.
  */
  CUVIS_SIZE mandatory_queue_size;

  /** @brief Number of threads working on supplementary processing steps
  * 
  * Set the number of processing slots / threads / queue size for supplementary processing steps in the worker
  * Supplementary steps always include generating a view of the measurement, if a viewer is set in the worker.
  * If no exporter is set, all steps are supplementary.
  */
  CUVIS_SIZE supplementary_queue_size;

  /** @brief Size of the workers result queue
  * 
  * Should be at least as big as "mandatory_queue_size" and "supplementary_queue_size" together
  */
  CUVIS_SIZE output_queue_size;

  /** @brief Wether the worker is allowed to reject measurements from the acquisition context, if its queues are full
  * 
  * If set to true (1), the worker will skip processing measurements it pulls from the acqusition context, when its mandatory queue is full.
  * If set to false (0), the worker will wait until a processing slot in its mandatory queue is available, before pulling a new measurement from the acquisition context.
  * This setting DOES NOT apply to measurements and session files given to the worker via the "cuvis_worker_ingest_xyz" functions.
  */
  CUVIS_INT can_skip_measurements;

  /** @brief Wether the worker is allowed to skip supplementary processing steps, if its queues are full.
  * 
  * If set to true (1), the worker will skip supplementary processing steps, when its supplementary queue is full.
  * If set to false (0), the worker will wait until a processing slot in its supplementary queue is available, before starting processing on a new measurement.
  * This setting DOES applies to measurements and session files given to the worker via the "cuvis_worker_ingest_xyz" functions.
  */
  CUVIS_INT can_skip_supplementary_steps;

  /** @brief Wether the worker is allowed to drop processing results  if its output queue is full */
  CUVIS_INT can_drop_results;
};

/** @brief Collection of worker stats */
struct cuvis_worker_state_t
{
  /** @brief Measurements currently in the input queue */
  CUVIS_SIZE measurementsInQueue;

  /** @brief Session files currently in the input queue */
  CUVIS_SIZE sessionFilesInQueue;

  /** @brief Total number of frames currently in the input queue accounting for sesssion file size */
  CUVIS_SIZE framesInQueue;

  /** @brief Number of measurments the worker is currently processing */
  CUVIS_SIZE measurementsBeingProcessed;

  /** @brief Number of results currently in the result queue */
  CUVIS_SIZE resultsInQueue;

  /** @brief Wether the worker has an acquisition context set */
  CUVIS_INT hasAcquisitionContext;

  /** @brief Wether the worker is currently allowed to process measurements; same attribute as queried by cuvis_worker_is_processing. */
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

/**
* \addtogroup cuvis_log Logging
* @{
*/

typedef void(SDK_CCALL* log_callback)(const char* msg, CUVIS_INT level);
typedef void(SDK_CCALL* log_callback_localized)(const CUVIS_WCHAR* msg, CUVIS_INT level);

/** @}*/
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

/** event callback type */
typedef void(SDK_CCALL* external_event_callback)(CUVIS_INT i_handler_id, CUVIS_EVENT i_event);

/** Register an event handler.
  * The event handler will be called on all events which satisfy the supplied event handler type. Returns an id for the event handler
  * to allow unregistering of the specific event handler
  * only valid during the runtime of the callback.
  *
  * @param[in] i_callback the event handler function callback
  * @param[in] i_type the type of the event handler which is registered
  * @param[out] o_p_handler_id a pointer where the handler id will be written to
  * */

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_register_external_event_callback(external_event_callback i_callback, CUVIS_INT i_type, CUVIS_INT* o_p_handler_id);

/** Unregisters an event handler. Supply a valid handler id to specific the correct callback which is going to be unregistered */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_unregister_event_callback(CUVIS_INT i_handler_id);

#endif

/** \addtogroup cuvis_returns Return Values of SDK Functions

More Information on the Return Values of the SDK Functions.

Most of the SDK functions return a @ref cuvis_status_t. This value indicates if the function call was executed sucessfully or if a error occurred.
If the value is @ref status_error for example, this indicates that an error occurred.
The specific error message can then be retrieved via @ref cuvis_get_last_error_msg to get more details.

*/


/** \addtogroup cuvis_returns Return Values of SDK Functions
 *  @{
*/

/** Call this function for obtaining the last error message */
SDK_CAPI const CUVIS_CHAR* SDK_CCALL cuvis_get_last_error_msg(void);

/** Set the locale for localized error messages
*
* @param[in] i_locale_id set the locale id, e.g. "de" for german. See the "locale" directory for available translations.
*/
SDK_CAPI const CUVIS_STATUS SDK_CCALL cuvis_set_last_error_locale(CUVIS_CHAR const* i_locale_id);

/** Call this function for obtaining the last localized error message
*
* remember to set locale with @ref cuvis_set_last_error_locale first.
*/
SDK_CAPI const CUVIS_WCHAR* SDK_CCALL cuvis_get_last_error_msg_localized(void);

/** @} */

/** \addtogroup cuvis_log Logging

There are several ways to configure the logging behaviour in the Cuvis SDK.

# Logfile Configuration Behaviour

The SDK provides the possibility to write the log to a logfile. For this a "log.cfg" file has to be created at a certain position.

When a local ".cuvis" directory exists with an empty "log.cfg" file, the cuvis sdk will create a debug log in that directory.
The log file name is the process name followed by log, e.g. "example.exe.log", if the process is named "example.log"

If a local ".cuvis" directory is not found, the system-wide configuration of the logging is used (activated by default from the installation of cuvis):
The configuration can be found under %PROGRAMDATA%/cuvis/log.cfg (usually "C:/Program Data/cuvis/log.cfg") for Windows or /etc/cuvis/log.cfg for linux. The log output can be found under %PROGRAMDATA%/cuvis for Windows and /var/log/cuvis for linux.

# Loglevel at Runtime

Secondly there is the option to adapt the logging behaviour the the standard output stream via @ref cuvis_set_log_level.

# Registration of Log Callbacks

As a third option there is the possibility to register a function as a callback that will be called every time a new log message is recevied with the
requested log level. See @ref cuvis_register_log_callback and @ref cuvis_register_log_callback_localized for more information.

*/

/**
* \addtogroup cuvis_log Logging
* @{
*/


/** Set the internal log level. Log output will be redirected to cout
    *
    * If this function is not called, a failback logger is used, with loglevel "warning"
    * The failback logger is de-activated, when this function is called or when a callback is
    * registered for the log messages.
    * However, when this function is called, messages are logged to console, even when a callaback is
    * registered.
    * debug = 4, info = 3, warning = 2, error = 1, fatal = 0
    *
    * @param[in] level the log level to be set */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_set_log_level(CUVIS_INT level);

#ifndef MATLAB

/** Register an additional logger.
  * Only one classic callback will be set, multiple calls will overwrite the previous callback. The callback's message argument pointer is
  * only valid during the runtime of the callback.
  * The "classic" logger will output original messages, instead of it's respective translations. For localized (translated) messages, @see cuvis_reset_log_callback_localized.
  * @note The classical logger and localized logger can be used simultaneously.
  * @param[in] i_callback the function callback
  * @param[in] i_min_level the minimum level of the callback
  * */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_register_log_callback(log_callback i_callback, CUVIS_INT i_min_level);

/** Unregister the additional logger. This will not clear the localized logger */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_reset_log_callback();

/** Register an additional logger with localized language.
  * Only one callback will be set, multiple calls will overwrite the previous callback. The callback's message argument pointer is
  * only valid during the runtime of the callback.
  * @note The classical logger and localized logger can be used simultaneously.
  * @param[in] i_callback_localized the function callback
  * @param[in] i_min_level the minimum level of the callback
  * @param[in] i_locale_id set the locale id, e.g. "de-DE.UTF8" for german. See the "locale" directory for available translations.
  * */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_register_log_callback_localized(log_callback_localized i_callback_localized, CUVIS_INT i_min_level, CUVIS_CHAR const* i_locale_id);

/** Unregister the additional localized logger. This will not clear the classic logger */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_reset_log_callback_localized();

#endif

/** @} */

/**
* @addtogroup cuvis_general General
* 
* @brief General Configuration Options of the SDK
* 
* The @ref cuvis_init function set the reference to a settings directory. It should be the first call in a program that uses the cuvis SDK, and is only possible once.
* In the settings directory there can be multiple settings file present. Settings files are identified by a .settings extension. 
* Each Settings file is a xml file that contains a collection of property nodes.
* All the settings files get merged into one collection of property nodes. Therefore no property nodes is allowed to be present multiple times.
* 
* 
* @{
*/

/** The init function set the settings path.
    *
    * @param[in] i_settings_path The path to the settings directory. 
    * @param[in] i_global_loglevel The log level that will be used for the backend logging system
    * @param[in] i_logfile_name The name of the logfile that is going to be written
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_init(CUVIS_CHAR const* i_settings_path, CUVIS_INT i_global_loglevel, CUVIS_CHAR const* i_logfile_name);

/** Function for shutting down Cuvis safely. Gently stops all threads. */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_shutdown();


/** @brief Get the SDK version
    *
    * @param[out] o_pVersion The output version string. The provided array must have the length of @ref CUVIS_MAXBUF
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_version(CUVIS_CHAR* o_pVersion);


/** @brief Get the Userplugin processing engine version number
    *
    * @param[out] o_pVersion The output version string. The provided array must have the length of @ref CUVIS_MAXBUF
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_get_userplugin_engine_version(CUVIS_CHAR* o_pVersion);

/** @} */

/**
* @addtogroup cuvis_async Async Programming
* 
* @brief The Async Capabilites of the SDK
* 
* The functions of the sdk with depend on either setting a state of the camera, or awaiting image data from the camera have async variations of themself.
* This includes most of the setter of the acqusition context as well as @ref cuvis_acq_cont_capture.
*
* The non async version of these functions execute the respective task and block as long as it takes.
* The async counterpart function call completes immediately and returns the handle to an aync result or async @ref cuvis_mesu.
* 
* Theses async handles can then be used to check the state of the respective function call.
* 
* @{
*/

/** @brief get the result of a async call.
    *
    * Get the return code (and error message, if applicable) of an async function, that has been called.
    * If result is not @ref status_ok use the @ref cuvis_get_last_error_msg function to get details.
    *
    * If the timeout is used (value above 0ms), @ref status_timeout or @ref status_deferred will be returned, if the function is not yet finished.
    * In that case, the asyncResult handle is still valid and can be used again.
    * If the result is @ref status_ok the function has finished. For both @ref status_ok and @ref status_error, the handle is now invalid.
    *
    * If the result is @ref status_overwritten the function's call was overwritten by another (similar) call. The actual value set by this
    * async function was not used, but the one of the other call. On this result, the handle is now invalid.
    *
    * @param[in,out] io_pAsyncResult the async handle obtained by calling a async function. If the call finished, the handle will be invalidated
    * @param[in] timeout_ms the timeout in ms. Give 0 to wait for ever.
    * @returns @ref status_ok if the async function finished successfully. @ref status_timeout or @ref status_deferred will be returned,
    * if the function is not yet finished. If the call failed, because it was overwritten it this function will return
    * @ref status_overwritten. If it failed for other reasons, the this function returns @ref status_error.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_get(CUVIS_ASYNC_CALL_RESULT* io_pAsyncResult, CUVIS_INT timeout_ms);

/** @brief Free an async measurement result without calling it */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_free(CUVIS_ASYNC_CAPTURE_RESULT* io_pAsyncResult);

/** @brief Free an async call result without calling it */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_free(CUVIS_ASYNC_CALL_RESULT* io_pAsyncResult);

/** @brief checks the status of the async call object and returns it */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_call_status(CUVIS_ASYNC_CALL_RESULT i_pAsyncResult, CUVIS_STATUS* io_pStatusResult);

/** @brief checks the status of the async capture object and returns it */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_status(CUVIS_ASYNC_CAPTURE_RESULT i_pAsyncResult, CUVIS_STATUS* io_pStatusResult);

/**@}*/

/**
* @addtogroup cuvis_acq Acquisition Context
*
* @brief Capturing Images with the SDK.
* 
* An handle for an acquisition context can be obtained by either loading it with a calibration handle (@ref cuvis_calib) or
* by loading it with a @ref cuvis_session handle.
* 
* The acquisition context handles the communication with the camera, including setting state variables and capturing images.
* 
*
* @{
*/

/** @brief Capture a measurement
    *
    * This function is only available in operation mode "Software". The function executes a software trigger synchronously.
    *
    *
    * @param[in] i_acqCont the acquisition context
    * @param[out] o_pMesu the handle of the recorded image will be written to this variable
    * @param[in] timeout_ms the timeout in ms. Give 0 to wait for ever.
    * @returns status_ok if the measurement was recorded. @ref status_timeout or @ref status_deferred is returned, if the capture was not completed (yet)
    * */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_capture(CUVIS_ACQ_CONT i_acqCont, CUVIS_MESU* o_pMesu, CUVIS_INT timeout_ms);

/** @brief Capture a measurement async
    *
    * This function is only available in operation mode "Software". The function executes a software trigger asynchronously.
    * The recorded measurement can be obtained by the function @ref cuvis_async_capture_get.
    *
    * If o_pAsyncResult is set to NULL, the measurement is added to the Acqusition Context's internal queue.
    * Retrieve it with @ref cuvis_acq_cont_get_next_measurement or via the worker (if used) @ref cuvis_worker_get_next_result
    *
    * @param[in] i_acqCont the acquisition context
    * @param[out] o_pAsyncResult the async capture handle will be written to this variable or NULL
    * @returns status_ok if the async call could be executed.
    * */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_capture_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CAPTURE_RESULT* o_pAsyncResult);

/**@}*/

/** @brief get the result of a async capture.
    *
    * Get the return code (and error message, if applicable) of an async capture, that has been called.
    * If result is not @ref status_ok use the @ref cuvis_get_last_error_msg function to get details.
    *
    * If the timeout is used (value above 0ms), @ref status_timeout or @ref status_deferred will be returned, if the function is not yet finished.
    * In that case, the asyncResult handle is still valid and can be used again.
    * If the result is @ref status_ok the function has finished. For both @ref status_ok and @ref status_error, the handle is now invalid.
    *
    * @param[in,out] io_pAsyncResult the async handle obtained by calling @ref cuvis_acq_cont_capture_async. If the call finished, the handle will be invalidated
    * @param[in] timeout_ms the timeout in ms. Give 0 to wait for ever.
    * @param[out] o_pMesu write the measurement handle to this variable, if the call was successful. Else write CUVIS_HANDLE_NULL
    * @returns @ref status_ok if the async function finished successfully. @ref status_timeout or @ref status_deferred will be returned,
    * if the function is not yet finished. If it failed for other reasons, the this function returns @ref status_error.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_async_capture_get(CUVIS_ASYNC_CAPTURE_RESULT* io_pAsyncResult, CUVIS_INT timeout_ms, CUVIS_MESU* o_pMesu);

/**
* @addtogroup cuvis_mesu Measurement
*
* How to interact with the Measurements taken by the SDK.
*
* @{
*/

/** @brief Creates an additional measurement handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_mesu The handle of the measurement to copy
    * @param[out] o_pMesu The new handle of the measurement.
    * @returns @ref status_ok if the measurement handle could be doubled
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_copy_handle(CUVIS_MESU i_mesu, CUVIS_MESU* o_pMesu);


/** @brief Load a measurement from disk.
    *
    * The measurement is a cu3 file - and if fragmented some additional tiff files with a postfix, e.g. _cube.tiff
    * To load the file, all fragmented parts must be in the same directory. Fragmented files must not be renamed.
    *
    * @param[in] i_path the file path of the measurement
    * @param[out] o_pMesu the handle of the measurement.
    * @returns @ref status_ok, if the measurement could be loaded.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_load(const CUVIS_CHAR* i_path, CUVIS_MESU* o_pMesu);

/** create a deep copy of a measurement
  *
  * All operations on a measurement are performed on the same object. If different processing needs to be perfomed on a measurement
  * It should be deep-copied. The copied meausrement's name will be changed to end with "_copy"
  *
  * @param[in] i_mesu The measurement copy source.
  * @param[out] o_pMesu The copy will be linked to the handle given.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_deep_copy(CUVIS_MESU i_mesu, CUVIS_MESU* o_pMesu);

/** @brief Clears the cube from a measurement
*
* Clears the proceessing result, i. e. the cube, from the measurement. This returns the measurement the state before
* applying the processing. This can be usefull for reduced data usage.
*
* @param[in] i_mesu The measurement
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_clear_cube(CUVIS_PROC_CONT i_mesu);

/** @brief Clears an implicit reference measurement
*
* Implict measurements are created, when a measurement is processed with a processing context, where 
* explicit references are set. Then, these references are remebemred by the measurement. When changing
* the processing context, the references are implicitly available, still. Clearing them may be interesing
* if the references set are wrong/invalid or if disk space is a concearn.
*
* @param[in] i_mesu The measurement
* @param[in] i_type The type of the reference to be cleard
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_clear_implicit_reference(CUVIS_PROC_CONT i_mesu, CUVIS_REFERENCE_TYPE i_type);

/**@}*/


/**
* @addtogroup cuvis_session Session File
*
* The main file format of the SDK
*
* @{
*/

/** @brief Creates an additional session file handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_sess The handle of the session file to copy
    * @param[out] o_pSess The new handle of the session file.
    * @returns @ref status_ok if the session file handle could be doubled
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_copy_handle(CUVIS_SESSION_FILE i_sess, CUVIS_SESSION_FILE* o_pSess);


/** @brief Load a session_info file from disk.
   *
   * The session_info file is a cu3s file and consists of binary cu3 measurement data. Call @ref cuvis_session_file_get_mesu
   * to obtain a single measurement frame. SessionFile files can be create with the Cube Exporter
   * (see @ref cuvis_exporter_create_cube)
   * @note Do not read a file currently opened for writing.
   *
   * @param[in] i_path the file path of the session_info file
   * @param[out] o_pSess the handle of the session_info file.
   * @returns @ref status_ok, if the measurement could be loaded.
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_load(const CUVIS_CHAR* i_path, CUVIS_SESSION_FILE* o_pSess);

/** @brief Release a session_info file handle
    *
    * Release a measurement by it's handle. The handle will be overwritten to @ref CUVIS_HANDLE_NULL
    * This will not affect any measurements on disk.
    * Measurements loaded from the session_info file remain valid.
    *
    * @param[in,out] o_pSess The handle to the measurement to be deleted
    * @returns @ref status_ok if the session_info file was released.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_free(CUVIS_SESSION_FILE* o_pSess);

/** @brief Load a measurement from the session_info file
  *
  * @param[in] i_sess the session_info file handle
  * @param[in] i_frameNo the frame no. Counting from 0, must be below value of @ref cuvis_session_file_get_size of it's respective @p i_type
  * @param[in] i_type the type of listing (size depends on type)
  * @param[out] o_pMesu the handle of the measurement.
  * @returns @ref status_ok, if the measurement could be loaded.
  *          @ref status_no_measurement if the measurement was dropped.
  *          @ref status_error if the frame exeeds the number of frames.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_session_file_get_mesu(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_frameNo, CUVIS_SESSION_ITEM_TYPE i_type, CUVIS_MESU* o_pMesu);

/** @brief Load a reference measurement from the session_info file
  *
  * @param[in] i_sess the session_info file handle
  * @param[in] i_frameNo the reference number. Counting from 0. If @p i_type is not set, refers to the index of all references and must be below the value of @ref cuvis_session_file_get_size using type session_item_type_references. If @p i_type is set, must be 0.
  * @param[in] i_type the type of reference measurement requested
  * @param[out] o_pMesu the handle of the measurement.
  * @returns @ref status_ok, if the reference could be loaded.
  *          @ref status_no_measurement if the reference does not exist.
  *          @ref status_error if the i_frameNo exeeds the number of references.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_session_file_get_reference_mesu(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_frameNo, CUVIS_REFERENCE_TYPE i_type, CUVIS_MESU* o_pMesu);

/** @brief Get number of total frames of session_info file
  *
  * @param[in] i_sess the session_info file handle
  * @param[in] i_type the type of listing (size depends on type)
  * @param[out] o_pSize the size is written here.
  * @returns @ref status_ok if no error occurred.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_size(CUVIS_SESSION_FILE i_sess, CUVIS_SESSION_ITEM_TYPE i_type, CUVIS_INT* o_pSize);

/** @brief Get the thumbnail image of a session file
    *
    * Return the thumbnail of a session file. The image data is valid as long as
    * the session file handle is not released.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_sess The session file handle
    * @param[out] o_pThumbnail The image buffer to be filled
    * @returns @ref status_ok if the buffer could be filled with the image element.
    *          @ref status_not_available if the requested data was empty, or the key could not be found
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_thumbnail(CUVIS_SESSION_FILE i_sess, CUVIS_IMBUFFER* o_pThumbnail);

/** @brief get a session_info file's FPS
   *
   * The session_info file meta-Information will be available only if the mode @ref cuvis_session_file_get_operation_mode returns "Internal"
   *
   * @param[in] i_sess the session_info file handle
   * @param[out] o_pFps the frames per second the session_info was recorded with.
   * @returns status_ok if fps could be retrieved, status_not_available if the session_info file has not FPS property set.
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_fps(CUVIS_SESSION_FILE i_sess, double* o_pFps);

/** @brief get a session_info file's hash
   *
   * @param[in] i_sess the session_info file handle
   * @param[out] o_pHash the hash of the sessionfile.
   * @returns status_ok if hash could be retrieved, status_not_available if the sessionfile has no hash property set.
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_hash(CUVIS_SESSION_FILE i_sess, CUVIS_CHAR* o_pHash);

/** @brief returns the operation mode the session_info file was recorded in
    *
    * The operation mode gives indication how the session_info file was recorded.
    *
    * @param[in] i_sess the session_info file handle
    * @param[out] o_pMode the operation mode of the session_info file.
    * @returns status_ok if no error occurred.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_session_file_get_operation_mode(CUVIS_SESSION_FILE i_sess, CUVIS_OPERATION_MODE* o_pMode);

/**@}*/

/**
* @addtogroup cuvis_acq Acquisition Context
* @{
*/


/** @brief Get measurement from internal cache
   *
   * This function is only available in operation mode "Internal" or "External". The function obtains the image from the internal
   * memory, if available.
   *
   *
   * @param[in] i_acqCont the acquisition context
   * @param[out] o_pMesu the handle of the recorded image will be written to this variable.
   * @param[in] timeout_ms the timeout in ms. Give 0 to wait for ever.
   * @returns status_ok if the measurement was recorded. Returns status_no_measurement if no measurement was made available during the timeout time. If any error occurred status_error is returned.
   * */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_next_measurement(CUVIS_ACQ_CONT i_acqCont, CUVIS_MESU* o_pMesu, CUVIS_INT timeout_ms);

/** @brief check if any measurements are available in the buffer
    *
    * This function is only available in operation mode "Internal" or "External".
    *
    * @param[in] i_acqCont the acquisition context
    * @param[in] o_pHasNext value of 0 is written, if no measurements are available. value > 0, if a measurement is available.
    * @returns status_ok if no error occurred. If any error occurred status_error is returned.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_has_next_measurement(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pHasNext);

/** @} */

/**
* @addtogroup cuvis_mesu Measurement
* @{
*/

/** @brief Save a measurement to disk
    *
    * Saves a single measurement to the disk in cu3 format.
    * The file name is given by the measurement's name (see \ref cuvis_measurement_set_name)
    *
    * @param[in] i_path The file directory
    * @param[in] i_mesu The handle of the measurement to be saved
    * @param[in] args The saving options
    * @returns @ref status_ok, if the measurement was save successfully.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_save(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_path, CUVIS_SAVE_ARGS args);

/** @brief Set the name of the measurement in memory
    *
    * By default, a newly aquired measurement has the name <SESSIONNAME>_<session_no>_<sequence_no> (see \ref CUVIS_SESSION_INFO).
    * This will also be the name of the file while saving it. This can be changed by this function.
    *
    * @param[in] i_mesu The measurements to be changed
    * @param[in] i_name The new measurement's name
    * @returns @ref status_ok, if the measurement's name was set successfully.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_set_name(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_name);

/** @brief Set the comment of the measurement in memory
    *
    * @param[in] i_mesu The measurements to be changed
    * @param[in] i_comment The new measurement's comment
    * @returns @ref status_ok, if the measurement's name was set successfully.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_set_comment(CUVIS_MESU const i_mesu, const CUVIS_CHAR* i_comment);

/** @brief Release a measurement handle
    *
    * Release a measurement by it's handle. The handle will be overwritten to @ref CUVIS_HANDLE_NULL
    * This will not affect any measurements on disk.
    *
    * @param[in,out] io_pMesu The handle to the measurement to be deleted
    * @returns @ref status_ok if the measurement was released.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_free(CUVIS_MESU* io_pMesu);

/** @brief Obtain metadata from measurement
    *
    * The meta-data from the measurement contains information about
    * the measurement when it was recorded: when and how. Meta-Data
    * do not contain the actual recorded data.
    *
    * @param[in] i_mesu The measurement's handle
    * @param[out] o_pMetaData The meta structure to be filled
    * @returns @ref status_ok, if the meta-data could be loaded without errors
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_metadata(CUVIS_MESU i_mesu, CUVIS_MESU_METADATA* o_pMetaData);

/** @brief Get image data from measurement
    *
    * Return image data from a measurement. The image data is valid as long as
    * the measurement handle is not released and the measurement is not
    * re-processed.
    *
    * This function can only be called, if he data type is @ref data_type_image.
    * This can be checked by the function @ref cuvis_measurement_get_data_info.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[in] i_key The data frame identification key (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[out] o_pBuf The image buffer to be filled
    * @returns @ref status_ok if the buffer could be filled with the image element.
    *          @ref status_not_available if the requested data was empty, or the key could not be found
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_image(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_IMBUFFER* o_pBuf);

/** @brief Get string data from measurement
    *
    * Return string data from a measurement.
    *
    * This function can only be called, if he data type is @ref data_type_string.
    * This can be checked by the function @ref cuvis_measurement_get_data_info.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[in] i_key the data frame identification key (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[in] i_outBufferlength the maximal possible length of the string that is going to be copied (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[out] o_pValue The string buffer to be filled. The provided array must have the length of @p i_length
    * @returns @ref status_ok if the buffer could be filled with the string.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_measurement_get_data_string(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SIZE i_outBufferlength, CUVIS_CHAR* o_pValue);

/** @brief Get the length of string data from measurement
    *
    * Return the length of a string data from a measurement.
    *
    * This function can only be called, if he data type is @ref data_type_string.
    * This can be checked by the function @ref cuvis_measurement_get_data_info.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[in] i_key the data frame identification key (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[out] o_pLength The length of the string data
    * @returns @ref status_ok if the length could be returned
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_string_length(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SIZE* o_pLength);


/** @brief Get image info data from measurement
    *
    * Return image data from a measurement. Tis
    *
    * This function can only be called, if he data type is @ref data_type_string.
    * This can be checked by the function @ref cuvis_measurement_get_data_info.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[in] i_key the data frame identification key (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[out] o_pValue The string buffer to be filled. The provided array must have the length of @ref CUVIS_MAXBUF
    * @returns @ref status_ok if the buffer could be filled with the string.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_sensor_info(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_SENSOR_INFO* o_pValue);

/** @brief Get GPS data from measurement
    *
    * Return gps data from a measurement.
    *
    * This function can only be called, if he data type is @ref data_type_gps.
    * This can be checked by the function @ref cuvis_measurement_get_data_info.
    *
    * see also: @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[in] i_key the data frame identification key (see @ref cuvis_measurement_get_data_info or @ref cuvis_reserved_keys)
    * @param[out] o_pGps The gps buffer to be filled.
    * @returns @ref status_ok if the buffer could be filled with the gps data set.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_gps(CUVIS_MESU i_mesu, const CUVIS_CHAR* i_key, CUVIS_GPS* o_pGps);

/** @brief get meta-information of a data element
    *
    * Retrieve the meta-informations of a data element identified by it's positional number.
    * A measurement has N data elements (obtain N with the functions @ref cuvis_measurement_get_data_count)
    * Thus, the meta-data of element 0 to N-1 can be obtained.
    * The @p o_pType defined the data type: If it is @ref data_type_image, retrieve it
    * with @ref cuvis_measurement_get_data_image.
    *
    * If it is data type is @ref data_type_gps, retrieve it with @ref cuvis_measurement_get_data_gps.
    * If it is @ref data_type_string, retrieve with @ref cuvis_measurement_get_data_string
    * If it is @ref data_type_unsupported, the data cannot be retrieved.
    *
    * To retrieve the data, you will require the @p o_pKey wich you can obtain by using this function.
    * The key is the name of the data channel.
    *
    * Some keys are reserved, see @ref cuvis_reserved_keys
    *
    * @param[in] i_mesu The measurement handle
    * @param[out] o_pKey Output the data key
    * @param[out] o_pType The data type
    * @param[in] i_id The number of the data element
    * @returns @ref status_ok if the data information could be obtained
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_info(CUVIS_MESU i_mesu, CUVIS_CHAR* o_pKey, CUVIS_DATA_TYPE* o_pType, CUVIS_INT i_id);

/** @brief Retrieve the number of data elements
    *
    * @param[in] i_mesu The measurement handle
    * @param[out] o_pCount The number of data elements
    * @returns @ref status_ok if the data element count could be retrieved
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_data_count(CUVIS_MESU i_mesu, CUVIS_INT* o_pCount);

/**@}*/

/**
* @addtogroup cuvis_calib Calibration
*
* Functions to interact with a calibration object of the SDK.
* 
* There are two ways to create a calibration object. One way is by loading it specifically from a factory directory (see @ref cuvis_calib_create_from_path).
* The other one is by loading it from a session file.
* The Calibration object is needed to load other parts of the SDK like the @ref cuvis_acq and the @ref cuvis_proc.
*
* @{
*/

/** @brief Creates an additional calibration handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_calibration The handle of the calibration to copy
    * @param[out] o_pCalibration The new handle of the calibration.
    * @returns @ref status_ok if the calibration handle could be doubled
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_copy_handle(CUVIS_CALIB i_calibration, CUVIS_CALIB* o_pCalibration);


/** @brief Create a calibration from factory path
    *
    * The calibration is created from a factory path, containing the license and calibration
    * file "init.daq" as well as further calibration files (e.g. SpRad.cu3).
    *
    * The calibration is lazy-loading, i.e. the AcquisitionContext and the
    * ProcessingContext will only be initialized, when explicitly called.
    *
    * @note do not load multiple calibration instances of the same camera
    *
    * @param[in] i_factoryDir The path to the factory directory
    * @param[in] o_pCalibration the handle of the calibration
    * @returns @ref status_ok if the calibration could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_create_from_path(const CUVIS_CHAR* i_factoryDir, CUVIS_CALIB* o_pCalibration);

/** @brief Create a calibration from session file
    *
    * Create a calibration from an existion session file.
    *
    * The calibration is lazy-loading, i.e. the AcquisitionContext and the
    * ProcessingContext will only be initialized, when explicitly called.
    * 
    * When you create a processing context from the calibration cerated with
    * this function, you won't have the references from the session file set.
    * Use @ref cuvis_proc_cont_create_from_session_file to load a processing context
    * where the referenecs are taken from the session file.
    *
    * @note do not load multiple calibration instances of the same camera
    *
    * @param[in] i_sess The session file
    * @param[in] o_pCalibration the handle of the calibration
    * @returns @ref status_ok if the calibration could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_create_from_session_file(const CUVIS_SESSION_FILE i_sess, CUVIS_CALIB* o_pCalibration);


/** @brief Clear a loaded calibration by it's handle
    *
    * The internal memory is freed.
    *
    * @param[in,out] io_pCalibration The handle of the calibration. The handle
    * number will be invalidated.
    * @returns @ref status_ok if the calibration could be released
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_free(CUVIS_CALIB* io_pCalibration);

/** @} */


/**
* @addtogroup cuvis_acq Acquisition Context
* @{
*/

/** @brief Creates an additional acquisition context handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_acqCont The handle of the acquisition context to copy
    * @param[out] o_pAcqCont The new handle of the acquisition context.
    * @returns @ref status_ok if the acquisition context handle could be doubled
    */

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_copy_handle(CUVIS_ACQ_CONT i_acqCont, CUVIS_ACQ_CONT* o_pAcqCont);


/** @brief Load a acquisition context from a given calibration
    *
    * Load the acquisition context from the calibration. This will load the hardware and initialize it.
    * Do not load multiple instances of the came calibration / camera.
    *
    * @param[in] i_calib The calibration instance the processing context will be loaded from
    * @param[out] o_pAcqCont The handle of the acquisition context.
    * @returns @ref status_ok if the acquisition context could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_create_from_calib(CUVIS_CALIB i_calib, CUVIS_ACQ_CONT* o_pAcqCont);

/** @brief Load a acquisition context from a given session_file
    *
    * The acquisition context from the embedded acquisition context of the session_info file.
    *
    * @param[in] i_sess The session_file the processing context will be loaded from
    * @param[in] i_simulate If True, uses the provided session file for simulated data capturing
    * @param[out] o_pAcqCont The handle of the acquisition context.
    * @returns @ref status_ok if the acquisition context could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_create_from_session_file(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_simulate, CUVIS_ACQ_CONT* o_pAcqCont);

/** @brief get the online state of the hardware
  *
  * Hardware can be used, when at least it's required components are online.
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_pState the state will be written here
  * @returns status_ok, if no internal error occurred.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_state(CUVIS_ACQ_CONT i_acqCont, CUVIS_HARDWARE_STATE* o_pState);

/** @brief get initialization state of the acquisition context
  *
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_pIsReady whether the acquisition context has completed all initialization tasks
  * @returns status_ok, if no internal error occurred.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_ready_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pIsReady);

/** @brief get the acquisition session_info
  *
  * Get the acquisition session_info settings. Also use this function to get the current sequence number.
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_pSessionInfo the state will be written here
  * @returns status_ok, if no internal error occurred.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_session_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_SESSION_INFO* o_pSessionInfo);

/** @brief set the acquisition session_info
  *
  * Set the acquisition session_info settings.
  * @param[in] i_acqCont the acquisition context
  * @param[out] i_pSessionInfo the session_info details to be set
  * @returns status_ok, if no internal error occurred.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_set_session_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_SESSION_INFO const* i_pSessionInfo);

/** @brief set the receive queue buffer size
  *
  * Set the amounts of measurements that will be stored internally, ready for retrieval. Default=100.
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_size the new queue size
  * @returns status_ok if the new queue size could be set.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_queue_size_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_size);

/** @brief Query whether the dead pixel correction is available
  *
  * Returns whether dead pixel correction information is available in the camera's calibration file.
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_is_available the result of the query is written here
  * @returns cuvis_ok if the query succeeded
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_available_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_is_available);

/** @brief Query whether the dead pixel correction is enabled
  *
  * Returns whether the Cuvis built-in dead pixel correction algorithm is currently enabled
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_is_enabled the result of the query is written here
  * @returns cuvis_ok if the query succeeded
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_is_enabled);

/** @brief Enable or disable the dead pixel correction algorithm
  *
  * Control whether the Cuvis built-in dead pixel correction algorithm is enabled or disabled.
  * The algorithm applies a custom dead-pixel correction to the sensor image(s).
  * Which pixels to correct and how is determined through the calibration process.
  * @param[in] i_acqCont the acquisition context
  * @param[in] o_set_enabled use 1 to enable, 0 to disable the correction algorithm
  * @returns cuvis_ok if the operation succeeded. Returns status_not_available if the calibration doesn't contain correction information.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT o_set_enabled);


/** @brief Clear a loaded acquisition context by it's handle
    *
    * The internal memory is freed.
    *
    * @param[in,out] io_pAcqCont The handle of the processing context. The handle
    * number will be invalidated.
    * @returns @ref status_ok if the acquisition context could be released
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_free(CUVIS_ACQ_CONT* io_pAcqCont);

/** @brief Get components general info
  *
  * Return general component information about a component build into the acquisition hardware. This helps
  * identifying the correct component for settings specific component settings (e.g. gain)
  *
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[out] o_pCompInfo the component info to be filled
  * @returns cuvis_ok if the info fields could be filled.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_component_info(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_COMPONENT_INFO* o_pCompInfo);

/** @brief Get the number of components
  *
  * The acquisition hardware is build from one or more components. Get the component count.
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_pCount the number of components is written here
  * @returns cuvis_ok if the number of components could be set
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_acq_cont_get_component_count(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT* o_pCount);

/** @brief Set components pixelformat
  *
  * Set components pixelformat
  *
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[in] i_pPixelFormat the components pixelformat
  * @returns cuvis_ok if the pixelformat was set.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_pixel_format_set(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_CHAR const* i_pPixelFormat);

/** @brief Set components pixelformat
  *
  * Set components pixelformat (asynchronous)
  *
  * @param[in] i_acqCont the acquisition context
  * @param[out] o_pAsyncResult The Async object that will contain the result of the operation
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[in] i_pPixelFormat the components pixelformat
  * @returns cuvis_ok if the pixelformat was set.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_comp_pixel_format_set_async(CUVIS_ACQ_CONT i_acqCont, CUVIS_ASYNC_CALL_RESULT* o_pAsyncResult, CUVIS_INT i_id, CUVIS_CHAR const* i_pPixelFormat);

/** @brief Get components actual pixelformat
  *
  * Return actual components pixelformat
  *
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[out] o_pPixelFormat the components pixelformat
  * @returns cuvis_ok if the pixelformat was returned.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_pixel_format_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_CHAR* o_pPixelFormat);

/** @brief Get components actual pixelformat
  *
  * Return the amount of components available pixelformats
  *
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[out] o_pCount amount of available pixel formats
  * @returns cuvis_ok if the amount was returned.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_available_pixel_format_count_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_INT* o_pCount);

/** @brief Get components actual pixelformat
  *
  * Return indexed components available pixelformat
  *
  * @param[in] i_acqCont the acquisition context
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[in] i_index index of the requested available pixelformat
  * @param[out] o_pPixelFormat the components available pixelformat
  * @returns cuvis_ok if the pixelformat was returned.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_comp_available_pixel_format_get(CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, CUVIS_INT i_index, CUVIS_CHAR* o_pPixelFormat);

/**@}*/

/**
\addtogroup cuvis_proc Processing Context

Processing Images with the SDK.

 @{
*/


/** @brief Creates an additional processing context handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_procCont The handle of the processing context to copy
    * @param[out] o_pProcCont The new handle of the processing context.
    * @returns @ref status_ok if the processing context handle could be doubled
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_copy_handle(CUVIS_PROC_CONT i_procCont, CUVIS_PROC_CONT* o_pProcCont);


/** @brief Load a processing context from a given calibration
    *
    *Load the processing context from the calibration.
    *
    *@param[in] i_calib The calibration instance the processing context will be loaded from
    *@param[out] o_pProcCont The handle of the processing context.
    *@returns @ref status_ok if the processing context could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_calib(CUVIS_CALIB i_calib, CUVIS_PROC_CONT* o_pProcCont);

/** @brief Load a processing context from a given measurement
    *
    * The processing context is loaded from the CALIBRATION directory, relative to
    * the measurement given ( ../Calibration/* ) . This directory is present in the normal camera operation
    * / recording, but the reference might get lost, if you manually move the
    * measurements. In that case, this function will fail.
    *
    * @param[in] i_mesu The measurement with a valid reference to the processing context
    * @param[out] o_pProcCont The handle of the processing context.
    * @returns @ref status_ok if the processing context could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_mesu(CUVIS_MESU i_mesu, CUVIS_INT i_loadReferences, CUVIS_PROC_CONT* o_pProcCont);

/** @brief Load a processing context from a given session_file
    *
    * The processing context from the embedded processing context of the session_info file.
    *
    * @param[in] i_sess The session_file with a valid reference to the processing context
    * @param[out] o_pProcCont The handle of the processing context.
    * @returns @ref status_ok if the processing context could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_create_from_session_file(CUVIS_SESSION_FILE i_sess, CUVIS_INT i_loadReferences, CUVIS_PROC_CONT* o_pProcCont);

/** @brief get a specific reference from the processing context
    *
    * The processing context can hold explicit references (e.g. a dark),
    * see @ref cuvis_proc_cont_set_reference. These reference can be obtained
    * by this functions
    *
    * @note Implicit references given by a measurement are not returned. If they are available can only be
    * checked indirectly by the @ref cuvis_proc_cont_is_capable or by checking for the measurement's data keys
    * @ref CUVIS_MESU_DARKREF_KEY, @ref CUVIS_MESU_WHITEREF_KEY and @ref CUVIS_MESU_WHITEDARKREF_KEY
    *
    * @param[in] i_procCont The handle of the processing context
    * @param[out] o_pMesu The reference measurement's handle
    * @param[in] i_type The type of the measurement to be retrieved.
    * @returns @ref status_ok if the reference measurement is available and could be loaded
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_get_reference(CUVIS_PROC_CONT i_procCont, CUVIS_MESU* o_pMesu, CUVIS_REFERENCE_TYPE i_type);

/** @brief Set a reference measurement
    *
    * The available processing modes (@ref cuvis_processing_mode_t) require certain references to be set.
    * When a measurement is recorded with references in place, these references are available per measurement implicitly.
    * However, if you want to process measurements with different references, or if the measurement lacks a reference,
    * they can be set with this function. 
    * 
    * @code
    * CUVIS_MESU mesu;
    * cuvis_measurement_load("mesu.cu3",&mesu);
    * //contains implicit Reference_Dark
    *
    * CUVIS_PROC_CONT pc;
    * cuvis_proc_cont_create_from_mesu(mesu,&pc); //will implicitly load Reference_Dark
    *
    * CUVIS_MESU white;
    * cuvis_measurement_load("white.cu3",&white);
    *
    * cuvis_proc_cont_set_reference(pc, white, Reference_White);
    *
    * //Cube_Reflectance requires Reference_Dark and Reference_White
    * cuvis_proc_cont_apply(pc,mesu,{Cube_Reflectance});
    * @endcode
    * @note The reference explicitly set by this function has priority over the implicit measurement.
    *
    * @param[in] i_procCont The handle of the processing context
    * @param[in] i_mesu The measurement to be used as explicit reference
    * @param[in] i_type The type of the reference
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_set_reference(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu, CUVIS_REFERENCE_TYPE i_type);

/** @brief Clears a reference measurement
*
* Clears a reference explicitly set by @ref cuvis_proc_cont_set_reference
*
* @param[in] i_procCont The handle of the processing context
* @param[in] i_type The type of the reference
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_clear_reference(CUVIS_PROC_CONT i_procCont, CUVIS_REFERENCE_TYPE i_type);

/** @brief Set the operating distance by value
    *
    * Some cameras require a distance reference (calibration). This is usually obtained from a measurement at
    * that distance. However, if the distance is known, it can be set manually.
    *
    * @note Some OEM-Cameras or older models do not support this.
    * @note Internally, a measurement is created. It can be obtained by @ref cuvis_proc_cont_get_reference.
    *
    * @param[in] i_procCont The handle of the processing context
    * @param[in] i_distanceMM The distance in millimeters.
    * @returns @ref status_ok if the distance could be set
    * */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_calc_distance(CUVIS_PROC_CONT i_procCont, double i_distanceMM);


/** @brief Check if an explicit reference was set
    *
    * @param[in] i_procCont The handle of the processing context
    * @param[in] i_type The reference type
    * @param[out] o_pHasReference true, if reference is explicitly set. false, otherwise
    * @return @ref status_ok if no error occurred.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_has_reference(CUVIS_PROC_CONT i_procCont, CUVIS_REFERENCE_TYPE i_type, CUVIS_INT* o_pHasReference);

/** @brief Check if a processing mode is possible for a measurement
    *
    * Depending on the measurement, it's intrinsic references, the processing
    * context's explicit references and the internal camera calibration itself
    * the availability of a mode varies.
    *
    * Use this function, to check whether a specific mode is explicitly possible for
    * a measurement.
    *
    * @param[in] i_procCont The handle of the processing context
    * @param[in] i_mesu The measurement to be checked
    * @param[in] i_args The processing options to be checked
    * @param[out] o_pIsCapable true, if mode is possible. false, otherwise
    * @return @ref status_ok if no error occurred.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_is_capable(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu, CUVIS_PROC_ARGS i_args, CUVIS_INT* o_pIsCapable);

/** @brief (Re-)Process a measurement
   *
   * Process a measurement according to the current settings of the processing context.
   * Those get set via @ref cuvis_proc_cont_set_args
   * The availability of the modes depends, use @ref cuvis_proc_cont_is_capable to check
   * if the processing is possible.
   *
   * In short:
   * @ref Cube_Raw does not require references (@ref Reference_Distance is optional)
   *
   * @ref Cube_DarkSubtract requires @ref Reference_Dark (and @ref Reference_Distance is optional)
   *
   * @ref Cube_Reflectance requires @ref Reference_Dark and @ref Reference_White reference (and @ref Reference_Distance
   * is optional), the @ref Reference_WhiteDark is strongly recommended if using different integration times.
   *
   * @ref Cube_SpectralRadiance depends on the camera model: All cameras require @ref Reference_SpRad. The Fireflye requires: @ref Reference_Dark, @ref Reference_White, the Ultris series requires only @ref Reference_Dark.
   *
   * @param[in] i_procCont The handle of the processing context
   * @param[in] i_mesu The measurement to be processed
   * @return @ref status_ok if measurement was processed.
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_apply(CUVIS_PROC_CONT i_procCont, CUVIS_MESU i_mesu);

/** @brief Sets the processing arguments for a processing contex
   *
   * For processing a measurement see @ref cuvis_proc_cont_apply
   *
   * @param[in] i_procCont The handle of the processing context
   * @param[in] i_args The processing arguments that will be set
   * @return @ref status_ok if measurement was processed.
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_set_args(CUVIS_PROC_CONT i_procCont, CUVIS_PROC_ARGS i_args);

/** @brief Clear a loaded processing context by it's handle
    *
    * The internal memory is freed.
    * @param[in,out] io_pProcCont The handle of the processing context. The handle
    * number will be invalidated.
    * @return @ref status_ok if processing context could be freed.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_free(CUVIS_PROC_CONT* io_pProcCont);

/**@}*/

/** @addtogroup cuvis_exporter Export API
* 
* How to export Measurement captured with the SDK.
* 
* A handle for each of the exporter can be obtainend by calling either @ref cuvis_exporter_create_cube, @ref cuvis_exporter_create_envi, @ref cuvis_exporter_create_tiff or @ref cuvis_exporter_create_view.
* Each of the so created exporter can then export a @ref cuvis_mesu to the respective format by calling @ref cuvis_exporter_apply.
* Each exporter takes options in form of @ref cuvis_export_general_settings_t and one of the following format specific structs @ref cuvis_save_args_t, @ref cuvis_export_view_settings_t, @ref 	cuvis_export_tiff_settings_t
* 
* See the respective struct documentations for more information on the individual options
* @{
*/

/** @brief Create a cube exporter
   *
   * @param[out] o_pExporter The handle of the exporter
   * @param[in] generalSettings General export settings
   * @param[in] formatSettings Additional Cube export settings
   * @returns @ref status_ok if the exporter was created successfully
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_cube(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_CUBE_SETTINGS formatSettings);

/** @brief Create a tiff exporter
   *
   * @param[out] o_pExporter The handle of the exporter
   * @param[in] generalSettings General export settings
   * @param[in] formatSettings Additional TIF export settings
   * @returns @ref status_ok if the exporter was created successfully
   */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_tiff(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_TIFF_SETTINGS formatSettings);

/** @brief Create a ENVI exporter
  *
  * @param[out] o_pExporter The handle of the exporter
  * @param[in] generalSettings General export settings
  * @returns @ref status_ok if the exporter was created successfully
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_create_envi(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings);

/** @brief Create a VIEW exporter
    *
    * Not to be confused with the VIEWER. The view exporter saves views to disk.
    *
    * @param[out] o_pExporter The handle of the exporter
    * @param[in] generalSettings General export settings
    * @param[in] formatSettings Additional view export settings
    * @returns @ref status_ok if the exporter was created successfully
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL
    cuvis_exporter_create_view(CUVIS_EXPORTER* o_pExporter, CUVIS_EXPORT_GENERAL_SETTINGS generalSettings, CUVIS_EXPORT_VIEW_SETTINGS formatSettings);

/** @brief Export a measurement with an exporter
    *
    * @param[in] i_exporter The exporter
    * @param[in] i_mesu the measurement
    * @returns @ref status_ok if the measurement was exported successfully. @ref status_not_stored if the measurement could not be stored.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_apply(CUVIS_EXPORTER i_exporter, CUVIS_MESU i_mesu);

/** @brief Flush an exporter
    *
    * @param[in] i_exporter The exporter to flush
    * @returns @ref status_ok if the exporter was flushed successfully.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_flush(CUVIS_EXPORTER i_exporter);

SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_get_queue_used(CUVIS_EXPORTER i_exporter, CUVIS_INT* o_pQueueUsed);

/** @brief Release an exporter
    *
    * @param[in,out] io_pExporter Exporter to be released. If successfully, handle will be invalidated
    * @returns @ref status_ok if the exporter was cleared.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_exporter_free(CUVIS_EXPORTER* io_pExporter);

/**@}*/

/** \addtogroup cuvis_viewer Viewer 
*
* Something about the viewer
* 
* @{
*/

/** @brief Creates an additional viewer handle 
    *
    * Creates an additional handle that points to the same instance as the supplied handle
    * 
    * @param[in] i_viewer The handle of the viewer to copy
    * @param[out] o_pViewer The new handle of the viewer.
    * @returns @ref status_ok if the viewer handle could be doubled
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_copy_handle(CUVIS_VIEWER i_viewer, CUVIS_VIEWER* o_pViewer);


/** @brief Create a viewer
    *
    * Not to be confused with the view exporter. The viewer returns the view in the memory
    *
    * @param[out] o_pViewer The handle of the viewer
    * @param[in] viewerSettings view settings
    * @returns @ref status_ok if the exporter was created successfully
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_create(CUVIS_VIEWER* o_pViewer, CUVIS_VIEWER_SETTINGS viewerSettings);

/** @brief Generate a view from a measurement
    *
    * The view is processed from a measurement by the viewer. The resulting view handle can be accessed by the
    * @ref cuvis_view_get_data_count to get number of elements,  @ref cuvis_view_get_data to get a single date element
    * and @ref cuvis_view_free to release the view (this must always be called)
    *
    * @param[in] i_viewer The viewer
    * @param[in] i_mesu the measurement
    * @param[out] o_pView the resulting view handle.
    * @returns @ref status_ok if the measurement was processed successfully.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_apply(CUVIS_VIEWER i_viewer, CUVIS_MESU i_mesu, CUVIS_VIEW* o_pView);

/** @brief Release a viewer
    *
    * @param[in,out] io_pViewer Viewer to be released. If successfully, handle will be invalidated
    * @returns @ref status_ok if the exporter was cleared.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_viewer_free(CUVIS_VIEWER* io_pViewer);


/** @brief retrieves the number of view data elements
  * @param[in] i_view the view handle
  * @param[out] o_pCount The number of elements
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_get_data_count(CUVIS_VIEW i_view, CUVIS_INT* o_pCount);

/** @brief Obtain data from view
    *
    * The data contains the actual view
    *
    * @param[in] i_view The view handle
    * @param[in] i_index The element number
    * @param[out] o_pData The actual view data
    * @returns @ref status_ok, if the meta-data could be loaded without errors
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_get_data(CUVIS_VIEW i_view, CUVIS_INT i_index, CUVIS_VIEW_DATA* o_pData);

/** @brief Release a view
    *
    * @param[in,out] io_pView View to be released. If successfully, handle will be invalidated
    * @returns @ref status_ok if the exporter was cleared.
    */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_view_free(CUVIS_VIEWER* io_pView); //VIEWER or VIEW???

/**@}*/

/*  MISC. */

/** @brief Get the capabilites of a given mode
*
* Use this function to evaluate which functions are available for a camera calibration.
* @param[in] i_calibration The calibration
* @param[in] i_mode The mode to check the capabiliets
* @param[out] o_pCapabilities write the capabilites here. See CUVIS_MODE_CAPABILITIES_x flags.
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_capabilities(CUVIS_CALIB i_calibration, CUVIS_OPERATION_MODE i_mode, CUVIS_INT* o_pCapabilities);

/** @brief Get the capabilites of the measurement which were present in the calibration during capture.
*    This doesn't indicate which capabilities are currently available for the measurement.
*    See @ref cuvis_proc_cont_is_capable
*
* Use this function to evaluate which functions are available for a given measurement.
* @param[in] i_mesu The measurement
* @param[out] o_pCapabilities write the capabilites here. See CUVIS_MODE_CAPABILITIES_x flags.
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_capabilities(CUVIS_MESU i_mesu, CUVIS_INT* o_pCapabilities);

/** @brief Get the unique calibration id of a measurement
* 
* The id unique to a calibration is stored into everything created from it, as such a measurement also contains this id.
* 
* @param[in] i_mesu the measurement
* @param[out] o_pCalibId the output string
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_measurement_get_calib_id(CUVIS_MESU i_mesu, CUVIS_CHAR* o_pCalibId);

/**
\addtogroup cuvis_calib Calibration
 @{
*/

/** @brief Get the unique id of a calibration 
* 
* @param[in] i_calib the calibration
* @param[out] o_pCalibId the unique id output string
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_id(CUVIS_CALIB i_calib, CUVIS_CHAR* o_pCalibId);

/** @brief Get info of a calibration 
* 
* @param[in] i_calib the calibration
* @param[out] o_pCalibInfo the info data struct
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_info(CUVIS_CALIB i_calib, CUVIS_CALIBRATION_INFO* o_pCalibInfo);

/** @brief Get components general info
  *
  * Return general component information about a component build into the acquisition hardware the calibration is made for.
  * This helps identifying the correct component for settings specific component settings (e.g. gain)
  *
  * @param[in] i_calib the calibration
  * @param[in] i_id the device id (value between 0 and below @ref cuvis_acq_cont_get_component_count)
  * @param[out] o_pCompInfo the component info to be filled
  * @returns cuvis_ok if the info fields could be filled.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_component_info(CUVIS_CALIB i_calib, CUVIS_INT i_id, CUVIS_COMPONENT_INFO* o_pCompInfo);

/** @brief Get the number of components
  *
  * The acquisition hardware is build from one or more components. Get the component count.
  * @param[in] i_calib the calibration
  * @param[out] o_pCount the number of components is written here
  * @returns cuvis_ok if the number of components could be set
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_calib_get_component_count(CUVIS_CALIB i_calib, CUVIS_INT* o_pCount);

/** @} */

/** @brief Get the unique calibration id of a processing context
* 
* The id unique to a calibration is stored into everything created from it, as such a processing context also contains this id.
* 
* @param[in] i_procCont the processing context
* @param[out] o_pCalibId the output string
*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_proc_cont_get_calib_id(CUVIS_PROC_CONT i_procCont, CUVIS_CHAR* o_pCalibId);


/**
\addtogroup cuvis_worker Worker
 @{
*/

/** @brief Create a Worker
  *
  * The encapsulates the functions of the Acquisiton Context, Processing Context, Exporter, and Viewer into a single
  * container and manages the communications between these.
  * It also enables multi-threaded operation
  * @note The set functions need to be called in order for the worker to be enabled.
  *
  * @param[out] o_pWorker The worker handle to be created
  * @param[in] worker_settings The worker configuration
  **/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_create(CUVIS_WORKER* o_pWorker, CUVIS_WORKER_SETTINGS worker_settings);

/** @brief release a worker */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_free(CUVIS_WORKER* io_pWorker);

/** @brief set the acquistion context for the worker. Give CUVIS_HANDLE_NULL to clear*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_acq_cont(CUVIS_WORKER i_worker, CUVIS_ACQ_CONT i_acq_cont);
/** @brief set the processing context for the worker. Give CUVIS_HANDLE_NULL to clear*/
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_proc_cont(CUVIS_WORKER i_worker, CUVIS_PROC_CONT i_proc_cont);
/** @brief set the exporter for the worker. Give CUVIS_HANDLE_NULL to clear */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_exporter(CUVIS_WORKER i_worker, CUVIS_EXPORTER i_exporter);
/** @brief set the viewer for the worker. Give CUVIS_HANDLE_NULL to clear */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_set_viewer(CUVIS_WORKER i_worker, CUVIS_VIEWER i_viewer);

/** @brief Get the current percentage of frames done of the current session. -1.0 if no session file is currently being processed. */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_query_session_progress(CUVIS_WORKER i_worker, double* o_frames_read);

/** @brief set a session file for the worker to process (read access only). Give CUVIS_HANDLE_NULL to clear.
  * Set parameter SkipDroppedFrames to 1 to skip any dropped frames contained in the session - 0 will insert empty frames.
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_ingest_session_file(CUVIS_WORKER i_worker, CUVIS_SESSION_FILE i_session_file, const char* i_frame_selection);
/** @brief Push a mesurement into the worker to process. Worker must have neither a session file nor an acquisition context. */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_ingest_mesu(CUVIS_WORKER i_worker, CUVIS_MESU i_mesu);

/** @brief Get the next result in order 
  *
  * The measurement will be readyly recorded, processed (if set), stored (if set) and have a view (if set).
  * 
  * @param[in] i_worker The worker handle
  * @param[out] o_pMesu The recorded measurement or NULL if recording failed
  * @param[out] o_pView The view, if calculated sucessfully, else NULL
  * @param[in] i_Timeout_ms The number of milliseconds to wait for a result. -1 to wait indefinitely
  * @returns @ref status_ok or on error: @ref status_error, @ref status_not_processed, @ref status_not_stored, or @ref status_no_view, or @ref status_not_available
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_next_result(CUVIS_WORKER i_worker, CUVIS_MESU* o_pMesu, CUVIS_VIEW* o_pView, CUVIS_SIZE i_Timeout_ms);

/** @brief Check, if a new worker result is available 
  * @param[in] i_worker The worker handle
  * @param[out] o_pHasNext 1 if a result is available now, else 0
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_has_next_result(CUVIS_WORKER i_worker, CUVIS_INT* o_pHasNext);

/** @brief Query the maximum queue size of the input queue
  * @param[in] i_worker The worker handle
  * @param[out] o_pInputQueueLimit The maximum size of the input queue
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_input_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pInputQueueLimit);

/** @brief Query the maximum queue size of the mandatory queue
  * @param[in] i_worker The worker handle
  * @param[out] o_pMandatoryLimit The maximum size of the mandatory queue. This is also the maximum number of measurements processed simultaneously
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_mandatory_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pMandatoryLimit);

/** @brief Query the maximum queue size of the supplementary queue
  * @param[in] i_worker The worker handle
  * @param[out] o_pSupplementaryLimit The maximum size of the supplementary queue. This is also the maximum number of measurements processed simultaneously
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_supplementary_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pSupplementaryLimit);

/** @brief Query the maximum queue size of the output queue
  * @param[in] i_worker The worker handle
  * @param[out] o_pOutputQueueLimit The maximum size of the output queue
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_output_queue_limit(CUVIS_WORKER i_worker, CUVIS_SIZE* o_pOutputQueueLimit);

/** @brief Query the number of items currently in the result queue.
  * @param[in] i_worker The worker handle
  * @param[out] o_pQueueUsed The number of results currently in the output queue
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_queue_used(CUVIS_WORKER i_worker, CUVIS_INT* o_pQueueUsed);

/** @brief Query current drop behavior
  * @param[in] i_worker The worker handle
  * @param[out] o_pCanDrop If 1, the worker is allowed to drop results when the output queue is full
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_drop_results(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanDrop);

/** @brief Query current skip behavior
  * @param[in] i_worker The worker handle
  * @param[out] o_pCanSkip If 1, the worker is allowed to entirely skip processing measurements, if the mandatory queue is full
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_skip_measurements(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanSkip);

/** @brief Query current skip behavior
  * @param[in] i_worker The worker handle
  * @param[out] o_pCanSkip If 1, the worker is allowed to skip supplementary processing of measurements, if the supplementary queue is full
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_can_skip_supplementary(CUVIS_WORKER i_worker, CUVIS_INT* o_pCanSkip);

/** @brief Query wether the processing step is currently mandatory
  * The result is only valid, if a processing context is assigned to the worker.
  * If no processing context is assigned, will always return 0 (false)
  * @param[in] i_worker The worker handle
  * @param[out] o_pProcessingMandatory If 1, the appying the processing context to the measurement is part of the mandatory processing steps
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_is_processing_mandatory(CUVIS_WORKER i_worker, CUVIS_INT* o_pProcessingMandatory);

/** @brief Start the worker */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_start(CUVIS_WORKER i_worker);

/** @brief Pause the worker */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_stop(CUVIS_WORKER i_worker);

/** @brief Command the worker to discard all measurements it is currently processing and empty the result queue. */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_drop_all_queued(CUVIS_WORKER i_worker);

/** @brief Query wether the worker is currently allowed to process measurements - wether it is running.
  * @param[in] i_worker The worker handle
  * @param[out] o_pIsProcessing If 1, the worker is allowed process measurements. This does not mean, that it is currently working on a measurement - see cuvis_worker_get_threads_busy
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_is_processing(CUVIS_WORKER i_worker, CUVIS_INT* o_pIsProcessing);

/** @brief Query how many measurements the worker is processing right now
  * @param[in] i_worker The worker handle
  * @param[out] o_pThreadsBusy The number of measurements currently being processed
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_threads_busy(CUVIS_WORKER i_worker, CUVIS_INT* o_pThreadsBusy);

/** @brief Query multiple attributes of the worker at once, see cuvis_worker_state_t
  * @param[in] i_worker The worker handle
  * @param[out] o_pWorkerState Collection of worker stats
  */
SDK_CAPI CUVIS_STATUS SDK_CCALL cuvis_worker_get_state(CUVIS_WORKER i_worker, CUVIS_WORKER_STATE* o_pWorkerState);

/**@}*/

/** @private */
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


/**
* @addtogroup cuvis_acq Acquisition Context
* @{
*/

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

/**@}*/

/**
* @addtogroup cuvis_comp Components
* @{
*/

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

/**@}*/

/** simple check function for error code */
#define CUVIS_CHECK(code)                                    \
  if (status_ok != (code))                                   \
  {                                                          \
    printf("Call failed. %s\n", cuvis_get_last_error_msg()); \
    return -1;                                               \
  }
;

/** helper macro for obtaining a pixel position from an imbuffer pointer */
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
