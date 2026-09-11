

# Class cuvis::CudaImage



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**CudaImage**](classcuvis_1_1CudaImage.md)



_Image data from a measurement that stays resident in CUDA device memory._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|  std::size\_t | [**bytes\_per\_element**](#function-bytes_per_element) () const<br> |
|  std::size\_t | [**channels**](#function-channels) () const<br> |
|  [**cuvis\_imbuffer\_format\_t**](structcuvis_1_1image__t.md) | [**format**](#function-format) () const<br> |
|  std::size\_t | [**height**](#function-height) () const<br> |
|  [**CudaIpcExport**](classcuvis_1_1CudaIpcExport.md) | [**make\_ipc**](#function-make_ipc) ([**cuda\_ipc\_backend\_t**](group__cuda.md#enum-cuda_ipc_backend_t) backend) const<br> |
|  std::size\_t | [**size\_in\_bytes**](#function-size_in_bytes) () const<br> |
|  [**cuda\_mem\_view\_t**](group__cuda.md#typedef-cuda_mem_view_t) | [**view**](#function-view) () const<br> |
|  std::uint32\_t [**const**](structcuvis_1_1image__t.md) \* | [**wavelength**](#function-wavelength) () const<br> |
|  std::size\_t | [**width**](#function-width) () const<br> |




























## Detailed Description


Obtained from [**Measurement::cuda\_image**](classcuvis_1_1Measurement.md#function-cuda_image). Mirrors [**image\_t**](structcuvis_1_1image__t.md), except the host pointer is replaced by a device buffer reachable through [**view**](classcuvis_1_1CudaImage.md#function-view) (same process) or [**make\_ipc**](classcuvis_1_1CudaImage.md#function-make_ipc) (another process). 


    
## Public Functions Documentation




### function bytes\_per\_element 

```C++
inline std::size_t cuvis::CudaImage::bytes_per_element () const
```



bytes per element 


        

<hr>



### function channels 

```C++
inline std::size_t cuvis::CudaImage::channels () const
```




<hr>



### function format 

```C++
inline cuvis_imbuffer_format_t cuvis::CudaImage::format () const
```




<hr>



### function height 

```C++
inline std::size_t cuvis::CudaImage::height () const
```




<hr>



### function make\_ipc 

```C++
CudaIpcExport cuvis::CudaImage::make_ipc (
    cuda_ipc_backend_t backend
) const
```




<hr>



### function size\_in\_bytes 

```C++
inline std::size_t cuvis::CudaImage::size_in_bytes () const
```



total bytes of the device buffer 


        

<hr>



### function view 

```C++
cuda_mem_view_t cuvis::CudaImage::view () const
```




<hr>



### function wavelength 

```C++
inline std::uint32_t const * cuvis::CudaImage::wavelength () const
```



wavelength vector, nullptr or an array of [**channels**](classcuvis_1_1CudaImage.md#function-channels) entries in nano meter 


        

<hr>



### function width 

```C++
inline std::size_t cuvis::CudaImage::width () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

