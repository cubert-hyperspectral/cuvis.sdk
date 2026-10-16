

# Struct cuvis\_session\_info\_t



[**ClassList**](annotated.md) **>** [**cuvis\_session\_info\_t**](structcuvis__session__info__t.md)



[More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**name**](#variable-name)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**sequence\_no**](#variable-sequence_no)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**session\_no**](#variable-session_no)  <br> |












































## Detailed Description


internal session\_info info of acquisition context 


    
## Public Attributes Documentation




### variable name 

```C++
CUVIS_CHAR cuvis_session_info_t::name[CUVIS_MAXBUF];
```



session\_info name 


        

<hr>



### variable sequence\_no 

```C++
CUVIS_INT cuvis_session_info_t::sequence_no;
```



Sequence number. Increases with each recorded frame. Reset, if session\_no changes 


        

<hr>



### variable session\_no 

```C++
CUVIS_INT cuvis_session_info_t::session_no;
```



SessionFile number. Will be increased by stopping & starting recording 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

