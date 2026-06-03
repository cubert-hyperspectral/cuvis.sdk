

# Group cuvis\_worker



[**Modules**](modules.md) **>** [**cuvis\_worker**](group__cuvis__worker.md)










































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_create**](#function-cuvis_worker_create) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) \* o\_pWorker, [**CUVIS\_WORKER\_SETTINGS**](cuvis_8h.md#define-cuvis_worker_settings) worker\_settings) <br>_Create a Worker._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_drop\_all\_queued**](#function-cuvis_worker_drop_all_queued) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker) <br>_Command the worker to discard all measurements it is currently processing and empty the result queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_free**](#function-cuvis_worker_free) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) \* io\_pWorker) <br>_release a worker_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_can\_drop\_results**](#function-cuvis_worker_get_can_drop_results) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCanDrop) <br>_Query current drop behavior._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_can\_skip\_measurements**](#function-cuvis_worker_get_can_skip_measurements) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCanSkip) <br>_Query current skip behavior._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_can\_skip\_supplementary**](#function-cuvis_worker_get_can_skip_supplementary) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCanSkip) <br>_Query current skip behavior._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_input\_queue\_limit**](#function-cuvis_worker_get_input_queue_limit) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) \* o\_pInputQueueLimit) <br>_Query the maximum queue size of the input queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_mandatory\_queue\_limit**](#function-cuvis_worker_get_mandatory_queue_limit) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) \* o\_pMandatoryLimit) <br>_Query the maximum queue size of the mandatory queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_next\_result**](#function-cuvis_worker_get_next_result) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu, [**CUVIS\_VIEW**](cuvis_8h.md#define-cuvis_view) \* o\_pView, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) i\_Timeout\_ms) <br>_Get the next result in order._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_output\_queue\_limit**](#function-cuvis_worker_get_output_queue_limit) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) \* o\_pOutputQueueLimit) <br>_Query the maximum queue size of the output queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_queue\_used**](#function-cuvis_worker_get_queue_used) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pQueueUsed) <br>_Query the number of items currently in the result queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_state**](#function-cuvis_worker_get_state) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_WORKER\_STATE**](cuvis_8h.md#define-cuvis_worker_state) \* o\_pWorkerState) <br>_Query multiple attributes of the worker at once, see_ [_**cuvis\_worker\_state\_t**_](structcuvis__worker__state__t.md) _._ |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_supplementary\_queue\_limit**](#function-cuvis_worker_get_supplementary_queue_limit) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) \* o\_pSupplementaryLimit) <br>_Query the maximum queue size of the supplementary queue._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_get\_threads\_busy**](#function-cuvis_worker_get_threads_busy) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pThreadsBusy) <br>_Query how many measurements the worker is processing right now._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_has\_next\_result**](#function-cuvis_worker_has_next_result) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pHasNext) <br>_Check, if a new worker result is available._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_ingest\_mesu**](#function-cuvis_worker_ingest_mesu) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu) <br>_Push a mesurement into the worker to process. Worker must have neither a session file nor an acquisition context._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_ingest\_session\_file**](#function-cuvis_worker_ingest_session_file) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_session\_file, const char \* i\_frame\_selection) <br>_set a session file for the worker to process (read access only). Give CUVIS\_HANDLE\_NULL to clear. Set parameter SkipDroppedFrames to 1 to skip any dropped frames contained in the session - 0 will insert empty frames._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_is\_processing**](#function-cuvis_worker_is_processing) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pIsProcessing) <br>_Query wether the worker is currently allowed to process measurements - wether it is running._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_is\_processing\_mandatory**](#function-cuvis_worker_is_processing_mandatory) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pProcessingMandatory) <br>_Query wether the processing step is currently mandatory The result is only valid, if a processing context is assigned to the worker. If no processing context is assigned, will always return 0 (false)_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_query\_session\_progress**](#function-cuvis_worker_query_session_progress) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, double \* o\_frames\_read) <br>_Get the current percentage of frames done of the current session. -1.0 if no session file is currently being processed._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_set\_acq\_cont**](#function-cuvis_worker_set_acq_cont) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_ACQ\_CONT**](cuvis_8h.md#define-cuvis_acq_cont) i\_acq\_cont) <br>_set the acquistion context for the worker. Give CUVIS\_HANDLE\_NULL to clear_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_set\_exporter**](#function-cuvis_worker_set_exporter) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_EXPORTER**](cuvis_8h.md#define-cuvis_exporter) i\_exporter) <br>_set the exporter for the worker. Give CUVIS\_HANDLE\_NULL to clear_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_set\_proc\_cont**](#function-cuvis_worker_set_proc_cont) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_proc\_cont) <br>_set the processing context for the worker. Give CUVIS\_HANDLE\_NULL to clear_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_set\_viewer**](#function-cuvis_worker_set_viewer) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker, [**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) i\_viewer) <br>_set the viewer for the worker. Give CUVIS\_HANDLE\_NULL to clear_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_start**](#function-cuvis_worker_start) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker) <br>_Start the worker._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_worker\_stop**](#function-cuvis_worker_stop) ([**CUVIS\_WORKER**](cuvis_8h.md#define-cuvis_worker) i\_worker) <br>_Pause the worker._  |




























## Public Functions Documentation




### function cuvis\_worker\_create 

_Create a Worker._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_create (
    CUVIS_WORKER * o_pWorker,
    CUVIS_WORKER_SETTINGS worker_settings
) 
```



The encapsulates the functions of the Acquisiton Context, Processing Context, Exporter, and Viewer into a single container and manages the communications between these. It also enables multi-threaded operation 

**Note:**

The set functions need to be called in order for the worker to be enabled.




**Parameters:**


* `o_pWorker` The worker handle to be created 
* `worker_settings` The worker configuration 




        

<hr>



### function cuvis\_worker\_drop\_all\_queued 

_Command the worker to discard all measurements it is currently processing and empty the result queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_drop_all_queued (
    CUVIS_WORKER i_worker
) 
```




<hr>



### function cuvis\_worker\_free 

_release a worker_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_free (
    CUVIS_WORKER * io_pWorker
) 
```




<hr>



### function cuvis\_worker\_get\_can\_drop\_results 

_Query current drop behavior._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_can_drop_results (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pCanDrop
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pCanDrop` If 1, the worker is allowed to drop results when the output queue is full 




        

<hr>



### function cuvis\_worker\_get\_can\_skip\_measurements 

_Query current skip behavior._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_can_skip_measurements (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pCanSkip
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pCanSkip` If 1, the worker is allowed to entirely skip processing measurements, if the mandatory queue is full 




        

<hr>



### function cuvis\_worker\_get\_can\_skip\_supplementary 

_Query current skip behavior._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_can_skip_supplementary (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pCanSkip
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pCanSkip` If 1, the worker is allowed to skip supplementary processing of measurements, if the supplementary queue is full 




        

<hr>



### function cuvis\_worker\_get\_input\_queue\_limit 

_Query the maximum queue size of the input queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_input_queue_limit (
    CUVIS_WORKER i_worker,
    CUVIS_SIZE * o_pInputQueueLimit
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pInputQueueLimit` The maximum size of the input queue 




        

<hr>



### function cuvis\_worker\_get\_mandatory\_queue\_limit 

_Query the maximum queue size of the mandatory queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_mandatory_queue_limit (
    CUVIS_WORKER i_worker,
    CUVIS_SIZE * o_pMandatoryLimit
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pMandatoryLimit` The maximum size of the mandatory queue. This is also the maximum number of measurements processed simultaneously 




        

<hr>



### function cuvis\_worker\_get\_next\_result 

_Get the next result in order._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_next_result (
    CUVIS_WORKER i_worker,
    CUVIS_MESU * o_pMesu,
    CUVIS_VIEW * o_pView,
    CUVIS_SIZE i_Timeout_ms
) 
```



The measurement will be readyly recorded, processed (if set), stored (if set) and have a view (if set).




**Parameters:**


* `i_worker` The worker handle 
* `o_pMesu` The recorded measurement or NULL if recording failed 
* `o_pView` The view, if calculated sucessfully, else NULL 
* `i_Timeout_ms` The number of milliseconds to wait for a result. -1 to wait indefinitely 



**Returns:**

status\_ok or on error: status\_error, status\_not\_processed, status\_not\_stored, or status\_no\_view, or status\_not\_available 





        

<hr>



### function cuvis\_worker\_get\_output\_queue\_limit 

_Query the maximum queue size of the output queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_output_queue_limit (
    CUVIS_WORKER i_worker,
    CUVIS_SIZE * o_pOutputQueueLimit
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pOutputQueueLimit` The maximum size of the output queue 




        

<hr>



### function cuvis\_worker\_get\_queue\_used 

_Query the number of items currently in the result queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_queue_used (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pQueueUsed
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pQueueUsed` The number of results currently in the output queue 




        

<hr>



### function cuvis\_worker\_get\_state 

_Query multiple attributes of the worker at once, see_ [_**cuvis\_worker\_state\_t**_](structcuvis__worker__state__t.md) _._
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_state (
    CUVIS_WORKER i_worker,
    CUVIS_WORKER_STATE * o_pWorkerState
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pWorkerState` Collection of worker stats 




        

<hr>



### function cuvis\_worker\_get\_supplementary\_queue\_limit 

_Query the maximum queue size of the supplementary queue._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_supplementary_queue_limit (
    CUVIS_WORKER i_worker,
    CUVIS_SIZE * o_pSupplementaryLimit
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pSupplementaryLimit` The maximum size of the supplementary queue. This is also the maximum number of measurements processed simultaneously 




        

<hr>



### function cuvis\_worker\_get\_threads\_busy 

_Query how many measurements the worker is processing right now._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_get_threads_busy (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pThreadsBusy
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pThreadsBusy` The number of measurements currently being processed 




        

<hr>



### function cuvis\_worker\_has\_next\_result 

_Check, if a new worker result is available._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_has_next_result (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pHasNext
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pHasNext` 1 if a result is available now, else 0 




        

<hr>



### function cuvis\_worker\_ingest\_mesu 

_Push a mesurement into the worker to process. Worker must have neither a session file nor an acquisition context._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_ingest_mesu (
    CUVIS_WORKER i_worker,
    CUVIS_MESU i_mesu
) 
```




<hr>



### function cuvis\_worker\_ingest\_session\_file 

_set a session file for the worker to process (read access only). Give CUVIS\_HANDLE\_NULL to clear. Set parameter SkipDroppedFrames to 1 to skip any dropped frames contained in the session - 0 will insert empty frames._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_ingest_session_file (
    CUVIS_WORKER i_worker,
    CUVIS_SESSION_FILE i_session_file,
    const char * i_frame_selection
) 
```




<hr>



### function cuvis\_worker\_is\_processing 

_Query wether the worker is currently allowed to process measurements - wether it is running._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_is_processing (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pIsProcessing
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pIsProcessing` If 1, the worker is allowed process measurements. This does not mean, that it is currently working on a measurement - see cuvis\_worker\_get\_threads\_busy 




        

<hr>



### function cuvis\_worker\_is\_processing\_mandatory 

_Query wether the processing step is currently mandatory The result is only valid, if a processing context is assigned to the worker. If no processing context is assigned, will always return 0 (false)_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_is_processing_mandatory (
    CUVIS_WORKER i_worker,
    CUVIS_INT * o_pProcessingMandatory
) 
```





**Parameters:**


* `i_worker` The worker handle 
* `o_pProcessingMandatory` If 1, the appying the processing context to the measurement is part of the mandatory processing steps 




        

<hr>



### function cuvis\_worker\_query\_session\_progress 

_Get the current percentage of frames done of the current session. -1.0 if no session file is currently being processed._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_query_session_progress (
    CUVIS_WORKER i_worker,
    double * o_frames_read
) 
```




<hr>



### function cuvis\_worker\_set\_acq\_cont 

_set the acquistion context for the worker. Give CUVIS\_HANDLE\_NULL to clear_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_set_acq_cont (
    CUVIS_WORKER i_worker,
    CUVIS_ACQ_CONT i_acq_cont
) 
```




<hr>



### function cuvis\_worker\_set\_exporter 

_set the exporter for the worker. Give CUVIS\_HANDLE\_NULL to clear_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_set_exporter (
    CUVIS_WORKER i_worker,
    CUVIS_EXPORTER i_exporter
) 
```




<hr>



### function cuvis\_worker\_set\_proc\_cont 

_set the processing context for the worker. Give CUVIS\_HANDLE\_NULL to clear_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_set_proc_cont (
    CUVIS_WORKER i_worker,
    CUVIS_PROC_CONT i_proc_cont
) 
```




<hr>



### function cuvis\_worker\_set\_viewer 

_set the viewer for the worker. Give CUVIS\_HANDLE\_NULL to clear_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_set_viewer (
    CUVIS_WORKER i_worker,
    CUVIS_VIEWER i_viewer
) 
```




<hr>



### function cuvis\_worker\_start 

_Start the worker._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_start (
    CUVIS_WORKER i_worker
) 
```




<hr>



### function cuvis\_worker\_stop 

_Pause the worker._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_worker_stop (
    CUVIS_WORKER i_worker
) 
```




<hr>

------------------------------


