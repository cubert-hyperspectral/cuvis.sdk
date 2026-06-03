

# Class cuvis::General



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**General**](classcuvis_1_1General.md)





* `#include <cuvis.hpp>`







































## Public Static Functions

| Type | Name |
| ---: | :--- |
|  [**void**](structcuvis_1_1image__t.md) | [**init**](#function-init) (std::string [**const**](structcuvis_1_1image__t.md) & settings\_path, [**int**](structcuvis_1_1image__t.md) global\_loglevel=4, std ::string logfile\_name="") <br> |
|  [**int\_t**](group__typedefs.md#typedef-int_t) | [**register\_event\_callback**](#function-register_event_callback) ([**cpp\_event\_callback\_t**](namespacecuvis.md#typedef-cpp_event_callback_t) callback, [**int\_t**](group__typedefs.md#typedef-int_t) i\_type) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**register\_log\_callback**](#function-register_log_callback) (std::function&lt; [**void**](structcuvis_1_1image__t.md)([**char**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md) \*, [**loglevel\_t**](group__typedefs.md#typedef-loglevel_t))&gt; callback, [**int\_t**](group__typedefs.md#typedef-int_t) min\_lvl) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**register\_log\_callback\_localized**](#function-register_log_callback_localized) (std::function&lt; [**void**](structcuvis_1_1image__t.md)([**wchar\_t**](structcuvis_1_1image__t.md) [**const**](structcuvis_1_1image__t.md) \*, [**loglevel\_t**](group__typedefs.md#typedef-loglevel_t))&gt; callback, [**int\_t**](group__typedefs.md#typedef-int_t) min\_lvl, std::string [**const**](structcuvis_1_1image__t.md) & loc\_id) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**reset\_log\_callback**](#function-reset_log_callback) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**reset\_log\_callback\_localized**](#function-reset_log_callback_localized) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_exception\_locale**](#function-set_exception_locale) (std::string [**const**](structcuvis_1_1image__t.md) & locale="") <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_log\_level**](#function-set_log_level) ([**int\_t**](group__typedefs.md#typedef-int_t) lvl) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**shutdown**](#function-shutdown) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**unregister\_event\_callback**](#function-unregister_event_callback) ([**int\_t**](group__typedefs.md#typedef-int_t) i\_handler\_id) <br> |
|  std::string | [**version**](#function-version) () <br> |


























## Public Static Functions Documentation




### function init 

```C++
static void cuvis::General::init (
    std::string const & settings_path,
    int global_loglevel=4,
    std ::string logfile_name=""
) 
```




<hr>



### function register\_event\_callback 

```C++
static int_t cuvis::General::register_event_callback (
    cpp_event_callback_t callback,
    int_t i_type
) 
```




<hr>



### function register\_log\_callback 

```C++
static void cuvis::General::register_log_callback (
    std::function< void ( char  const *, loglevel_t )> callback,
    int_t min_lvl
) 
```




<hr>



### function register\_log\_callback\_localized 

```C++
static void cuvis::General::register_log_callback_localized (
    std::function< void ( wchar_t  const *, loglevel_t )> callback,
    int_t min_lvl,
    std::string const & loc_id
) 
```




<hr>



### function reset\_log\_callback 

```C++
static void cuvis::General::reset_log_callback () 
```




<hr>



### function reset\_log\_callback\_localized 

```C++
static void cuvis::General::reset_log_callback_localized () 
```




<hr>



### function set\_exception\_locale 

```C++
static void cuvis::General::set_exception_locale (
    std::string const & locale=""
) 
```




<hr>



### function set\_log\_level 

```C++
static void cuvis::General::set_log_level (
    int_t lvl
) 
```




<hr>



### function shutdown 

```C++
static void cuvis::General::shutdown () 
```




<hr>



### function unregister\_event\_callback 

```C++
static void cuvis::General::unregister_event_callback (
    int_t i_handler_id
) 
```




<hr>



### function version 

```C++
static std::string cuvis::General::version () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

