

# Struct cuvis\_worker\_settings\_t



[**ClassList**](annotated.md) **>** [**cuvis\_worker\_settings\_t**](structcuvis__worker__settings__t.md)



[More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**can\_drop\_results**](#variable-can_drop_results)  <br>_Wether the worker is allowed to drop processing results if its output queue is full._  |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**can\_skip\_measurements**](#variable-can_skip_measurements)  <br>_Wether the worker is allowed to reject measurements from the acquisition context, if its queues are full._  |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**can\_skip\_supplementary\_steps**](#variable-can_skip_supplementary_steps)  <br>_Wether the worker is allowed to skip supplementary processing steps, if its queues are full._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**input\_queue\_size**](#variable-input_queue_size)  <br>_Size of the input queue for measurements and session files._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**mandatory\_queue\_size**](#variable-mandatory_queue_size)  <br>_Number of threads working on mandatory processing steps._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**output\_queue\_size**](#variable-output_queue_size)  <br>_Size of the workers result queue._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**supplementary\_queue\_size**](#variable-supplementary_queue_size)  <br>_Number of threads working on supplementary processing steps._  |












































## Detailed Description


settings for the worker 


    
## Public Attributes Documentation




### variable can\_drop\_results 

_Wether the worker is allowed to drop processing results if its output queue is full._ 
```C++
CUVIS_INT cuvis_worker_settings_t::can_drop_results;
```




<hr>



### variable can\_skip\_measurements 

_Wether the worker is allowed to reject measurements from the acquisition context, if its queues are full._ 
```C++
CUVIS_INT cuvis_worker_settings_t::can_skip_measurements;
```



If set to true (1), the worker will skip processing measurements it pulls from the acqusition context, when its mandatory queue is full. If set to false (0), the worker will wait until a processing slot in its mandatory queue is available, before pulling a new measurement from the acquisition context. This setting DOES NOT apply to measurements and session files given to the worker via the "cuvis\_worker\_ingest\_xyz" functions. 


        

<hr>



### variable can\_skip\_supplementary\_steps 

_Wether the worker is allowed to skip supplementary processing steps, if its queues are full._ 
```C++
CUVIS_INT cuvis_worker_settings_t::can_skip_supplementary_steps;
```



If set to true (1), the worker will skip supplementary processing steps, when its supplementary queue is full. If set to false (0), the worker will wait until a processing slot in its supplementary queue is available, before starting processing on a new measurement. This setting DOES applies to measurements and session files given to the worker via the "cuvis\_worker\_ingest\_xyz" functions. 


        

<hr>



### variable input\_queue\_size 

_Size of the input queue for measurements and session files._ 
```C++
CUVIS_SIZE cuvis_worker_settings_t::input_queue_size;
```



The worker has an input queue that accepts measurements and entire session files. To limit the memory usage, the queue is bounded by this value 


        

<hr>



### variable mandatory\_queue\_size 

_Number of threads working on mandatory processing steps._ 
```C++
CUVIS_SIZE cuvis_worker_settings_t::mandatory_queue_size;
```



Set the number of processing slots / threads / queue size for mandatory processing steps in the worker Mandatory steps always include exporting the measurement, if an exporter is set in the worker. If the measurement needs to be processed before it can be exported, the processing is also a mandatory step. 


        

<hr>



### variable output\_queue\_size 

_Size of the workers result queue._ 
```C++
CUVIS_SIZE cuvis_worker_settings_t::output_queue_size;
```



Should be at least as big as "mandatory\_queue\_size" and "supplementary\_queue\_size" together 


        

<hr>



### variable supplementary\_queue\_size 

_Number of threads working on supplementary processing steps._ 
```C++
CUVIS_SIZE cuvis_worker_settings_t::supplementary_queue_size;
```



Set the number of processing slots / threads / queue size for supplementary processing steps in the worker Supplementary steps always include generating a view of the measurement, if a viewer is set in the worker. If no exporter is set, all steps are supplementary. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

