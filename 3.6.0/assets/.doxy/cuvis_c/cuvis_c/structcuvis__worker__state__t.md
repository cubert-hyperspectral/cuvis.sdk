

# Struct cuvis\_worker\_state\_t



[**ClassList**](annotated.md) **>** [**cuvis\_worker\_state\_t**](structcuvis__worker__state__t.md)



_Collection of worker stats._ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**framesInQueue**](#variable-framesinqueue)  <br>_Total number of frames currently in the input queue accounting for sesssion file size._  |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**hasAcquisitionContext**](#variable-hasacquisitioncontext)  <br>_Wether the worker has an acquisition context set._  |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**isProcessing**](#variable-isprocessing)  <br>_Wether the worker is currently allowed to process measurements; same attribute as queried by cuvis\_worker\_is\_processing._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**measurementsBeingProcessed**](#variable-measurementsbeingprocessed)  <br>_Number of measurments the worker is currently processing._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**measurementsInQueue**](#variable-measurementsinqueue)  <br>_Measurements currently in the input queue._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**resultsInQueue**](#variable-resultsinqueue)  <br>_Number of results currently in the result queue._  |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**sessionFilesInQueue**](#variable-sessionfilesinqueue)  <br>_Session files currently in the input queue._  |












































## Public Attributes Documentation




### variable framesInQueue 

_Total number of frames currently in the input queue accounting for sesssion file size._ 
```C++
CUVIS_SIZE cuvis_worker_state_t::framesInQueue;
```




<hr>



### variable hasAcquisitionContext 

_Wether the worker has an acquisition context set._ 
```C++
CUVIS_INT cuvis_worker_state_t::hasAcquisitionContext;
```




<hr>



### variable isProcessing 

_Wether the worker is currently allowed to process measurements; same attribute as queried by cuvis\_worker\_is\_processing._ 
```C++
CUVIS_INT cuvis_worker_state_t::isProcessing;
```




<hr>



### variable measurementsBeingProcessed 

_Number of measurments the worker is currently processing._ 
```C++
CUVIS_SIZE cuvis_worker_state_t::measurementsBeingProcessed;
```




<hr>



### variable measurementsInQueue 

_Measurements currently in the input queue._ 
```C++
CUVIS_SIZE cuvis_worker_state_t::measurementsInQueue;
```




<hr>



### variable resultsInQueue 

_Number of results currently in the result queue._ 
```C++
CUVIS_SIZE cuvis_worker_state_t::resultsInQueue;
```




<hr>



### variable sessionFilesInQueue 

_Session files currently in the input queue._ 
```C++
CUVIS_SIZE cuvis_worker_state_t::sessionFilesInQueue;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

