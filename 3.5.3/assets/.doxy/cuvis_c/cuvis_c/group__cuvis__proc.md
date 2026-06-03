

# Group cuvis\_proc



[**Modules**](modules.md) **>** [**cuvis\_proc**](group__cuvis__proc.md)



[More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_apply**](#function-cuvis_proc_cont_apply) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu) <br>_(Re-)Process a measurement_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_calc\_distance**](#function-cuvis_proc_cont_calc_distance) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, double i\_distanceMM) <br>_Set the operating distance by value._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_clear\_reference**](#function-cuvis_proc_cont_clear_reference) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type) <br>_Clears a reference measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_copy\_handle**](#function-cuvis_proc_cont_copy_handle) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) \* o\_pProcCont) <br>_Creates an additional processing context handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_create\_from\_calib**](#function-cuvis_proc_cont_create_from_calib) ([**CUVIS\_CALIB**](cuvis_8h.md#define-cuvis_calib) i\_calib, [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) \* o\_pProcCont) <br>_Load a processing context from a given calibration._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_create\_from\_mesu**](#function-cuvis_proc_cont_create_from_mesu) ([**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_loadReferences, [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) \* o\_pProcCont) <br>_Load a processing context from a given measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_create\_from\_session\_file**](#function-cuvis_proc_cont_create_from_session_file) ([**CUVIS\_SESSION\_FILE**](cuvis_8h.md#define-cuvis_session_file) i\_sess, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_loadReferences, [**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) \* o\_pProcCont) <br>_Load a processing context from a given session\_file._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_free**](#function-cuvis_proc_cont_free) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) \* io\_pProcCont) <br>_Clear a loaded processing context by it's handle._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_get\_reference**](#function-cuvis_proc_cont_get_reference) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) \* o\_pMesu, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type) <br>_get a specific reference from the processing context_  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_has\_reference**](#function-cuvis_proc_cont_has_reference) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pHasReference) <br>_Check if an explicit reference was set._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_is\_capable**](#function-cuvis_proc_cont_is_capable) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_PROC\_ARGS**](cuvis_8h.md#define-cuvis_proc_args) i\_args, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) \* o\_pIsCapable) <br>_Check if a processing mode is possible for a measurement._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_set\_args**](#function-cuvis_proc_cont_set_args) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_PROC\_ARGS**](cuvis_8h.md#define-cuvis_proc_args) i\_args) <br>_Sets the processing arguments for a processing contex._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_proc\_cont\_set\_reference**](#function-cuvis_proc_cont_set_reference) ([**CUVIS\_PROC\_CONT**](cuvis_8h.md#define-cuvis_proc_cont) i\_procCont, [**CUVIS\_MESU**](cuvis_8h.md#define-cuvis_mesu) i\_mesu, [**CUVIS\_REFERENCE\_TYPE**](cuvis_8h.md#define-cuvis_reference_type) i\_type) <br>_Set a reference measurement._  |




























## Detailed Description


Processing Images with the SDK. 


    
## Public Functions Documentation




### function cuvis\_proc\_cont\_apply 

_(Re-)Process a measurement_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_apply (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_MESU i_mesu
) 
```



Process a measurement according to the current settings of the processing context. Those get set via [**cuvis\_proc\_cont\_set\_args**](group__cuvis__proc.md#function-cuvis_proc_cont_set_args) The availability of the modes depends, use [**cuvis\_proc\_cont\_is\_capable**](group__cuvis__proc.md#function-cuvis_proc_cont_is_capable) to check if the processing is possible.


In short: Cube\_Raw does not require references (Reference\_Distance is optional)


Cube\_DarkSubtract requires Reference\_Dark (and Reference\_Distance is optional)


Cube\_Reflectance requires Reference\_Dark and Reference\_White reference (and Reference\_Distance is optional), the Reference\_WhiteDark is strongly recommended if using different integration times.


Cube\_SpectralRadiance depends on the camera model: All cameras require Reference\_SpRad. The Fireflye requires: Reference\_Dark, Reference\_White, the Ultris series requires only Reference\_Dark.




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_mesu` The measurement to be processed 



**Returns:**

status\_ok if measurement was processed. 





        

<hr>



### function cuvis\_proc\_cont\_calc\_distance 

_Set the operating distance by value._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_calc_distance (
    CUVIS_PROC_CONT i_procCont,
    double i_distanceMM
) 
```



Some cameras require a distance reference (calibration). This is usually obtained from a measurement at that distance. However, if the distance is known, it can be set manually.




**Note:**

Some OEM-Cameras or older models do not support this. 




**Note:**

Internally, a measurement is created. It can be obtained by [**cuvis\_proc\_cont\_get\_reference**](group__cuvis__proc.md#function-cuvis_proc_cont_get_reference).




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_distanceMM` The distance in millimeters. 



**Returns:**

status\_ok if the distance could be set 





        

<hr>



### function cuvis\_proc\_cont\_clear\_reference 

_Clears a reference measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_clear_reference (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_REFERENCE_TYPE i_type
) 
```



Clears a reference explicitly set by [**cuvis\_proc\_cont\_set\_reference**](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference)




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_type` The type of the reference 




        

<hr>



### function cuvis\_proc\_cont\_copy\_handle 

_Creates an additional processing context handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_copy_handle (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_PROC_CONT * o_pProcCont
) 
```



Creates an additional handle that points to the same instance as the supplied handle




**Parameters:**


* `i_procCont` The handle of the processing context to copy 
* `o_pProcCont` The new handle of the processing context. 



**Returns:**

status\_ok if the processing context handle could be doubled 





        

<hr>



### function cuvis\_proc\_cont\_create\_from\_calib 

_Load a processing context from a given calibration._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_create_from_calib (
    CUVIS_CALIB i_calib,
    CUVIS_PROC_CONT * o_pProcCont
) 
```



Load the processing context from the calibration.




**Parameters:**


* `i_calib` The calibration instance the processing context will be loaded from 
* `o_pProcCont` The handle of the processing context. 



**Returns:**

status\_ok if the processing context could be loaded 





        

<hr>



### function cuvis\_proc\_cont\_create\_from\_mesu 

_Load a processing context from a given measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_create_from_mesu (
    CUVIS_MESU i_mesu,
    CUVIS_INT i_loadReferences,
    CUVIS_PROC_CONT * o_pProcCont
) 
```



The processing context is loaded from the CALIBRATION directory, relative to the measurement given ( ../Calibration/\* ) . This directory is present in the normal camera operation / recording, but the reference might get lost, if you manually move the measurements. In that case, this function will fail.




**Parameters:**


* `i_mesu` The measurement with a valid reference to the processing context 
* `o_pProcCont` The handle of the processing context. 



**Returns:**

status\_ok if the processing context could be loaded 





        

<hr>



### function cuvis\_proc\_cont\_create\_from\_session\_file 

_Load a processing context from a given session\_file._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_create_from_session_file (
    CUVIS_SESSION_FILE i_sess,
    CUVIS_INT i_loadReferences,
    CUVIS_PROC_CONT * o_pProcCont
) 
```



The processing context from the embedded processing context of the session\_info file.




**Parameters:**


* `i_sess` The session\_file with a valid reference to the processing context 
* `o_pProcCont` The handle of the processing context. 



**Returns:**

status\_ok if the processing context could be loaded 





        

<hr>



### function cuvis\_proc\_cont\_free 

_Clear a loaded processing context by it's handle._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_free (
    CUVIS_PROC_CONT * io_pProcCont
) 
```



The internal memory is freed. 

**Parameters:**


* `io_pProcCont` The handle of the processing context. The handle number will be invalidated. 



**Returns:**

status\_ok if processing context could be freed. 





        

<hr>



### function cuvis\_proc\_cont\_get\_reference 

_get a specific reference from the processing context_ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_get_reference (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_MESU * o_pMesu,
    CUVIS_REFERENCE_TYPE i_type
) 
```



