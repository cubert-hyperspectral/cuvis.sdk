

# Struct cuvis\_mesu\_metadata\_t



[**ClassList**](annotated.md) **>** [**cuvis\_mesu\_metadata\_t**](structcuvis__mesu__metadata__t.md)



_The measurement meta structure._ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**assembly**](#variable-assembly)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**averages**](#variable-averages)  <br> |
|  [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp) | [**capture\_time**](#variable-capture_time)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**comment**](#variable-comment)  <br> |
|  double | [**distance**](#variable-distance)  <br> |
|  [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp) | [**factory\_calibration**](#variable-factory_calibration)  <br> |
|  double | [**integration\_time**](#variable-integration_time)  <br> |
|  [**CUVIS\_FLAGS**](cuvis_8h.md#define-cuvis_flags) | [**measurement\_flags**](#variable-measurement_flags)  <br> |
|  [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) | [**measurement\_frame\_id**](#variable-measurement_frame_id)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**name**](#variable-name)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**path**](#variable-path)  <br> |
|  [**CUVIS\_PROCESSING\_MODE**](cuvis_8h.md#define-cuvis_processing_mode) | [**processing\_mode**](#variable-processing_mode)  <br> |
|  [**CUVIS\_PROCESSING\_MODE**](cuvis_8h.md#define-cuvis_processing_mode) | [**processing\_mode\_at\_capture**](#variable-processing_mode_at_capture)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**product\_name**](#variable-product_name)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**serial\_number**](#variable-serial_number)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**session\_info\_name**](#variable-session_info_name)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**session\_info\_sequence\_no**](#variable-session_info_sequence_no)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**session\_info\_session\_no**](#variable-session_info_session_no)  <br> |












































## Public Attributes Documentation




### variable assembly 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::assembly[CUVIS_MAXBUF];
```



The Assembly Data of the device 


        

<hr>



### variable averages 

```C++
CUVIS_INT cuvis_mesu_metadata_t::averages;
```



Number of averaging taken 


        

<hr>



### variable capture\_time 

```C++
CUVIS_TIMESTAMP cuvis_mesu_metadata_t::capture_time;
```



The Capture Time of the Measurement 


        

<hr>



### variable comment 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::comment[CUVIS_MAXBUF];
```



The User Comment linked to the measurement 


        

<hr>



### variable distance 

```C++
double cuvis_mesu_metadata_t::distance;
```



Distance, the measurement was recorded in mm. If not provided, value is -1 


        

<hr>



### variable factory\_calibration 

```C++
CUVIS_TIMESTAMP cuvis_mesu_metadata_t::factory_calibration;
```



The factory calibration date of the device 


        

<hr>



### variable integration\_time 

```C++
double cuvis_mesu_metadata_t::integration_time;
```



The integration time of the measurement (exposure time) in ms 


        

<hr>



### variable measurement\_flags 

```C++
CUVIS_FLAGS cuvis_mesu_metadata_t::measurement_flags;
```



measurement flags 


        

<hr>



### variable measurement\_frame\_id 

```C++
CUVIS_SIZE cuvis_mesu_metadata_t::measurement_frame_id;
```



The frame ID assigned by cuvis to this measurement 


        

<hr>



### variable name 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::name[CUVIS_MAXBUF];
```



The name of the measurement 


        

<hr>



### variable path 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::path[CUVIS_MAXBUF];
```



The output file path 


        

<hr>



### variable processing\_mode 

```C++
CUVIS_PROCESSING_MODE cuvis_mesu_metadata_t::processing_mode;
```



The current processing mode of the cube 


        

<hr>



### variable processing\_mode\_at\_capture 

```C++
CUVIS_PROCESSING_MODE cuvis_mesu_metadata_t::processing_mode_at_capture;
```



The processing mode at the time of the cube was recorded 


        

<hr>



### variable product\_name 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::product_name[CUVIS_MAXBUF];
```



The name of the device, which took the measurement 


        

<hr>



### variable serial\_number 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::serial_number[CUVIS_MAXBUF];
```



The serial number of the device, which took the measurement 


        

<hr>



### variable session\_info\_name 

```C++
CUVIS_CHAR cuvis_mesu_metadata_t::session_info_name[CUVIS_MAXBUF];
```



session\_info name 


        

<hr>



### variable session\_info\_sequence\_no 

```C++
CUVIS_INT cuvis_mesu_metadata_t::session_info_sequence_no;
```



Sequence number. Increases with each recorded frame. Reset, if session\_no changes 


        

<hr>



### variable session\_info\_session\_no 

```C++
CUVIS_INT cuvis_mesu_metadata_t::session_info_session_no;
```



SessionFile number. Will be increased by stopping & starting recording 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

