

# Class cuvis::EnviExporter



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**EnviExporter**](classcuvis_1_1EnviExporter.md)





* `#include <cuvis.hpp>`



Inherits the following classes: [cuvis::Exporter](classcuvis_1_1Exporter.md)
















## Public Types inherited from cuvis::Exporter

See [cuvis::Exporter](classcuvis_1_1Exporter.md)

| Type | Name |
| ---: | :--- |
| typedef [**cuvis\_export\_general\_settings\_t**](structcuvis_1_1image__t.md) | [**general\_export\_settings\_t**](classcuvis_1_1Exporter.md#typedef-general_export_settings_t)  <br> |






































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**EnviExporter**](#function-enviexporter) ([**EnviArgs**](structcuvis_1_1EnviArgs.md) [**const**](structcuvis_1_1image__t.md) & args) <br> |


## Public Functions inherited from cuvis::Exporter

See [cuvis::Exporter](classcuvis_1_1Exporter.md)

| Type | Name |
| ---: | :--- |
|  [**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & | [**apply**](classcuvis_1_1Exporter.md#function-apply) ([**Measurement**](classcuvis_1_1Measurement.md) [**const**](structcuvis_1_1image__t.md) & mesu) const<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**flush**](classcuvis_1_1Exporter.md#function-flush) () <br> |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**get\_queue\_used**](classcuvis_1_1Exporter.md#function-get_queue_used) () const<br> |
















































## Protected Functions inherited from cuvis::Exporter

See [cuvis::Exporter](classcuvis_1_1Exporter.md)

| Type | Name |
| ---: | :--- |
|   | [**Exporter**](classcuvis_1_1Exporter.md#function-exporter) () = default<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**setHandle**](classcuvis_1_1Exporter.md#function-sethandle) ([**CUVIS\_EXPORTER**](structcuvis_1_1image__t.md) exporter) <br> |






## Public Functions Documentation




### function EnviExporter 

```C++
cuvis::EnviExporter::EnviExporter (
    EnviArgs  const & args
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

