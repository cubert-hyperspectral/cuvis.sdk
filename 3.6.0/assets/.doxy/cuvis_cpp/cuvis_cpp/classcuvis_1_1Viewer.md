

# Class cuvis::Viewer



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**Viewer**](classcuvis_1_1Viewer.md)





* `#include <cuvis.hpp>`

















## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::map&lt; std::string, [**view\_variant\_t**](classcuvis_1_1Viewer.md#typedef-view_variant_t) &gt; | [**view\_data\_t**](#typedef-view_data_t)  <br> |
| typedef std::variant&lt; [**view\_t**](structcuvis_1_1view__t.md)&lt; std::uint8\_t &gt;, [**view\_t**](structcuvis_1_1view__t.md)&lt; [**float**](structcuvis_1_1image__t.md) &gt; &gt; | [**view\_variant\_t**](#typedef-view_variant_t)  <br> |
| typedef [**cuvis\_viewer\_settings\_t**](structcuvis_1_1image__t.md) | [**viewer\_settings\_t**](#typedef-viewer_settings_t)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Viewer**](#function-viewer-12) ([**ViewArgs**](structcuvis_1_1ViewArgs.md) [**const**](structcuvis_1_1image__t.md) & args) <br> |
|   | [**Viewer**](#function-viewer-22) ([**CUVIS\_VIEWER**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  [**view\_data\_t**](classcuvis_1_1Viewer.md#typedef-view_data_t) | [**apply**](#function-apply) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu) <br> |
|  [**CUVIS\_VIEWER**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_VIEWER**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |




























## Public Types Documentation




### typedef view\_data\_t 

```C++
using cuvis::Viewer::view_data_t =  std::map<std::string, view_variant_t>;
```




<hr>



### typedef view\_variant\_t 

```C++
using cuvis::Viewer::view_variant_t =  std::variant<view_t<std::uint8_t>, view_t<float> >;
```




<hr>



### typedef viewer\_settings\_t 

```C++
using cuvis::Viewer::viewer_settings_t =  cuvis_viewer_settings_t;
```




<hr>
## Public Functions Documentation




### function Viewer [1/2]

```C++
cuvis::Viewer::Viewer (
    ViewArgs  const & args
) 
```




<hr>



### function Viewer [2/2]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::Viewer::Viewer (
    CUVIS_VIEWER handle
) 
```




<hr>



### function apply 

```C++
view_data_t cuvis::Viewer::apply (
    Measurement  const & mesu
) 
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_VIEWER cuvis::Viewer::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_VIEWER cuvis::Viewer::get_handle_copy () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

