

# Struct cuvis\_proc\_args\_t



[**ClassList**](annotated.md) **>** [**cuvis\_proc\_args\_t**](structcuvis__proc__args__t.md)



_processing arguments_ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**allow\_recalib**](#variable-allow_recalib)  <br> |
|  [**CUVIS\_PROCESSING\_MODE**](cuvis_8h.md#define-cuvis_processing_mode) | [**processing\_mode**](#variable-processing_mode)  <br> |












































## Public Attributes Documentation




### variable allow\_recalib 

```C++
CUVIS_INT cuvis_proc_args_t::allow_recalib;
```



allow to use different calibration (expert option)


This options allows to process raw data with a different calibration. this is, however, limited to the same hardware.


If the hardware was mechanically changed, results may be poor or not usable at all. Unless the accuracy of the result can be verified, this option is not recommended. 


        

<hr>



### variable processing\_mode 

```C++
CUVIS_PROCESSING_MODE cuvis_proc_args_t::processing_mode;
```



the processing mode to be used.


use [**cuvis\_proc\_cont\_is\_capable**](group__cuvis__proc.md#function-cuvis_proc_cont_is_capable) to check, if the mode is currently possible of a specific measurement 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

