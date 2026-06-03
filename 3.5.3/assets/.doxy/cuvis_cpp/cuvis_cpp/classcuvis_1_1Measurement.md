

# Class cuvis::Measurement



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**Measurement**](classcuvis_1_1Measurement.md)



_central measurement class_ 

* `#include <cuvis.hpp>`

















## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::map&lt; std::string, [**cuvis\_gps\_t**](structcuvis_1_1image__t.md) &gt; | [**gps\_data\_t**](#typedef-gps_data_t)  <br> |
| typedef std::map&lt; std::string, [**image\_variant\_t**](classcuvis_1_1Measurement.md#typedef-image_variant_t) &gt; | [**image\_data\_t**](#typedef-image_data_t)  <br> |
| typedef std::variant&lt; [**image\_t**](structcuvis_1_1image__t.md)&lt; std::uint8\_t &gt;, [**image\_t**](structcuvis_1_1image__t.md)&lt; std::uint16\_t &gt;, [**image\_t**](structcuvis_1_1image__t.md)&lt; std::uint32\_t &gt;, [**image\_t**](structcuvis_1_1image__t.md)&lt; [**float**](structcuvis_1_1image__t.md) &gt; &gt; | [**image\_variant\_t**](#typedef-image_variant_t)  <br> |
| typedef std::map&lt; std::string, [**SensorInfoData**](structcuvis_1_1SensorInfoData.md) &gt; | [**sensor\_info\_data\_t**](#typedef-sensor_info_data_t)  <br> |
| typedef std::map&lt; std::string, std::string &gt; | [**string\_data\_t**](#typedef-string_data_t)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Measurement**](#function-measurement-14) ([**Measurement**](classcuvis_1_1Measurement.md) && measurement) = default<br> |
|   | [**Measurement**](#function-measurement-24) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & source) <br> |
|   | [**Measurement**](#function-measurement-34) (std::filesystem::path [**const**](structcuvis_1_1image__t.md) & path) <br> |
|   | [**Measurement**](#function-measurement-44) ([**CUVIS\_MESU**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  [**void**](structcuvis_1_1image__t.md) | [**clear\_cube**](#function-clear_cube) () <br>_clears the cube from the measurement_  |
|  [**void**](structcuvis_1_1image__t.md) | [**clear\_implicit\_reference**](#function-clear_implicit_reference) ([**reference\_type\_t**](group__typedefs.md#typedef-reference_type_t) type) <br>_Clear the implicit reference measurement._  |
|  std::string | [**get\_calib\_id**](#function-get_calib_id) () const<br>_get calibration id of this measurement_  |
|  std::vector&lt; [**capabilities\_t**](group__typedefs.md#typedef-capabilities_t) &gt; | [**get\_capabilities**](#function-get_capabilities) () const<br>_Get the capabilites of the measurement which were present in the calibration during capture. This doesn't indicate which capabilities are currently available for the measurement._  |
|  [**gps\_data\_t**](classcuvis_1_1Measurement.md#typedef-gps_data_t) [**const**](structcuvis_1_1image__t.md) \* | [**get\_gps**](#function-get_gps) () const<br>_Get GPS data from measurement._  |
|  [**CUVIS\_MESU**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_MESU**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |
|  [**image\_data\_t**](classcuvis_1_1Measurement.md#typedef-image_data_t) [**const**](structcuvis_1_1image__t.md) \* | [**get\_imdata**](#function-get_imdata) () const<br>_Get image data from measurement._  |
|  [**MeasurementMetaData**](structcuvis_1_1MeasurementMetaData.md) [**const**](structcuvis_1_1image__t.md) \* | [**get\_meta**](#function-get_meta) () const<br>_Get the metadata of the measurement._  |
|  [**sensor\_info\_data\_t**](classcuvis_1_1Measurement.md#typedef-sensor_info_data_t) [**const**](structcuvis_1_1image__t.md) \* | [**get\_sensor\_info**](#function-get_sensor_info) () const<br>_Get image info data from measurement._  |
|  [**string\_data\_t**](classcuvis_1_1Measurement.md#typedef-string_data_t) [**const**](structcuvis_1_1image__t.md) \* | [**get\_strdata**](#function-get_strdata) () const<br>_Get string data from measurement._  |
|  [**image\_t**](structcuvis_1_1image__t.md)&lt; std::uint8\_t &gt; [**const**](structcuvis_1_1image__t.md) \* | [**get\_thumbnail**](#function-get_thumbnail) () const<br>_Get thumbnail / preview image of measurement._  |
|  [**Measurement**](classcuvis_1_1Measurement.md) & | [**operator=**](#function-operator) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & measurement) = default<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**refresh**](#function-refresh) () <br>_Resynchronize the_ [_**Measurement**_](classcuvis_1_1Measurement.md) _with the SDK data._ |
|  [**void**](structcuvis_1_1image__t.md) | [**save**](#function-save) ([**SaveArgs**](structcuvis_1_1SaveArgs.md) [**const**](structcuvis_1_1image__t.md) & args) <br>_Save measurement._  |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_comment**](#function-set_comment) (std::string [**const**](structcuvis_1_1image__t.md) & comment) <br>_set comment of measurement_  |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_name**](#function-set_name) (std::string [**const**](structcuvis_1_1image__t.md) & name) <br>_Set name of measurement._  |




























## Public Types Documentation




### typedef gps\_data\_t 

```C++
using cuvis::Measurement::gps_data_t =  std::map<std::string, cuvis_gps_t>;
```




<hr>



### typedef image\_data\_t 

```C++
using cuvis::Measurement::image_data_t =  std::map<std::string, image_variant_t>;
```




<hr>



### typedef image\_variant\_t 

```C++
using cuvis::Measurement::image_variant_t =  std::variant<image_t<std::uint8_t>, image_t<std::uint16_t>, image_t<std::uint32_t>, image_t<float> >;
```




<hr>



### typedef sensor\_info\_data\_t 

```C++
using cuvis::Measurement::sensor_info_data_t =  std::map<std::string, SensorInfoData>;
```




<hr>



### typedef string\_data\_t 

```C++
using cuvis::Measurement::string_data_t =  std::map<std::string, std::string>;
```




<hr>
## Public Functions Documentation




### function Measurement [1/4]

```C++
cuvis::Measurement::Measurement (
    Measurement && measurement
) = default
```




<hr>



### function Measurement [2/4]

```C++
cuvis::Measurement::Measurement (
    Measurement  const & source
) 
```




<hr>



### function Measurement [3/4]

```C++
cuvis::Measurement::Measurement (
    std::filesystem::path const & path
) 
```




<hr>



### function Measurement [4/4]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::Measurement::Measurement (
    CUVIS_MESU handle
) 
```




<hr>



### function clear\_cube 

_clears the cube from the measurement_ 
```C++
void cuvis::Measurement::clear_cube () 
```



Clears the proceessing result, i. e. the cube, from the measurement. This returns the measurement the state before applying the processing. This can be usefull for reduced data usage. 


        

<hr>



### function clear\_implicit\_reference 

_Clear the implicit reference measurement._ 
```C++
void cuvis::Measurement::clear_implicit_reference (
    reference_type_t type
) 
```



Implict measurements are created, when a measurement is processed with a processing context, where explicit references are set. Then, these references are remebemred by the measurement. When changing the processing context, the references are implicitly available, still. Clearing them may be interesing if the references set are wrong/invalid or if disk space is a concearn.




**Parameters:**


* `type` Type of reference to clear 




        

<hr>



### function get\_calib\_id 

_get calibration id of this measurement_ 
```C++
std::string cuvis::Measurement::get_calib_id () const
```




<hr>



### function get\_capabilities 

_Get the capabilites of the measurement which were present in the calibration during capture. This doesn't indicate which capabilities are currently available for the measurement._ 
```C++
std::vector< capabilities_t > cuvis::Measurement::get_capabilities () const
```




<hr>



### function get\_gps 

_Get GPS data from measurement._ 
```C++
inline gps_data_t  const * cuvis::Measurement::get_gps () const
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_MESU cuvis::Measurement::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_MESU cuvis::Measurement::get_handle_copy () const
```




<hr>



### function get\_imdata 

_Get image data from measurement._ 
```C++
inline image_data_t  const * cuvis::Measurement::get_imdata () const
```



Return image data from measurement. 


        

<hr>



### function get\_meta 

_Get the metadata of the measurement._ 
```C++
MeasurementMetaData  const * cuvis::Measurement::get_meta () const
```



The meta-data from the measurement contains information about the measurement when it was recorded: when and how. Meta-Data do not contain the actual recorded data. 


        

<hr>



### function get\_sensor\_info 

_Get image info data from measurement._ 
```C++
sensor_info_data_t  const * cuvis::Measurement::get_sensor_info () const
```



Return image data from a measurement. 


        

<hr>



### function get\_strdata 

_Get string data from measurement._ 
```C++
inline string_data_t  const * cuvis::Measurement::get_strdata () const
```




<hr>



### function get\_thumbnail 

_Get thumbnail / preview image of measurement._ 
```C++
image_t < std::uint8_t > const * cuvis::Measurement::get_thumbnail () const
```




<hr>



### function operator= 

```C++
Measurement & cuvis::Measurement::operator= (
    Measurement  const & measurement
) = default
```




<hr>



### function refresh 

_Resynchronize the_ [_**Measurement**_](classcuvis_1_1Measurement.md) _with the SDK data._
```C++
void cuvis::Measurement::refresh () 
```



usally this does not have to be called manually, but is rather called internally by any operation that may result in invalidated (meta-)data 


        

<hr>



### function save 

_Save measurement._ 
```C++
void cuvis::Measurement::save (
    SaveArgs  const & args
) 
```



Save the measurement with given arguments




**Parameters:**


* `args` The Save Arguments to use for saving the measurement. See also [**SaveArgs**](structcuvis_1_1SaveArgs.md) 




        

<hr>



### function set\_comment 

_set comment of measurement_ 
```C++
void cuvis::Measurement::set_comment (
    std::string const & comment
) 
```





**Parameters:**


* `comment` String to use as comment for the measurement 




        

<hr>



### function set\_name 

_Set name of measurement._ 
```C++
void cuvis::Measurement::set_name (
    std::string const & name
) 
```





**Parameters:**


* `name` String to use as name of the measuremen 




        

<hr>## Friends Documentation





### friend AcquisitionContext 

```C++
class cuvis::Measurement::AcquisitionContext (
    AcquisitionContext
) 
```




<hr>



### friend AsyncMesu 

```C++
class cuvis::Measurement::AsyncMesu (
    AsyncMesu
) 
```




<hr>



### friend Exporter 

```C++
class cuvis::Measurement::Exporter (
    Exporter
) 
```




<hr>



### friend ProcessingContext 

```C++
class cuvis::Measurement::ProcessingContext (
    ProcessingContext
) 
```




<hr>



### friend SessionFile 

```C++
class cuvis::Measurement::SessionFile (
    SessionFile
) 
```




<hr>



### friend Viewer 

```C++
class cuvis::Measurement::Viewer (
    Viewer
) 
```




<hr>



### friend Worker 

```C++
class cuvis::Measurement::Worker (
    Worker
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

