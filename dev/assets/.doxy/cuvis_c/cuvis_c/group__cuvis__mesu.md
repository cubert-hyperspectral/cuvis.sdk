

# Group cuvis\_mesu



[**Modules**](modules.md) **>** [**cuvis\_mesu**](group__cuvis__mesu.md)



[More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_clear\_cube**](#function-cuvis_measurement_clear_cube) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_mesu) <br>_Clears the cube from a measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_clear\_implicit\_reference**](#function-cuvis_measurement_clear_implicit_reference) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_mesu, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type) <br>_Clears an implicit reference measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_copy\_handle**](#function-cuvis_measurement_copy_handle) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br>_Creates an additional measurement handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_deep\_copy**](#function-cuvis_measurement_deep_copy) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_free**](#function-cuvis_measurement_free) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* io\_pMesu) <br>_Release a measurement handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_count**](#function-cuvis_measurement_get_data_count) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pCount) <br>_Retrieve the number of data elements._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_gps**](#function-cuvis_measurement_get_data_gps) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_GPS**](cuvis_8h.md#define-cuvis_gps) \* o\_pGps) <br>_Get GPS data from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_image**](#function-cuvis_measurement_get_data_image) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_IMBUFFER**](cuvis_8h.md#define-cuvis_imbuffer) \* o\_pBuf) <br>_Get image data from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_info**](#function-cuvis_measurement_get_data_info) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pKey, [**CUVIS\_DATA\_TYPE**](cuvis_8h.md#define-cuvis_data_type) \* o\_pType, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_id) <br>_get meta-information of a data element_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_sensor\_info**](#function-cuvis_measurement_get_data_sensor_info) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_SENSOR\_INFO**](cuvis_8h.md#define-cuvis_sensor_info) \* o\_pValue) <br>_Get image info data from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_string**](#function-cuvis_measurement_get_data_string) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) i\_outBufferlength, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pValue) <br>_Get string data from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_data\_string\_length**](#function-cuvis_measurement_get_data_string_length) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_key, [**CUVIS\_SIZE**](cuvis_8h.md#define-cuvis_size) \* o\_pLength) <br>_Get the length of string data from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_get\_metadata**](#function-cuvis_measurement_get_metadata) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_MESU\_METADATA**](cuvis_8h.md#define-cuvis_mesu_metadata) \* o\_pMetaData) <br>_Obtain metadata from measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_load**](#function-cuvis_measurement_load) (const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_path, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br>_Load a measurement from disk._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_save**](#function-cuvis_measurement_save) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) const i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_path, [**CUVIS\_SAVE\_ARGS**](cuvis_8h.md#define-cuvis_save_args) args) <br>_Save a measurement to disk._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_set\_comment**](#function-cuvis_measurement_set_comment) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) const i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_comment) <br>_Set the comment of the measurement in memory._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_measurement\_set\_name**](#function-cuvis_measurement_set_name) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) const i\_mesu, const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_name) <br>_Set the name of the measurement in memory._  |




























## Detailed Description


How to interact with the Measurements taken by the SDK. 


    
## Public Functions Documentation




### function cuvis\_measurement\_clear\_cube 

_Clears the cube from a measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_clear_cube (
    CUVIS_PROC_CONT i_mesu
) 
```



Clears the proceessing result, i. e. the cube, from the measurement. This returns the measurement the state before applying the processing. This can be usefull for reduced data usage.




**Parameters:**


* `i_mesu` The measurement 




        

<hr>



### function cuvis\_measurement\_clear\_implicit\_reference 

_Clears an implicit reference measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_clear_implicit_reference (
    CUVIS_PROC_CONT i_mesu,
    CUVIS_REFERENCE_TYPE i_type
) 
```



Implict measurements are created, when a measurement is processed with a processing context, where explicit references are set. Then, these references are remebemred by the measurement. When changing the processing context, the references are implicitly available, still. Clearing them may be interesing if the references set are wrong/invalid or if disk space is a concearn.




**Parameters:**


* `i_mesu` The measurement 
* `i_type` The type of the reference to be cleard 




        

<hr>



### function cuvis\_measurement\_copy\_handle 

_Creates an additional measurement handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_copy_handle (
    CUVIS_MESU i_mesu,
    CUVIS_MESU * o_pMesu
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_mesu` The handle of the measurement to copy 
* `o_pMesu` The new handle of the measurement. 



**Returns:**

status\_ok if the measurement handle could be doubled 





        

<hr>



### function cuvis\_measurement\_deep\_copy 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_deep_copy (
    CUVIS_MESU i_mesu,
    CUVIS_MESU * o_pMesu
) 
```



create a deep copy of a measurement


All operations on a measurement are performed on the same object. If different processing needs to be perfomed on a measurement It should be deep-copied. The copied meausrement's name will be changed to end with "\_copy"




**Parameters:**


* `i_mesu` The measurement copy source. 
* `o_pMesu` The copy will be linked to the handle given. 




        

<hr>



### function cuvis\_measurement\_free 

_Release a measurement handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_free (
    CUVIS_MESU * io_pMesu
) 
```



Release a measurement by it's handle. The handle will be overwritten to [**CUVIS\_HANDLE\_NULL**](cuvis_8h.md#define-cuvis_handle_null) This will not affect any measurements on disk.




**Parameters:**


* `io_pMesu` The handle to the measurement to be deleted 



**Returns:**

status\_ok if the measurement was released. 





        

<hr>



### function cuvis\_measurement\_get\_data\_count 

_Retrieve the number of data elements._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_count (
    CUVIS_MESU i_mesu,
    CUVIS_INT * o_pCount
) 
```





**Parameters:**


* `i_mesu` The measurement handle 
* `o_pCount` The number of data elements 



**Returns:**

status\_ok if the data element count could be retrieved 





        

<hr>



### function cuvis\_measurement\_get\_data\_gps 

_Get GPS data from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_gps (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_GPS * o_pGps
) 
```



Return gps data from a measurement.


This function can only be called, if he data type is data\_type\_gps. This can be checked by the function [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info).


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `i_key` the data frame identification key (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `o_pGps` The gps buffer to be filled. 



**Returns:**

status\_ok if the buffer could be filled with the gps data set. 





        

<hr>



### function cuvis\_measurement\_get\_data\_image 

_Get image data from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_image (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_IMBUFFER * o_pBuf
) 
```



Return image data from a measurement. The image data is valid as long as the measurement handle is not released and the measurement is not re-processed.


This function can only be called, if he data type is data\_type\_image. This can be checked by the function [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info).


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `i_key` The data frame identification key (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `o_pBuf` The image buffer to be filled 



**Returns:**

status\_ok if the buffer could be filled with the image element. status\_not\_available if the requested data was empty, or the key could not be found 





        

<hr>



### function cuvis\_measurement\_get\_data\_info 

_get meta-information of a data element_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_info (
    CUVIS_MESU i_mesu,
    CUVIS_CHAR * o_pKey,
    CUVIS_DATA_TYPE * o_pType,
    CUVIS_INT i_id
) 
```



Retrieve the meta-informations of a data element identified by it's positional number. A measurement has N data elements (obtain N with the functions [**cuvis\_measurement\_get\_data\_count**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_count)) Thus, the meta-data of element 0 to N-1 can be obtained. The `o_pType` defined the data type: If it is data\_type\_image, retrieve it with [**cuvis\_measurement\_get\_data\_image**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_image).


If it is data type is data\_type\_gps, retrieve it with [**cuvis\_measurement\_get\_data\_gps**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_gps). If it is data\_type\_string, retrieve with [**cuvis\_measurement\_get\_data\_string**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_string) If it is data\_type\_unsupported, the data cannot be retrieved.


To retrieve the data, you will require the `o_pKey` wich you can obtain by using this function. The key is the name of the data channel.


Some keys are reserved, see [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `o_pKey` Output the data key 
* `o_pType` The data type 
* `i_id` The number of the data element 



**Returns:**

status\_ok if the data information could be obtained 





        

<hr>



### function cuvis\_measurement\_get\_data\_sensor\_info 

_Get image info data from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_sensor_info (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_SENSOR_INFO * o_pValue
) 
```



Return image data from a measurement. Tis


This function can only be called, if he data type is data\_type\_string. This can be checked by the function [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info).


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `i_key` the data frame identification key (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `o_pValue` The string buffer to be filled. The provided array must have the length of [**CUVIS\_MAXBUF**](cuvis_8h.md#define-cuvis_maxbuf) 



**Returns:**

status\_ok if the buffer could be filled with the string. 





        

<hr>



### function cuvis\_measurement\_get\_data\_string 

_Get string data from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_string (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_SIZE i_outBufferlength,
    CUVIS_CHAR * o_pValue
) 
```



Return string data from a measurement.


This function can only be called, if he data type is data\_type\_string. This can be checked by the function [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info).


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `i_key` the data frame identification key (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `i_outBufferlength` the maximal possible length of the string that is going to be copied (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `o_pValue` The string buffer to be filled. The provided array must have the length of `i_length` 



**Returns:**

status\_ok if the buffer could be filled with the string. 





        

<hr>



### function cuvis\_measurement\_get\_data\_string\_length 

_Get the length of string data from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_data_string_length (
    CUVIS_MESU i_mesu,
    const CUVIS_CHAR * i_key,
    CUVIS_SIZE * o_pLength
) 
```



Return the length of a string data from a measurement.


This function can only be called, if he data type is data\_type\_string. This can be checked by the function [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info).


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_mesu` The measurement handle 
* `i_key` the data frame identification key (see [**cuvis\_measurement\_get\_data\_info**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_info) or [**Reserved Keys**](group__cuvis__reserved__keys.md)) 
* `o_pLength` The length of the string data 



**Returns:**

status\_ok if the length could be returned 





        

<hr>



### function cuvis\_measurement\_get\_metadata 

_Obtain metadata from measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_get_metadata (
    CUVIS_MESU i_mesu,
    CUVIS_MESU_METADATA * o_pMetaData
) 
```



The meta-data from the measurement contains information about the measurement when it was recorded: when and how. Meta-Data do not contain the actual recorded data.




**Parameters:**


* `i_mesu` The measurement's handle 
* `o_pMetaData` The meta structure to be filled 



**Returns:**

status\_ok, if the meta-data could be loaded without errors 





        

<hr>



### function cuvis\_measurement\_load 

_Load a measurement from disk._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_load (
    const CUVIS_CHAR * i_path,
    CUVIS_MESU * o_pMesu
) 
```



The measurement is a cu3 file - and if fragmented some additional tiff files with a postfix, e.g. \_cube.tiff To load the file, all fragmented parts must be in the same directory. Fragmented files must not be renamed.




**Parameters:**


* `i_path` the file path of the measurement 
* `o_pMesu` the handle of the measurement. 



**Returns:**

status\_ok, if the measurement could be loaded. 





        

<hr>



### function cuvis\_measurement\_save 

_Save a measurement to disk._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_save (
    CUVIS_MESU const i_mesu,
    const CUVIS_CHAR * i_path,
    CUVIS_SAVE_ARGS args
) 
```



Saves a single measurement to the disk in cu3 format. The file name is given by the measurement's name (see [**cuvis\_measurement\_set\_name**](group__cuvis__mesu.md#function-cuvis_measurement_set_name))




**Parameters:**


* `i_path` The file directory 
* `i_mesu` The handle of the measurement to be saved 
* `args` The saving options 



**Returns:**

status\_ok, if the measurement was save successfully. 





        

<hr>



### function cuvis\_measurement\_set\_comment 

_Set the comment of the measurement in memory._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_set_comment (
    CUVIS_MESU const i_mesu,
    const CUVIS_CHAR * i_comment
) 
```





**Parameters:**


* `i_mesu` The measurements to be changed 
* `i_comment` The new measurement's comment 



**Returns:**

status\_ok, if the measurement's name was set successfully. 





        

<hr>



### function cuvis\_measurement\_set\_name 

_Set the name of the measurement in memory._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_measurement_set_name (
    CUVIS_MESU const i_mesu,
    const CUVIS_CHAR * i_name
) 
```



By default, a newly aquired measurement has the name &lt;SESSIONNAME&gt;\_&lt;session\_no&gt;\_&lt;sequence\_no&gt; (see [**CUVIS\_SESSION\_INFO**](cuvis_8h.md#define-cuvis_session_info)). This will also be the name of the file while saving it. This can be changed by this function.




**Parameters:**


* `i_mesu` The measurements to be changed 
* `i_name` The new measurement's name 



**Returns:**

status\_ok, if the measurement's name was set successfully. 





        

<hr>

------------------------------


