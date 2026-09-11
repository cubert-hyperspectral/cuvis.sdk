

# Struct cuvis::TiffArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**TiffArgs**](structcuvis_1_1TiffArgs.md)



_Additional settings for exporting tiff._ 

* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)






















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**tiff\_compression\_mode\_t**](group__typedefs.md#typedef-tiff_compression_mode_t) | [**compression\_mode**](#variable-compression_mode)  <br> |
|  [**tiff\_format\_t**](group__typedefs.md#typedef-tiff_format_t) | [**format**](#variable-format)  <br> |


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
|   | [**TiffArgs**](#function-tiffargs) () <br> |
|   | [**operator cuvis\_export\_tiff\_settings\_t**](#function-operator-cuvis_export_tiff_settings_t) () const<br> |


## Public Functions inherited from cuvis::GeneralExportArgs

See [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)

| Type | Name |
| ---: | :--- |
|   | [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md#function-generalexportargs) () <br> |
|   | [**operator cuvis\_export\_general\_settings\_t**](structcuvis_1_1GeneralExportArgs.md#function-operator-cuvis_export_general_settings_t) () const<br> |






















































## Public Attributes Documentation




### variable compression\_mode 

```C++
tiff_compression_mode_t cuvis::TiffArgs::compression_mode;
```




<hr>



### variable format 

```C++
tiff_format_t cuvis::TiffArgs::format;
```




<hr>
## Public Functions Documentation




### function TiffArgs 

```C++
cuvis::TiffArgs::TiffArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_export\_tiff\_settings\_t 

```C++
cuvis::TiffArgs::operator cuvis_export_tiff_settings_t () const
```



convert to C - SDK settings structure 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

