

# Struct cuvis\_export\_view\_settings\_t



[**ClassList**](annotated.md) **>** [**cuvis\_export\_view\_settings\_t**](structcuvis__export__view__settings__t.md)



_Additional settings for exporting to a userplugin view. See also_ [_**cuvis\_export\_general\_settings\_t**_](structcuvis__export__general__settings__t.md) _._

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**complete**](#variable-complete)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**pan\_failback**](#variable-pan_failback)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const  \* | [**userplugin**](#variable-userplugin)  <br> |












































## Public Attributes Documentation




### variable complete 

```C++
CUVIS_INT cuvis_export_view_settings_t::complete;
```



When using View Exporter: export all output elements of the user plugin, even if they're not marked as "show" 


        

<hr>



### variable pan\_failback 

```C++
CUVIS_INT cuvis_export_view_settings_t::pan_failback;
```



failback to pan image if cube is not available 


        

<hr>



### variable userplugin 

```C++
CUVIS_CHAR const* cuvis_export_view_settings_t::userplugin;
```



The userplugin xml string. See userplugin manual. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

