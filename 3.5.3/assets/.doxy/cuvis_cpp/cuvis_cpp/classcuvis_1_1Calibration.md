

# Class cuvis::Calibration



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**Calibration**](classcuvis_1_1Calibration.md)



[More...](#detailed-description)

* `#include <cuvis.hpp>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Calibration**](#function-calibration-13) (std::filesystem::path [**const**](structcuvis_1_1image__t.md) & path) <br>_Create a calibration from factory path._  |
|   | [**Calibration**](#function-calibration-23) ([**SessionFile**](classcuvis_1_1SessionFile.md) [**const**](structcuvis_1_1image__t.md) & session) <br>_Create a calibration from session file._  |
|   | [**Calibration**](#function-calibration-33) ([**CUVIS\_CALIB**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  std::vector&lt; [**capabilities\_t**](group__typedefs.md#typedef-capabilities_t) &gt; | [**get\_capabilities**](#function-get_capabilities) ([**CUVIS\_OPERATION\_MODE**](structcuvis_1_1image__t.md) mode) const<br>_get calibration capabilities_  |
|  [**int\_t**](group__typedefs.md#typedef-int_t) | [**get\_component\_count**](#function-get_component_count) () const<br>_get number of components_  |
|  [**CUVIS\_COMPONENT\_INFO**](structcuvis_1_1image__t.md) | [**get\_component\_info**](#function-get_component_info) ([**int\_t**](group__typedefs.md#typedef-int_t) id) const<br>_get a components information_  |
|  [**CUVIS\_CALIB**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_CALIB**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |
|  std::string | [**get\_id**](#function-get_id) () const<br>_get the calibration id_  |
|  [**CalibrationInfo**](structcuvis_1_1CalibrationInfo.md) | [**get\_info**](#function-get_info) () const<br>_get calibration infos_  |




























## Detailed Description


central calibration Class 


    
## Public Functions Documentation




### function Calibration [1/3]

_Create a calibration from factory path._ 
```C++
cuvis::Calibration::Calibration (
    std::filesystem::path const & path
) 
```



The calibration is created from a factory path, containing the license and calibration file "init.daq" as well as further calibration files (e.g. SpRad.cu3).


The calibration is lazy-loading, i.e. the [**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md) and the [**ProcessingContext**](classcuvis_1_1ProcessingContext.md) will only be initialized, when explicitly called.




**Note:**

do not load multiple calibration instances of the same camera




**Parameters:**


* `path` The path to the factory directory 




        

<hr>



### function Calibration [2/3]

_Create a calibration from session file._ 
```C++
cuvis::Calibration::Calibration (
    SessionFile  const & session
) 
```



Create a calibration from an existion session file.


The calibration is lazy-loading, i.e. the [**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md) and the [**ProcessingContext**](classcuvis_1_1ProcessingContext.md) will only be initialized, when explicitly called.


When you create a processing context from the calibration cerated with this function, you won't have the references from the session file set. Use cuvis\_proc\_cont\_create\_from\_session\_file to load a processing context where the referenecs are taken from the session file.




**Note:**

do not load multiple calibration instances of the same camera




**Parameters:**


* `session` The session file 




        

<hr>



### function Calibration [3/3]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::Calibration::Calibration (
    CUVIS_CALIB handle
) 
```




<hr>



### function get\_capabilities 

_get calibration capabilities_ 
```C++
std::vector< capabilities_t > cuvis::Calibration::get_capabilities (
    CUVIS_OPERATION_MODE mode
) const
```





**Parameters:**


* `mode` Operation mode of the camera see also cuvis\_operation\_mode\_t 




        

<hr>



### function get\_component\_count 

_get number of components_ 
```C++
int_t cuvis::Calibration::get_component_count () const
```




<hr>



### function get\_component\_info 

_get a components information_ 
```C++
CUVIS_COMPONENT_INFO cuvis::Calibration::get_component_info (
    int_t id
) const
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_CALIB cuvis::Calibration::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_CALIB cuvis::Calibration::get_handle_copy () const
```




<hr>



### function get\_id 

_get the calibration id_ 
```C++
std::string cuvis::Calibration::get_id () const
```




<hr>



### function get\_info 

_get calibration infos_ 
```C++
CalibrationInfo cuvis::Calibration::get_info () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

