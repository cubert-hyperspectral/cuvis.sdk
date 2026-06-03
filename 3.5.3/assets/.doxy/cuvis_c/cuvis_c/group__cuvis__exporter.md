

# Group cuvis\_exporter



[**Modules**](modules.md) **>** [**cuvis\_exporter**](group__cuvis__exporter.md)



[More...](#detailed-description)
















## Classes

| Type | Name |
| ---: | :--- |
| struct | [**cuvis\_export\_general\_settings\_t**](structcuvis__export__general__settings__t.md) <br>_general export settings_  |
| struct | [**cuvis\_export\_tiff\_settings\_t**](structcuvis__export__tiff__settings__t.md) <br>_Additional settings for exporting tiff. See also_ [_**cuvis\_export\_general\_settings\_t**_](structcuvis__export__general__settings__t.md) _._ |
| struct | [**cuvis\_export\_view\_settings\_t**](structcuvis__export__view__settings__t.md) <br>_Additional settings for exporting to a userplugin view. See also_ [_**cuvis\_export\_general\_settings\_t**_](structcuvis__export__general__settings__t.md) _._ |
| struct | [**cuvis\_pansharpening\_settings\_t**](structcuvis__pansharpening__settings__t.md) <br>_general export settings_  |
| struct | [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md) <br>_options for saving as cu3/cu3s files_  |






















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_apply**](#function-cuvis_exporter_apply) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) i\_exporter, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu) <br>_Export a measurement with an exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_create\_cube**](#function-cuvis_exporter_create_cube) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) \* o\_pExporter, [**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings) generalSettings, [**CUVIS\_EXPORT\_CUBE\_SETTINGS**](cuvis_8h.md#define-cuvis_export_cube_settings) formatSettings) <br>_Create a cube exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_create\_envi**](#function-cuvis_exporter_create_envi) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) \* o\_pExporter, [**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings) generalSettings) <br>_Create a ENVI exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_create\_tiff**](#function-cuvis_exporter_create_tiff) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) \* o\_pExporter, [**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings) generalSettings, [**CUVIS\_EXPORT\_TIFF\_SETTINGS**](cuvis_8h.md#define-cuvis_export_tiff_settings) formatSettings) <br>_Create a tiff exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_create\_view**](#function-cuvis_exporter_create_view) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) \* o\_pExporter, [**CUVIS\_EXPORT\_GENERAL\_SETTINGS**](cuvis_8h.md#define-cuvis_export_general_settings) generalSettings, [**CUVIS\_EXPORT\_VIEW\_SETTINGS**](cuvis_8h.md#define-cuvis_export_view_settings) formatSettings) <br>_Create a VIEW exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_flush**](#function-cuvis_exporter_flush) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) i\_exporter) <br>_Flush an exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_free**](#function-cuvis_exporter_free) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) \* io\_pExporter) <br>_Release an exporter._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_exporter\_get\_queue\_used**](#function-cuvis_exporter_get_queue_used) ([**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) i\_exporter, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pQueueUsed) <br> |




























## Detailed Description


How to export Measurement captured with the SDK.


A handle for each of the exporter can be obtainend by calling either [**cuvis\_exporter\_create\_cube**](group__cuvis__exporter.md#function-cuvis_exporter_create_cube), [**cuvis\_exporter\_create\_envi**](group__cuvis__exporter.md#function-cuvis_exporter_create_envi), [**cuvis\_exporter\_create\_tiff**](group__cuvis__exporter.md#function-cuvis_exporter_create_tiff) or [**cuvis\_exporter\_create\_view**](group__cuvis__exporter.md#function-cuvis_exporter_create_view). Each of the so created exporter can then export a [**Measurement**](group__cuvis__mesu.md) to the respective format by calling [**cuvis\_exporter\_apply**](group__cuvis__exporter.md#function-cuvis_exporter_apply). Each exporter takes options in form of [**cuvis\_export\_general\_settings\_t**](structcuvis__export__general__settings__t.md) and one of the following format specific structs [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md), [**cuvis\_export\_view\_settings\_t**](structcuvis__export__view__settings__t.md), [**cuvis\_export\_tiff\_settings\_t**](structcuvis__export__tiff__settings__t.md)


See the respective struct documentations for more information on the individual options 


    
## Public Functions Documentation




### function cuvis\_exporter\_apply 

_Export a measurement with an exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_apply (
    CUVIS_EXPORTER i_exporter,
    CUVIS_MESU i_mesu
) 
```





**Parameters:**


* `i_exporter` The exporter 
* `i_mesu` the measurement 



**Returns:**

status\_ok if the measurement was exported successfully. status\_not\_stored if the measurement could not be stored. 





        

<hr>



### function cuvis\_exporter\_create\_cube 

_Create a cube exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_create_cube (
    CUVIS_EXPORTER * o_pExporter,
    CUVIS_EXPORT_GENERAL_SETTINGS generalSettings,
    CUVIS_EXPORT_CUBE_SETTINGS formatSettings
) 
```





**Parameters:**


* `o_pExporter` The handle of the exporter 
* `generalSettings` General export settings 
* `formatSettings` Additional Cube export settings 



**Returns:**

status\_ok if the exporter was created successfully 





        

<hr>



### function cuvis\_exporter\_create\_envi 

_Create a ENVI exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_create_envi (
    CUVIS_EXPORTER * o_pExporter,
    CUVIS_EXPORT_GENERAL_SETTINGS generalSettings
) 
```





**Parameters:**


* `o_pExporter` The handle of the exporter 
* `generalSettings` General export settings 



**Returns:**

status\_ok if the exporter was created successfully 





        

<hr>



### function cuvis\_exporter\_create\_tiff 

_Create a tiff exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_create_tiff (
    CUVIS_EXPORTER * o_pExporter,
    CUVIS_EXPORT_GENERAL_SETTINGS generalSettings,
    CUVIS_EXPORT_TIFF_SETTINGS formatSettings
) 
```





**Parameters:**


* `o_pExporter` The handle of the exporter 
* `generalSettings` General export settings 
* `formatSettings` Additional TIF export settings 



**Returns:**

status\_ok if the exporter was created successfully 





        

<hr>



### function cuvis\_exporter\_create\_view 

_Create a VIEW exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_create_view (
    CUVIS_EXPORTER * o_pExporter,
    CUVIS_EXPORT_GENERAL_SETTINGS generalSettings,
    CUVIS_EXPORT_VIEW_SETTINGS formatSettings
) 
```



Not to be confused with the VIEWER. The view exporter saves views to disk.




**Parameters:**


* `o_pExporter` The handle of the exporter 
* `generalSettings` General export settings 
* `formatSettings` Additional view export settings 



**Returns:**

status\_ok if the exporter was created successfully 





        

<hr>



### function cuvis\_exporter\_flush 

_Flush an exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_flush (
    CUVIS_EXPORTER i_exporter
) 
```





**Parameters:**


* `i_exporter` The exporter to flush 



**Returns:**

status\_ok if the exporter was flushed successfully. 





        

<hr>



### function cuvis\_exporter\_free 

_Release an exporter._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_free (
    CUVIS_EXPORTER * io_pExporter
) 
```





**Parameters:**


* `io_pExporter` Exporter to be released. If successfully, handle will be invalidated 



**Returns:**

status\_ok if the exporter was cleared. 





        

<hr>



### function cuvis\_exporter\_get\_queue\_used 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_exporter_get_queue_used (
    CUVIS_EXPORTER i_exporter,
    CUVIS_INT * o_pQueueUsed
) 
```




<hr>

------------------------------


