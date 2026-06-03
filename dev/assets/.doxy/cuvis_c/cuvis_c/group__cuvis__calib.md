

# Group cuvis\_calib



[**Modules**](modules.md) **>** [**cuvis\_calib**](group__cuvis__calib.md)



[More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_copy\_handle**](#function-cuvis_calib_copy_handle) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calibration, [**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) \* o\_pCalibration) <br>_Creates an additional calibration handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_create\_from\_path**](#function-cuvis_calib_create_from_path) (const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_factoryDir, [**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) \* o\_pCalibration) <br>_Create a calibration from factory path._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_create\_from\_session\_file**](#function-cuvis_calib_create_from_session_file) (const [**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) \* o\_pCalibration) <br>_Create a calibration from session file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_free**](#function-cuvis_calib_free) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) \* io\_pCalibration) <br>_Clear a loaded calibration by it's handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_get\_component\_count**](#function-cuvis_calib_get_component_count) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCount) <br>_Get the number of components._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_get\_component\_info**](#function-cuvis_calib_get_component_info) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_COMPONENT\_INFO**](cuvis_8h.md#define-cuvis_component_info) \* o\_pCompInfo) <br>_Get components general info._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_get\_id**](#function-cuvis_calib_get_id) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pCalibId) <br>_Get the unique id of a calibration._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_calib\_get\_info**](#function-cuvis_calib_get_info) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_CALIBRATION\_INFO**](cuvis_8h.md#define-cuvis_calibration_info) \* o\_pCalibInfo) <br>_Get info of a calibration._  |




























## Detailed Description


Functions to interact with a calibration object of the SDK.


There are two ways to create a calibration object. One way is by loading it specifically from a factory directory (see [**cuvis\_calib\_create\_from\_path**](group__cuvis__calib.md#function-cuvis_calib_create_from_path)). The other one is by loading it from a session file. The Calibration object is needed to load other parts of the SDK like the [**Acquisition Context**](group__cuvis__acq.md) and the [**Processing Context**](group__cuvis__proc.md). 


    
## Public Functions Documentation




### function cuvis\_calib\_copy\_handle 

_Creates an additional calibration handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_copy_handle (
    CUVIS_CALIB i_calibration,
    CUVIS_CALIB * o_pCalibration
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_calibration` The handle of the calibration to copy 
* `o_pCalibration` The new handle of the calibration. 



**Returns:**

status\_ok if the calibration handle could be doubled 





        

<hr>



### function cuvis\_calib\_create\_from\_path 

_Create a calibration from factory path._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_create_from_path (
    const CUVIS_CHAR * i_factoryDir,
    CUVIS_CALIB * o_pCalibration
) 
```



The calibration is created from a factory path, containing the license and calibration file "init.daq" as well as further calibration files (e.g. SpRad.cu3).


The calibration is lazy-loading, i.e. the AcquisitionContext and the ProcessingContext will only be initialized, when explicitly called.




**Note:**

do not load multiple calibration instances of the same camera




**Parameters:**


* `i_factoryDir` The path to the factory directory 
* `o_pCalibration` the handle of the calibration 



**Returns:**

status\_ok if the calibration could be loaded 





        

<hr>



### function cuvis\_calib\_create\_from\_session\_file 

_Create a calibration from session file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_create_from_session_file (
    const CUVIS_SESSION_FILE i_sess,
    CUVIS_CALIB * o_pCalibration
) 
```



Create a calibration from an existion session file.


The calibration is lazy-loading, i.e. the AcquisitionContext and the ProcessingContext will only be initialized, when explicitly called.


When you create a processing context from the calibration cerated with this function, you won't have the references from the session file set. Use [**cuvis\_proc\_cont\_create\_from\_session\_file**](group__cuvis__proc.md#function-cuvis_proc_cont_create_from_session_file) to load a processing context where the referenecs are taken from the session file.




**Note:**

do not load multiple calibration instances of the same camera




**Parameters:**


* `i_sess` The session file 
* `o_pCalibration` the handle of the calibration 



**Returns:**

status\_ok if the calibration could be loaded 





        

<hr>



### function cuvis\_calib\_free 

_Clear a loaded calibration by it's handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_free (
    CUVIS_CALIB * io_pCalibration
) 
```



The internal memory is freed.




**Parameters:**


* `io_pCalibration` The handle of the calibration. The handle number will be invalidated. 



**Returns:**

status\_ok if the calibration could be released 





        

<hr>



### function cuvis\_calib\_get\_component\_count 

_Get the number of components._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_get_component_count (
    CUVIS_CALIB i_calib,
    CUVIS_INT * o_pCount
) 
```



The acquisition hardware is build from one or more components. Get the component count. 

**Parameters:**


* `i_calib` the calibration 
* `o_pCount` the number of components is written here 



**Returns:**

cuvis\_ok if the number of components could be set 





        

<hr>



### function cuvis\_calib\_get\_component\_info 

_Get components general info._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_get_component_info (
    CUVIS_CALIB i_calib,
    CUVIS_INT i_id,
    CUVIS_COMPONENT_INFO * o_pCompInfo
) 
```



Return general component information about a component build into the acquisition hardware the calibration is made for. This helps identifying the correct component for settings specific component settings (e.g. gain)




**Parameters:**


* `i_calib` the calibration 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `o_pCompInfo` the component info to be filled 



**Returns:**

cuvis\_ok if the info fields could be filled. 





        

<hr>



### function cuvis\_calib\_get\_id 

_Get the unique id of a calibration._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_get_id (
    CUVIS_CALIB i_calib,
    CUVIS_CHAR * o_pCalibId
) 
```





**Parameters:**


* `i_calib` the calibration 
* `o_pCalibId` the unique id output string 




        

<hr>



### function cuvis\_calib\_get\_info 

_Get info of a calibration._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_calib_get_info (
    CUVIS_CALIB i_calib,
    CUVIS_CALIBRATION_INFO * o_pCalibInfo
) 
```





**Parameters:**


* `i_calib` the calibration 
* `o_pCalibInfo` the info data struct 




        

<hr>

------------------------------


