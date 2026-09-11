

# Group cuvis\_cuda



[**Modules**](modules.md) **>** [**cuvis\_cuda**](group__cuvis__cuda.md)




















## Classes

| Type | Name |
| ---: | :--- |
| struct | [**cuvis\_cuda\_imbuffer\_t**](structcuvis__cuda__imbuffer__t.md) <br> |
| struct | [**cuvis\_cuda\_ipc\_descriptor\_t**](structcuvis__cuda__ipc__descriptor__t.md) <br> |
| struct | [**cuvis\_cuda\_mem\_view\_t**](structcuvis__cuda__mem__view__t.md) <br> |


## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**group\_\_cuvis\_\_cuda\_1ga06fc87d81c62e9abb8790b6e5713c55b**](#enum-group__cuvis__cuda_1ga06fc87d81c62e9abb8790b6e5713c55b)  <br> |
| enum  | [**group\_\_cuvis\_\_cuda\_1ga99fb83031ce9923c84392b4e92f956b5**](#enum-group__cuvis__cuda_1ga99fb83031ce9923c84392b4e92f956b5)  <br> |
| enum  | [**group\_\_cuvis\_\_cuda\_1gabc6126af1d45847bc59afa0aa3216b04**](#enum-group__cuvis__cuda_1gabc6126af1d45847bc59afa0aa3216b04)  <br> |
| enum  | [**group\_\_cuvis\_\_cuda\_1gadf764cbdea00d65edcd07bb9953ad2b7**](#enum-group__cuvis__cuda_1gadf764cbdea00d65edcd07bb9953ad2b7)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_ipc\_backend\_available**](#function-cuvis_cuda_ipc_backend_available) (int i\_backend, int \* o\_pAvailable) <br>_Check if a specific IPC backend is available. Support of the different IPC backends varies._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_ipc\_get\_descriptor**](#function-cuvis_cuda_ipc_get_descriptor) ([**CUVIS\_CUDA\_IPC**](group__cuvis__cuda.md#define-cuvis_cuda_ipc) i\_ipc, [**CUVIS\_CUDA\_IPC\_DESCRIPTOR**](group__cuvis__cuda.md#define-cuvis_cuda_ipc_descriptor) \* o\_pDesc) <br>_Returns the IPC specific information of the underlying handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_ipc\_handle\_create**](#function-cuvis_cuda_ipc_handle_create) ([**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem) i\_mem, int i\_backend, [**CUVIS\_CUDA\_IPC**](group__cuvis__cuda.md#define-cuvis_cuda_ipc) \* o\_pIpc) <br>_Registers an cuda memory allocation to be used with cudas IPC protocols._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_ipc\_handle\_free**](#function-cuvis_cuda_ipc_handle_free) ([**CUVIS\_CUDA\_IPC**](group__cuvis__cuda.md#define-cuvis_cuda_ipc) \* i\_ipc) <br>_Frees a cuda ipc handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_mem\_copy\_handle**](#function-cuvis_cuda_mem_copy_handle) ([**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem) i\_mem, [**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem) \* o\_pCopy) <br>_Make a copy of the supplied cuda memory handle. Afterwards both handles need to be freed for the underlying memory to be released._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_mem\_free**](#function-cuvis_cuda_mem_free) ([**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem) \* i\_mem) <br>_Frees a cuda memory hanlde._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_cuda\_mem\_get\_view**](#function-cuvis_cuda_mem_get_view) ([**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem) i\_mem, [**CUVIS\_CUDA\_MEM\_VIEW**](group__cuvis__cuda.md#define-cuvis_cuda_mem_view) \* o\_pView) <br>_return the raw device pointer + size + device index for wrapping it in the same process._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) | [**cuvis\_measurement\_get\_data\_image\_cuda**](#function-cuvis_measurement_get_data_image_cuda) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_CUDA\_IMBUFFER**](group__cuvis__cuda.md#define-cuvis_cuda_imbuffer) \* o\_pBuf) <br> |



























## Macros

| Type | Name |
| ---: | :--- |
| define  | [**CUVIS\_CUDA\_IMBUFFER**](group__cuvis__cuda.md#define-cuvis_cuda_imbuffer)  `struct [**cuvis\_cuda\_imbuffer\_t**](structcuvis__cuda__imbuffer__t.md)`<br> |
| define  | [**CUVIS\_CUDA\_IPC**](group__cuvis__cuda.md#define-cuvis_cuda_ipc)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_CUDA\_IPC\_DESCRIPTOR**](group__cuvis__cuda.md#define-cuvis_cuda_ipc_descriptor)  `struct [**cuvis\_cuda\_ipc\_descriptor\_t**](structcuvis__cuda__ipc__descriptor__t.md)`<br> |
| define  | [**CUVIS\_CUDA\_MEM**](group__cuvis__cuda.md#define-cuvis_cuda_mem)  `[**CUVIS\_HANDLE**](cuvis_8h.md#define-cuvis_handle)`<br> |
| define  | [**CUVIS\_CUDA\_MEM\_VIEW**](group__cuvis__cuda.md#define-cuvis_cuda_mem_view)  `struct [**cuvis\_cuda\_mem\_view\_t**](structcuvis__cuda__mem__view__t.md)`<br> |

## Public Types Documentation




### enum group\_\_cuvis\_\_cuda\_1ga06fc87d81c62e9abb8790b6e5713c55b 

```
enum group__cuvis__cuda_1ga06fc87d81c62e9abb8790b6e5713c55b {
    CUVIS_CUDA_IPC_BACKEND_AUTO = 0,
    CUVIS_CUDA_IPC_BACKEND_POOL = 1,
    CUVIS_CUDA_IPC_BACKEND_LEGACY = 2,
    CUVIS_CUDA_IPC_BACKEND_VMM = 3
};
```




<hr>



### enum group\_\_cuvis\_\_cuda\_1ga99fb83031ce9923c84392b4e92f956b5 

```
enum group__cuvis__cuda_1ga99fb83031ce9923c84392b4e92f956b5 {
    CUVIS_CUDA_IPC_BLOB_MAX = 64
};
```




<hr>



### enum group\_\_cuvis\_\_cuda\_1gabc6126af1d45847bc59afa0aa3216b04 

```
enum group__cuvis__cuda_1gabc6126af1d45847bc59afa0aa3216b04 {
    CUVIS_CUDA_IPC_PTR_BLOB_MAX = 64
};
```




<hr>



### enum group\_\_cuvis\_\_cuda\_1gadf764cbdea00d65edcd07bb9953ad2b7 

```
enum group__cuvis__cuda_1gadf764cbdea00d65edcd07bb9953ad2b7 {
    CUVIS_CUDA_IPC_HANDLE_NONE = 0,
    CUVIS_CUDA_IPC_HANDLE_WIN32 = 1,
    CUVIS_CUDA_IPC_HANDLE_WIN32_KMT = 2,
    CUVIS_CUDA_IPC_HANDLE_POSIX_FD = 3
};
```




<hr>
## Public Functions Documentation




### function cuvis\_cuda\_ipc\_backend\_available 

_Check if a specific IPC backend is available. Support of the different IPC backends varies._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_ipc_backend_available (
    int i_backend,
    int * o_pAvailable
) 
```





**Parameters:**


* `i_backend` The backend to be checked. See CUVIS\_CUDA\_IPC\_BACKEND\_ for supported values 
* `o_pAvailable` Indicates if the request IPC backend is available 




        

<hr>



### function cuvis\_cuda\_ipc\_get\_descriptor 

_Returns the IPC specific information of the underlying handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_ipc_get_descriptor (
    CUVIS_CUDA_IPC i_ipc,
    CUVIS_CUDA_IPC_DESCRIPTOR * o_pDesc
) 
```



The meaning of the values differs depending on which cuda backend IPC protocol is used. 

**Parameters:**


* `i_mem` The cuda memory handle 
* `o_pDesc` The IPC descriptor that is going to be filled 




        

<hr>



### function cuvis\_cuda\_ipc\_handle\_create 

_Registers an cuda memory allocation to be used with cudas IPC protocols._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_ipc_handle_create (
    CUVIS_CUDA_MEM i_mem,
    int i_backend,
    CUVIS_CUDA_IPC * o_pIpc
) 
```



This is only supported for specific implementations. For the memory to be released both handles need to be freed. 

**Parameters:**


* `i_mem` The cuda memory handle 
* `o_pIpc` The new cuda ipc handle 




        

<hr>



### function cuvis\_cuda\_ipc\_handle\_free 

_Frees a cuda ipc handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_ipc_handle_free (
    CUVIS_CUDA_IPC * i_ipc
) 
```





**Parameters:**


* `i_ipc` The cuda memory handle 




        

<hr>



### function cuvis\_cuda\_mem\_copy\_handle 

_Make a copy of the supplied cuda memory handle. Afterwards both handles need to be freed for the underlying memory to be released._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_mem_copy_handle (
    CUVIS_CUDA_MEM i_mem,
    CUVIS_CUDA_MEM * o_pCopy
) 
```





**Parameters:**


* `i_mem` The cuda memory handle 
* `o_pCopy` The new cuda memory handle 




        

<hr>



### function cuvis\_cuda\_mem\_free 

_Frees a cuda memory hanlde._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_mem_free (
    CUVIS_CUDA_MEM * i_mem
) 
```





**Parameters:**


* `i_mem` The cuda memory handle 




        

<hr>



### function cuvis\_cuda\_mem\_get\_view 

_return the raw device pointer + size + device index for wrapping it in the same process._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_cuda_mem_get_view (
    CUVIS_CUDA_MEM i_mem,
    CUVIS_CUDA_MEM_VIEW * o_pView
) 
```





**Parameters:**


* `i_mem` The cuda memory handle 
* `o_pView` Returns device pointer + size + device index 




        

<hr>



### function cuvis\_measurement\_get\_data\_image\_cuda 

```
SDK_CAPI  CUVIS_STATUS cuvis_measurement_get_data_image_cuda (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_CUDA_IMBUFFER * o_pBuf
) 
```




<hr>
## Macro Definition Documentation





### define CUVIS\_CUDA\_IMBUFFER 

```
#define CUVIS_CUDA_IMBUFFER `struct cuvis_cuda_imbuffer_t`
```




<hr>



### define CUVIS\_CUDA\_IPC 

```
#define CUVIS_CUDA_IPC `CUVIS_HANDLE`
```



handle to an active ipc export registration; 


        

<hr>



### define CUVIS\_CUDA\_IPC\_DESCRIPTOR 

```
#define CUVIS_CUDA_IPC_DESCRIPTOR `struct cuvis_cuda_ipc_descriptor_t`
```




<hr>



### define CUVIS\_CUDA\_MEM 

```
#define CUVIS_CUDA_MEM `CUVIS_HANDLE`
```



handle to a shareable CUDA device buffer 


        

<hr>



### define CUVIS\_CUDA\_MEM\_VIEW 

```
#define CUVIS_CUDA_MEM_VIEW `struct cuvis_cuda_mem_view_t`
```




<hr>

------------------------------


