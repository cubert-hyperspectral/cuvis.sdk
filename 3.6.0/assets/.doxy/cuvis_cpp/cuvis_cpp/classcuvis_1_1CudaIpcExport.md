

# Class cuvis::CudaIpcExport



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**CudaIpcExport**](classcuvis_1_1CudaIpcExport.md)



_A live cross-process export of a device buffer._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**cuda\_ipc\_backend\_t**](group__cuda.md#enum-cuda_ipc_backend_t) | [**backend**](#function-backend) () const<br> |
|  [**cuda\_ipc\_descriptor\_t**](group__cuda.md#typedef-cuda_ipc_descriptor_t) [**const**](structcuvis_1_1image__t.md) & | [**descriptor**](#function-descriptor) () const<br> |
|  [**cuda\_ipc\_handle\_type\_t**](group__cuda.md#enum-cuda_ipc_handle_type_t) | [**handle\_type**](#function-handle_type) () const<br> |




























## Detailed Description


Holds the descriptor a consumer needs to map the buffer. There is no cross-process refcount: the consumer's mapping stays valid only while this object is alive. 


    
## Public Functions Documentation




### function backend 

```C++
inline cuda_ipc_backend_t cuvis::CudaIpcExport::backend () const
```




<hr>



### function descriptor 

```C++
inline cuda_ipc_descriptor_t  const & cuvis::CudaIpcExport::descriptor () const
```




<hr>



### function handle\_type 

```C++
inline cuda_ipc_handle_type_t cuvis::CudaIpcExport::handle_type () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

