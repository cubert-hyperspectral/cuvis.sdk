

# Struct cuvis::ProcessingArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**ProcessingArgs**](structcuvis_1_1ProcessingArgs.md)



_processing arguments_ 

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**allow\_recalib**](#variable-allow_recalib)  <br> |
|  [**processing\_mode\_t**](group__typedefs.md#typedef-processing_mode_t) | [**processing\_mode**](#variable-processing_mode)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ProcessingArgs**](#function-processingargs) () <br> |
|   | [**operator cuvis\_proc\_args\_t**](#function-operator-cuvis_proc_args_t) () const<br>_convert to C - SDK settings structure_  |




























## Public Attributes Documentation




### variable allow\_recalib 

```C++
bool cuvis::ProcessingArgs::allow_recalib;
```




<hr>



### variable processing\_mode 

```C++
processing_mode_t cuvis::ProcessingArgs::processing_mode;
```




<hr>
## Public Functions Documentation




### function ProcessingArgs 

```C++
cuvis::ProcessingArgs::ProcessingArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_proc\_args\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::ProcessingArgs::operator cuvis_proc_args_t () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

