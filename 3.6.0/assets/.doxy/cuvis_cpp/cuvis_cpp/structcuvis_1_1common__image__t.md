

# Struct cuvis::common\_image\_t

**template &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;**



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**common\_image\_t**](structcuvis_1_1common__image__t.md)



_Metaclass for handling image data (2d or 3d)_ [More...](#detailed-description)

* `#include <cuvis.hpp>`





Inherited by the following classes: [cuvis::image\_t](structcuvis_1_1image__t.md),  [cuvis::view\_t](structcuvis_1_1view__t.md)
















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::size\_t | [**\_channels**](#variable-_channels)  <br> |
|  [**data\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md)  \* | [**\_data**](#variable-_data)  <br>_The raw data pointer._  |
|  std::size\_t | [**\_height**](#variable-_height)  <br> |
|  std::size\_t | [**\_width**](#variable-_width)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**data\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md) & | [**get**](#function-get) (std::size\_t x, std::size\_t y, std::size\_t z=std::size\_t(0)) const<br> |




























## Detailed Description


Holds an X/Y/Z- dimensional image cube, without wavelength informaiton.




**Template parameters:**


* `data_t` The pixel bit depth, either std::uint8\_t, std::uint16\_t, std::uint32\_t or float 




    
## Public Attributes Documentation




### variable \_channels 

```C++
std::size_t cuvis::common_image_t< data_t >::_channels;
```



number of channels 


        

<hr>



### variable \_data 

_The raw data pointer._ 
```C++
data_t const* cuvis::common_image_t< data_t >::_data;
```



It is recommended to access the data with the [**get**](structcuvis_1_1common__image__t.md#function-get) function.
 The memory interleave is BIP. E.g. for a 3x3x2 (x,y,z) the coordinates are:



> (0,0,0); (0,0,1); (0,1,0); (0,1,1) 
> 
(1,0,0); (1,0,1); (1,1,0); (0,1,1) 
> 
(2,0,0); (2,0,1); (2,1,0); (0,1,1) 
> 




        

<hr>



### variable \_height 

```C++
std::size_t cuvis::common_image_t< data_t >::_height;
```



height of channel(Z - dimension) 


        

<hr>



### variable \_width 

```C++
std::size_t cuvis::common_image_t< data_t >::_width;
```



width of channel(X - dimension) 


        

<hr>
## Public Functions Documentation




### function get 

```C++
data_t  const & cuvis::common_image_t::get (
    std::size_t x,
    std::size_t y,
    std::size_t z=std::size_t(0)
) const
```



Access to a given memory location within [**\_data**](structcuvis_1_1common__image__t.md#variable-_data)




**Parameters:**


* `x` x pixel position (0 - [**\_width**](structcuvis_1_1common__image__t.md#variable-_width) - 1) 
* `y` y pixel position (0 - [**\_height**](structcuvis_1_1common__image__t.md#variable-_height) - 1) 
* `y` z pixel position (0 - [**\_channels**](structcuvis_1_1common__image__t.md#variable-_channels) - 1), Use "0" for a 2d image 



**Returns:**

the pixel value of the image / cube at position (x,y,z) 





        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

