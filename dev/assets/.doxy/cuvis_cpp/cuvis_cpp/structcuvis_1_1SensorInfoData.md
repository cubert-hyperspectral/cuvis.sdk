

# Struct cuvis::SensorInfoData



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**SensorInfoData**](structcuvis_1_1SensorInfoData.md)



[More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**averages**](#variable-averages)  <br> |
|  [**double**](structcuvis_1_1image__t.md) | [**gain**](#variable-gain)  <br> |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**height**](#variable-height)  <br> |
|  [**double**](structcuvis_1_1image__t.md) | [**integration\_time**](#variable-integration_time)  <br> |
|  std::string | [**pixel\_format**](#variable-pixel_format)  <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**raw\_frame\_id**](#variable-raw_frame_id)  <br> |
|  [**timestamp\_t**](namespacecuvis.md#typedef-timestamp_t) | [**readout\_time**](#variable-readout_time)  <br> |
|  [**double**](structcuvis_1_1image__t.md) | [**temperature**](#variable-temperature)  <br> |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**width**](#variable-width)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SensorInfoData**](#function-sensorinfodata) ([**sensor\_info\_t**](group__typedefs.md#typedef-sensor_info_t) [**const**](structcuvis_1_1image__t.md) & info) <br> |




























## Detailed Description


sensor info data structure 


    
## Public Attributes Documentation




### variable averages 

```C++
uint32_t cuvis::SensorInfoData::averages;
```



number of averages used 


        

<hr>



### variable gain 

```C++
double cuvis::SensorInfoData::gain;
```



gain value while recording 


        

<hr>



### variable height 

```C++
uint32_t cuvis::SensorInfoData::height;
```



height of buffer 


        

<hr>



### variable integration\_time 

```C++
double cuvis::SensorInfoData::integration_time;
```



the sensors's real integration time (exposure time in ms) 


        

<hr>



### variable pixel\_format 

```C++
std::string cuvis::SensorInfoData::pixel_format;
```



The sensor read-out pixel format used by this device. Informs how many bits per pixel are available. 


        

<hr>



### variable raw\_frame\_id 

```C++
size_t cuvis::SensorInfoData::raw_frame_id;
```



The sensor frame ID given to this devices frame by the hardware or driver of the device. May reset without warning! 


        

<hr>



### variable readout\_time 

```C++
timestamp_t cuvis::SensorInfoData::readout_time;
```



the timestamp (UTC) of the image readout (senor's hardware clock ) 


        

<hr>



### variable temperature 

```C++
double cuvis::SensorInfoData::temperature;
```



the sensors's temperature while readout (0 if not applicable) 


        

<hr>



### variable width 

```C++
uint32_t cuvis::SensorInfoData::width;
```



width of buffer 


        

<hr>
## Public Functions Documentation




### function SensorInfoData 

```C++
cuvis::SensorInfoData::SensorInfoData (
    sensor_info_t  const & info
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

