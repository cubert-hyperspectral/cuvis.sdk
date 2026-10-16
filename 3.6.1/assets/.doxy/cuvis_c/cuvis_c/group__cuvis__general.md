

# Group cuvis\_general



[**Modules**](modules.md) **>** [**cuvis\_general**](group__cuvis__general.md)



_General Configuration Options of the SDK._ [More...](#detailed-description)






































## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_get\_userplugin\_engine\_version**](#function-cuvis_get_userplugin_engine_version) ([**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pVersion) <br>_Get the Userplugin processing engine version number._  |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_init**](#function-cuvis_init) ([**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_settings\_path, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_global\_loglevel, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_logfile\_name) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_shutdown**](#function-cuvis_shutdown) () <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_version**](#function-cuvis_version) ([**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \* o\_pVersion) <br>_Get the SDK version._  |




























## Detailed Description


The [**cuvis\_init**](group__cuvis__general.md#function-cuvis_init) function set the reference to a settings directory. It should be the first call in a program that uses the cuvis SDK, and is only possible once. In the settings directory there can be multiple settings file present. Settings files are identified by a .settings extension. Each Settings file is a xml file that contains a collection of property nodes. All the settings files get merged into one collection of property nodes. Therefore no property nodes is allowed to be present multiple times. 


    
## Public Functions Documentation




### function cuvis\_get\_userplugin\_engine\_version 

_Get the Userplugin processing engine version number._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_get_userplugin_engine_version (
    CUVIS_CHAR * o_pVersion
) 
```





**Parameters:**


* `o_pVersion` The output version string. The provided array must have the length of [**CUVIS\_MAXBUF**](cuvis_8h.md#define-cuvis_maxbuf) 




        

<hr>



### function cuvis\_init 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_init (
    CUVIS_CHAR const * i_settings_path,
    CUVIS_INT i_global_loglevel,
    CUVIS_CHAR const * i_logfile_name
) 
```



The init function set the settings path.




**Parameters:**


* `i_settings_path` The path to the settings directory. 
* `i_global_loglevel` The log level that will be used for the backend logging system 
* `i_logfile_name` The name of the logfile that is going to be written 




        

<hr>



### function cuvis\_shutdown 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_shutdown () 
```



Function for shutting down Cuvis safely. Gently stops all threads. 


        

<hr>



### function cuvis\_version 

_Get the SDK version._ 
```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_version (
    CUVIS_CHAR * o_pVersion
) 
```





**Parameters:**


* `o_pVersion` The output version string. The provided array must have the length of [**CUVIS\_MAXBUF**](cuvis_8h.md#define-cuvis_maxbuf) 




        

<hr>

------------------------------


