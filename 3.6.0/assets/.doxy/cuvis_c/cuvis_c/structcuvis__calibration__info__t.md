

# Struct cuvis\_calibration\_info\_t



[**ClassList**](annotated.md) **>** [**cuvis\_calibration\_info\_t**](structcuvis__calibration__info__t.md)



[More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**annotation\_name**](#variable-annotation_name)  <br> |
|  [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp) | [**calibration\_date**](#variable-calibration_date)  <br> |
|  uint32\_t | [**cube\_channels**](#variable-cube_channels)  <br> |
|  uint32\_t | [**cube\_height**](#variable-cube_height)  <br> |
|  uint32\_t const  \* | [**cube\_wavelengths**](#variable-cube_wavelengths)  <br> |
|  uint32\_t | [**cube\_width**](#variable-cube_width)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**file\_path**](#variable-file_path)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**model\_name**](#variable-model_name)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**serial\_no**](#variable-serial_no)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**unique\_id**](#variable-unique_id)  <br> |












































## Detailed Description


internal info/data of calibration 


    
## Public Attributes Documentation




### variable annotation\_name 

```C++
CUVIS_CHAR cuvis_calibration_info_t::annotation_name[CUVIS_MAXBUF];
```



calibration annotation name 


        

<hr>



### variable calibration\_date 

```C++
CUVIS_TIMESTAMP cuvis_calibration_info_t::calibration_date;
```



timestamp (UTC) of calibration date 


        

<hr>



### variable cube\_channels 

```C++
uint32_t cuvis_calibration_info_t::cube_channels;
```



cube number of channels, -1 if unknown 


        

<hr>



### variable cube\_height 

```C++
uint32_t cuvis_calibration_info_t::cube_height;
```



cube height, -1 if unknown 


        

<hr>



### variable cube\_wavelengths 

```C++
uint32_t const* cuvis_calibration_info_t::cube_wavelengths;
```



cubes wavelengths (nm) vector, contains 'cube\_channels' values, can be nullptr if wavelengths are unknown 


        

<hr>



### variable cube\_width 

```C++
uint32_t cuvis_calibration_info_t::cube_width;
```



cube width, -1 if unknown 


        

<hr>



### variable file\_path 

```C++
CUVIS_CHAR cuvis_calibration_info_t::file_path[CUVIS_MAXBUF];
```



calibration file path 


        

<hr>



### variable model\_name 

```C++
CUVIS_CHAR cuvis_calibration_info_t::model_name[CUVIS_MAXBUF];
```



camera model name 


        

<hr>



### variable serial\_no 

```C++
CUVIS_CHAR cuvis_calibration_info_t::serial_no[CUVIS_MAXBUF];
```



camera serial number 


        

<hr>



### variable unique\_id 

```C++
CUVIS_CHAR cuvis_calibration_info_t::unique_id[CUVIS_MAXBUF];
```



calibration unique ID 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

