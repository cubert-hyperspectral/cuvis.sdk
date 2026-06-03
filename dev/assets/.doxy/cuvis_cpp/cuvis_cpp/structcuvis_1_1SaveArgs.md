

# Struct cuvis::SaveArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**SaveArgs**](structcuvis_1_1SaveArgs.md)



_Options for saving cu3s/cu3 files._ [More...](#detailed-description)

* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)






















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**allow\_drop**](#variable-allow_drop)  <br>_allow to drop measurements if internal buffers a depleted (default: false)_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**allow\_info\_file**](#variable-allow_info_file)  <br>_allow to write an additional .info file (default: true)_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**allow\_overwrite**](#variable-allow_overwrite)  <br>_allow to overwrite existing files (default: false)_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**allow\_session\_file**](#variable-allow_session_file)  <br>_allow to drop measurements if internal buffers a depleted (default: false)_  |
|  [**double**](structcuvis_1_1image__t.md) | [**fps**](#variable-fps)  <br>_The fps to be stored with a session file (default: 0)_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**full\_export**](#variable-full_export)  <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**hard\_limit**](#variable-hard_limit)  <br>_Maximum number of elements in output cache._  |
|  std::chrono::milliseconds | [**max\_buftime**](#variable-max_buftime)  <br> |
|  [**session\_merge\_mode\_t**](group__typedefs.md#typedef-session_merge_mode_t) | [**merge\_mode**](#variable-merge_mode)  <br>_allow to split to several files (default: false)_  |
|  [**operation\_mode\_t**](group__typedefs.md#typedef-operation_mode_t) | [**operation\_mode**](#variable-operation_mode)  <br>_The operation mode to be stored with a session file (default: operation\_mode\_t.OperationMode\_Software)_  |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**soft\_limit**](#variable-soft_limit)  <br>_Out-of-order frames are sorted within the cache, as long as the cache useage is below this limit._  |


## Public Attributes inherited from cuvis::GeneralExportArgs

See [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**add\_fullscale\_pan**](structcuvis_1_1GeneralExportArgs.md#variable-add_fullscale_pan)  <br>_Add a full-resolution pan image to the export (default: false)_  |
|  std::filesystem::path | [**export\_dir**](structcuvis_1_1GeneralExportArgs.md#variable-export_dir)  <br> |
|  [**struct**](structcuvis_1_1image__t.md) [**PanSharpeningArgs**](structcuvis_1_1PanSharpeningArgs.md) | [**pansharpening\_settings**](structcuvis_1_1GeneralExportArgs.md#variable-pansharpening_settings)  <br>_Settings to define Pansharpening and channel selection._  |
|  [**bool**](structcuvis_1_1image__t.md) | [**permissive**](structcuvis_1_1GeneralExportArgs.md#variable-permissive)  <br>_Set_ [_**Exporter**_](classcuvis_1_1Exporter.md) _to permisive mode (default: false)_ |






























## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**SaveArgs**](#function-saveargs) () <br> |
|   | [**operator cuvis\_save\_args\_t**](#function-operator-cuvis_save_args_t) () const<br>_convert to C - SDK settings structure_  |


## Public Functions inherited from cuvis::GeneralExportArgs

See [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)

| Type | Name |
| ---: | :--- |
|   | [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md#function-generalexportargs) () <br> |
|   | [**operator cuvis\_export\_general\_settings\_t**](structcuvis_1_1GeneralExportArgs.md#function-operator-cuvis_export_general_settings_t) () const<br> |






















































## Detailed Description


Use with either [**CubeExporter**](classcuvis_1_1CubeExporter.md) (recommended) or [**Measurement::save**](classcuvis_1_1Measurement.md#function-save) 


    
## Public Attributes Documentation




### variable allow\_drop 

_allow to drop measurements if internal buffers a depleted (default: false)_ 
```C++
bool cuvis::SaveArgs::allow_drop;
```




<hr>



### variable allow\_info\_file 

_allow to write an additional .info file (default: true)_ 
```C++
bool cuvis::SaveArgs::allow_info_file;
```




<hr>



### variable allow\_overwrite 

_allow to overwrite existing files (default: false)_ 
```C++
bool cuvis::SaveArgs::allow_overwrite;
```




<hr>



### variable allow\_session\_file 

_allow to drop measurements if internal buffers a depleted (default: false)_ 
```C++
bool cuvis::SaveArgs::allow_session_file;
```




<hr>



### variable fps 

_The fps to be stored with a session file (default: 0)_ 
```C++
double cuvis::SaveArgs::fps;
```




<hr>



### variable full\_export 

```C++
bool cuvis::SaveArgs::full_export;
```



The frame is saved including all results from processing, e.g. the cube.


        

<hr>



### variable hard\_limit 

_Maximum number of elements in output cache._ 
```C++
size_t cuvis::SaveArgs::hard_limit;
```




<hr>



### variable max\_buftime 

```C++
std::chrono::milliseconds cuvis::SaveArgs::max_buftime;
```



Any frame is forced to be written after this time, latest.


        

<hr>



### variable merge\_mode 

_allow to split to several files (default: false)_ 
```C++
session_merge_mode_t cuvis::SaveArgs::merge_mode;
```




<hr>



### variable operation\_mode 

_The operation mode to be stored with a session file (default: operation\_mode\_t.OperationMode\_Software)_ 
```C++
operation_mode_t cuvis::SaveArgs::operation_mode;
```




<hr>



### variable soft\_limit 

_Out-of-order frames are sorted within the cache, as long as the cache useage is below this limit._ 
```C++
size_t cuvis::SaveArgs::soft_limit;
```




<hr>
## Public Functions Documentation




### function SaveArgs 

```C++
cuvis::SaveArgs::SaveArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_save\_args\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::SaveArgs::operator cuvis_save_args_t () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

