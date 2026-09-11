

# Struct cuvis::CalibrationInfo



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**CalibrationInfo**](structcuvis_1_1CalibrationInfo.md)





* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::string | [**annotation\_name**](#variable-annotation_name)  <br> |
|  [**timestamp\_t**](namespacecuvis.md#typedef-timestamp_t) | [**calibration\_date**](#variable-calibration_date)  <br> |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**cube\_channels**](#variable-cube_channels)  <br> |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**cube\_height**](#variable-cube_height)  <br> |
|  std::vector&lt; [**uint32\_t**](structcuvis_1_1image__t.md) &gt; [**const**](structcuvis_1_1image__t.md) | [**cube\_wavelengths**](#variable-cube_wavelengths)  <br> |
|  [**uint32\_t**](structcuvis_1_1image__t.md) | [**cube\_width**](#variable-cube_width)  <br> |
|  std::string | [**file\_path**](#variable-file_path)  <br> |
|  std::string | [**model\_name**](#variable-model_name)  <br> |
|  std::string | [**serial\_no**](#variable-serial_no)  <br> |
|  std::string | [**unique\_id**](#variable-unique_id)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**CalibrationInfo**](#function-calibrationinfo) ([**calibration\_info\_t**](group__typedefs.md#typedef-calibration_info_t) [**const**](structcuvis_1_1image__t.md) & calib) <br> |




























## Public Attributes Documentation




### variable annotation\_name 

```C++
std::string cuvis::CalibrationInfo::annotation_name;
```




<hr>



### variable calibration\_date 

```C++
timestamp_t cuvis::CalibrationInfo::calibration_date;
```




<hr>



### variable cube\_channels 

```C++
uint32_t cuvis::CalibrationInfo::cube_channels;
```




<hr>



### variable cube\_height 

```C++
uint32_t cuvis::CalibrationInfo::cube_height;
```




<hr>



### variable cube\_wavelengths 

```C++
std::vector<uint32_t> const cuvis::CalibrationInfo::cube_wavelengths;
```




<hr>



### variable cube\_width 

```C++
uint32_t cuvis::CalibrationInfo::cube_width;
```




<hr>



### variable file\_path 

```C++
std::string cuvis::CalibrationInfo::file_path;
```




<hr>



### variable model\_name 

```C++
std::string cuvis::CalibrationInfo::model_name;
```




<hr>



### variable serial\_no 

```C++
std::string cuvis::CalibrationInfo::serial_no;
```




<hr>



### variable unique\_id 

```C++
std::string cuvis::CalibrationInfo::unique_id;
```




<hr>
## Public Functions Documentation




### function CalibrationInfo 

```C++
cuvis::CalibrationInfo::CalibrationInfo (
    calibration_info_t  const & calib
) 
```



Constructor to create session info from session 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

