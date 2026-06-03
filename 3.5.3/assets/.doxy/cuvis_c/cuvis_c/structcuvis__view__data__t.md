

# Struct cuvis\_view\_data\_t



[**ClassList**](annotated.md) **>** [**cuvis\_view\_data\_t**](structcuvis__view__data__t.md)



_The view meta structure._ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_VIEW\_CATEGORY**](cuvis_8h.md#define-cuvis_view_category) | [**category**](#variable-category)  <br> |
|  [**CUVIS\_IMBUFFER**](cuvis_8h.md#define-cuvis_imbuffer) | [**data**](#variable-data)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**id**](#variable-id)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**show**](#variable-show)  <br> |












































## Public Attributes Documentation




### variable category 

```C++
CUVIS_VIEW_CATEGORY cuvis_view_data_t::category;
```



the type of view data 


        

<hr>



### variable data 

```C++
CUVIS_IMBUFFER cuvis_view_data_t::data;
```



the actual data. View data is always 8 bit, i.e. imbuffer bytes = 1 


        

<hr>



### variable id 

```C++
CUVIS_CHAR cuvis_view_data_t::id[CUVIS_MAXBUF];
```



The id of the view 


        

<hr>



### variable show 

```C++
CUVIS_INT cuvis_view_data_t::show;
```



1 if dataset is intended for showing, 0 else 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

