

# Struct cuvis::EnviArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**EnviArgs**](structcuvis_1_1EnviArgs.md)





* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)
























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
|   | [**EnviArgs**](#function-enviargs) () = default<br> |


## Public Functions inherited from cuvis::GeneralExportArgs

See [cuvis::GeneralExportArgs](structcuvis_1_1GeneralExportArgs.md)

| Type | Name |
| ---: | :--- |
|   | [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md#function-generalexportargs) () <br> |
|   | [**operator cuvis\_export\_general\_settings\_t**](structcuvis_1_1GeneralExportArgs.md#function-operator-cuvis_export_general_settings_t) () const<br> |






















































## Public Functions Documentation




### function EnviArgs 

```C++
cuvis::EnviArgs::EnviArgs () = default
```



Constructor to create default parameters 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

