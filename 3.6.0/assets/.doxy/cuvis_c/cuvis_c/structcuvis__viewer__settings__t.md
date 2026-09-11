

# Struct cuvis\_viewer\_settings\_t



[**ClassList**](annotated.md) **>** [**cuvis\_viewer\_settings\_t**](structcuvis__viewer__settings__t.md)



_viewer settings_ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**complete**](#variable-complete)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**pan\_failback**](#variable-pan_failback)  <br> |
|  [**CUVIS\_PANSHARPENING\_SETTINGS**](cuvis_8h.md#define-cuvis_pansharpening_settings) | [**pansharpening\_settings**](#variable-pansharpening_settings)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const  \* | [**userplugin**](#variable-userplugin)  <br> |












































## Public Attributes Documentation




### variable complete 

```C++
CUVIS_INT cuvis_viewer_settings_t::complete;
```



also include parts that were not marked as "show". 


        

<hr>



### variable pan\_failback 

```C++
CUVIS_INT cuvis_viewer_settings_t::pan_failback;
```



failback to pan image if cube is not available 


        

<hr>



### variable pansharpening\_settings 

```C++
CUVIS_PANSHARPENING_SETTINGS cuvis_viewer_settings_t::pansharpening_settings;
```



Settings regarding pansharpening and channel selection 


        

<hr>



### variable userplugin 

```C++
CUVIS_CHAR const* cuvis_viewer_settings_t::userplugin;
```



The userplugin xml string. See userplugin manual. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

