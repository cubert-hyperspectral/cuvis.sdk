

# Group cuvis\_async



[**Modules**](modules.md) **>** [**cuvis\_async**](group__cuvis__async.md)



_The Async Capabilites of the SDK._ [More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_call\_free**](#function-cuvis_async_call_free) ([**CUVIS\_ASYNC\_CALL\_RESULT**](cuvis_8h.md#define-cuvis_async_call_result) \* io\_pAsyncResult) <br>_Free an async call result without calling it._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_call\_get**](#function-cuvis_async_call_get) ([**CUVIS\_ASYNC\_CALL\_RESULT**](cuvis_8h.md#define-cuvis_async_call_result) \* io\_pAsyncResult, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) timeout\_ms) <br>_get the result of a async call._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_call\_status**](#function-cuvis_async_call_status) ([**CUVIS\_ASYNC\_CALL\_RESULT**](cuvis_8h.md#define-cuvis_async_call_result) i\_pAsyncResult, [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) \* io\_pStatusResult) <br>_checks the status of the async call object and returns it_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_capture\_free**](#function-cuvis_async_capture_free) ([**CUVIS\_ASYNC\_CAPTURE\_RESULT**](cuvis_8h.md#define-cuvis_async_capture_result) \* io\_pAsyncResult) <br>_Free an async measurement result without calling it._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_async\_capture\_status**](#function-cuvis_async_capture_status) ([**CUVIS\_ASYNC\_CAPTURE\_RESULT**](cuvis_8h.md#define-cuvis_async_capture_result) i\_pAsyncResult, [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) \* io\_pStatusResult) <br>_checks the status of the async capture object and returns it_  |




























## Detailed Description


The functions of the sdk with depend on either setting a state of the camera, or awaiting image data from the camera have async variations of themself. This includes most of the setter of the acqusition context as well as [**cuvis\_acq\_cont\_capture**](group__cuvis__acq.md#function-cuvis_acq_cont_capture).


The non async version of these functions execute the respective task and block as long as it takes. The async counterpart function call completes immediately and returns the handle to an aync result or async [**Measurement**](group__cuvis__mesu.md).


Theses async handles can then be used to check the state of the respective function call. 


    
## Public Functions Documentation




### function cuvis\_async\_call\_free 

_Free an async call result without calling it._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_call_free (
    CUVIS_ASYNC_CALL_RESULT * io_pAsyncResult
) 
```




<hr>



### function cuvis\_async\_call\_get 

_get the result of a async call._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_call_get (
    CUVIS_ASYNC_CALL_RESULT * io_pAsyncResult,
    CUVIS_INT timeout_ms
) 
```



Get the return code (and error message, if applicable) of an async function, that has been called. If result is not status\_ok use the [**cuvis\_get\_last\_error\_msg**](group__cuvis__returns.md#function-cuvis_get_last_error_msg) function to get details.


If the timeout is used (value above 0ms), status\_timeout or status\_deferred will be returned, if the function is not yet finished. In that case, the asyncResult handle is still valid and can be used again. If the result is status\_ok the function has finished. For both status\_ok and status\_error, the handle is now invalid.


If the result is status\_overwritten the function's call was overwritten by another (similar) call. The actual value set by this async function was not used, but the one of the other call. On this result, the handle is now invalid.




**Parameters:**


* `io_pAsyncResult` the async handle obtained by calling a async function. If the call finished, the handle will be invalidated 
* `timeout_ms` the timeout in ms. Give 0 to wait for ever. 



**Returns:**

status\_ok if the async function finished successfully. status\_timeout or status\_deferred will be returned, if the function is not yet finished. If the call failed, because it was overwritten it this function will return status\_overwritten. If it failed for other reasons, the this function returns status\_error. 





        

<hr>



### function cuvis\_async\_call\_status 

_checks the status of the async call object and returns it_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_call_status (
    CUVIS_ASYNC_CALL_RESULT i_pAsyncResult,
    CUVIS_STATUS * io_pStatusResult
) 
```




<hr>



### function cuvis\_async\_capture\_free 

_Free an async measurement result without calling it._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_capture_free (
    CUVIS_ASYNC_CAPTURE_RESULT * io_pAsyncResult
) 
```




<hr>



### function cuvis\_async\_capture\_status 

_checks the status of the async capture object and returns it_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_async_capture_status (
    CUVIS_ASYNC_CAPTURE_RESULT i_pAsyncResult,
    CUVIS_STATUS * io_pStatusResult
) 
```




<hr>

------------------------------


