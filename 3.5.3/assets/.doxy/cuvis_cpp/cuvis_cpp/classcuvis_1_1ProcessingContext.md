

# Class cuvis::ProcessingContext



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**ProcessingContext**](classcuvis_1_1ProcessingContext.md)





* `#include <cuvis.hpp>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ProcessingContext**](#function-processingcontext-14) ([**Calibration**](classcuvis_1_1Calibration.md) [**const**](structcuvis_1_1image__t.md) & calib) <br> |
|   | [**ProcessingContext**](#function-processingcontext-24) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu, [**bool**](structcuvis_1_1image__t.md) load\_references=[**true**](structcuvis_1_1image__t.md)) <br> |
|   | [**ProcessingContext**](#function-processingcontext-34) ([**SessionFile**](classcuvis_1_1SessionFile.md) [**const**](structcuvis_1_1image__t.md) & session, [**bool**](structcuvis_1_1image__t.md) load\_references=[**true**](structcuvis_1_1image__t.md)) <br> |
|   | [**ProcessingContext**](#function-processingcontext-44) ([**CUVIS\_PROC\_CONT**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  [**Measurement**](classcuvis_1_1Measurement.md) & | [**apply**](#function-apply) ([**Measurement**](classcuvis_1_1Measurement.md) & mesu) const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**calc\_distance**](#function-calc_distance) ([**double**](structcuvis_1_1image__t.md) distMM) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**clear\_reference**](#function-clear_reference) ([**reference\_type\_t**](group__typedefs.md#typedef-reference_type_t) type) <br>_Clear a reference measurement._  |
|  std::string | [**get\_calib\_id**](#function-get_calib_id) () const<br>_get the calibration id of the procession context_  |
|  [**CUVIS\_PROC\_CONT**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_PROC\_CONT**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |
|  [**ProcessingArgs**](structcuvis_1_1ProcessingArgs.md) [**const**](structcuvis_1_1image__t.md) & | [**get\_processingArgs**](#function-get_processingargs) () const<br>_get the arguments of the processing context_  |
|  std::optional&lt; [**Measurement**](classcuvis_1_1Measurement.md) &gt; | [**get\_reference**](#function-get_reference) ([**reference\_type\_t**](group__typedefs.md#typedef-reference_type_t) type) const<br>_get a specific reference from the processing context_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**has\_reference**](#function-has_reference) ([**reference\_type\_t**](group__typedefs.md#typedef-reference_type_t) type) const<br>_Check if an explicit reference was set._  |
|  [**bool**](structcuvis_1_1image__t.md) | [**is\_capable**](#function-is_capable) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu, [**ProcessingArgs**](structcuvis_1_1ProcessingArgs.md) [**const**](structcuvis_1_1image__t.md) & procArgs) const<br>_Check if a processing mode is possible for a measurement._  |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_processingArgs**](#function-set_processingargs) ([**ProcessingArgs**](structcuvis_1_1ProcessingArgs.md) [**const**](structcuvis_1_1image__t.md) & procArgs) <br>_set the processing arguments for the processing context_  |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_reference**](#function-set_reference) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu, [**reference\_type\_t**](group__typedefs.md#typedef-reference_type_t) type) <br>_Set the reference for processing context._  |




























## Public Functions Documentation




### function ProcessingContext [1/4]

```C++
cuvis::ProcessingContext::ProcessingContext (
    Calibration  const & calib
) 
```




<hr>



### function ProcessingContext [2/4]

```C++
cuvis::ProcessingContext::ProcessingContext (
    Measurement  const & mesu,
    bool load_references=true
) 
```




<hr>



### function ProcessingContext [3/4]

```C++
cuvis::ProcessingContext::ProcessingContext (
    SessionFile  const & session,
    bool load_references=true
) 
```




<hr>



### function ProcessingContext [4/4]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::ProcessingContext::ProcessingContext (
    CUVIS_PROC_CONT handle
) 
```




<hr>



### function apply 

```C++
Measurement & cuvis::ProcessingContext::apply (
    Measurement & mesu
) const
```




<hr>



### function calc\_distance 

```C++
bool cuvis::ProcessingContext::calc_distance (
    double distMM
) 
```




<hr>



### function clear\_reference 

_Clear a reference measurement._ 
```C++
void cuvis::ProcessingContext::clear_reference (
    reference_type_t type
) 
```





**Parameters:**


* `type` Type of reference to clear 




        

<hr>



### function get\_calib\_id 

_get the calibration id of the procession context_ 
```C++
std::string cuvis::ProcessingContext::get_calib_id () const
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_PROC_CONT cuvis::ProcessingContext::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_PROC_CONT cuvis::ProcessingContext::get_handle_copy () const
```




<hr>



### function get\_processingArgs 

_get the arguments of the processing context_ 
```C++
ProcessingArgs  const & cuvis::ProcessingContext::get_processingArgs () const
```




<hr>



### function get\_reference 

_get a specific reference from the processing context_ 
```C++
std::optional< Measurement > cuvis::ProcessingContext::get_reference (
    reference_type_t type
) const
```



The processing context can hold explicit references (e.g. a dark), see ProcessingArgs.set\_reference . These reference can be obtained by this functions 


        

<hr>



### function has\_reference 

_Check if an explicit reference was set._ 
```C++
bool cuvis::ProcessingContext::has_reference (
    reference_type_t type
) const
```





**Parameters:**


* `type` reference type to check for 




        

<hr>



### function is\_capable 

_Check if a processing mode is possible for a measurement._ 
```C++
bool cuvis::ProcessingContext::is_capable (
    Measurement  const & mesu,
    ProcessingArgs  const & procArgs
) const
```



Depending on the measurement, it's intrinsic references, the processing context's explicit references and the internal camera calibration itself the availability of a mode varies.


Use this function, to check whether a specific mode is explicitly possible for a measurement. 


        

<hr>



### function set\_processingArgs 

_set the processing arguments for the processing context_ 
```C++
void cuvis::ProcessingContext::set_processingArgs (
    ProcessingArgs  const & procArgs
) 
```





**Parameters:**


* `procArgs` arguments to set 




        

<hr>



### function set\_reference 

_Set the reference for processing context._ 
```C++
void cuvis::ProcessingContext::set_reference (
    Measurement  const & mesu,
    reference_type_t type
) 
```





**Parameters:**


* `mesu` measurement The measurement to be used as explicit reference 
* `type` Type of reference to set 




        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

