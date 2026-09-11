

# Group cuvis\_log



[**Modules**](modules.md) **>** [**cuvis\_log**](group__cuvis__log.md)



[More...](#detailed-description)


















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**cuvis\_loglevel\_t**](#enum-cuvis_loglevel_t)  <br>_The available log levels._  |
| typedef void([**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) \* | [**log\_callback**](#typedef-log_callback)  <br> |
| typedef void([**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) \* | [**log\_callback\_localized**](#typedef-log_callback_localized)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_register\_log\_callback**](#function-cuvis_register_log_callback) ([**log\_callback**](group__cuvis__log.md#typedef-log_callback) i\_callback, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_min\_level) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_register\_log\_callback\_localized**](#function-cuvis_register_log_callback_localized) ([**log\_callback\_localized**](group__cuvis__log.md#typedef-log_callback_localized) i\_callback\_localized, [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) i\_min\_level, [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_locale\_id) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_reset\_log\_callback**](#function-cuvis_reset_log_callback) () <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_reset\_log\_callback\_localized**](#function-cuvis_reset_log_callback_localized) () <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_set\_log\_level**](#function-cuvis_set_log_level) ([**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) level) <br> |




























## Detailed Description


There are several ways to configure the logging behaviour in the Cuvis SDK.


## Logfile Configuration Behaviour



The SDK provides the possibility to write the log to a logfile. For this a "log.cfg" file has to be created at a certain position.


When a local ".cuvis" directory exists with an empty "log.cfg" file, the cuvis sdk will create a debug log in that directory. The log file name is the process name followed by log, e.g. "example.exe.log", if the process is named "example.log"


If a local ".cuvis" directory is not found, the system-wide configuration of the logging is used (activated by default from the installation of cuvis): The configuration can be found under PROGRAMDATA%/cuvis/log.cfg (usually "C:/Program Data/cuvis/log.cfg") for Windows or /etc/cuvis/log.cfg for linux. The log output can be found under PROGRAMDATA%/cuvis for Windows and /var/log/cuvis for linux.



## Loglevel at Runtime



Secondly there is the option to adapt the logging behaviour the the standard output stream via [**cuvis\_set\_log\_level**](group__cuvis__log.md#function-cuvis_set_log_level).



## Registration of Log Callbacks



As a third option there is the possibility to register a function as a callback that will be called every time a new log message is recevied with the requested log level. See [**cuvis\_register\_log\_callback**](group__cuvis__log.md#function-cuvis_register_log_callback) and [**cuvis\_register\_log\_callback\_localized**](group__cuvis__log.md#function-cuvis_register_log_callback_localized) for more information. 



    
## Public Types Documentation




### enum cuvis\_loglevel\_t 

_The available log levels._ 
```
enum cuvis_loglevel_t {
    loglevel_fatal = 0,
    loglevel_error = 1,
    loglevel_warning = 2,
    loglevel_info = 3,
    loglevel_debug = 4
};
```




<hr>



### typedef log\_callback 

```
typedef void(SDK_CCALL * log_callback) (const char *msg, CUVIS_INT level);
```




<hr>



### typedef log\_callback\_localized 

```
typedef void(SDK_CCALL * log_callback_localized) (const CUVIS_WCHAR *msg, CUVIS_INT level);
```




<hr>
## Public Functions Documentation




### function cuvis\_register\_log\_callback 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_register_log_callback (
    log_callback i_callback,
    CUVIS_INT i_min_level
) 
```



Register an additional logger. Only one classic callback will be set, multiple calls will overwrite the previous callback. The callback's message argument pointer is only valid during the runtime of the callback. The "classic" logger will output original messages, instead of it's respective translations. For localized (translated) messages, 

**See also:** [**cuvis\_reset\_log\_callback\_localized**](group__cuvis__log.md#function-cuvis_reset_log_callback_localized). 


**Note:**

The classical logger and localized logger can be used simultaneously. 




**Parameters:**


* `i_callback` the function callback 
* `i_min_level` the minimum level of the callback 




        

<hr>



### function cuvis\_register\_log\_callback\_localized 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_register_log_callback_localized (
    log_callback_localized i_callback_localized,
    CUVIS_INT i_min_level,
    CUVIS_CHAR const * i_locale_id
) 
```



Register an additional logger with localized language. Only one callback will be set, multiple calls will overwrite the previous callback. The callback's message argument pointer is only valid during the runtime of the callback. 

**Note:**

The classical logger and localized logger can be used simultaneously. 




**Parameters:**


* `i_callback_localized` the function callback 
* `i_min_level` the minimum level of the callback 
* `i_locale_id` set the locale id, e.g. "de-DE.UTF8" for german. See the "locale" directory for available translations. 




        

<hr>



### function cuvis\_reset\_log\_callback 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_reset_log_callback () 
```



Unregister the additional logger. This will not clear the localized logger 


        

<hr>



### function cuvis\_reset\_log\_callback\_localized 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_reset_log_callback_localized () 
```



Unregister the additional localized logger. This will not clear the classic logger 


        

<hr>



### function cuvis\_set\_log\_level 

```
SDK_CAPI  CUVIS_STATUS  SDK_CCALL cuvis_set_log_level (
    CUVIS_INT level
) 
```



Set the internal log level. Log output will be redirected to cout


If this function is not called, a failback logger is used, with loglevel "warning" The failback logger is de-activated, when this function is called or when a callback is registered for the log messages. However, when this function is called, messages are logged to console, even when a callaback is registered. debug = 4, info = 3, warning = 2, error = 1, fatal = 0




**Parameters:**


* `level` the log level to be set 




        

<hr>

------------------------------


