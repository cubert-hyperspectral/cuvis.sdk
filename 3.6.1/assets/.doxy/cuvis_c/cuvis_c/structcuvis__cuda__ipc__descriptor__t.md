

# Struct cuvis\_cuda\_ipc\_descriptor\_t



[**ClassList**](annotated.md) **>** [**cuvis\_cuda\_ipc\_descriptor\_t**](structcuvis__cuda__ipc__descriptor__t.md)





* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  uint32\_t | [**\_pad**](#variable-_pad)  <br> |
|  uint64\_t | [**alloc\_size**](#variable-alloc_size)  <br> |
|  int32\_t | [**backend**](#variable-backend)  <br> |
|  uint8\_t | [**blob**](#variable-blob)  <br> |
|  uint32\_t | [**blob\_len**](#variable-blob_len)  <br> |
|  int32\_t | [**device\_ordinal**](#variable-device_ordinal)  <br> |
|  uint64\_t | [**exporter\_pid**](#variable-exporter_pid)  <br> |
|  int32\_t | [**handle\_type**](#variable-handle_type)  <br> |
|  uint64\_t | [**offset**](#variable-offset)  <br> |
|  uint8\_t | [**ptr\_blob**](#variable-ptr_blob)  <br> |
|  uint32\_t | [**ptr\_blob\_len**](#variable-ptr_blob_len)  <br> |
|  uint64\_t | [**size**](#variable-size)  <br> |












































## Public Attributes Documentation




### variable \_pad 

```C++
uint32_t cuvis_cuda_ipc_descriptor_t::_pad;
```




<hr>



### variable alloc\_size 

```C++
uint64_t cuvis_cuda_ipc_descriptor_t::alloc_size;
```




<hr>



### variable backend 

```C++
int32_t cuvis_cuda_ipc_descriptor_t::backend;
```




<hr>



### variable blob 

```C++
uint8_t cuvis_cuda_ipc_descriptor_t::blob[CUVIS_CUDA_IPC_BLOB_MAX];
```




<hr>



### variable blob\_len 

```C++
uint32_t cuvis_cuda_ipc_descriptor_t::blob_len;
```




<hr>



### variable device\_ordinal 

```C++
int32_t cuvis_cuda_ipc_descriptor_t::device_ordinal;
```




<hr>



### variable exporter\_pid 

```C++
uint64_t cuvis_cuda_ipc_descriptor_t::exporter_pid;
```




<hr>



### variable handle\_type 

```C++
int32_t cuvis_cuda_ipc_descriptor_t::handle_type;
```




<hr>



### variable offset 

```C++
uint64_t cuvis_cuda_ipc_descriptor_t::offset;
```




<hr>



### variable ptr\_blob 

```C++
uint8_t cuvis_cuda_ipc_descriptor_t::ptr_blob[CUVIS_CUDA_IPC_PTR_BLOB_MAX];
```




<hr>



### variable ptr\_blob\_len 

```C++
uint32_t cuvis_cuda_ipc_descriptor_t::ptr_blob_len;
```




<hr>



### variable size 

```C++
uint64_t cuvis_cuda_ipc_descriptor_t::size;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

