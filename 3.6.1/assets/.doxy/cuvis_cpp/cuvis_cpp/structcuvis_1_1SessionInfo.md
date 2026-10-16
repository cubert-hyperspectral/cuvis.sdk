

# Struct cuvis::SessionInfo



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**SessionInfo**](structcuvis_1_1SessionInfo.md)





* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::string | [**name**](#variable-name)  <br> |
|  [**unsigned**](structcuvis_1_1image__t.md) | [**sequence\_no**](#variable-sequence_no)  <br> |
|  [**unsigned**](structcuvis_1_1image__t.md) | [**session\_no**](#variable-session_no)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SessionInfo**](#function-sessioninfo-12) () <br> |
|   | [**SessionInfo**](#function-sessioninfo-22) ([**session\_info\_t**](group__typedefs.md#typedef-session_info_t) [**const**](structcuvis_1_1image__t.md) & sess) <br> |
|   | [**operator session\_info\_t**](#function-operator-session_info_t) () const<br>_convert to C - SDK settings structure_  |




























## Public Attributes Documentation




### variable name 

```C++
std::string cuvis::SessionInfo::name;
```




<hr>



### variable sequence\_no 

```C++
unsigned cuvis::SessionInfo::sequence_no;
```




<hr>



### variable session\_no 

```C++
unsigned cuvis::SessionInfo::session_no;
```




<hr>
## Public Functions Documentation




### function SessionInfo [1/2]

```C++
cuvis::SessionInfo::SessionInfo () 
```



Constructor to create default parameters 


        

<hr>



### function SessionInfo [2/2]

```C++
cuvis::SessionInfo::SessionInfo (
    session_info_t  const & sess
) 
```



Constructor to create session info from session 


        

<hr>



### function operator session\_info\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::SessionInfo::operator session_info_t () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

