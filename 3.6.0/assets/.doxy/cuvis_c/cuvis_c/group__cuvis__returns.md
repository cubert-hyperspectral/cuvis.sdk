

# Group cuvis\_returns



[**Modules**](modules.md) **>** [**cuvis\_returns**](group__cuvis__returns.md)



[More...](#detailed-description)


















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**cuvis\_status\_t**](#enum-cuvis_status_t)  <br>_return state of any SDK function_  |




















## Public Functions

| Type | Name |
| ---: | :--- |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) const [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) \*[**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_get\_last\_error\_msg**](#function-cuvis_get_last_error_msg) (void) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) const [**CUVIS\_WCHAR**](cuvis_8h.md#define-cuvis_wchar) \*[**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_get\_last\_error\_msg\_localized**](#function-cuvis_get_last_error_msg_localized) (void) <br> |
|  [**SDK\_CAPI**](cuvis_8h.md#define-sdk_capi) const [**CUVIS\_STATUS**](cuvis_8h.md#define-cuvis_status) [**SDK\_CCALL**](cuvis_8h.md#define-sdk_ccall) | [**cuvis\_set\_last\_error\_locale**](#function-cuvis_set_last_error_locale) ([**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) const \* i\_locale\_id) <br> |




























## Detailed Description


More Information on the Return Values of the SDK Functions.


Most of the SDK functions return a [**cuvis\_status\_t**](group__cuvis__returns.md#enum-cuvis_status_t). This value indicates if the function call was executed sucessfully or if a error occurred. If the value is status\_error for example, this indicates that an error occurred. The specific error message can then be retrieved via [**cuvis\_get\_last\_error\_msg**](group__cuvis__returns.md#function-cuvis_get_last_error_msg) to get more details. 


    
## Public Types Documentation




### enum cuvis\_status\_t 

_return state of any SDK function_ 
```
enum cuvis_status_t {
    status_ok = 1,
    status_error = -1,
    status_deferred = -10,
    status_overwritten = -11,
    status_timeout = -12,
    status_no_measurement = -20,
    status_not_available = -30,
    status_not_processed = -41,
    status_not_stored = -42,
    status_no_view = -43
};
```




<hr>
## Public Functions Documentation




### function cuvis\_get\_last\_error\_msg 

```
SDK_CAPI const CUVIS_CHAR * SDK_CCALL cuvis_get_last_error_msg (
    void
) 
```



Call this function for obtaining the last error message 


        

<hr>



### function cuvis\_get\_last\_error\_msg\_localized 

```
SDK_CAPI const CUVIS_WCHAR * SDK_CCALL cuvis_get_last_error_msg_localized (
    void
) 
```



Call this function for obtaining the last localized error message


remember to set locale with [**cuvis\_set\_last\_error\_locale**](group__cuvis__returns.md#function-cuvis_set_last_error_locale) first. 


        

<hr>



### function cuvis\_set\_last\_error\_locale 

```
SDK_CAPI const CUVIS_STATUS  SDK_CCALL cuvis_set_last_error_locale (
    CUVIS_CHAR const * i_locale_id
) 
```



Set the locale for localized error messages




**Parameters:**


* `i_locale_id` set the locale id, e.g. "de" for german. See the "locale" directory for available translations. 




        

<hr>

------------------------------


