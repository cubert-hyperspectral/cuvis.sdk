

# Struct cuvis::ViewArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**ViewArgs**](structcuvis_1_1ViewArgs.md)



_viewer settings_ 

* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)






















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**complete**](#variable-complete)  <br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**pan\_failback**](#variable-pan_failback)  <br> |
|  std::string | [**userplugin**](#variable-userplugin)  <br> |


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
|   | [**ViewArgs**](#function-viewargs) () <br> |
|   | [**operator cuvis\_export\_view\_settings\_t**](#function-operator-cuvis_export_view_settings_t) () const<br>_convert to C - SDK settings structure_  |
|   | [**operator cuvis\_viewer\_settings\_t**](#function-operator-cuvis_viewer_settings_t) () const<br>_convert to C - SDK settings structure_  |


## Public Functions inherited from cuvis::GeneralExportArgs

See [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)

| Type | Name |
| ---: | :--- |
|   | [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md#function-generalexportargs) () <br> |
|   | [**operator cuvis\_export\_general\_settings\_t**](structcuvis_1_1GeneralExportArgs.md#function-operator-cuvis_export_general_settings_t) () const<br> |






















































## Public Attributes Documentation




### variable complete 

```C++
bool cuvis::ViewArgs::complete;
```




<hr>



### variable pan\_failback 

```C++
bool cuvis::ViewArgs::pan_failback;
```




<hr>



### variable userplugin 

```C++
std::string cuvis::ViewArgs::userplugin;
```




<hr>
## Public Functions Documentation




### function ViewArgs 

```C++
cuvis::ViewArgs::ViewArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_export\_view\_settings\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::ViewArgs::operator cuvis_export_view_settings_t () const
```




<hr>



### function operator cuvis\_viewer\_settings\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::ViewArgs::operator cuvis_viewer_settings_t () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

