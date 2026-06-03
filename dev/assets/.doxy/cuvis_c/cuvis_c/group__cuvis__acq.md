

# Group cuvis\_acq



[**Modules**](modules.md) **>** [**cuvis\_acq**](group__cuvis__acq.md)



_Capturing Images with the SDK._ [More...](#detailed-description)


















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**cuvis\_operation\_mode\_t**](#enum-cuvis_operation_mode_t)  <br>_Operation mode of a camera._  |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_fps, double, "Frames per second") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_average, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "Number of averages") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_integration\_time, double, "Integration time in milliseconds") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_auto\_exp, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "get\_auto\_exp") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_auto\_exp\_comp, double, "get auto exposure compensation") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_operation\_mode, [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode), "enumeration value") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_bandwidth, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "bandwidth in MBit/s") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_queue\_size, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "size of measurement queue") <br> |
|   | [**ACQ\_GET\_SINGLE\_VALUE**](#function-acq_get_single_value) (cuvis\_acq\_cont\_queue\_used, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "used part of measurement queue") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_fps, double, "Frames per second") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_average, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "Number of averages") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_integration\_time, double, "Integration time in milliseconds") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_auto\_exp, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), "set\_auto\_exp") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_auto\_exp\_comp, double, "set auto exposure compensation") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_operation\_mode, [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode), "enumeration value") <br> |
|   | [**ACQ\_SET\_SINGLE\_VALUE**](#function-acq_set_single_value) (cuvis\_acq\_cont\_continuous, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int), " 0=stop) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_capture**](#function-cuvis_acq_cont_capture) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) timeout\_ms) <br>_Capture a measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_capture\_async**](#function-cuvis_acq_cont_capture_async) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_ASYNC\_CAPTURE\_RESULT**](cuvis_8h.md#define-cuvis_async_capture_result) \* o\_pAsyncResult) <br>_Capture a measurement async._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_copy\_handle**](#function-cuvis_acq_cont_copy_handle) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) \* o\_pAcqCont) <br>_Creates an additional acquisition context handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_create\_from\_calib**](#function-cuvis_acq_cont_create_from_calib) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) \* o\_pAcqCont) <br>_Load a acquisition context from a given calibration._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_create\_from\_session\_file**](#function-cuvis_acq_cont_create_from_session_file) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_simulate, [**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) \* o\_pAcqCont) <br>_Load a acquisition context from a given session\_file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_dead\_pixel\_correction\_available\_get**](#function-cuvis_acq_cont_dead_pixel_correction_available_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_is\_available) <br>_Query whether the dead pixel correction is available._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_dead\_pixel\_correction\_enabled\_get**](#function-cuvis_acq_cont_dead_pixel_correction_enabled_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_is\_enabled) <br>_Query whether the dead pixel correction is enabled._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_dead\_pixel\_correction\_enabled\_set**](#function-cuvis_acq_cont_dead_pixel_correction_enabled_set) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) o\_set\_enabled) <br>_Enable or disable the dead pixel correction algorithm._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_free**](#function-cuvis_acq_cont_free) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) \* io\_pAcqCont) <br>_Clear a loaded acquisition context by it's handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_get\_component\_count**](#function-cuvis_acq_cont_get_component_count) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCount) <br>_Get the number of components._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_get\_component\_info**](#function-cuvis_acq_cont_get_component_info) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_COMPONENT\_INFO**](cuvis_8h.md#define-cuvis_component_info) \* o\_pCompInfo) <br>_Get components general info._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_get\_next\_measurement**](#function-cuvis_acq_cont_get_next_measurement) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) timeout\_ms) <br>_Get measurement from internal cache._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_get\_session\_info**](#function-cuvis_acq_cont_get_session_info) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_SESSION\_INFO**](cuvis_8h.md#define-cuvis_session_info) \* o\_pSessionInfo) <br>_get the acquisition session\_info_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_get\_state**](#function-cuvis_acq_cont_get_state) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_HARDWARE\_STATE**](cuvis_8h.md#define-cuvis_hardware_state) \* o\_pState) <br>_get the online state of the hardware_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_has\_next\_measurement**](#function-cuvis_acq_cont_has_next_measurement) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pHasNext) <br>_check if any measurements are available in the buffer_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_queue\_size\_set**](#function-cuvis_acq_cont_queue_size_set) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_size) <br>_set the receive queue buffer size_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_ready\_get**](#function-cuvis_acq_cont_ready_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pIsReady) <br>_get initialization state of the acquisition context_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_acq\_cont\_set\_session\_info**](#function-cuvis_acq_cont_set_session_info) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_SESSION\_INFO**](cuvis_8h.md#define-cuvis_session_info) const \* i\_pSessionInfo) <br>_set the acquisition session\_info_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_comp\_available\_pixel\_format\_count\_get**](#function-cuvis_comp_available_pixel_format_count_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCount) <br>_Get components actual pixelformat._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_comp\_available\_pixel\_format\_get**](#function-cuvis_comp_available_pixel_format_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_index, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pPixelFormat) <br>_Get components actual pixelformat._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_comp\_pixel\_format\_get**](#function-cuvis_comp_pixel_format_get) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pPixelFormat) <br>_Get components actual pixelformat._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_comp\_pixel\_format\_set**](#function-cuvis_comp_pixel_format_set) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_pPixelFormat) <br>_Set components pixelformat._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_comp\_pixel\_format\_set\_async**](#function-cuvis_comp_pixel_format_set_async) ([**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acqCont, [**CUVIS\_ASYNC\_CALL\_RESULT**](cuvis_8h.md#define-cuvis_async_call_result) \* o\_pAsyncResult, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_pPixelFormat) <br>_Set components pixelformat._  |




























## Detailed Description


An handle for an acquisition context can be obtained by either loading it with a calibration handle ([**Calibration**](group__cuvis__calib.md)) or by loading it with a [**Session File**](group__cuvis__session.md) handle.


The acquisition context handles the communication with the camera, including setting state variables and capturing images. 


    
## Public Types Documentation




### enum cuvis\_operation\_mode\_t 

_Operation mode of a camera._ 
```
enum cuvis_operation_mode_t {
    OperationMode_Software = 1,
    OperationMode_Internal = 2,
    OperationMode_External = 3,
    OperationMode_Undefined = 4
};
```




<hr>
## Public Functions Documentation




### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_fps,
    double,
    "Frames per second"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_average,
    CUVIS_INT,
    "Number of averages"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_integration_time,
    double,
    "Integration time in milliseconds"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_auto_exp,
    CUVIS_INT,
    "get_auto_exp"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_auto_exp_comp,
    double,
    "get auto exposure compensation"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_operation_mode,
    CUVIS_OPERATION_MODE,
    "enumeration value"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_bandwidth,
    CUVIS_INT,
    "bandwidth in MBit/s"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_queue_size,
    CUVIS_INT,
    "size of measurement queue"
) 
```




<hr>



### function ACQ\_GET\_SINGLE\_VALUE 

```
ACQ_GET_SINGLE_VALUE (
    cuvis_acq_cont_queue_used,
    CUVIS_INT,
    "used part of measurement queue"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_fps,
    double,
    "Frames per second"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_average,
    CUVIS_INT,
    "Number of averages"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_integration_time,
    double,
    "Integration time in milliseconds"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_auto_exp,
    CUVIS_INT,
    "set_auto_exp"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_auto_exp_comp,
    double,
    "set auto exposure compensation"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_operation_mode,
    CUVIS_OPERATION_MODE,
    "enumeration value"
) 
```




<hr>



### function ACQ\_SET\_SINGLE\_VALUE 

```
ACQ_SET_SINGLE_VALUE (
    cuvis_acq_cont_continuous,
    CUVIS_INT,
    " 0=stop
) 
```




<hr>



### function cuvis\_acq\_cont\_capture 

_Capture a measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_capture (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_MESU * o_pMesu,
    CUVIS_INT timeout_ms
) 
```



This function is only available in operation mode "Software". The function executes a software trigger synchronously.




**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pMesu` the handle of the recorded image will be written to this variable 
* `timeout_ms` the timeout in ms. Give 0 to wait for ever. 



**Returns:**

status\_ok if the measurement was recorded. status\_timeout or status\_deferred is returned, if the capture was not completed (yet) 





        

<hr>



### function cuvis\_acq\_cont\_capture\_async 

_Capture a measurement async._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_capture_async (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_ASYNC_CAPTURE_RESULT * o_pAsyncResult
) 
```



This function is only available in operation mode "Software". The function executes a software trigger asynchronously. The recorded measurement can be obtained by the function [**cuvis\_async\_capture\_get**](cuvis_8h.md#function-cuvis_async_capture_get).


If o\_pAsyncResult is set to NULL, the measurement is added to the Acqusition Context's internal queue. Retrieve it with [**cuvis\_acq\_cont\_get\_next\_measurement**](group__cuvis__acq.md#function-cuvis_acq_cont_get_next_measurement) or via the worker (if used) [**cuvis\_worker\_get\_next\_result**](group__cuvis__worker.md#function-cuvis_worker_get_next_result)




**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pAsyncResult` the async capture handle will be written to this variable or NULL 



**Returns:**

status\_ok if the async call could be executed. 





        

<hr>



### function cuvis\_acq\_cont\_copy\_handle 

_Creates an additional acquisition context handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_copy_handle (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_ACQ_CONT * o_pAcqCont
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_acqCont` The handle of the acquisition context to copy 
* `o_pAcqCont` The new handle of the acquisition context. 



**Returns:**

status\_ok if the acquisition context handle could be doubled 





        

<hr>



### function cuvis\_acq\_cont\_create\_from\_calib 

_Load a acquisition context from a given calibration._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_create_from_calib (
    CUVIS_CALIB i_calib,
    CUVIS_ACQ_CONT * o_pAcqCont
) 
```



Load the acquisition context from the calibration. This will load the hardware and initialize it. Do not load multiple instances of the came calibration / camera.




**Parameters:**


* `i_calib` The calibration instance the processing context will be loaded from 
* `o_pAcqCont` The handle of the acquisition context. 



**Returns:**

status\_ok if the acquisition context could be loaded 





        

<hr>



### function cuvis\_acq\_cont\_create\_from\_session\_file 

_Load a acquisition context from a given session\_file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_create_from_session_file (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_INT i_simulate,
    CUVIS_ACQ_CONT * o_pAcqCont
) 
```



The acquisition context from the embedded acquisition context of the session\_info file.




**Parameters:**


* `i_sess` The session\_file the processing context will be loaded from 
* `i_simulate` If True, uses the provided session file for simulated data capturing 
* `o_pAcqCont` The handle of the acquisition context. 



**Returns:**

status\_ok if the acquisition context could be loaded 





        

<hr>



### function cuvis\_acq\_cont\_dead\_pixel\_correction\_available\_get 

_Query whether the dead pixel correction is available._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_dead_pixel_correction_available_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT * o_is_available
) 
```



Returns whether dead pixel correction information is available in the camera's calibration file. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_is_available` the result of the query is written here 



**Returns:**

cuvis\_ok if the query succeeded 





        

<hr>



### function cuvis\_acq\_cont\_dead\_pixel\_correction\_enabled\_get 

_Query whether the dead pixel correction is enabled._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT * o_is_enabled
) 
```



Returns whether the Cuvis built-in dead pixel correction algorithm is currently enabled 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_is_enabled` the result of the query is written here 



**Returns:**

cuvis\_ok if the query succeeded 





        

<hr>



### function cuvis\_acq\_cont\_dead\_pixel\_correction\_enabled\_set 

_Enable or disable the dead pixel correction algorithm._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_dead_pixel_correction_enabled_set (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT o_set_enabled
) 
```



Control whether the Cuvis built-in dead pixel correction algorithm is enabled or disabled. The algorithm applies a custom dead-pixel correction to the sensor image(s). Which pixels to correct and how is determined through the calibration process. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_set_enabled` use 1 to enable, 0 to disable the correction algorithm 



**Returns:**

cuvis\_ok if the operation succeeded. Returns status\_not\_available if the calibration doesn't contain correction information. 





        

<hr>



### function cuvis\_acq\_cont\_free 

_Clear a loaded acquisition context by it's handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_free (
    CUVIS_ACQ_CONT * io_pAcqCont
) 
```



The internal memory is freed.




**Parameters:**


* `io_pAcqCont` The handle of the processing context. The handle number will be invalidated. 



**Returns:**

status\_ok if the acquisition context could be released 





        

<hr>



### function cuvis\_acq\_cont\_get\_component\_count 

_Get the number of components._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_get_component_count (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT * o_pCount
) 
```



