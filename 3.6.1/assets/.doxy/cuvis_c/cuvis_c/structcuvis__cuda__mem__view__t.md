

# Struct cuvis\_cuda\_mem\_view\_t



[**ClassList**](annotated.md) **>** [**cuvis\_cuda\_mem\_view\_t**](structcuvis__cuda__mem__view__t.md)



[More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  int32\_t | [**device\_ordinal**](#variable-device_ordinal)  <br> |
|  const void \* | [**device\_ptr**](#variable-device_ptr)  <br> |
|  uint64\_t | [**size**](#variable-size)  <br> |












































## Detailed Description


Raw device pointer + size + device for wrapping in-process (e.g. as a torch tensor via **cuda\_array\_interface** / DLPack). Does NOT create an IPC handle. The device\_ptr is read-only from the SDK's side; external code that maps it may still write the memory. 


    
## Public Attributes Documentation




### variable device\_ordinal 

```C++
int32_t cuvis_cuda_mem_view_t::device_ordinal;
```




<hr>



### variable device\_ptr 

```C++
const void* cuvis_cuda_mem_view_t::device_ptr;
```




<hr>



### variable size 

```C++
uint64_t cuvis_cuda_mem_view_t::size;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

