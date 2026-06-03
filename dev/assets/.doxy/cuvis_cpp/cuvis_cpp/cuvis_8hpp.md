

# File cuvis.hpp



[**FileList**](files.md) **>** [**cuvis.cpp**](dir_b7b6b3b8c7c1af37deb2edd57e45d625.md) **>** [**interface**](dir_54d883fdc8557ce650ece9447ae50278.md) **>** [**cuvis.hpp**](cuvis_8hpp.md)

[Go to the source code of this file](cuvis_8hpp_source.md)

[More...](#detailed-description)

* `#include "cuvis.h"`
* `#include <atomic>`
* `#include <cassert>`
* `#include <chrono>`
* `#include <cstring>`
* `#include <deque>`
* `#include <exception>`
* `#include <filesystem>`
* `#include <functional>`
* `#include <future>`
* `#include <map>`
* `#include <memory>`
* `#include <mutex>`
* `#include <optional>`
* `#include <string>`
* `#include <thread>`
* `#include <type_traits>`
* `#include <variant>`













## Namespaces

| Type | Name |
| ---: | :--- |
| namespace | [**cuvis**](namespacecuvis.md) <br> |


## Classes

| Type | Name |
| ---: | :--- |
| class | [**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md) <br> |
| struct | [**component\_state\_info\_t**](structcuvis_1_1AcquisitionContext_1_1component__state__info__t.md) <br> |
| class | [**Async**](classcuvis_1_1Async.md) <br> |
| class | [**AsyncMesu**](classcuvis_1_1AsyncMesu.md) <br> |
| class | [**Calibration**](classcuvis_1_1Calibration.md) <br> |
| struct | [**CalibrationInfo**](structcuvis_1_1CalibrationInfo.md) <br> |
| class | [**CubeExporter**](classcuvis_1_1CubeExporter.md) <br> |
| struct | [**EnviArgs**](structcuvis_1_1EnviArgs.md) <br> |
| class | [**EnviExporter**](classcuvis_1_1EnviExporter.md) <br> |
| class | [**Exporter**](classcuvis_1_1Exporter.md) <br> |
| class | [**General**](classcuvis_1_1General.md) <br> |
| struct | [**GeneralExportArgs**](structcuvis_1_1GeneralExportArgs.md) <br>_Export Settings common to all exporters._  |
| class | [**Measurement**](classcuvis_1_1Measurement.md) <br>_central measurement class_  |
| struct | [**MeasurementMetaData**](structcuvis_1_1MeasurementMetaData.md) <br> |
| struct | [**PanSharpeningArgs**](structcuvis_1_1PanSharpeningArgs.md) <br>_Settings defining Pansharpening and channel selection for all exporters._  |
| struct | [**ProcessingArgs**](structcuvis_1_1ProcessingArgs.md) <br>_processing arguments_  |
| class | [**ProcessingContext**](classcuvis_1_1ProcessingContext.md) <br> |
| struct | [**SaveArgs**](structcuvis_1_1SaveArgs.md) <br>_Options for saving cu3s/cu3 files._  |
| struct | [**SensorInfoData**](structcuvis_1_1SensorInfoData.md) <br> |
| class | [**SessionFile**](classcuvis_1_1SessionFile.md) <br> |
| struct | [**SessionInfo**](structcuvis_1_1SessionInfo.md) <br> |
| struct | [**TiffArgs**](structcuvis_1_1TiffArgs.md) <br>_Additional settings for exporting tiff._  |
| class | [**TiffExporter**](classcuvis_1_1TiffExporter.md) <br> |
| struct | [**ViewArgs**](structcuvis_1_1ViewArgs.md) <br>_viewer settings_  |
| class | [**ViewExporter**](classcuvis_1_1ViewExporter.md) <br> |
| class | [**Viewer**](classcuvis_1_1Viewer.md) <br> |
| class | [**Worker**](classcuvis_1_1Worker.md) <br> |
| struct | [**worker\_return\_t**](structcuvis_1_1Worker_1_1worker__return__t.md) <br> |
| struct | [**worker\_state\_t**](structcuvis_1_1Worker_1_1worker__state__t.md) <br> |
| struct | [**WorkerArgs**](structcuvis_1_1WorkerArgs.md) <br> |
| struct | [**common\_image\_t**](structcuvis_1_1common__image__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Metaclass for handling image data (2d or 3d)_  |
| class | [**cuvis\_sdk\_exception**](classcuvis_1_1cuvis__sdk__exception.md) <br> |
| struct | [**image\_t**](structcuvis_1_1image__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Image data from a measurement._  |
| struct | [**view\_t**](structcuvis_1_1view__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Image data created from_ [_**ViewExporter**_](classcuvis_1_1ViewExporter.md) _._ |

















































## Macros

| Type | Name |
| ---: | :--- |
| define  | [**ACQ\_STUB\_0a**](cuvis_8hpp.md#define-acq_stub_0a) (funname, sdkname, type\_ifcae, type\_wrapped) `/* multi line expression */`<br> |
| define  | [**ACQ\_STUB\_0b**](cuvis_8hpp.md#define-acq_stub_0b) (funname, sdkname, type\_ifcae, type\_wrapped) `/* multi line expression */`<br> |
| define  | [**ACQ\_STUB\_1a**](cuvis_8hpp.md#define-acq_stub_1a) (funname, sdkname, type\_ifcae, type\_wrapped) `/* multi line expression */`<br> |
| define  | [**ACQ\_STUB\_1b**](cuvis_8hpp.md#define-acq_stub_1b) (funname, sdkname, type\_ifcae, type\_wrapped) `/* multi line expression */`<br> |

## Detailed Description


SDK calls for cuvis CPP SDK (wrapper).


This header defines all public CPP SDK (wrapper) functions 


    
## Macro Definition Documentation





### define ACQ\_STUB\_0a 

```C++
#define ACQ_STUB_0a (
    funname,
    sdkname,
    type_ifcae,
    type_wrapped
) `/* multi line expression */`
```




<hr>



### define ACQ\_STUB\_0b 

```C++
#define ACQ_STUB_0b (
    funname,
    sdkname,
    type_ifcae,
    type_wrapped
) `/* multi line expression */`
```




<hr>



### define ACQ\_STUB\_1a 

```C++
#define ACQ_STUB_1a (
    funname,
    sdkname,
    type_ifcae,
    type_wrapped
) `/* multi line expression */`
```




<hr>



### define ACQ\_STUB\_1b 

```C++
#define ACQ_STUB_1b (
    funname,
    sdkname,
    type_ifcae,
    type_wrapped
) `/* multi line expression */`
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