The acquisition hardware is build from one or more components. Get the component count. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pCount` the number of components is written here 



**Returns:**

cuvis\_ok if the number of components could be set 





        

<hr>



### function cuvis\_acq\_cont\_get\_component\_info 

_Get components general info._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_get_component_info (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_id,
    CUVIS_COMPONENT_INFO * o_pCompInfo
) 
```



Return general component information about a component build into the acquisition hardware. This helps identifying the correct component for settings specific component settings (e.g. gain)




**Parameters:**


* `i_acqCont` the acquisition context 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `o_pCompInfo` the component info to be filled 



**Returns:**

cuvis\_ok if the info fields could be filled. 





        

<hr>



### function cuvis\_acq\_cont\_get\_next\_measurement 

_Get measurement from internal cache._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_get_next_measurement (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_MESU * o_pMesu,
    CUVIS_INT timeout_ms
) 
```



This function is only available in operation mode "Internal" or "External". The function obtains the image from the internal memory, if available.




**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pMesu` the handle of the recorded image will be written to this variable. 
* `timeout_ms` the timeout in ms. Give 0 to wait for ever. 



**Returns:**

status\_ok if the measurement was recorded. Returns status\_no\_measurement if no measurement was made available during the timeout time. If any error occurred status\_error is returned. 





        

