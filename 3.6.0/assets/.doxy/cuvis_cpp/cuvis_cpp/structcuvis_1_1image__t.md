

# Struct cuvis::image\_t

**template &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;**



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**image\_t**](structcuvis_1_1image__t.md)



_Image data from a measurement._ [More...](#detailed-description)

* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::common\_image\_t](structcuvis_1_1common__image__t.md)






















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**uint32\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md)  \* | [**\_wavelength**](#variable-_wavelength)  <br> |


## Public Attributes inherited from cuvis::common_image_t

See [cuvis::common\_image\_t](structcuvis_1_1common__image__t.md)

| Type | Name |
| ---: | :--- |
|  std::size\_t | [**\_channels**](structcuvis_1_1common__image__t.md#variable-_channels)  <br> |
|  [**data\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md)  \* | [**\_data**](structcuvis_1_1common__image__t.md#variable-_data)  <br>_The raw data pointer._  |
|  std::size\_t | [**\_height**](structcuvis_1_1common__image__t.md#variable-_height)  <br> |
|  std::size\_t | [**\_width**](structcuvis_1_1common__image__t.md#variable-_width)  <br> |
































## Public Functions inherited from cuvis::common_image_t

See [cuvis::common\_image\_t](structcuvis_1_1common__image__t.md)

| Type | Name |
| ---: | :--- |
|  [**data\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md) & | [**get**](structcuvis_1_1common__image__t.md#function-get) (std::size\_t x, std::size\_t y, std::size\_t z=std::size\_t(0)) const<br> |






















































## Detailed Description


See [**common\_image\_t**](structcuvis_1_1common__image__t.md) for single pixel access. The [**\_wavelength**](structcuvis_1_1image__t.md#variable-_wavelength) is either a nullptr or, if set contains the cube's wavelengths in nano meter.




**Template parameters:**


* `data_t` The pixel bit depth, either std::uint8\_t, std::uint16\_t, std::uint32\_t or float 




    
## Public Attributes Documentation




### variable \_wavelength 

```C++
uint32_t const* cuvis::image_t< data_t >::_wavelength;
```



wavelength vector. nullptr, an array of size [**\_channels**](structcuvis_1_1common__image__t.md#variable-_channels) contianing the wavelengths in nano meter. 


        

<hr>## Friends Documentation





### friend Measurement 

```C++
class cuvis::image_t::Measurement (
    Measurement
) 
```




<hr>



### friend Viewer 

```C++
class cuvis::image_t::Viewer (
    Viewer
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

