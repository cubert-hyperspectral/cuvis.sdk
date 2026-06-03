

# File cuvis.h



[**FileList**](files.md) **>** [**\_api\_sources**](dir_461ad87a78e7eefd7882d4ef5ca214ae.md) **>** [**cuvis.h**](cuvis_8h.md)

[Go to the source code of this file](cuvis_8h_source.md)

[More...](#detailed-description)

* `#include <stddef.h>`
* `#include <stdint.h>`















## Classes

| Type | Name |
| ---: | :--- |
| struct | [**cuvis\_calibration\_info\_t**](structcuvis__calibration__info__t.md) <br> |
| struct | [**cuvis\_component\_info\_t**](structcuvis__component__info__t.md) <br> |
| struct | [**cuvis\_event\_acquisition\_data\_t**](structcuvis__event__acquisition__data__t.md) <br> |
| struct | [**cuvis\_event\_base\_data\_t**](structcuvis__event__base__data__t.md) <br> |
| struct | [**cuvis\_event\_component\_data\_t**](structcuvis__event__component__data__t.md) <br> |
| struct | [**cuvis\_event\_processing\_event\_t**](structcuvis__event__processing__event__t.md) <br> |
| struct | [**cuvis\_event\_quality\_event\_t**](structcuvis__event__quality__event__t.md) <br> |
| struct | [**cuvis\_export\_general\_settings\_t**](structcuvis__export__general__settings__t.md) <br>_general export settings_  |
| struct | [**cuvis\_export\_tiff\_settings\_t**](structcuvis__export__tiff__settings__t.md) <br>_Additional settings for exporting tiff. See also_ [_**cuvis\_export\_general\_settings\_t**_](structcuvis__export__general__settings__t.md) _._ |
| struct | [**cuvis\_export\_view\_settings\_t**](structcuvis__export__view__settings__t.md) <br>_Additional settings for exporting to a userplugin view. See also_ [_**cuvis\_export\_general\_settings\_t**_](structcuvis__export__general__settings__t.md) _._ |
| struct | [**cuvis\_gps\_t**](structcuvis__gps__t.md) <br>_The gps data structure._  |
| struct | [**cuvis\_imbuffer\_t**](structcuvis__imbuffer__t.md) <br>_image buffer data structure with meta-data_  |
| struct | [**cuvis\_mesu\_metadata\_t**](structcuvis__mesu__metadata__t.md) <br>_The measurement meta structure._  |
| struct | [**cuvis\_pansharpening\_settings\_t**](structcuvis__pansharpening__settings__t.md) <br>_general export settings_  |
| struct | [**cuvis\_proc\_args\_t**](structcuvis__proc__args__t.md) <br>_processing arguments_  |
| struct | [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md) <br>_options for saving as cu3/cu3s files_  |
| struct | [**cuvis\_sensor\_info\_t**](structcuvis__sensor__info__t.md) <br> |
| struct | [**cuvis\_session\_info\_t**](structcuvis__session__info__t.md) <br> |
| struct | [**cuvis\_view\_data\_t**](structcuvis__view__data__t.md) <br>_The view meta structure._  |
| struct | [**cuvis\_viewer\_settings\_t**](structcuvis__viewer__settings__t.md) <br>_viewer settings_  |
| struct | [**cuvis\_worker\_settings\_t**](structcuvis__worker__settings__t.md) <br> |
| struct | [**cuvis\_worker\_state\_t**](structcuvis__worker__state__t.md) <br>_Collection of worker stats._  |


## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**cuvis\_capabilities\_t**](#enum-cuvis_capabilities_t)  <br> |
| enum  | [**cuvis\_component\_type\_t**](#enum-cuvis_component_type_t)  <br> |
| enum  | [**cuvis\_data\_type\_t**](#enum-cuvis_data_type_t)  <br>_the data field's type_  |
| enum  | [**cuvis\_hardware\_state\_t**](#enum-cuvis_hardware_state_t)  <br> |
| enum  | [**cuvis\_imbuffer\_format\_t**](#enum-cuvis_imbuffer_format_t)  <br>_supported image buffer formats_  |
| enum  | [**cuvis\_pan\_sharpening\_algorithm\_t**](#enum-cuvis_pan_sharpening_algorithm_t)  <br>_the pan-sharpening algorithm for calculating the pan image's weights_  |
| enum  | [**cuvis\_pan\_sharpening\_interpolation\_type\_t**](#enum-cuvis_pan_sharpening_interpolation_type_t)  <br>_the pan sharpening interpolation type for scaling up the cube before applying the pan image's weights_  |
| enum  | [**cuvis\_processing\_mode\_t**](#enum-cuvis_processing_mode_t)  <br>_The processing mode (a.k.a. capture mode) of a measurement._  |
| enum  | [**cuvis\_reference\_type\_t**](#enum-cuvis_reference_type_t)  <br>_The type of a reference._  |
| enum  | [**cuvis\_session\_item\_type\_t**](#enum-cuvis_session_item_type_t)  <br> |
| enum  | [**cuvis\_session\_merge\_mode\_t**](#enum-cuvis_session_merge_mode_t)  <br>_merge mode for the cube exporter_  |
| enum  | [**cuvis\_tiff\_compression\_mode\_t**](#enum-cuvis_tiff_compression_mode_t)  <br>_the tiff compression options_  |
| enum  | [**cuvis\_tiff\_format\_t**](#enum-cuvis_tiff_format_t)  <br>_the tiff export format._  |
| enum  | [**cuvis\_view\_category\_t**](#enum-cuvis_view_category_t)  <br> |
| typedef void([**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) \* | [**external\_event\_callback**](#typedef-external_event_callback)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_IMBUFFER**](cuvis_8h.md#define-cuvis_imbuffer), imbuffer) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_GPS**](cuvis_8h.md#define-cuvis_gps), gps) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_SENSOR\_INFO**](cuvis_8h.md#define-cuvis_sensor_info), sensor\_info) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_SESSION\_INFO**](cuvis_8h.md#define-cuvis_session_info), session\_info) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_MESU\_METADATA**](cuvis_8h.md#define-cuvis_mesu_metadata), mesu\_metadata) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_SAVE\_ARGS**](cuvis_8h.md#define-cuvis_save_args), save\_args) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_PROC\_ARGS**](cuvis_8h.md#define-cuvis_proc_args), proc\_args) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings), export\_general\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_EXPORT\_CUBE\_SETTINGS**](cuvis_8h.md#define-cuvis_export_cube_settings), export\_cube\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_EXPORT\_VIEW\_SETTINGS**](cuvis_8h.md#define-cuvis_export_view_settings), export\_view\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_EXPORT\_TIFF\_SETTINGS**](cuvis_8h.md#define-cuvis_export_tiff_settings), export\_tiff\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_VIEWER\_SETTINGS**](cuvis_8h.md#define-cuvis_viewer_settings), viewer\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_VIEW\_DATA**](cuvis_8h.md#define-cuvis_view_data), view\_data) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_COMPONENT\_INFO**](cuvis_8h.md#define-cuvis_component_info), component\_info) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_WORKER\_SETTINGS**](cuvis_8h.md#define-cuvis_worker_settings), worker\_settings) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_WORKER\_STATE**](cuvis_8h.md#define-cuvis_worker_state), worker\_state) <br> |
|   | [**ALLOCATE\_AND\_FREE**](#function-allocate_and_free) ([**CUVIS\_CALIBRATION\_INFO**](cuvis_8h.md#define-cuvis_calibration_info), calibration\_info) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_capture\_get**](#function-cuvis_async_capture_get) ([**CUVIS\_ASYNC\_CAPTURE\_RESULT**](cuvis_8h.md#define-cuvis_async_capture_result) \* io\_pAsyncResult, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) timeout\_ms, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br>_get the result of a async capture._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_get\_capabilities**](#function-cuvis_calib_get_capabilities) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calibration, [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode) i\_mode, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCapabilities) <br>_Get the capabilites of a given mode._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_event\_get\_acquisition\_data**](#function-cuvis_event_get_acquisition_data) ([**CUVIS\_EVENT**](cuvis_8h.md#define-cuvis_event) i\_event, [**CUVIS\_EVENT\_ACQUISITION\_DATA**](cuvis_8h.md#define-cuvis_event_acquisition_data) \* o\_p\_acquisition\_data) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_calib\_id**](#function-cuvis_measurement_get_calib_id) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pCalibId) <br>_Get the unique calibration id of a measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_capabilities**](#function-cuvis_measurement_get_capabilities) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCapabilities) <br>_Get the capabilites of the measurement which were present in the calibration during capture. This doesn't indicate which capabilities are currently available for the measurement. See_ [_**cuvis\_proc\_cont\_is\_capable**_](group__cuvis__proc.md#function-cuvis_proc_cont_is_capable) _._ |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_get\_calib\_id**](#function-cuvis_proc_cont_get_calib_id) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pCalibId) <br>_Get the unique calibration id of a processing context._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_register\_external\_event\_callback**](#function-cuvis_register_external_event_callback) ([**external\_event\_callback**](cuvis_8h.md#typedef-external_event_callback) i\_callback, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_type, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_p\_handler\_id) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_unregister\_event\_callback**](#function-cuvis_unregister_event_callback) ([**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_handler\_id) <br> |



























## Macros

| Type | Name |
| ---: | :--- |
| define  | [**ACQ\_GET\_SINGLE\_VALUE**](cuvis_8h.md#define-acq_get_single_value) (NAME, TYPE, COMMENT) `/* multi line expression */`<br> |
| define  | [**ACQ\_SET\_SINGLE\_VALUE**](cuvis_8h.md#define-acq_set_single_value) (NAME, TYPE, UNIT\_STR) `/* multi line expression */`<br> |
| define  | [**ALLOCATE\_AND\_FREE**](cuvis_8h.md#define-allocate_and_free) (DATATYPE, NAME) `/* multi line expression */`<br> |
| define  | [**COMP\_GET\_SINGLE\_VALUE**](cuvis_8h.md#define-comp_get_single_value) (NAME, TYPE, COMMENT) `/* multi line expression */`<br> |
| define  | [**COMP\_SET\_SINGLE\_VALUE**](cuvis_8h.md#define-comp_set_single_value) (NAME, TYPE, UNIT\_STR) `/* multi line expression */`<br> |
| define  | [**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_ASYNC\_CALL\_RESULT**](cuvis_8h.md#define-cuvis_async_call_result)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br>_handle to an async function call result._  |
| define  | [**CUVIS\_ASYNC\_CAPTURE\_RESULT**](cuvis_8h.md#define-cuvis_async_capture_result)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br>_handle to an async capture result._  |
| define  | [**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_CALIBRATION\_INFO**](cuvis_8h.md#define-cuvis_calibration_info)  `struct [**cuvis\_calibration\_info\_t**](structcuvis__calibration__info__t.md)`<br> |
| define  | [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char)  `char`<br> |
| define  | [**CUVIS\_CHECK**](cuvis_8h.md#define-cuvis_check) (code) `/* multi line expression */`<br> |
| define  | [**CUVIS\_COMPONENT\_INFO**](cuvis_8h.md#define-cuvis_component_info)  `struct [**cuvis\_component\_info\_t**](structcuvis__component__info__t.md)`<br> |
| define  | [**CUVIS\_COMPONENT\_TYPE**](cuvis_8h.md#define-cuvis_component_type)  `enum [**cuvis\_component\_type\_t**](cuvis_8h.md#enum-cuvis_component_type_t)`<br> |
| define  | [**CUVIS\_DATA\_TYPE**](cuvis_8h.md#define-cuvis_data_type)  `enum [**cuvis\_data\_type\_t**](cuvis_8h.md#enum-cuvis_data_type_t)`<br> |
| define  | [**CUVIS\_EVENT**](cuvis_8h.md#define-cuvis_event)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_EVENT\_ACQUISITION\_DATA**](cuvis_8h.md#define-cuvis_event_acquisition_data)  `struct [**cuvis\_event\_acquisition\_data\_t**](structcuvis__event__acquisition__data__t.md)`<br> |
| define  | [**CUVIS\_EVENT\_ACQUISTION**](cuvis_8h.md#define-cuvis_event_acquistion)  `(1 &lt;&lt; 8)`<br> |
| define  | [**CUVIS\_EVENT\_BASE\_DATA**](cuvis_8h.md#define-cuvis_event_base_data)  `struct [**cuvis\_event\_base\_data\_t**](structcuvis__event__base__data__t.md)`<br> |
| define  | [**CUVIS\_EVENT\_COMPONENT**](cuvis_8h.md#define-cuvis_event_component)  `([**CUVIS\_EVENT\_ACQUISTION**](cuvis_8h.md#define-cuvis_event_acquistion) \| (1 &lt;&lt; 4))`<br> |
| define  | [**CUVIS\_EVENT\_COMPONENT\_DATA**](cuvis_8h.md#define-cuvis_event_component_data)  `struct [**cuvis\_event\_component\_data\_t**](structcuvis__event__component__data__t.md)`<br> |
| define  | [**CUVIS\_EVENT\_PROCESSING**](cuvis_8h.md#define-cuvis_event_processing)  `(2 &lt;&lt; 8)`<br> |
| define  | [**CUVIS\_EVENT\_PROCESSING\_DATA**](cuvis_8h.md#define-cuvis_event_processing_data)  `struct [**cuvis\_event\_processing\_event\_t**](structcuvis__event__processing__event__t.md)`<br> |
| define  | [**CUVIS\_EVENT\_QUALITY\_DATA**](cuvis_8h.md#define-cuvis_event_quality_data)  `struct [**cuvis\_event\_quality\_event\_t**](structcuvis__event__quality__event__t.md)`<br> |
| define  | [**CUVIS\_EVENT\_TRIGGER\_SKIPPED**](cuvis_8h.md#define-cuvis_event_trigger_skipped)  `([**CUVIS\_EVENT\_COMPONENT**](cuvis_8h.md#define-cuvis_event_component) \| 1)`<br> |
| define  | [**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_EXPORT\_CUBE\_SETTINGS**](cuvis_8h.md#define-cuvis_export_cube_settings)  `struct [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md)`<br> |
| define  | [**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings)  `struct [**cuvis\_export\_general\_settings\_t**](structcuvis__export__general__settings__t.md)`<br> |
| define  | [**CUVIS\_EXPORT\_TIFF\_SETTINGS**](cuvis_8h.md#define-cuvis_export_tiff_settings)  `struct [**cuvis\_export\_tiff\_settings\_t**](structcuvis__export__tiff__settings__t.md)`<br> |
| define  | [**CUVIS\_EXPORT\_VIEW\_SETTINGS**](cuvis_8h.md#define-cuvis_export_view_settings)  `struct [**cuvis\_export\_view\_settings\_t**](structcuvis__export__view__settings__t.md)`<br> |
| define  | [**CUVIS\_FLAGS**](cuvis_8h.md#define-cuvis_flags)  `uint32\_t`<br> |
| define  | [**CUVIS\_GPS**](cuvis_8h.md#define-cuvis_gps)  `struct [**cuvis\_gps\_t**](structcuvis__gps__t.md)`<br> |
| define  | [**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)  `[**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int)`<br> |
| define  | [**CUVIS\_HANDLE\_NULL**](cuvis_8h.md#define-cuvis_handle_null)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)(0)`<br> |
| define  | [**CUVIS\_HARDWARE\_STATE**](cuvis_8h.md#define-cuvis_hardware_state)  `enum [**cuvis\_hardware\_state\_t**](cuvis_8h.md#enum-cuvis_hardware_state_t)`<br> |
| define  | [**CUVIS\_IMBUFFER**](cuvis_8h.md#define-cuvis_imbuffer)  `struct [**cuvis\_imbuffer\_t**](structcuvis__imbuffer__t.md)`<br> |
| define  | [**CUVIS\_IMBUFFER\_FORMAT**](cuvis_8h.md#define-cuvis_imbuffer_format)  `enum [**cuvis\_imbuffer\_format\_t**](cuvis_8h.md#enum-cuvis_imbuffer_format_t)`<br> |
| define  | [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int)  `int32\_t`<br> |
| define  | [**CUVIS\_LOGLEVEL**](cuvis_8h.md#define-cuvis_loglevel)  `enum [**cuvis\_loglevel\_t**](group__cuvis__log.md#enum-cuvis_loglevel_t)`<br> |
| define  | [**CUVIS\_MAXBUF**](cuvis_8h.md#define-cuvis_maxbuf)  `256`<br> |
| define  | [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_DARK\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_dark_inttime)  `8`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_DARK\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_dark_temp)  `16`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_OVERILLUMINATED**](cuvis_8h.md#define-cuvis_mesu_flag_overilluminated)  `1`<br>_the measurement was over-illuminated_  |
| define  | [**CUVIS\_MESU\_FLAG\_PAN\_OVERILLUMINATED**](cuvis_8h.md#define-cuvis_mesu_flag_pan_overilluminated)  `512`<br>_the measurements pan image was over-illuminated_  |
| define  | [**CUVIS\_MESU\_FLAG\_POOR\_REFERENCE**](cuvis_8h.md#define-cuvis_mesu_flag_poor_reference)  `2`<br>_A reference measurement used has poor quality._  |
| define  | [**CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING**](cuvis_8h.md#define-cuvis_mesu_flag_poor_white_balancing)  `4`<br>_the white balancing detected bad data_  |
| define  | [**CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_whitedark_inttime)  `128`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_whitedark_temp)  `256`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITE\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_white_inttime)  `32`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITE\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_white_temp)  `64`<br> |
| define  | [**CUVIS\_MESU\_METADATA**](cuvis_8h.md#define-cuvis_mesu_metadata)  `struct [**cuvis\_mesu\_metadata\_t**](structcuvis__mesu__metadata__t.md)`<br> |
| define  | [**CUVIS\_MISC\_PTR**](cuvis_8h.md#define-cuvis_misc_ptr)  `void\*`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITIES**](cuvis_8h.md#define-cuvis_mode_capabilities)  `[**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int)`<br>_holds capabilities for operation mode as flags_  |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_AVERAGING**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_averaging)  `64`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_CAPTURE**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_capture)  `1`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_CONTINUOUS**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_continuous)  `4`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SETGAIN**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_setgain)  `32`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SETINTEGRATIONTIME**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_setintegrationtime)  `16`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SNAPSHOT**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_snapshot)  `8`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_TIMELAPSE**](cuvis_8h.md#define-cuvis_mode_capability_acquisition_timelapse)  `2`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_AUTOEXPOSURE**](cuvis_8h.md#define-cuvis_mode_capability_processing_autoexposure)  `65536`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CALC\_LIVE**](cuvis_8h.md#define-cuvis_mode_capability_processing_calc_live)  `32768`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CLEAR\_RAW**](cuvis_8h.md#define-cuvis_mode_capability_processing_clear_raw)  `16384`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_DARKSUBTRACT**](cuvis_8h.md#define-cuvis_mode_capability_processing_cube_darksubtract)  `1024`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_FLATFIELDING**](cuvis_8h.md#define-cuvis_mode_capability_processing_cube_flatfielding)  `2048`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_RAW**](cuvis_8h.md#define-cuvis_mode_capability_processing_cube_raw)  `256`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_REF**](cuvis_8h.md#define-cuvis_mode_capability_processing_cube_ref)  `512`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_SPECTRALRADIANCE**](cuvis_8h.md#define-cuvis_mode_capability_processing_cube_spectralradiance)  `4096`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_ORIENTATION**](cuvis_8h.md#define-cuvis_mode_capability_processing_orientation)  `131072`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_REQUIRE\_WHITEDARK\_REFLECTANCE**](cuvis_8h.md#define-cuvis_mode_capability_processing_require_whitedark_reflectance)  `33554432`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SAVE\_FILE**](cuvis_8h.md#define-cuvis_mode_capability_processing_save_file)  `8192`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SENSOR\_RAW**](cuvis_8h.md#define-cuvis_mode_capability_processing_sensor_raw)  `128`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DARK**](cuvis_8h.md#define-cuvis_mode_capability_processing_set_dark)  `524288`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DISTANCECALIB**](cuvis_8h.md#define-cuvis_mode_capability_processing_set_distancecalib)  `2097152`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DISTANCE\_VALUE**](cuvis_8h.md#define-cuvis_mode_capability_processing_set_distance_value)  `4194304`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_SPRADCALIB**](cuvis_8h.md#define-cuvis_mode_capability_processing_set_spradcalib)  `1048576`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_WHITE**](cuvis_8h.md#define-cuvis_mode_capability_processing_set_white)  `262144`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_USE\_DARK\_SPRADCALIB**](cuvis_8h.md#define-cuvis_mode_capability_processing_use_dark_spradcalib)  `8388608`<br> |
| define  | [**CUVIS\_MODE\_CAPABILITY\_PROCESSING\_USE\_WHITE\_SPRADCALIB**](cuvis_8h.md#define-cuvis_mode_capability_processing_use_white_spradcalib)  `16777216`<br> |
| define  | [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode)  `enum [**cuvis\_operation\_mode\_t**](group__cuvis__acq.md#enum-cuvis_operation_mode_t)`<br> |
| define  | [**CUVIS\_PANSHARPENING\_SETTINGS**](cuvis_8h.md#define-cuvis_pansharpening_settings)  `struct [**cuvis\_pansharpening\_settings\_t**](structcuvis__pansharpening__settings__t.md)`<br> |
| define  | [**CUVIS\_PAN\_SHAPRENING\_ALGORITHM\_TYPE**](cuvis_8h.md#define-cuvis_pan_shaprening_algorithm_type)  `enum [**cuvis\_pan\_sharpening\_algorithm\_t**](cuvis_8h.md#enum-cuvis_pan_sharpening_algorithm_t)`<br> |
| define  | [**CUVIS\_PAN\_SHAPRENING\_INTERPOLATION\_TYPE**](cuvis_8h.md#define-cuvis_pan_shaprening_interpolation_type)  `enum [**cuvis\_pan\_sharpening\_interpolation\_type\_t**](cuvis_8h.md#enum-cuvis_pan_sharpening_interpolation_type_t)`<br> |
| define  | [**CUVIS\_PROCESSING\_MODE**](cuvis_8h.md#define-cuvis_processing_mode)  `enum [**cuvis\_processing\_mode\_t**](cuvis_8h.md#enum-cuvis_processing_mode_t)`<br> |
| define  | [**CUVIS\_PROC\_ARGS**](cuvis_8h.md#define-cuvis_proc_args)  `struct [**cuvis\_proc\_args\_t**](structcuvis__proc__args__t.md)`<br> |
| define  | [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type)  `enum [**cuvis\_reference\_type\_t**](cuvis_8h.md#enum-cuvis_reference_type_t)`<br> |
| define  | [**CUVIS\_SAVE\_ARGS**](cuvis_8h.md#define-cuvis_save_args)  `struct [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md)`<br> |
| define  | [**CUVIS\_SENSOR\_INFO**](cuvis_8h.md#define-cuvis_sensor_info)  `struct [**cuvis\_sensor\_info\_t**](structcuvis__sensor__info__t.md)`<br> |
| define  | [**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_SESSION\_INFO**](cuvis_8h.md#define-cuvis_session_info)  `struct [**cuvis\_session\_info\_t**](structcuvis__session__info__t.md)`<br> |
| define  | [**CUVIS\_SESSION\_ITEM\_TYPE**](cuvis_8h.md#define-cuvis_session_item_type)  `enum [**cuvis\_session\_item\_type\_t**](cuvis_8h.md#enum-cuvis_session_item_type_t)`<br> |
| define  | [**CUVIS\_SESSION\_MERGE\_MODE**](cuvis_8h.md#define-cuvis_session_merge_mode)  `enum [**cuvis\_session\_merge\_mode\_t**](cuvis_8h.md#enum-cuvis_session_merge_mode_t)`<br> |
| define  | [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size)  `uint64\_t`<br> |
| define  | [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status)  `enum [**cuvis\_status\_t**](group__cuvis__returns.md#enum-cuvis_status_t)`<br> |
| define  | [**CUVIS\_STRING**](cuvis_8h.md#define-cuvis_string)  `[**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char)[[**CUVIS\_MAXBUF**](cuvis_8h.md#define-cuvis_maxbuf)]`<br> |
| define  | [**CUVIS\_TIFF\_COMPRESSION\_MODE**](cuvis_8h.md#define-cuvis_tiff_compression_mode)  `enum [**cuvis\_tiff\_compression\_mode\_t**](cuvis_8h.md#enum-cuvis_tiff_compression_mode_t)`<br> |
| define  | [**CUVIS\_TIFF\_FORMAT**](cuvis_8h.md#define-cuvis_tiff_format)  `enum [**cuvis\_tiff\_format\_t**](cuvis_8h.md#enum-cuvis_tiff_format_t)`<br> |
| define  | [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp)  `uint64\_t`<br> |
| define  | [**CUVIS\_VIEW**](cuvis_8h.md#define-cuvis_view)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_VIEWER\_SETTINGS**](cuvis_8h.md#define-cuvis_viewer_settings)  `struct [**cuvis\_viewer\_settings\_t**](structcuvis__viewer__settings__t.md)`<br> |
| define  | [**CUVIS\_VIEW\_CATEGORY**](cuvis_8h.md#define-cuvis_view_category)  `enum [**cuvis\_view\_category\_t**](cuvis_8h.md#enum-cuvis_view_category_t)`<br> |
| define  | [**CUVIS\_VIEW\_DATA**](cuvis_8h.md#define-cuvis_view_data)  `struct [**cuvis\_view\_data\_t**](structcuvis__view__data__t.md)`<br> |
| define  | [**CUVIS\_WCHAR**](cuvis_8h.md#define-cuvis_wchar)  `wchar\_t`<br> |
| define  | [**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_WORKER\_SETTINGS**](cuvis_8h.md#define-cuvis_worker_settings)  `struct [**cuvis\_worker\_settings\_t**](structcuvis__worker__settings__t.md)`<br> |
| define  | [**CUVIS\_WORKER\_STATE**](cuvis_8h.md#define-cuvis_worker_state)  `struct [**cuvis\_worker\_state\_t**](structcuvis__worker__state__t.md)`<br> |
| define  | [**IMBUFFER\_GET**](cuvis_8h.md#define-imbuffer_get) (ptr, x, y, chn, imbuf) `ptr[((y) \* (imbuf).width + (x)) \* (imbuf).channels + (chn)]`<br> |
| define  | [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi)  <br> |
| define  | [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall)  <br> |
| define  | [**\_CRT\_SECURE\_NO\_WARNINGS**](cuvis_8h.md#define-_crt_secure_no_warnings)  <br> |

## Detailed Description


SDK calls for cuvis C SDK. This header defines all public C SDK functions and data types 


    
## Public Types Documentation




### enum cuvis\_capabilities\_t 

```C++
enum cuvis_capabilities_t {
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
```




<hr>



### enum cuvis\_component\_type\_t 

```C++
enum cuvis_component_type_t {
    component_type_image_sensor = 0,
    component_type_misc_sensor = 1
};
```



the component types 


        

<hr>



### enum cuvis\_data\_type\_t 

_the data field's type_ 
```C++
enum cuvis_data_type_t {
    data_type_unsupported = 0,
    data_type_image = 1,
    data_type_gps = 2,
    data_type_string = 3,
    data_type_sensor_info = 4
};
```




<hr>



### enum cuvis\_hardware\_state\_t 

```C++
enum cuvis_hardware_state_t {
    hardware_state_offline = 0,
    hardware_state_partially_online = 1,
    hardware_state_online = 2
};
```



the state of the hardware 


        

<hr>



### enum cuvis\_imbuffer\_format\_t 

_supported image buffer formats_ 
```C++
enum cuvis_imbuffer_format_t {
    imbuffer_format_uint8 = 1,
    imbuffer_format_uint16 = 2,
    imbuffer_format_uint32 = 3,
    imbuffer_format_float = 4
};
```




<hr>



### enum cuvis\_pan\_sharpening\_algorithm\_t 

_the pan-sharpening algorithm for calculating the pan image's weights_ 
```C++
enum cuvis_pan_sharpening_algorithm_t {
    pan_sharpening_algorithm_Noop = 0,
    pan_sharpening_algorithm_CubertMacroPixel = 1,
    pan_sharpening_algorithm_CubertPanRatio = 2,
    pan_sharpening_algorithm_PCAFusion = 3
};
```




<hr>



### enum cuvis\_pan\_sharpening\_interpolation\_type\_t 

_the pan sharpening interpolation type for scaling up the cube before applying the pan image's weights_ 
```C++
enum cuvis_pan_sharpening_interpolation_type_t {
    pan_sharpening_interpolation_type_NearestNeighbor = 0,
    pan_sharpening_interpolation_type_Linear = 1,
    pan_sharpening_interpolation_type_Cubic = 2,
    pan_sharpening_interpolation_type_Lanczos = 4
};
```




<hr>



### enum cuvis\_processing\_mode\_t 

_The processing mode (a.k.a. capture mode) of a measurement._ 
```C++
enum cuvis_processing_mode_t {
    Cube_Raw = 0,
    Cube_DarkSubtract = 1,
    Cube_Reflectance = 2,
    Cube_SpectralRadiance = 3,
    Preview = 5
};
```




<hr>



### enum cuvis\_reference\_type\_t 

_The type of a reference._ 
```C++
enum cuvis_reference_type_t {
    Reference_Dark = 0,
    Reference_White = 1,
    Reference_WhiteDark = 2,
    Reference_SpRad = 3,
    Reference_Distance = 4
};
```




<hr>



### enum cuvis\_session\_item\_type\_t 

```C++
enum cuvis_session_item_type_t {
    session_item_type_frames = 0,
    session_item_type_frames_no_gaps = 1,
    session_item_type_references = 2
};
```



The session file item type 


        

<hr>



### enum cuvis\_session\_merge\_mode\_t 

_merge mode for the cube exporter_ 
```C++
enum cuvis_session_merge_mode_t {
    session_merge_mode_Default = 0,
    session_merge_mode_Fragmentation = 1,
    session_merge_mode_Merge = 2
};
```




<hr>



### enum cuvis\_tiff\_compression\_mode\_t 

_the tiff compression options_ 
```C++
enum cuvis_tiff_compression_mode_t {
    tiff_compression_mode_None = 0,
    tiff_compression_mode_LZW = 1
};
```




<hr>



### enum cuvis\_tiff\_format\_t 

_the tiff export format._ 
```C++
enum cuvis_tiff_format_t {
    tiff_format_Single = 0,
    tiff_format_MultiChannel = 1,
    tiff_format_MultiPage = 2
};
```




<hr>



### enum cuvis\_view\_category\_t 

```C++
enum cuvis_view_category_t {
    view_category_image = 0,
    view_category_data = 1
};
```



image data types for view data 


        

<hr>



### typedef external\_event\_callback 

```C++
typedef void(SDK_CCALL * external_event_callback) (CUVIS_INT i_handler_id, CUVIS_EVENT i_event);
```



event callback type 


        

<hr>
## Public Functions Documentation




### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_IMBUFFER,
    imbuffer
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_GPS,
    gps
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_SENSOR_INFO,
    sensor_info
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_SESSION_INFO,
    session_info
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_MESU_METADATA,
    mesu_metadata
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_SAVE_ARGS,
    save_args
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_PROC_ARGS,
    proc_args
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_EXPORT_GENERAL_SETTINGS,
    export_general_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_EXPORT_CUBE_SETTINGS,
    export_cube_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_EXPORT_VIEW_SETTINGS,
    export_view_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_EXPORT_TIFF_SETTINGS,
    export_tiff_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_VIEWER_SETTINGS,
    viewer_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_VIEW_DATA,
    view_data
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_COMPONENT_INFO,
    component_info
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_WORKER_SETTINGS,
    worker_settings
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_WORKER_STATE,
    worker_state
) 
```




<hr>



### function ALLOCATE\_AND\_FREE 

```C++
ALLOCATE_AND_FREE (
    CUVIS_CALIBRATION_INFO,
    calibration_info
) 
```




<hr>



### function cuvis\_async\_capture\_get 

_get the result of a async capture._ 
```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_capture_get (
    CUVIS_ASYNC_CAPTURE_RESULT * io_pAsyncResult,
    CUVIS_INT timeout_ms,
    CUVIS_MESU * o_pMesu
) 
```



Get the return code (and error message, if applicable) of an async capture, that has been called. If result is not status\_ok use the [**cuvis\_get\_last\_error\_msg**](group__cuvis__returns.md#function-cuvis_get_last_error_msg) function to get details.


If the timeout is used (value above 0ms), status\_timeout or status\_deferred will be returned, if the function is not yet finished. In that case, the asyncResult handle is still valid and can be used again. If the result is status\_ok the function has finished. For both status\_ok and status\_error, the handle is now invalid.




**Parameters:**


* `io_pAsyncResult` the async handle obtained by calling [**cuvis\_acq\_cont\_capture\_async**](group__cuvis__acq.md#function-cuvis_acq_cont_capture_async). If the call finished, the handle will be invalidated 
* `timeout_ms` the timeout in ms. Give 0 to wait for ever. 
* `o_pMesu` write the measurement handle to this variable, if the call was successful. Else write CUVIS\_HANDLE\_NULL 



**Returns:**

status\_ok if the async function finished successfully. status\_timeout or status\_deferred will be returned, if the function is not yet finished. If it failed for other reasons, the this function returns status\_error. 





        

<hr>



### function cuvis\_calib\_get\_capabilities 

_Get the capabilites of a given mode._ 
```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_get_capabilities (
    CUVIS_CALIB i_calibration,
    CUVIS_OPERATION_MODE i_mode,
    CUVIS_INT * o_pCapabilities
) 
```



Use this function to evaluate which functions are available for a camera calibration. 

**Parameters:**


* `i_calibration` The calibration 
* `i_mode` The mode to check the capabiliets 
* `o_pCapabilities` write the capabilites here. See CUVIS\_MODE\_CAPABILITIES\_x flags. 




        

<hr>



### function cuvis\_event\_get\_acquisition\_data 

```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_event_get_acquisition_data (
    CUVIS_EVENT i_event,
    CUVIS_EVENT_ACQUISITION_DATA * o_p_acquisition_data
) 
```




<hr>



### function cuvis\_measurement\_get\_calib\_id 

_Get the unique calibration id of a measurement._ 
```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_calib_id (
    CUVIS_MESU i_mesu,
    CUVIS_CHAR * o_pCalibId
) 
```



The id unique to a calibration is stored into everything created from it, as such a measurement also contains this id.




**Parameters:**


* `i_mesu` the measurement 
* `o_pCalibId` the output string 




        

<hr>



### function cuvis\_measurement\_get\_capabilities 

_Get the capabilites of the measurement which were present in the calibration during capture. This doesn't indicate which capabilities are currently available for the measurement. See_ [_**cuvis\_proc\_cont\_is\_capable**_](group__cuvis__proc.md#function-cuvis_proc_cont_is_capable) _._
```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_capabilities (
    CUVIS_MESU i_mesu,
    CUVIS_INT * o_pCapabilities
) 
```



Use this function to evaluate which functions are available for a given measurement. 

**Parameters:**


* `i_mesu` The measurement 
* `o_pCapabilities` write the capabilites here. See CUVIS\_MODE\_CAPABILITIES\_x flags. 




        

<hr>



### function cuvis\_proc\_cont\_get\_calib\_id 

_Get the unique calibration id of a processing context._ 
```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_get_calib_id (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_CHAR * o_pCalibId
) 
```



The id unique to a calibration is stored into everything created from it, as such a processing context also contains this id.




**Parameters:**


* `i_procCont` the processing context 
* `o_pCalibId` the output string 




        

<hr>



### function cuvis\_register\_external\_event\_callback 

```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_register_external_event_callback (
    external_event_callback i_callback,
    CUVIS_INT i_type,
    CUVIS_INT * o_p_handler_id
) 
```



Register an event handler. The event handler will be called on all events which satisfy the supplied event handler type. Returns an id for the event handler to allow unregistering of the specific event handler only valid during the runtime of the callback.




**Parameters:**


* `i_callback` the event handler function callback 
* `i_type` the type of the event handler which is registered 
* `o_p_handler_id` a pointer where the handler id will be written to 




        

<hr>



### function cuvis\_unregister\_event\_callback 

```C++
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_unregister_event_callback (
    CUVIS_INT i_handler_id
) 
```



Unregisters an event handler. Supply a valid handler id to specific the correct callback which is going to be unregistered 


        

<hr>
## Macro Definition Documentation





### define ACQ\_GET\_SINGLE\_VALUE 

```C++
#define ACQ_GET_SINGLE_VALUE (
    NAME,
    TYPE,
    COMMENT
) `/** Get NAME function. Details: COMMENT\n Result is written to o_pvalue */ \ SDK_CAPI  CUVIS_STATUS  SDK_CCALL NAME##_get( CUVIS_ACQ_CONT i_acqCont, TYPE* o_pvalue);`
```



macro for creating acquisition getter functions 


        

<hr>



### define ACQ\_SET\_SINGLE\_VALUE 

```C++
#define ACQ_SET_SINGLE_VALUE (
    NAME,
    TYPE,
    UNIT_STR
) `/* multi line expression */`
```



macro for creating stubs of sync and async acquisition setter functions 


        

<hr>



### define ALLOCATE\_AND\_FREE 

```C++
#define ALLOCATE_AND_FREE (
    DATATYPE,
    NAME
) `/* multi line expression */`
```



macro for creating allocate and free functions for c data structures 


        

<hr>



### define COMP\_GET\_SINGLE\_VALUE 

```C++
#define COMP_GET_SINGLE_VALUE (
    NAME,
    TYPE,
    COMMENT
) `/** Get NAME function. Details: COMMENT\n Result is written to o_pvalue */ \ SDK_CAPI  CUVIS_STATUS  SDK_CCALL NAME##_get( CUVIS_ACQ_CONT i_acqCont, CUVIS_INT i_id, TYPE* o_pvalue);`
```



macro for creating acquisition-component getter functions 


        

<hr>



### define COMP\_SET\_SINGLE\_VALUE 

```C++
#define COMP_SET_SINGLE_VALUE (
    NAME,
    TYPE,
    UNIT_STR
) `/* multi line expression */`
```



macro for creating stubs of sync and async acquisition-component setter functions 


        

<hr>



### define CUVIS\_ACQ\_CONT 

```C++
#define CUVIS_ACQ_CONT `CUVIS_HANDLE`
```



acquisition context handle 


        

<hr>



### define CUVIS\_ASYNC\_CALL\_RESULT 

_handle to an async function call result._ 
```C++
#define CUVIS_ASYNC_CALL_RESULT `CUVIS_HANDLE`
```



A handle can be checked by the function [**cuvis\_async\_call\_get**](group__cuvis__async.md#function-cuvis_async_call_get) 


        

<hr>



### define CUVIS\_ASYNC\_CAPTURE\_RESULT 

_handle to an async capture result._ 
```C++
#define CUVIS_ASYNC_CAPTURE_RESULT `CUVIS_HANDLE`
```



A handle can be checked by the function [**cuvis\_async\_capture\_get**](cuvis_8h.md#function-cuvis_async_capture_get) 


        

<hr>



### define CUVIS\_CALIB 

```C++
#define CUVIS_CALIB `CUVIS_HANDLE`
```



calibration handle 


        

<hr>



### define CUVIS\_CALIBRATION\_INFO 

```C++
#define CUVIS_CALIBRATION_INFO `struct cuvis_calibration_info_t`
```




<hr>



### define CUVIS\_CHAR 

```C++
#define CUVIS_CHAR `char`
```




<hr>



### define CUVIS\_CHECK 

```C++
#define CUVIS_CHECK (
    code
) `/* multi line expression */`
```



simple check function for error code 


        

<hr>



### define CUVIS\_COMPONENT\_INFO 

```C++
#define CUVIS_COMPONENT_INFO `struct cuvis_component_info_t`
```




<hr>



### define CUVIS\_COMPONENT\_TYPE 

```C++
#define CUVIS_COMPONENT_TYPE `enum cuvis_component_type_t`
```




<hr>



### define CUVIS\_DATA\_TYPE 

```C++
#define CUVIS_DATA_TYPE `enum cuvis_data_type_t`
```




<hr>



### define CUVIS\_EVENT 

```C++
#define CUVIS_EVENT `CUVIS_HANDLE`
```




<hr>



### define CUVIS\_EVENT\_ACQUISITION\_DATA 

```C++
#define CUVIS_EVENT_ACQUISITION_DATA `struct cuvis_event_acquisition_data_t`
```




<hr>



### define CUVIS\_EVENT\_ACQUISTION 

```C++
#define CUVIS_EVENT_ACQUISTION `(1 << 8)`
```




<hr>



### define CUVIS\_EVENT\_BASE\_DATA 

```C++
#define CUVIS_EVENT_BASE_DATA `struct cuvis_event_base_data_t`
```




<hr>



### define CUVIS\_EVENT\_COMPONENT 

```C++
#define CUVIS_EVENT_COMPONENT `( CUVIS_EVENT_ACQUISTION | (1 << 4))`
```




<hr>



### define CUVIS\_EVENT\_COMPONENT\_DATA 

```C++
#define CUVIS_EVENT_COMPONENT_DATA `struct cuvis_event_component_data_t`
```




<hr>



### define CUVIS\_EVENT\_PROCESSING 

```C++
#define CUVIS_EVENT_PROCESSING `(2 << 8)`
```




<hr>



### define CUVIS\_EVENT\_PROCESSING\_DATA 

```C++
#define CUVIS_EVENT_PROCESSING_DATA `struct cuvis_event_processing_event_t`
```




<hr>



### define CUVIS\_EVENT\_QUALITY\_DATA 

```C++
#define CUVIS_EVENT_QUALITY_DATA `struct cuvis_event_quality_event_t`
```




<hr>



### define CUVIS\_EVENT\_TRIGGER\_SKIPPED 

```C++
#define CUVIS_EVENT_TRIGGER_SKIPPED `( CUVIS_EVENT_COMPONENT | 1)`
```




<hr>



### define CUVIS\_EXPORTER 

```C++
#define CUVIS_EXPORTER `CUVIS_HANDLE`
```



exporter handle (all exporter types) 


        

<hr>



### define CUVIS\_EXPORT\_CUBE\_SETTINGS 

```C++
#define CUVIS_EXPORT_CUBE_SETTINGS `struct cuvis_save_args_t`
```




<hr>



### define CUVIS\_EXPORT\_GENERAL\_SETTINGS 

```C++
#define CUVIS_EXPORT_GENERAL_SETTINGS `struct cuvis_export_general_settings_t`
```




<hr>



### define CUVIS\_EXPORT\_TIFF\_SETTINGS 

```C++
#define CUVIS_EXPORT_TIFF_SETTINGS `struct cuvis_export_tiff_settings_t`
```




<hr>



### define CUVIS\_EXPORT\_VIEW\_SETTINGS 

```C++
#define CUVIS_EXPORT_VIEW_SETTINGS `struct cuvis_export_view_settings_t`
```




<hr>



### define CUVIS\_FLAGS 

```C++
#define CUVIS_FLAGS `uint32_t`
```



field for binary flags 


        

<hr>



### define CUVIS\_GPS 

```C++
#define CUVIS_GPS `struct cuvis_gps_t`
```




<hr>



### define CUVIS\_HANDLE 

```C++
#define CUVIS_HANDLE `CUVIS_INT`
```



handle 


        

<hr>



### define CUVIS\_HANDLE\_NULL 

```C++
#define CUVIS_HANDLE_NULL `CUVIS_HANDLE (0)`
```



handle value of 0 is reserved for invalid handles 


        

<hr>



### define CUVIS\_HARDWARE\_STATE 

```C++
#define CUVIS_HARDWARE_STATE `enum cuvis_hardware_state_t`
```




<hr>



### define CUVIS\_IMBUFFER 

```C++
#define CUVIS_IMBUFFER `struct cuvis_imbuffer_t`
```




<hr>



### define CUVIS\_IMBUFFER\_FORMAT 

```C++
#define CUVIS_IMBUFFER_FORMAT `enum cuvis_imbuffer_format_t`
```




<hr>



### define CUVIS\_INT 

```C++
#define CUVIS_INT `int32_t`
```




<hr>



### define CUVIS\_LOGLEVEL 

```C++
#define CUVIS_LOGLEVEL `enum cuvis_loglevel_t`
```




<hr>



### define CUVIS\_MAXBUF 

```C++
#define CUVIS_MAXBUF `256`
```



max string buffer length (e.g. for paths) 


        

<hr>



### define CUVIS\_MESU 

```C++
#define CUVIS_MESU `CUVIS_HANDLE`
```



measurement handle 


        

<hr>



### define CUVIS\_MESU\_FLAG\_DARK\_INTTIME 

```C++
#define CUVIS_MESU_FLAG_DARK_INTTIME `8`
```



the dark's integration time does not match the measurement


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_DARK\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_dark_inttime_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_DARK\_TEMP 

```C++
#define CUVIS_MESU_FLAG_DARK_TEMP `16`
```



the sensor temperature at dark's recording does not match measurement's recording device temperature


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_DARK\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_dark_temp_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_OVERILLUMINATED 

_the measurement was over-illuminated_ 
```C++
#define CUVIS_MESU_FLAG_OVERILLUMINATED `1`
```



One of the devices sensor data points were over-saturated while recording This may not be directly visible in the data cube, as the sensor data needs extensive processing. 

**Note:**

only the spectral data is checked. The pan image's saturation is not checked.


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_OVERILLUMINATED\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_overilluminated_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_PAN\_OVERILLUMINATED 

_the measurements pan image was over-illuminated_ 
```C++
#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED `512`
```



One of the devices pan sensor data points were over-saturated while recording This may not be directly visible in the data cube, as the sensor data needs extensive processing. 

**Note:**

only the pan data is checked. The spectral image's saturation is not checked.


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_PAN\_OVERILLUMINATED\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_pan_overilluminated_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_POOR\_REFERENCE 

_A reference measurement used has poor quality._ 
```C++
#define CUVIS_MESU_FLAG_POOR_REFERENCE `2`
```



One or more of the reference measurements used had a poor data quality. This may lead to invalid results.


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_POOR\_REFERENCE\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_poor_reference_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING 

_the white balancing detected bad data_ 
```C++
#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING `4`
```



If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_poor_white_balancing_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME 

```C++
#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME `128`
```



the white's dark integration time does not match the measurement


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_whitedark_inttime_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP 

```C++
#define CUVIS_MESU_FLAG_WHITEDARK_TEMP `256`
```



the sensor temperature at white's dark recording does not match measurement's recording device temperature


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_whitedark_temp_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITE\_INTTIME 

```C++
#define CUVIS_MESU_FLAG_WHITE_INTTIME `32`
```



the white's integration time does not match the measurement


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_WHITE\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_white_inttime_key) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITE\_TEMP 

```C++
#define CUVIS_MESU_FLAG_WHITE_TEMP `64`
```



the sensor temperature at white's recording does not match measurement's recording device temperature


If this flag is set, additional information can retrieved by calling [**cuvis\_measurement\_get\_data\_sensor\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_sensor_info) with the key [**CUVIS\_MESU\_FLAG\_WHITE\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_white_temp_key) 


        

<hr>



### define CUVIS\_MESU\_METADATA 

```C++
#define CUVIS_MESU_METADATA `struct cuvis_mesu_metadata_t`
```




<hr>



### define CUVIS\_MISC\_PTR 

```C++
#define CUVIS_MISC_PTR `void*`
```



placeholder data type 


        

<hr>



### define CUVIS\_MODE\_CAPABILITIES 

_holds capabilities for operation mode as flags_ 
```C++
#define CUVIS_MODE_CAPABILITIES `CUVIS_INT`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_AVERAGING 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_AVERAGING `64`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_CAPTURE 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_CAPTURE `1`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_CONTINUOUS 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_CONTINUOUS `4`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SETGAIN 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SETGAIN `32`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SETINTEGRATIONTIME 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SETINTEGRATIONTIME `16`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_SNAPSHOT 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_SNAPSHOT `8`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_ACQUISITION\_TIMELAPSE 

```C++
#define CUVIS_MODE_CAPABILITY_ACQUISITION_TIMELAPSE `2`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_AUTOEXPOSURE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_AUTOEXPOSURE `65536`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CALC\_LIVE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CALC_LIVE `32768`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CLEAR\_RAW 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CLEAR_RAW `16384`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_DARKSUBTRACT 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_DARKSUBTRACT `1024`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_FLATFIELDING 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_FLATFIELDING `2048`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_RAW 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_RAW `256`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_REF 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_REF `512`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_CUBE\_SPECTRALRADIANCE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_SPECTRALRADIANCE `4096`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_ORIENTATION 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_ORIENTATION `131072`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_REQUIRE\_WHITEDARK\_REFLECTANCE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_REQUIRE_WHITEDARK_REFLECTANCE `33554432`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SAVE\_FILE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SAVE_FILE `8192`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SENSOR\_RAW 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SENSOR_RAW `128`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DARK 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DARK `524288`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DISTANCECALIB 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCECALIB `2097152`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_DISTANCE\_VALUE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCE_VALUE `4194304`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_SPRADCALIB 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_SPRADCALIB `1048576`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_SET\_WHITE 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_SET_WHITE `262144`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_USE\_DARK\_SPRADCALIB 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_USE_DARK_SPRADCALIB `8388608`
```




<hr>



### define CUVIS\_MODE\_CAPABILITY\_PROCESSING\_USE\_WHITE\_SPRADCALIB 

```C++
#define CUVIS_MODE_CAPABILITY_PROCESSING_USE_WHITE_SPRADCALIB `16777216`
```




<hr>



### define CUVIS\_OPERATION\_MODE 

```C++
#define CUVIS_OPERATION_MODE `enum cuvis_operation_mode_t`
```




<hr>



### define CUVIS\_PANSHARPENING\_SETTINGS 

```C++
#define CUVIS_PANSHARPENING_SETTINGS `struct cuvis_pansharpening_settings_t`
```




<hr>



### define CUVIS\_PAN\_SHAPRENING\_ALGORITHM\_TYPE 

```C++
#define CUVIS_PAN_SHAPRENING_ALGORITHM_TYPE `enum cuvis_pan_sharpening_algorithm_t`
```




<hr>



### define CUVIS\_PAN\_SHAPRENING\_INTERPOLATION\_TYPE 

```C++
#define CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE `enum cuvis_pan_sharpening_interpolation_type_t`
```




<hr>



### define CUVIS\_PROCESSING\_MODE 

```C++
#define CUVIS_PROCESSING_MODE `enum cuvis_processing_mode_t`
```




<hr>



### define CUVIS\_PROC\_ARGS 

```C++
#define CUVIS_PROC_ARGS `struct cuvis_proc_args_t`
```




<hr>



### define CUVIS\_PROC\_CONT 

```C++
#define CUVIS_PROC_CONT `CUVIS_HANDLE`
```



processing context handle 


        

<hr>



### define CUVIS\_REFERENCE\_TYPE 

```C++
#define CUVIS_REFERENCE_TYPE `enum cuvis_reference_type_t`
```




<hr>



### define CUVIS\_SAVE\_ARGS 

```C++
#define CUVIS_SAVE_ARGS `struct cuvis_save_args_t`
```




<hr>



### define CUVIS\_SENSOR\_INFO 

```C++
#define CUVIS_SENSOR_INFO `struct cuvis_sensor_info_t`
```




<hr>



### define CUVIS\_SESSION\_FILE 

```C++
#define CUVIS_SESSION_FILE `CUVIS_HANDLE`
```



measurement session\_info file handle 


        

<hr>



### define CUVIS\_SESSION\_INFO 

```C++
#define CUVIS_SESSION_INFO `struct cuvis_session_info_t`
```




<hr>



### define CUVIS\_SESSION\_ITEM\_TYPE 

```C++
#define CUVIS_SESSION_ITEM_TYPE `enum cuvis_session_item_type_t`
```




<hr>



### define CUVIS\_SESSION\_MERGE\_MODE 

```C++
#define CUVIS_SESSION_MERGE_MODE `enum cuvis_session_merge_mode_t`
```




<hr>



### define CUVIS\_SIZE 

```C++
#define CUVIS_SIZE `uint64_t`
```




<hr>



### define CUVIS\_STATUS 

```C++
#define CUVIS_STATUS `enum cuvis_status_t`
```




<hr>



### define CUVIS\_STRING 

```C++
#define CUVIS_STRING `CUVIS_CHAR [ CUVIS_MAXBUF ]`
```



cstring data type definition 


        

<hr>



### define CUVIS\_TIFF\_COMPRESSION\_MODE 

```C++
#define CUVIS_TIFF_COMPRESSION_MODE `enum cuvis_tiff_compression_mode_t`
```




<hr>



### define CUVIS\_TIFF\_FORMAT 

```C++
#define CUVIS_TIFF_FORMAT `enum cuvis_tiff_format_t`
```




<hr>



### define CUVIS\_TIMESTAMP 

```C++
#define CUVIS_TIMESTAMP `uint64_t`
```



time since epoch in millisecond steps 


        

<hr>



### define CUVIS\_VIEW 

```C++
#define CUVIS_VIEW `CUVIS_HANDLE`
```



data viewer result handle (view) 


        

<hr>



### define CUVIS\_VIEWER 

```C++
#define CUVIS_VIEWER `CUVIS_HANDLE`
```



data viewer handle 


        

<hr>



### define CUVIS\_VIEWER\_SETTINGS 

```C++
#define CUVIS_VIEWER_SETTINGS `struct cuvis_viewer_settings_t`
```




<hr>



### define CUVIS\_VIEW\_CATEGORY 

```C++
#define CUVIS_VIEW_CATEGORY `enum cuvis_view_category_t`
```




<hr>



### define CUVIS\_VIEW\_DATA 

```C++
#define CUVIS_VIEW_DATA `struct cuvis_view_data_t`
```




<hr>



### define CUVIS\_WCHAR 

```C++
#define CUVIS_WCHAR `wchar_t`
```




<hr>



### define CUVIS\_WORKER 

```C++
#define CUVIS_WORKER `CUVIS_HANDLE`
```



worker handle 


        

<hr>



### define CUVIS\_WORKER\_SETTINGS 

```C++
#define CUVIS_WORKER_SETTINGS `struct cuvis_worker_settings_t`
```




<hr>



### define CUVIS\_WORKER\_STATE 

```C++
#define CUVIS_WORKER_STATE `struct cuvis_worker_state_t`
```




<hr>



### define IMBUFFER\_GET 

```C++
#define IMBUFFER_GET (
    ptr,
    x,
    y,
    chn,
    imbuf
) `ptr[((y) * (imbuf).width + (x)) * (imbuf).channels + (chn)]`
```



helper macro for obtaining a pixel position from an imbuffer pointer 


        

<hr>



### define SDK\_CAPI 

```C++
#define SDK_CAPI 
```




<hr>



### define SDK\_CCALL 

```C++
#define SDK_CCALL 
```




<hr>



### define \_CRT\_SECURE\_NO\_WARNINGS 

```C++
#define _CRT_SECURE_NO_WARNINGS 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

