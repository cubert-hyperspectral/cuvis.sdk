

# Struct cuvis::MeasurementMetaData



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**MeasurementMetaData**](structcuvis_1_1MeasurementMetaData.md)



[More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::string | [**assembly**](#variable-assembly)  <br> |
|  [**unsigned**](structcuvis_1_1image__t.md) | [**averages**](#variable-averages)  <br> |
|  [**timestamp\_t**](namespacecuvis.md#typedef-timestamp_t) | [**capture\_time**](#variable-capture_time)  <br> |
|  std::string | [**comment**](#variable-comment)  <br> |
|  std::optional&lt; [**double**](structcuvis_1_1image__t.md) &gt; | [**distance**](#variable-distance)  <br> |
|  [**timestamp\_t**](namespacecuvis.md#typedef-timestamp_t) | [**factory\_calibration**](#variable-factory_calibration)  <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**frame\_id**](#variable-frame_id)  <br> |
|  [**double**](structcuvis_1_1image__t.md) | [**integration\_time**](#variable-integration_time)  <br> |
|  std::map&lt; std::string, std::string &gt; | [**measurement\_flags**](#variable-measurement_flags)  <br> |
|  std::string | [**name**](#variable-name)  <br> |
|  std::string | [**path**](#variable-path)  <br> |
|  [**processing\_mode\_t**](group__typedefs.md#typedef-processing_mode_t) | [**processing\_mode**](#variable-processing_mode)  <br> |
|  std::string | [**product\_name**](#variable-product_name)  <br> |
|  std::string | [**serial\_number**](#variable-serial_number)  <br> |
|  [**SessionInfo**](structcuvis_1_1SessionInfo.md) | [**session\_info**](#variable-session_info)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**MeasurementMetaData**](#function-measurementmetadata) ([**mesu\_metadata\_t**](group__typedefs.md#typedef-mesu_metadata_t) [**const**](structcuvis_1_1image__t.md) & meta) <br> |




























## Detailed Description


measurement meta structure 


    
## Public Attributes Documentation




### variable assembly 

```C++
std::string cuvis::MeasurementMetaData::assembly;
```




<hr>



### variable averages 

```C++
unsigned cuvis::MeasurementMetaData::averages;
```




<hr>



### variable capture\_time 

```C++
timestamp_t cuvis::MeasurementMetaData::capture_time;
```




<hr>



### variable comment 

```C++
std::string cuvis::MeasurementMetaData::comment;
```




<hr>



### variable distance 

```C++
std::optional<double> cuvis::MeasurementMetaData::distance;
```



The distance, the measurement was recorded in, in millimeters, if available. 


        

<hr>



### variable factory\_calibration 

```C++
timestamp_t cuvis::MeasurementMetaData::factory_calibration;
```




<hr>



### variable frame\_id 

```C++
size_t cuvis::MeasurementMetaData::frame_id;
```



The incremental frame ID given by cuvis to this measurement 


        

<hr>



### variable integration\_time 

```C++
double cuvis::MeasurementMetaData::integration_time;
```




<hr>



### variable measurement\_flags 

```C++
std::map<std::string, std::string> cuvis::MeasurementMetaData::measurement_flags;
```




<hr>



### variable name 

```C++
std::string cuvis::MeasurementMetaData::name;
```




<hr>



### variable path 

```C++
std::string cuvis::MeasurementMetaData::path;
```




<hr>



### variable processing\_mode 

```C++
processing_mode_t cuvis::MeasurementMetaData::processing_mode;
```




<hr>



### variable product\_name 

```C++
std::string cuvis::MeasurementMetaData::product_name;
```




<hr>



### variable serial\_number 

```C++
std::string cuvis::MeasurementMetaData::serial_number;
```




<hr>



### variable session\_info 

```C++
SessionInfo cuvis::MeasurementMetaData::session_info;
```



The session information of the measurement. 


        

<hr>
## Public Functions Documentation




### function MeasurementMetaData 

```C++
cuvis::MeasurementMetaData::MeasurementMetaData (
    mesu_metadata_t  const & meta
) 
```



Constructor to create default parameters 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

