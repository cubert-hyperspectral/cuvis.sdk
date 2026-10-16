

# Class cuvis::cuvis\_sdk\_exception



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**cuvis\_sdk\_exception**](classcuvis_1_1cuvis__sdk__exception.md)





* `#include <cuvis.hpp>`



Inherits the following classes: std::exception


































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**cuvis\_sdk\_exception**](#function-cuvis_sdk_exception) (std::string [**const**](structcuvis_1_1image__t.md) & msg, std::wstring [**const**](structcuvis_1_1image__t.md) & wmsg) <br> |
|  [**char**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md) \* | [**what**](#function-what) ([**void**](structcuvis_1_1image__t.md)) noexcept const<br> |
|  std::wstring | [**what\_wstr**](#function-what_wstr) ([**void**](structcuvis_1_1image__t.md)) noexcept const<br> |








## Protected Attributes

| Type | Name |
| ---: | :--- |
|  std::string [**const**](structcuvis_1_1image__t.md) | [**\_msg**](#variable-_msg)  <br> |
|  std::wstring [**const**](structcuvis_1_1image__t.md) | [**\_wmsg**](#variable-_wmsg)  <br> |




















## Public Functions Documentation




### function cuvis\_sdk\_exception 

```C++
cuvis::cuvis_sdk_exception::cuvis_sdk_exception (
    std::string const & msg,
    std::wstring const & wmsg
) 
```




<hr>



### function what 

```C++
char  const * cuvis::cuvis_sdk_exception::what (
    void
) noexcept const
```




<hr>



### function what\_wstr 

```C++
std::wstring cuvis::cuvis_sdk_exception::what_wstr (
    void
) noexcept const
```




<hr>
## Protected Attributes Documentation




### variable \_msg 

```C++
std::string const cuvis::cuvis_sdk_exception::_msg;
```




<hr>



### variable \_wmsg 

```C++
std::wstring const cuvis::cuvis_sdk_exception::_wmsg;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