The processing context can hold explicit references (e.g. a dark), see [**cuvis\_proc\_cont\_set\_reference**](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference). These reference can be obtained by this functions




**Note:**

Implicit references given by a measurement are not returned. If they are available can only be checked indirectly by the [**cuvis\_proc\_cont\_is\_capable**](group__cuvis__proc.md#function-cuvis_proc_cont_is_capable) or by checking for the measurement's data keys [**CUVIS\_MESU\_DARKREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_darkref_key), [**CUVIS\_MESU\_WHITEREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_whiteref_key) and [**CUVIS\_MESU\_WHITEDARKREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_whitedarkref_key)




**Parameters:**


* `i_procCont` The handle of the processing context 
* `o_pMesu` The reference measurement's handle 
* `i_type` The type of the measurement to be retrieved. 



**Returns:**

status\_ok if the reference measurement is available and could be loaded 





        

<hr>



### function cuvis\_proc\_cont\_has\_reference 

_Check if an explicit reference was set._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_has_reference (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_REFERENCE_TYPE i_type,
    CUVIS_INT * o_pHasReference
) 
```





**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_type` The reference type 
* `o_pHasReference` true, if reference is explicitly set. false, otherwise 



**Returns:**

status\_ok if no error occurred. 





        

<hr>



### function cuvis\_proc\_cont\_is\_capable 

_Check if a processing mode is possible for a measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_is_capable (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_MESU i_mesu,
    CUVIS_PROC_ARGS i_args,
    CUVIS_INT * o_pIsCapable
) 
```



Depending on the measurement, it's intrinsic references, the processing context's explicit references and the internal camera calibration itself the availability of a mode varies.


Use this function, to check whether a specific mode is explicitly possible for a measurement.




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_mesu` The measurement to be checked 
* `i_args` The processing options to be checked 
* `o_pIsCapable` true, if mode is possible. false, otherwise 



**Returns:**

status\_ok if no error occurred. 





        

<hr>



### function cuvis\_proc\_cont\_set\_args 

_Sets the processing arguments for a processing contex._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_set_args (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_PROC_ARGS i_args
) 
```



For processing a measurement see [**cuvis\_proc\_cont\_apply**](group__cuvis__proc.md#function-cuvis_proc_cont_apply)




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_args` The processing arguments that will be set 



**Returns:**

status\_ok if measurement was processed. 





        

<hr>



### function cuvis\_proc\_cont\_set\_reference 

_Set a reference measurement._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_proc_cont_set_reference (
    CUVIS_PROC_CONT i_procCont,
    CUVIS_MESU i_mesu,
    CUVIS_REFERENCE_TYPE i_type
) 
```



The available processing modes ([**cuvis\_processing\_mode\_t**](cuvis_8h.md#enum-cuvis_processing_mode_t)) require certain references to be set. When a measurement is recorded with references in place, these references are available per measurement implicitly. However, if you want to process measurements with different references, or if the measurement lacks a reference, they can be set with this function.



```
CUVIS_MESU mesu;
cuvis_measurement_load("mesu.cu3",&mesu);
//contains implicit Reference_Dark

CUVIS_PROC_CONT pc;
cuvis_proc_cont_create_from_mesu(mesu,&pc); //will implicitly load Reference_Dark

CUVIS_MESU white;
cuvis_measurement_load("white.cu3",&white);

cuvis_proc_cont_set_reference(pc, white, Reference_White);

//Cube_Reflectance requires Reference_Dark and Reference_White
cuvis_proc_cont_apply(pc,mesu,{Cube_Reflectance});
```
 

**Note:**

The reference explicitly set by this function has priority over the implicit measurement.




**Parameters:**


* `i_procCont` The handle of the processing context 
* `i_mesu` The measurement to be used as explicit reference 
* `i_type` The type of the reference 




        

<hr>

------------------------------


