

# Group cuvis\_session



[**Modules**](modules.md) **>** [**cuvis\_session**](group__cuvis__session.md)



[More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_copy\_handle**](#function-cuvis_session_file_copy_handle) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) \* o\_pSess) <br>_Creates an additional session file handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_free**](#function-cuvis_session_file_free) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) \* o\_pSess) <br>_Release a session\_info file handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_fps**](#function-cuvis_session_file_get_fps) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, double \* o\_pFps) <br>_get a session\_info file's FPS_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_hash**](#function-cuvis_session_file_get_hash) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pHash) <br>_get a session\_info file's hash_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_mesu**](#function-cuvis_session_file_get_mesu) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_frameNo, [**CUVIS\_SESSION\_ITEM\_TYPE**](cuvis_8h.md#define-cuvis_session_item_type) i\_type, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br>_Load a measurement from the session\_info file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_operation\_mode**](#function-cuvis_session_file_get_operation_mode) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode) \* o\_pMode) <br>_returns the operation mode the session\_info file was recorded in_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_reference\_mesu**](#function-cuvis_session_file_get_reference_mesu) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_frameNo, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu) <br>_Load a reference measurement from the session\_info file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_size**](#function-cuvis_session_file_get_size) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_SESSION\_ITEM\_TYPE**](cuvis_8h.md#define-cuvis_session_item_type) i\_type, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pSize) <br>_Get number of total frames of session\_info file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_get\_thumbnail**](#function-cuvis_session_file_get_thumbnail) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_IMBUFFER**](cuvis_8h.md#define-cuvis_imbuffer) \* o\_pThumbnail) <br>_Get the thumbnail image of a session file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_session\_file\_load**](#function-cuvis_session_file_load) (const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* i\_path, [**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) \* o\_pSess) <br>_Load a session\_info file from disk._  |




























## Detailed Description


The main file format of the SDK 


    
## Public Functions Documentation




### function cuvis\_session\_file\_copy\_handle 

_Creates an additional session file handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_copy_handle (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_SESSION_FILE * o_pSess
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_sess` The handle of the session file to copy 
* `o_pSess` The new handle of the session file. 



**Returns:**

status\_ok if the session file handle could be doubled 





        

<hr>



### function cuvis\_session\_file\_free 

_Release a session\_info file handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_free (
    CUVIS_SESSION_FILE * o_pSess
) 
```



Release a measurement by it's handle. The handle will be overwritten to [**CUVIS\_HANDLE\_NULL**](cuvis_8h.md#define-cuvis_handle_null) This will not affect any measurements on disk. Measurements loaded from the session\_info file remain valid.




**Parameters:**


* `o_pSess` The handle to the measurement to be deleted 



**Returns:**

status\_ok if the session\_info file was released. 





        

<hr>



### function cuvis\_session\_file\_get\_fps 

_get a session\_info file's FPS_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_fps (
    CUVIS_SESSION_FILE i_sess,
    double * o_pFps
) 
```



The session\_info file meta-Information will be available only if the mode [**cuvis\_session\_file\_get\_operation\_mode**](group__cuvis__session.md#function-cuvis_session_file_get_operation_mode) returns "Internal"




**Parameters:**


* `i_sess` the session\_info file handle 
* `o_pFps` the frames per second the session\_info was recorded with. 



**Returns:**

status\_ok if fps could be retrieved, status\_not\_available if the session\_info file has not FPS property set. 





        

<hr>



### function cuvis\_session\_file\_get\_hash 

_get a session\_info file's hash_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_hash (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_CHAR * o_pHash
) 
```





**Parameters:**


* `i_sess` the session\_info file handle 
* `o_pHash` the hash of the sessionfile. 



**Returns:**

status\_ok if hash could be retrieved, status\_not\_available if the sessionfile has no hash property set. 





        

<hr>



### function cuvis\_session\_file\_get\_mesu 

_Load a measurement from the session\_info file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_mesu (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_INT i_frameNo,
    CUVIS_SESSION_ITEM_TYPE i_type,
    CUVIS_MESU * o_pMesu
) 
```





**Parameters:**


* `i_sess` the session\_info file handle 
* `i_frameNo` the frame no. Counting from 0, must be below value of [**cuvis\_session\_file\_get\_size**](group__cuvis__session.md#function-cuvis_session_file_get_size) of it's respective `i_type` 
* `i_type` the type of listing (size depends on type) 
* `o_pMesu` the handle of the measurement. 



**Returns:**

status\_ok, if the measurement could be loaded. status\_no\_measurement if the measurement was dropped. status\_error if the frame exeeds the number of frames. 





        

<hr>



### function cuvis\_session\_file\_get\_operation\_mode 

_returns the operation mode the session\_info file was recorded in_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_operation_mode (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_OPERATION_MODE * o_pMode
) 
```



The operation mode gives indication how the session\_info file was recorded.




**Parameters:**


* `i_sess` the session\_info file handle 
* `o_pMode` the operation mode of the session\_info file. 



**Returns:**

status\_ok if no error occurred. 





        

<hr>



### function cuvis\_session\_file\_get\_reference\_mesu 

_Load a reference measurement from the session\_info file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_reference_mesu (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_INT i_frameNo,
    CUVIS_REFERENCE_TYPE i_type,
    CUVIS_MESU * o_pMesu
) 
```





**Parameters:**


* `i_sess` the session\_info file handle 
* `i_frameNo` the reference number. Counting from 0. If `i_type` is not set, refers to the index of all references and must be below the value of [**cuvis\_session\_file\_get\_size**](group__cuvis__session.md#function-cuvis_session_file_get_size) using type session\_item\_type\_references. If `i_type` is set, must be 0. 
* `i_type` the type of reference measurement requested 
* `o_pMesu` the handle of the measurement. 



**Returns:**

status\_ok, if the reference could be loaded. status\_no\_measurement if the reference does not exist. status\_error if the i\_frameNo exeeds the number of references. 





        

<hr>



### function cuvis\_session\_file\_get\_size 

_Get number of total frames of session\_info file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_size (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_SESSION_ITEM_TYPE i_type,
    CUVIS_INT * o_pSize
) 
```





**Parameters:**


* `i_sess` the session\_info file handle 
* `i_type` the type of listing (size depends on type) 
* `o_pSize` the size is written here. 



**Returns:**

status\_ok if no error occurred. 





        

<hr>



### function cuvis\_session\_file\_get\_thumbnail 

_Get the thumbnail image of a session file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_get_thumbnail (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_IMBUFFER * o_pThumbnail
) 
```



Return the thumbnail of a session file. The image data is valid as long as the session file handle is not released.


see also: [**Reserved Keys**](group__cuvis__reserved__keys.md)




**Parameters:**


* `i_sess` The session file handle 
* `o_pThumbnail` The image buffer to be filled 



**Returns:**

status\_ok if the buffer could be filled with the image element. status\_not\_available if the requested data was empty, or the key could not be found 





        

<hr>



### function cuvis\_session\_file\_load 

_Load a session\_info file from disk._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_session_file_load (
    const CUVIS_CHAR * i_path,
    CUVIS_SESSION_FILE * o_pSess
) 
```



The session\_info file is a cu3s file and consists of binary cu3 measurement data. Call [**cuvis\_session\_file\_get\_mesu**](group__cuvis__session.md#function-cuvis_session_file_get_mesu) to obtain a single measurement frame. SessionFile files can be create with the Cube Exporter (see [**cuvis\_exporter\_create\_cube**](group__cuvis__exporter.md#function-cuvis_exporter_create_cube)) 

**Note:**

Do not read a file currently opened for writing.




**Parameters:**


* `i_path` the file path of the session\_info file 
* `o_pSess` the handle of the session\_info file. 



**Returns:**

status\_ok, if the measurement could be loaded. 





        

<hr>

------------------------------