<hr>



### function cuvis\_acq\_cont\_get\_session\_info 

_get the acquisition session\_info_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_get_session_info (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_SESSION_INFO * o_pSessionInfo
) 
```



Get the acquisition session\_info settings. Also use this function to get the current sequence number. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pSessionInfo` the state will be written here 



**Returns:**

status\_ok, if no internal error occurred. 





        

<hr>



### function cuvis\_acq\_cont\_get\_state 

_get the online state of the hardware_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_get_state (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_HARDWARE_STATE * o_pState
) 
```



Hardware can be used, when at least it's required components are online. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pState` the state will be written here 



**Returns:**

status\_ok, if no internal error occurred. 





        

<hr>



### function cuvis\_acq\_cont\_has\_next\_measurement 

_check if any measurements are available in the buffer_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_has_next_measurement (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT * o_pHasNext
) 
```



This function is only available in operation mode "Internal" or "External".




**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pHasNext` value of 0 is written, if no measurements are available. value &gt; 0, if a measurement is available. 



**Returns:**

status\_ok if no error occurred. If any error occurred status\_error is returned. 





        

<hr>



### function cuvis\_acq\_cont\_queue\_size\_set 

_set the receive queue buffer size_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_queue_size_set (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_size
) 
```



Set the amounts of measurements that will be stored internally, ready for retrieval. Default=100. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `i_size` the new queue size 



**Returns:**

status\_ok if the new queue size could be set. 





        

<hr>



### function cuvis\_acq\_cont\_ready\_get 

_get initialization state of the acquisition context_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_ready_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT * o_pIsReady
) 
```





