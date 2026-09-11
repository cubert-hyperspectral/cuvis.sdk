

# Struct cuvis\_component\_info\_t



[**ClassList**](annotated.md) **>** [**cuvis\_component\_info\_t**](structcuvis__component__info__t.md)



[More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**displayname**](#variable-displayname)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**pixelformat**](#variable-pixelformat)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**sensorinfo**](#variable-sensorinfo)  <br> |
|  [**CUVIS\_COMPONENT\_TYPE**](cuvis_8h.md#define-cuvis_component_type) | [**type**](#variable-type)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**userfield**](#variable-userfield)  <br> |












































## Detailed Description


Information about components 


    
## Public Attributes Documentation




### variable displayname 

```C++
CUVIS_CHAR cuvis_component_info_t::displayname[CUVIS_MAXBUF];
```



the name that can be displayed human-readable 


        

<hr>



### variable pixelformat 

```C++
CUVIS_CHAR cuvis_component_info_t::pixelformat[CUVIS_MAXBUF];
```



additional sensor informaiton 


        

<hr>



### variable sensorinfo 

```C++
CUVIS_CHAR cuvis_component_info_t::sensorinfo[CUVIS_MAXBUF];
```



the sensor's meta-informaiton 


        

<hr>



### variable type 

```C++
CUVIS_COMPONENT_TYPE cuvis_component_info_t::type;
```



type of the component 


        

<hr>



### variable userfield 

```C++
CUVIS_CHAR cuvis_component_info_t::userfield[CUVIS_MAXBUF];
```



additional sensor informaiton 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

