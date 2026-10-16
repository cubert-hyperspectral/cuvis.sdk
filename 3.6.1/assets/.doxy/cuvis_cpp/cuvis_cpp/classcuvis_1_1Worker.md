

# Class cuvis::Worker



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**Worker**](classcuvis_1_1Worker.md)





* `#include <cuvis.hpp>`















## Classes

| Type | Name |
| ---: | :--- |
| struct | [**worker\_return\_t**](structcuvis_1_1Worker_1_1worker__return__t.md) <br> |
| struct | [**worker\_state\_t**](structcuvis_1_1Worker_1_1worker__state__t.md) <br> |


## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::function&lt; [**void**](structcuvis_1_1image__t.md)([**worker\_return\_t**](structcuvis_1_1Worker_1_1worker__return__t.md))&gt; | [**worker\_callback\_t**](#typedef-worker_callback_t)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Worker**](#function-worker) ([**WorkerArgs**](structcuvis_1_1WorkerArgs.md) [**const**](structcuvis_1_1image__t.md) & args) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**drop\_all\_queued**](#function-drop_all_queued) () <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**get\_can\_drop\_results**](#function-get_can_drop_results) () <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**get\_can\_skip\_measurements**](#function-get_can_skip_measurements) () <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**get\_can\_skip\_supplementary**](#function-get_can_skip_supplementary) () <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_input\_queue\_limit**](#function-get_input_queue_limit) () const<br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_mandatory\_queue\_limit**](#function-get_mandatory_queue_limit) () const<br> |
|  [**worker\_return\_t**](structcuvis_1_1Worker_1_1worker__return__t.md) | [**get\_next\_result**](#function-get_next_result) (std::chrono::milliseconds timeout) const<br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_output\_queue\_limit**](#function-get_output_queue_limit) () const<br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_queue\_used**](#function-get_queue_used) () const<br> |
|  [**worker\_state\_t**](structcuvis_1_1Worker_1_1worker__state__t.md) | [**get\_state**](#function-get_state) () const<br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_supplementary\_queue\_limit**](#function-get_supplementary_queue_limit) () const<br> |
|  [**int32\_t**](structcuvis_1_1image__t.md) | [**get\_threads\_busy**](#function-get_threads_busy) () const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**has\_next\_result**](#function-has_next_result) () const<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**ingest\_measurement**](#function-ingest_measurement) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & measurement) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**ingest\_session\_file**](#function-ingest_session_file) ([**SessionFile**](classcuvis_1_1SessionFile.md) [**const**](structcuvis_1_1image__t.md) & session, std::string frame\_selection) <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**is\_processing**](#function-is_processing) () const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**is\_processing\_mandatory**](#function-is_processing_mandatory) () const<br> |
|  [**double**](structcuvis_1_1image__t.md) | [**query\_session\_progress**](#function-query_session_progress) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**register\_worker\_callback**](#function-register_worker_callback) ([**worker\_callback\_t**](classcuvis_1_1Worker.md#typedef-worker_callback_t) callback, [**unsigned**](structcuvis_1_1image__t.md) concurrency=1, [**size\_t**](structcuvis_1_1image__t.md) measurement\_timeout\_ms=1000) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**reset\_worker\_callback**](#function-reset_worker_callback) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_acq\_cont**](#function-set_acq_cont) ([**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md) [**const**](structcuvis_1_1image__t.md) \* acqCont) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_exporter**](#function-set_exporter) ([**Exporter**](classcuvis_1_1Exporter.md) [**const**](structcuvis_1_1image__t.md) \* exporter) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_proc\_cont**](#function-set_proc_cont) ([**ProcessingContext**](classcuvis_1_1ProcessingContext.md) [**const**](structcuvis_1_1image__t.md) \* procCont) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_viewer**](#function-set_viewer) ([**Viewer**](classcuvis_1_1Viewer.md) [**const**](structcuvis_1_1image__t.md) \* viewer) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**start\_processing**](#function-start_processing) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**stop\_processing**](#function-stop_processing) () <br> |




























## Public Types Documentation




### typedef worker\_callback\_t 

```C++
using cuvis::Worker::worker_callback_t =  std::function<void(worker_return_t)>;
```




<hr>
## Public Functions Documentation




### function Worker 

```C++
cuvis::Worker::Worker (
    WorkerArgs  const & args
) 
```




<hr>



### function drop\_all\_queued 

```C++
void cuvis::Worker::drop_all_queued () 
```




<hr>



### function get\_can\_drop\_results 

```C++
bool cuvis::Worker::get_can_drop_results () 
```




<hr>



### function get\_can\_skip\_measurements 

```C++
bool cuvis::Worker::get_can_skip_measurements () 
```




<hr>



### function get\_can\_skip\_supplementary 

```C++
bool cuvis::Worker::get_can_skip_supplementary () 
```




<hr>



### function get\_input\_queue\_limit 

```C++
size_t cuvis::Worker::get_input_queue_limit () const
```




<hr>



### function get\_mandatory\_queue\_limit 

```C++
size_t cuvis::Worker::get_mandatory_queue_limit () const
```




<hr>



### function get\_next\_result 

```C++
worker_return_t cuvis::Worker::get_next_result (
    std::chrono::milliseconds timeout
) const
```




<hr>



### function get\_output\_queue\_limit 

```C++
size_t cuvis::Worker::get_output_queue_limit () const
```




<hr>



### function get\_queue\_used 

```C++
size_t cuvis::Worker::get_queue_used () const
```




<hr>



### function get\_state 

```C++
worker_state_t cuvis::Worker::get_state () const
```




<hr>



### function get\_supplementary\_queue\_limit 

```C++
size_t cuvis::Worker::get_supplementary_queue_limit () const
```




<hr>



### function get\_threads\_busy 

```C++
int32_t cuvis::Worker::get_threads_busy () const
```




<hr>



### function has\_next\_result 

```C++
bool cuvis::Worker::has_next_result () const
```




<hr>



### function ingest\_measurement 

```C++
void cuvis::Worker::ingest_measurement (
    Measurement  const & measurement
) 
```




<hr>



### function ingest\_session\_file 

```C++
void cuvis::Worker::ingest_session_file (
    SessionFile  const & session,
    std::string frame_selection
) 
```




<hr>



### function is\_processing 

```C++
bool cuvis::Worker::is_processing () const
```




<hr>



### function is\_processing\_mandatory 

```C++
bool cuvis::Worker::is_processing_mandatory () const
```




<hr>



### function query\_session\_progress 

```C++
double cuvis::Worker::query_session_progress () 
```




<hr>



### function register\_worker\_callback 

```C++
void cuvis::Worker::register_worker_callback (
    worker_callback_t callback,
    unsigned concurrency=1,
    size_t measurement_timeout_ms=1000
) 
```




<hr>



### function reset\_worker\_callback 

```C++
void cuvis::Worker::reset_worker_callback () 
```




<hr>



### function set\_acq\_cont 

```C++
void cuvis::Worker::set_acq_cont (
    AcquisitionContext  const * acqCont
) 
```




<hr>



### function set\_exporter 

```C++
void cuvis::Worker::set_exporter (
    Exporter  const * exporter
) 
```




<hr>



### function set\_proc\_cont 

```C++
void cuvis::Worker::set_proc_cont (
    ProcessingContext  const * procCont
) 
```




<hr>



### function set\_viewer 

```C++
void cuvis::Worker::set_viewer (
    Viewer  const * viewer
) 
```




<hr>



### function start\_processing 

```C++
void cuvis::Worker::start_processing () 
```




<hr>



### function stop\_processing 

```C++
void cuvis::Worker::stop_processing () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

