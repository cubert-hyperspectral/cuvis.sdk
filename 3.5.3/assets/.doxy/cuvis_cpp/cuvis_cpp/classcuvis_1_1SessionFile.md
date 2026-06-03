

# Class cuvis::SessionFile



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**SessionFile**](classcuvis_1_1SessionFile.md)





* `#include <cuvis.hpp>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SessionFile**](#function-sessionfile-12) (std::filesystem::path [**const**](structcuvis_1_1image__t.md) & path) <br> |
|   | [**SessionFile**](#function-sessionfile-22) ([**CUVIS\_SESSION\_FILE**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  [**double**](structcuvis_1_1image__t.md) | [**get\_fps**](#function-get_fps) () const<br>_get the frame rate of this session_  |
|  [**CUVIS\_SESSION\_FILE**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_SESSION\_FILE**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |
|  std::string | [**get\_hash**](#function-get_hash) () const<br> |
|  std::optional&lt; [**Measurement**](classcuvis_1_1Measurement.md) &gt; | [**get\_mesu**](#function-get_mesu) ([**int\_t**](group__typedefs.md#typedef-int_t) frameNo, [**cuvis\_session\_item\_type\_t**](structcuvis_1_1image__t.md) type=cuvis\_session\_item\_type\_t::session\_item\_type\_frames) const<br> |
|  [**CUVIS\_OPERATION\_MODE**](structcuvis_1_1image__t.md) | [**get\_operation\_mode**](#function-get_operation_mode) () const<br>_get operation mode of the session_  |
|  std::optional&lt; [**Measurement**](classcuvis_1_1Measurement.md) &gt; | [**get\_ref**](#function-get_ref) ([**int\_t**](group__typedefs.md#typedef-int_t) refNo, [**cuvis\_reference\_type\_t**](structcuvis_1_1image__t.md) type) const<br> |
|  [**int\_t**](group__typedefs.md#typedef-int_t) | [**get\_size**](#function-get_size) ([**cuvis\_session\_item\_type\_t**](structcuvis_1_1image__t.md) type=cuvis\_session\_item\_type\_t::session\_item\_type\_frames) const<br>_get size of the_ [_**SessionFile**_](classcuvis_1_1SessionFile.md) __ |
|  [**common\_image\_t**](structcuvis_1_1common__image__t.md)&lt; std::uint8\_t &gt; | [**get\_thumbnail**](#function-get_thumbnail) () const<br> |




























## Public Functions Documentation




### function SessionFile [1/2]

```C++
cuvis::SessionFile::SessionFile (
    std::filesystem::path const & path
) 
```




<hr>



### function SessionFile [2/2]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::SessionFile::SessionFile (
    CUVIS_SESSION_FILE handle
) 
```




<hr>



### function get\_fps 

_get the frame rate of this session_ 
```C++
double cuvis::SessionFile::get_fps () const
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_SESSION_FILE cuvis::SessionFile::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_SESSION_FILE cuvis::SessionFile::get_handle_copy () const
```




<hr>



### function get\_hash 

```C++
std::string cuvis::SessionFile::get_hash () const
```




<hr>



### function get\_mesu 

```C++
std::optional< Measurement > cuvis::SessionFile::get_mesu (
    int_t frameNo,
    cuvis_session_item_type_t type=cuvis_session_item_type_t::session_item_type_frames
) const
```




<hr>



### function get\_operation\_mode 

_get operation mode of the session_ 
```C++
CUVIS_OPERATION_MODE cuvis::SessionFile::get_operation_mode () const
```




<hr>



### function get\_ref 

```C++
std::optional< Measurement > cuvis::SessionFile::get_ref (
    int_t refNo,
    cuvis_reference_type_t type
) const
```




<hr>



### function get\_size 

_get size of the_ [_**SessionFile**_](classcuvis_1_1SessionFile.md) __
```C++
int_t cuvis::SessionFile::get_size (
    cuvis_session_item_type_t type=cuvis_session_item_type_t::session_item_type_frames
) const
```




<hr>



### function get\_thumbnail 

```C++
common_image_t < std::uint8_t > cuvis::SessionFile::get_thumbnail () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

