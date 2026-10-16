

# Class cuvis::Exporter



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**Exporter**](classcuvis_1_1Exporter.md)





* `#include <cuvis.hpp>`





Inherited by the following classes: [cuvis::CubeExporter](classcuvis_1_1CubeExporter.md),  [cuvis::EnviExporter](classcuvis_1_1EnviExporter.md),  [cuvis::TiffExporter](classcuvis_1_1TiffExporter.md),  [cuvis::ViewExporter](classcuvis_1_1ViewExporter.md)












## Public Types

| Type | Name |
| ---: | :--- |
| typedef [**cuvis\_export\_general\_settings\_t**](structcuvis_1_1image__t.md) | [**general\_export\_settings\_t**](#typedef-general_export_settings_t)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & | [**apply**](#function-apply) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu) const<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**flush**](#function-flush) () <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_queue\_used**](#function-get_queue_used) () const<br> |
























## Protected Functions

| Type | Name |
| ---: | :--- |
|   | [**Exporter**](#function-exporter) () = default<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**setHandle**](#function-sethandle) ([**CUVIS\_EXPORTER**](structcuvis_1_1image__t.md) exporter) <br> |




## Public Types Documentation




### typedef general\_export\_settings\_t 

```C++
using cuvis::Exporter::general_export_settings_t =  cuvis_export_general_settings_t;
```




<hr>
## Public Functions Documentation




### function apply 

```C++
Measurement  const & cuvis::Exporter::apply (
    Measurement  const & mesu
) const
```




<hr>



### function flush 

```C++
void cuvis::Exporter::flush () 
```




<hr>



### function get\_queue\_used 

```C++
size_t cuvis::Exporter::get_queue_used () const
```




<hr>
## Protected Functions Documentation




### function Exporter 

```C++
cuvis::Exporter::Exporter () = default
```




<hr>



### function setHandle 

```C++
void cuvis::Exporter::setHandle (
    CUVIS_EXPORTER exporter
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

