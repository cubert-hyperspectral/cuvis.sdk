

# Struct cuvis\_sensor\_info\_t



[**ClassList**](annotated.md) **>** [**cuvis\_sensor\_info\_t**](structcuvis__sensor__info__t.md)





* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  uint32\_t | [**averages**](#variable-averages)  <br> |
|  double | [**gain**](#variable-gain)  <br> |
|  uint32\_t | [**height**](#variable-height)  <br> |
|  double | [**integration\_time**](#variable-integration_time)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**pixel\_format**](#variable-pixel_format)  <br> |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**raw\_frame\_id**](#variable-raw_frame_id)  <br> |
|  [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp) | [**readout\_time**](#variable-readout_time)  <br> |
|  double | [**temperature**](#variable-temperature)  <br> |
|  uint32\_t | [**width**](#variable-width)  <br> |












































## Public Attributes Documentation




### variable averages 

```C++
uint32_t cuvis_sensor_info_t::averages;
```



number of averages used 


        

<hr>



### variable gain 

```C++
double cuvis_sensor_info_t::gain;
```



gain value while recording 


        

<hr>



### variable height 

```C++
uint32_t cuvis_sensor_info_t::height;
```



height of buffer 


        

<hr>



### variable integration\_time 

```C++
double cuvis_sensor_info_t::integration_time;
```



The real integration time of the sensor (exposure time) in ms 


        

<hr>



### variable pixel\_format 

```C++
CUVIS_CHAR cuvis_sensor_info_t::pixel_format[CUVIS_MAXBUF];
```



The sensor read-out pixel format used by this device. Informs how many bits per pixel are available. 


        

<hr>



### variable raw\_frame\_id 

```C++
CUVIS_SIZE cuvis_sensor_info_t::raw_frame_id;
```



ID given to this measurement by the device hardware or driver 


        

<hr>



### variable readout\_time 

```C++
CUVIS_TIMESTAMP cuvis_sensor_info_t::readout_time;
```



the timestamp (UTC) of the image readout (senor's hardware clock ) 


        

<hr>



### variable temperature 

```C++
double cuvis_sensor_info_t::temperature;
```



the sensors's temperature while readout (0 if not applicable) 


        

<hr>



### variable width 

```C++
uint32_t cuvis_sensor_info_t::width;
```



width of buffer 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

