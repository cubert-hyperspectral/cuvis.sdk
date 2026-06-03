

# Group cuvis\_viewer



[**Modules**](modules.md) **>** [**cuvis\_viewer**](group__cuvis__viewer.md)



[More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_view\_free**](#function-cuvis_view_free) ([**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) \* io\_pView) <br>_Release a view._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_view\_get\_data**](#function-cuvis_view_get_data) ([**CUVIS\_VIEW**](cuvis_8h.md#define-cuvis_view) i\_view, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_index, [**CUVIS\_VIEW\_DATA**](cuvis_8h.md#define-cuvis_view_data) \* o\_pData) <br>_Obtain data from view._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_view\_get\_data\_count**](#function-cuvis_view_get_data_count) ([**CUVIS\_VIEW**](cuvis_8h.md#define-cuvis_view) i\_view, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCount) <br>_retrieves the number of view data elements_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_viewer\_apply**](#function-cuvis_viewer_apply) ([**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) i\_viewer, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_VIEW**](cuvis_8h.md#define-cuvis_view) \* o\_pView) <br>_Generate a view from a measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_viewer\_copy\_handle**](#function-cuvis_viewer_copy_handle) ([**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) i\_viewer, [**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) \* o\_pViewer) <br>_Creates an additional viewer handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_viewer\_create**](#function-cuvis_viewer_create) ([**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) \* o\_pViewer, [**CUVIS\_VIEWER\_SETTINGS**](cuvis_8h.md#define-cuvis_viewer_settings) viewerSettings) <br>_Create a viewer._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_viewer\_free**](#function-cuvis_viewer_free) ([**CUVIS\_VIEWER**](cuvis_8h.md#define-cuvis_viewer) \* io\_pViewer) <br>_Release a viewer._  |




























## Detailed Description


Something about the viewer 


    
## Public Functions Documentation




### function cuvis\_view\_free 

_Release a view._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_view_free (
    CUVIS_VIEWER * io_pView
) 
```





**Parameters:**


* `io_pView` View to be released. If successfully, handle will be invalidated 



**Returns:**

status\_ok if the exporter was cleared. 





        

<hr>



### function cuvis\_view\_get\_data 

_Obtain data from view._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_view_get_data (
    CUVIS_VIEW i_view,
    CUVIS_INT i_index,
    CUVIS_VIEW_DATA * o_pData
) 
```



The data contains the actual view




**Parameters:**


* `i_view` The view handle 
* `i_index` The element number 
* `o_pData` The actual view data 



**Returns:**

status\_ok, if the meta-data could be loaded without errors 





        

<hr>



### function cuvis\_view\_get\_data\_count 

_retrieves the number of view data elements_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_view_get_data_count (
    CUVIS_VIEW i_view,
    CUVIS_INT * o_pCount
) 
```





**Parameters:**


* `i_view` the view handle 
* `o_pCount` The number of elements 




        

<hr>



### function cuvis\_viewer\_apply 

_Generate a view from a measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_viewer_apply (
    CUVIS_VIEWER i_viewer,
    CUVIS_MESU i_mesu,
    CUVIS_VIEW * o_pView
) 
```



The view is processed from a measurement by the viewer. The resulting view handle can be accessed by the [**cuvis\_view\_get\_data\_count**](group__cuvis__viewer.md#function-cuvis_view_get_data_count) to get number of elements, [**cuvis\_view\_get\_data**](group__cuvis__viewer.md#function-cuvis_view_get_data) to get a single date element and [**cuvis\_view\_free**](group__cuvis__viewer.md#function-cuvis_view_free) to release the view (this must always be called)




**Parameters:**


* `i_viewer` The viewer 
* `i_mesu` the measurement 
* `o_pView` the resulting view handle. 



**Returns:**

status\_ok if the measurement was processed successfully. 





        

<hr>



### function cuvis\_viewer\_copy\_handle 

_Creates an additional viewer handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_viewer_copy_handle (
    CUVIS_VIEWER i_viewer,
    CUVIS_VIEWER * o_pViewer
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_viewer` The handle of the viewer to copy 
* `o_pViewer` The new handle of the viewer. 



**Returns:**

status\_ok if the viewer handle could be doubled 





        

<hr>



### function cuvis\_viewer\_create 

_Create a viewer._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_viewer_create (
    CUVIS_VIEWER * o_pViewer,
    CUVIS_VIEWER_SETTINGS viewerSettings
) 
```



Not to be confused with the view exporter. The viewer returns the view in the memory




**Parameters:**


* `o_pViewer` The handle of the viewer 
* `viewerSettings` view settings 



**Returns:**

status\_ok if the exporter was created successfully 





        

<hr>



### function cuvis\_viewer\_free 

_Release a viewer._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_viewer_free (
    CUVIS_VIEWER * io_pViewer
) 
```





**Parameters:**


* `io_pViewer` Viewer to be released. If successfully, handle will be invalidated 



**Returns:**

status\_ok if the exporter was cleared. 





        

<hr>

------------------------------


