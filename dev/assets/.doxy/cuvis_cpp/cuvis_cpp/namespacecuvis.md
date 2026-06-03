

# Namespace cuvis



[**Namespace List**](namespaces.md) **>** [**cuvis**](namespacecuvis.md)




















## Classes

| Type | Name |
| ---: | :--- |
| class | [**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md) <br> |
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
| struct | [**WorkerArgs**](structcuvis_1_1WorkerArgs.md) <br> |
| struct | [**common\_image\_t**](structcuvis_1_1common__image__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Metaclass for handling image data (2d or 3d)_  |
| class | [**cuvis\_sdk\_exception**](classcuvis_1_1cuvis__sdk__exception.md) <br> |
| struct | [**image\_t**](structcuvis_1_1image__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Image data from a measurement._  |
| struct | [**view\_t**](structcuvis_1_1view__t.md) &lt;[**typename**](structcuvis_1_1image__t.md) [**data\_t**](structcuvis_1_1image__t.md)&gt;<br>_Image data created from_ [_**ViewExporter**_](classcuvis_1_1ViewExporter.md) _._ |


## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**async\_result\_t**](#enum-async_result_t)  <br> |
| typedef std::function&lt; [**void**](structcuvis_1_1image__t.md)([**event\_t**](group__typedefs.md#typedef-event_t))&gt; | [**cpp\_event\_callback\_t**](#typedef-cpp_event_callback_t)  <br> |
| typedef std::chrono::time\_point&lt; std::chrono::system\_clock &gt; | [**timestamp\_t**](#typedef-timestamp_t)  <br> |
















































## Public Types Documentation




### enum async\_result\_t 

```C++
enum cuvis::async_result_t {
    done,
    timeout,
    overwritten,
    deferred
};
```




<hr>



### typedef cpp\_event\_callback\_t 

```C++
using cuvis::cpp_event_callback_t = typedef std::function<void(event_t)>;
```



The event call-back type must be of the format void fun(event\_t) 


        

<hr>



### typedef timestamp\_t 

```C++
using cuvis::timestamp_t = typedef std::chrono::time_point<std::chrono::system_clock>;
```



as timesamp use STL system clock 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

