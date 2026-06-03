

# Struct cuvis::GeneralExportArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md)



_Export Settings common to all exporters._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





Inherited by the following classes: [cuvis::EnviArgs](structcuvis_1_1EnviArgs.md),  [cuvis::SaveArgs](structcuvis_1_1SaveArgs.md),  [cuvis::TiffArgs](structcuvis_1_1TiffArgs.md),  [cuvis::ViewArgs](structcuvis_1_1ViewArgs.md)
















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**add\_fullscale\_pan**](#variable-add_fullscale_pan)  <br>_Add a full-resolution pan image to the export (default: false)_  |
|  std::filesystem::path | [**export\_dir**](#variable-export_dir)  <br> |
|  [**struct**](structcuvis_1_1image__t.md) [**PanSharpeningArgs**](structcuvis_1_1PanSharpeningArgs.md) | [**pansharpening\_settings**](#variable-pansharpening_settings)  <br>_Settings to define Pansharpening and channel selection._  |
|  [**bool**](structcuvis_1_1image__t.md) | [**permissive**](#variable-permissive)  <br>_Set_ [_**Exporter**_](classcuvis_1_1Exporter.md) _to permisive mode (default: false)_ |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**GeneralExportArgs**](#function-generalexportargs) () <br> |
|   | [**operator cuvis\_export\_general\_settings\_t**](#function-operator-cuvis_export_general_settings_t) () const<br> |




























## Detailed Description


The options of this structure can be set for any [**Exporter**](classcuvis_1_1Exporter.md). However, not all options are respected by the [**Exporter**](classcuvis_1_1Exporter.md). 


    
## Public Attributes Documentation




### variable add\_fullscale\_pan 

_Add a full-resolution pan image to the export (default: false)_ 
```C++
bool cuvis::GeneralExportArgs::add_fullscale_pan;
```




<hr>



### variable export\_dir 

```C++
std::filesystem::path cuvis::GeneralExportArgs::export_dir;
```



The directory where the files should be exported to (default: ".") 


        

<hr>



### variable pansharpening\_settings 

_Settings to define Pansharpening and channel selection._ 
```C++
struct PanSharpeningArgs cuvis::GeneralExportArgs::pansharpening_settings;
```




<hr>



### variable permissive 

_Set_ [_**Exporter**_](classcuvis_1_1Exporter.md) _to permisive mode (default: false)_
```C++
bool cuvis::GeneralExportArgs::permissive;
```




<hr>
## Public Functions Documentation




### function GeneralExportArgs 

```C++
cuvis::GeneralExportArgs::GeneralExportArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_export\_general\_settings\_t 

```C++
cuvis::GeneralExportArgs::operator cuvis_export_general_settings_t () const
```



convert to C - SDK settings structure 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

