

# Struct cuvis::view\_t

**template &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;**



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**view\_t**](structcuvis_1_1view__t.md)



_Image data created from_ [_**ViewExporter**_](classcuvis_1_1ViewExporter.md) _._[More...](#detailed-description)

* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::common\_image\_t](structcuvis_1_1common__image__t.md)






















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**cuvis\_view\_category\_t**](structcuvis_1_1image__t.md) | [**\_category**](#variable-_category)  <br> |
|  std::string | [**\_id**](#variable-_id)  <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**\_show**](#variable-_show)  <br> |


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


The ViewExpoter generates image views (int 8 bit resolution) and data views (in floating point precision). Each image is named by it's [**\_id**](structcuvis_1_1view__t.md#variable-_id). Also the [**\_show**](structcuvis_1_1view__t.md#variable-_show) flag is set with respect to the setting of the view's author. See [**ViewExporter**](classcuvis_1_1ViewExporter.md) for more information. See [**common\_image\_t**](structcuvis_1_1common__image__t.md) for single pixel access.




**Template parameters:**


* `data_t` The pixel bit depth, either std::uint8\_t or float 




    
## Public Attributes Documentation




### variable \_category 

```C++
cuvis_view_category_t cuvis::view_t< data_t >::_category;
```



The image categroy 


        

<hr>



### variable \_id 

```C++
std::string cuvis::view_t< data_t >::_id;
```



The name of the image 


        

<hr>



### variable \_show 

```C++
bool cuvis::view_t< data_t >::_show;
```



Hint, if data can be shown on a screen as an image 


        

<hr>## Friends Documentation





### friend Viewer 

```C++
class cuvis::view_t::Viewer (
    Viewer
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

