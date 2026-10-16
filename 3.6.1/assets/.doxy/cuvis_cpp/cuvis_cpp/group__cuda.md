

# Group cuda



[**Modules**](modules.md) **>** [**cuda**](group__cuda.md)



[More...](#detailed-description)
















## Classes

| Type | Name |
| ---: | :--- |
| class | [**cuvis::CudaImage**](classcuvis_1_1CudaImage.md) <br>_Image data from a measurement that stays resident in CUDA device memory._  |
| class | [**cuvis::CudaIpcExport**](classcuvis_1_1CudaIpcExport.md) <br>_A live cross-process export of a device buffer._  |
| class | [**cuvis::cuda\_unavailable\_error**](classcuvis_1_1cuda__unavailable__error.md) <br>_The loaded cuvis library does not provide a CUDA function that was called._  |


## Public Types

| Type | Name |
| ---: | :--- |
| typedef cuvis\_cuda\_imbuffer\_t | [**cuda\_imbuffer\_t**](#typedef-cuda_imbuffer_t)  <br>_Image buffer described by a device handle._  |
| enum int | [**cuda\_ipc\_backend\_t**](#enum-cuda_ipc_backend_t)  <br>_IPC transport backing a device buffer export._  |
| typedef cuvis\_cuda\_ipc\_descriptor\_t | [**cuda\_ipc\_descriptor\_t**](#typedef-cuda_ipc_descriptor_t)  <br>_Everything a consumer needs to map an exported buffer._  |
| enum int | [**cuda\_ipc\_handle\_type\_t**](#enum-cuda_ipc_handle_type_t)  <br>_Kind of OS handle carried in a descriptor's blob._  |
| typedef CUVIS\_HANDLE | [**cuda\_ipc\_t**](#typedef-cuda_ipc_t)  <br>_handle to an active ipc export registration_  |
| typedef CUVIS\_HANDLE | [**cuda\_mem\_t**](#typedef-cuda_mem_t)  <br>_handle to a shareable CUDA device buffer_  |
| typedef cuvis\_cuda\_mem\_view\_t | [**cuda\_mem\_view\_t**](#typedef-cuda_mem_view_t)  <br>_Raw device pointer, size and device index._  |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  bool | [**cuda\_ipc\_backend\_available**](#function-cuda_ipc_backend_available) (cuda\_ipc\_backend\_t backend) <br>_Whether this device and driver support one IPC backend._  |
|  std::vector&lt; std::string &gt; const & | [**cuda\_missing\_symbols**](#function-cuda_missing_symbols) () <br>_The CUDA entry points the loaded cuvis library did not provide._  |
|  bool | [**cuda\_supported**](#function-cuda_supported) () <br>_Whether the loaded cuvis library provides every CUDA entry point._  |




























## Detailed Description


The CUDA entry points are looked up in the loaded cuvis library at first use instead of being imported at link time, so an older library is a degraded run rather than a dead process. The declarations still come from cuvis.h, so the header must have the CUDA block even when the library turns out not to export it. Two questions are kept apart because they fail for different reasons: [**cuda\_supported**](group__cuda.md#function-cuda_supported) asks whether the library provides the functions, [**cuda\_ipc\_backend\_available**](group__cuda.md#function-cuda_ipc_backend_available) asks whether this device and driver support a transport.


Nothing here needs the CUDA toolkit. The device pointer is handed out as an opaque address for a consumer to wrap. 


    
## Public Types Documentation




### typedef cuda\_imbuffer\_t 

_Image buffer described by a device handle._ 
```
using cuvis::cuda_imbuffer_t = typedef cuvis_cuda_imbuffer_t;
```




<hr>



### enum cuda\_ipc\_backend\_t 

_IPC transport backing a device buffer export._ 
```
enum cuda_ipc_backend_t {
    automatic = CUVIS_CUDA_IPC_BACKEND_AUTO,
    pool = CUVIS_CUDA_IPC_BACKEND_POOL,
    legacy = CUVIS_CUDA_IPC_BACKEND_LEGACY,
    vmm = CUVIS_CUDA_IPC_BACKEND_VMM
};
```




<hr>



### typedef cuda\_ipc\_descriptor\_t 

_Everything a consumer needs to map an exported buffer._ 
```
using cuvis::cuda_ipc_descriptor_t = typedef cuvis_cuda_ipc_descriptor_t;
```




<hr>



### enum cuda\_ipc\_handle\_type\_t 

_Kind of OS handle carried in a descriptor's blob._ 
```
enum cuda_ipc_handle_type_t {
    none = CUVIS_CUDA_IPC_HANDLE_NONE,
    win32 = CUVIS_CUDA_IPC_HANDLE_WIN32,
    win32_kmt = CUVIS_CUDA_IPC_HANDLE_WIN32_KMT,
    posix_fd = CUVIS_CUDA_IPC_HANDLE_POSIX_FD
};
```




<hr>



### typedef cuda\_ipc\_t 

_handle to an active ipc export registration_ 
```
using cuvis::cuda_ipc_t = typedef CUVIS_HANDLE;
```




<hr>



### typedef cuda\_mem\_t 

_handle to a shareable CUDA device buffer_ 
```
using cuvis::cuda_mem_t = typedef CUVIS_HANDLE;
```




<hr>



### typedef cuda\_mem\_view\_t 

_Raw device pointer, size and device index._ 
```
using cuvis::cuda_mem_view_t = typedef cuvis_cuda_mem_view_t;
```




<hr>
## Public Functions Documentation




### function cuda\_ipc\_backend\_available 

_Whether this device and driver support one IPC backend._ 
```
bool cuda_ipc_backend_available (
    cuda_ipc_backend_t backend
) 
```



Returns false rather than throwing when the library provides no CUDA API, so a caller can ask both questions with one call.


        

<hr>



### function cuda\_missing\_symbols 

_The CUDA entry points the loaded cuvis library did not provide._ 
```
std::vector< std::string > const & cuda_missing_symbols () 
```



Empty when [**cuda\_supported**](group__cuda.md#function-cuda_supported) is true. Naming them is the only field diagnostic that separates an old SDK from a device that cannot do IPC. 


        

<hr>



### function cuda\_supported 

_Whether the loaded cuvis library provides every CUDA entry point._ 
```
bool cuda_supported () 
```



Answers only the library question and never touches the device. Cheap and cached; safe to call before [**General::init**](classcuvis_1_1General.md#function-init). 


        

<hr>

------------------------------


