

# Struct cuvis\_imbuffer\_t



[**ClassList**](annotated.md) **>** [**cuvis\_imbuffer\_t**](structcuvis__imbuffer__t.md)



_image buffer data structure with meta-data_ [More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  uint32\_t | [**bytes**](#variable-bytes)  <br> |
|  uint16\_t | [**channels**](#variable-channels)  <br> |
|  [**CUVIS\_IMBUFFER\_FORMAT**](cuvis_8h.md#define-cuvis_imbuffer_format) | [**format**](#variable-format)  <br>_the buffer format_  |
|  uint32\_t | [**height**](#variable-height)  <br> |
|  uint32\_t | [**length**](#variable-length)  <br> |
|  uint8\_t const  \* | [**raw**](#variable-raw)  <br> |
|  uint32\_t const  \* | [**wavelength**](#variable-wavelength)  <br>_the wavelength vector_  |
|  uint32\_t | [**width**](#variable-width)  <br> |












































## Detailed Description


The image buffer data structure holds a anonymous raw data pointer, that can be interpreted to give a meaningful data array with the help of the other members: The [**format**](structcuvis__imbuffer__t.md#variable-format) gives the information of the data type, the [**width**](structcuvis__imbuffer__t.md#variable-width), [**length**](structcuvis__imbuffer__t.md#variable-length), and [**channels**](structcuvis__imbuffer__t.md#variable-channels) give the number of elements in the array.


The [**wavelength**](structcuvis__imbuffer__t.md#variable-wavelength) property is only set for hyperspectral cubes but not for normal images. If it exists, it is an array with the number of channels


Example: 
```C++
// format = CUVIS_IMBUFFER_FORMAT_UINT16
// x in [0, width)
// y in [0,   height)
// chn in [0, channels)
unsigned index = (y * width + x) * channels + chn;
uint16_t value = ((uint16_t*) raw)[index];
unsigned lambda = cube.wavelength[chn];
```



see also: [**IMBUFFER\_GET**](cuvis_8h.md#define-imbuffer_get) 


    
## Public Attributes Documentation




### variable bytes 

```C++
uint32_t cuvis_imbuffer_t::bytes;
```



number of bytes per data element 


        

<hr>



### variable channels 

```C++
uint16_t cuvis_imbuffer_t::channels;
```



number of channels 


        

<hr>



### variable format 

_the buffer format_ 
```C++
CUVIS_IMBUFFER_FORMAT cuvis_imbuffer_t::format;
```



The buffer format defines what the member [**raw**](structcuvis__imbuffer__t.md#variable-raw) can be casted into. 


        

<hr>



### variable height 

```C++
uint32_t cuvis_imbuffer_t::height;
```



height of buffer 


        

<hr>



### variable length 

```C++
uint32_t cuvis_imbuffer_t::length;
```



total number of bytes in array 


        

<hr>



### variable raw 

```C++
uint8_t const* cuvis_imbuffer_t::raw;
```



the memory reference of the cube. Valid as long as the parent element (e.g. measurement) is valid and unchanged. 


        

<hr>



### variable wavelength 

_the wavelength vector_ 
```C++
uint32_t const* cuvis_imbuffer_t::wavelength;
```



If the [**cuvis\_imbuffer\_t**](structcuvis__imbuffer__t.md) is not a hyperspectral cube, the value will be nullptr For cubes this is an array of length channels, the elements define the cube's wavelength in nanometers. 


        

<hr>



### variable width 

```C++
uint32_t cuvis_imbuffer_t::width;
```



width of buffer 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