**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pIsReady` whether the acquisition context has completed all initialization tasks 



**Returns:**

status\_ok, if no internal error occurred. 





        

<hr>



### function cuvis\_acq\_cont\_set\_session\_info 

_set the acquisition session\_info_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_acq_cont_set_session_info (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_SESSION_INFO const * i_pSessionInfo
) 
```



Set the acquisition session\_info settings. 

**Parameters:**


* `i_acqCont` the acquisition context 
* `i_pSessionInfo` the session\_info details to be set 



**Returns:**

status\_ok, if no internal error occurred. 





        

<hr>



### function cuvis\_comp\_available\_pixel\_format\_count\_get 

_Get components actual pixelformat._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_comp_available_pixel_format_count_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_id,
    CUVIS_INT * o_pCount
) 
```



Return the amount of components available pixelformats




**Parameters:**


* `i_acqCont` the acquisition context 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `o_pCount` amount of available pixel formats 



**Returns:**

cuvis\_ok if the amount was returned. 





        

<hr>



### function cuvis\_comp\_available\_pixel\_format\_get 

_Get components actual pixelformat._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_comp_available_pixel_format_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_id,
    CUVIS_INT i_index,
    CUVIS_CHAR * o_pPixelFormat
) 
```



Return indexed components available pixelformat




**Parameters:**


* `i_acqCont` the acquisition context 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `i_index` index of the requested available pixelformat 
* `o_pPixelFormat` the components available pixelformat 



**Returns:**

cuvis\_ok if the pixelformat was returned. 





        

<hr>



### function cuvis\_comp\_pixel\_format\_get 

_Get components actual pixelformat._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_comp_pixel_format_get (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_id,
    CUVIS_CHAR * o_pPixelFormat
) 
```



Return actual components pixelformat




**Parameters:**


* `i_acqCont` the acquisition context 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `o_pPixelFormat` the components pixelformat 



**Returns:**

cuvis\_ok if the pixelformat was returned. 





        

<hr>



### function cuvis\_comp\_pixel\_format\_set 

_Set components pixelformat._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_comp_pixel_format_set (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_INT i_id,
    CUVIS_CHAR const * i_pPixelFormat
) 
```



Set components pixelformat




**Parameters:**


* `i_acqCont` the acquisition context 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `i_pPixelFormat` the components pixelformat 



**Returns:**

cuvis\_ok if the pixelformat was set. 





        

<hr>



### function cuvis\_comp\_pixel\_format\_set\_async 

_Set components pixelformat._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_comp_pixel_format_set_async (
    CUVIS_ACQ_CONT i_acqCont,
    CUVIS_ASYNC_CALL_RESULT * o_pAsyncResult,
    CUVIS_INT i_id,
    CUVIS_CHAR const * i_pPixelFormat
) 
```



Set components pixelformat (asynchronous)




**Parameters:**


* `i_acqCont` the acquisition context 
* `o_pAsyncResult` The Async object that will contain the result of the operation 
* `i_id` the device id (value between 0 and below [**cuvis\_acq\_cont\_get\_component\_count**](group__cuvis__acq.md#function-cuvis_acq_cont_get_component_count)) 
* `i_pPixelFormat` the components pixelformat 



**Returns:**

cuvis\_ok if the pixelformat was set. 





        

<hr>

------------------------------


