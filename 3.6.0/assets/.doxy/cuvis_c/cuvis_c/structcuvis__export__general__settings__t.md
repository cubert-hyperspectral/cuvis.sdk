

# Struct cuvis\_export\_general\_settings\_t



[**ClassList**](annotated.md) **>** [**cuvis\_export\_general\_settings\_t**](structcuvis__export__general__settings__t.md)



_general export settings_ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**add\_fullscale\_pan**](#variable-add_fullscale_pan)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**export\_dir**](#variable-export_dir)  <br> |
|  [**CUVIS\_PANSHARPENING\_SETTINGS**](cuvis_8h.md#define-cuvis_pansharpening_settings) | [**pansharpening\_settings**](#variable-pansharpening_settings)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**permissive**](#variable-permissive)  <br> |












































## Public Attributes Documentation




### variable add\_fullscale\_pan 

```C++
CUVIS_INT cuvis_export_general_settings_t::add_fullscale_pan;
```



add full-resolution pan to the export. The pan image is exported seperately 


        

<hr>



### variable export\_dir 

```C++
CUVIS_CHAR cuvis_export_general_settings_t::export_dir[CUVIS_MAXBUF];
```



The export directory 


        

<hr>



### variable pansharpening\_settings 

```C++
CUVIS_PANSHARPENING_SETTINGS cuvis_export_general_settings_t::pansharpening_settings;
```



Settings regarding pansharpening and channel selection 


        

<hr>



### variable permissive 

```C++
CUVIS_INT cuvis_export_general_settings_t::permissive;
```



Set exporter to "permisive mode"


If set, errors will be skipped and alternative values assumed, wherever possible.


E.g., if add\_pan is selected but there is no panchromatic image avaialbe, the export is not possible. In permissive mode, however, the add\_pan option is de-activated and an exprot without pan image is conducted instead.




**Note:**

This mode may lead to unexpected behaviour and should be used with caution. 





        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

