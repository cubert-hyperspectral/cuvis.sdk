

# Class cuvis::AcquisitionContext



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**AcquisitionContext**](classcuvis_1_1AcquisitionContext.md)





* `#include <cuvis.hpp>`















## Classes

| Type | Name |
| ---: | :--- |
| struct | [**component\_state\_info\_t**](structcuvis_1_1AcquisitionContext_1_1component__state__info__t.md) <br> |


## Public Types

| Type | Name |
| ---: | :--- |
| typedef std::pair&lt; std::string, [**bool**](structcuvis_1_1image__t.md) &gt; | [**component\_state\_t**](#typedef-component_state_t)  <br> |
| typedef std::function&lt; [**void**](structcuvis_1_1image__t.md)([**Measurement**](classcuvis_1_1Measurement.md))&gt; | [**mesu\_callback\_t**](#typedef-mesu_callback_t)  <br> |
| typedef std::function&lt; [**void**](structcuvis_1_1image__t.md)([**hardware\_state\_t**](group__typedefs.md#typedef-hardware_state_t), std::map&lt; [**int\_t**](group__typedefs.md#typedef-int_t), [**component\_state\_info\_t**](structcuvis_1_1AcquisitionContext_1_1component__state__info__t.md) &gt;)&gt; | [**state\_callback\_t**](#typedef-state_callback_t)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-19) (fps, [**cuvis\_acq\_cont\_fps**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-29) (integration\_time, [**cuvis\_acq\_cont\_integration\_time**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-39) ([**auto\_exp**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_auto\_exp**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**bool**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-49) ([**auto\_exp\_comp**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_auto\_exp\_comp**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-59) (operation\_mode, [**cuvis\_acq\_cont\_operation\_mode**](structcuvis_1_1image__t.md), [**cuvis\_operation\_mode\_t**](structcuvis_1_1image__t.md), [**operation\_mode\_t**](group__typedefs.md#typedef-operation_mode_t)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-69) ([**average**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_average**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-79) ([**bandwidth**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_bandwidth**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-89) ([**queue\_size**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_queue\_size**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0a**](#function-acq_stub_0a-99) ([**queue\_used**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_queue\_used**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-17) (fps, [**cuvis\_acq\_cont\_fps**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-27) (integration\_time, [**cuvis\_acq\_cont\_integration\_time**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-37) ([**auto\_exp**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_auto\_exp**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**bool**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-47) ([**auto\_exp\_comp**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_auto\_exp\_comp**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-57) (operation\_mode, [**cuvis\_acq\_cont\_operation\_mode**](structcuvis_1_1image__t.md), [**cuvis\_operation\_mode\_t**](structcuvis_1_1image__t.md), [**operation\_mode\_t**](group__typedefs.md#typedef-operation_mode_t)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-67) ([**average**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_average**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_0b**](#function-acq_stub_0b-77) ([**continuous**](structcuvis_1_1image__t.md), [**cuvis\_acq\_cont\_continuous**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-19) ([**component\_online**](structcuvis_1_1image__t.md), [**cuvis\_comp\_online**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-29) ([**component\_gain**](structcuvis_1_1image__t.md), [**cuvis\_comp\_gain**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-39) ([**component\_integration\_time\_factor**](structcuvis_1_1image__t.md), [**cuvis\_comp\_integration\_time\_factor**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-49) ([**bandwidth**](structcuvis_1_1image__t.md), [**cuvis\_comp\_bandwidth**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**int**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-59) ([**driver\_queue\_size**](structcuvis_1_1image__t.md), [**cuvis\_comp\_driver\_queue\_size**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**size\_t**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-69) ([**driver\_queue\_used**](structcuvis_1_1image__t.md), [**cuvis\_comp\_driver\_queue\_used**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**size\_t**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-79) ([**hardware\_queue\_size**](structcuvis_1_1image__t.md), [**cuvis\_comp\_hardware\_queue\_size**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**size\_t**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-89) ([**hardware\_queue\_used**](structcuvis_1_1image__t.md), [**cuvis\_comp\_hardware\_queue\_used**](structcuvis_1_1image__t.md), [**int\_t**](group__typedefs.md#typedef-int_t), [**size\_t**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1a**](#function-acq_stub_1a-99) (temperature, [**cuvis\_comp\_temperature**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1b**](#function-acq_stub_1b-12) ([**component\_gain**](structcuvis_1_1image__t.md), [**cuvis\_comp\_gain**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**ACQ\_STUB\_1b**](#function-acq_stub_1b-22) ([**component\_integration\_time\_factor**](structcuvis_1_1image__t.md), [**cuvis\_comp\_integration\_time\_factor**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md), [**double**](structcuvis_1_1image__t.md)) <br> |
|   | [**AcquisitionContext**](#function-acquisitioncontext-13) ([**Calibration**](classcuvis_1_1Calibration.md) [**const**](structcuvis_1_1image__t.md) & calib) <br> |
|   | [**AcquisitionContext**](#function-acquisitioncontext-23) ([**SessionFile**](classcuvis_1_1SessionFile.md) [**const**](structcuvis_1_1image__t.md) & sess, [**bool**](structcuvis_1_1image__t.md) simulate=[**false**](structcuvis_1_1image__t.md)) <br> |
|   | [**AcquisitionContext**](#function-acquisitioncontext-33) ([**CUVIS\_ACQ\_CONT**](structcuvis_1_1image__t.md) handle) <br>_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._  |
|  [**AsyncMesu**](classcuvis_1_1AsyncMesu.md) | [**capture**](#function-capture) () <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**capture\_queue**](#function-capture_queue) () <br> |
|  std::vector&lt; std::string &gt; | [**get\_component\_available\_pixel\_formats**](#function-get_component_available_pixel_formats) ([**int\_t**](group__typedefs.md#typedef-int_t) id) const<br> |
|  [**int\_t**](group__typedefs.md#typedef-int_t) | [**get\_component\_count**](#function-get_component_count) () const<br> |
|  [**CUVIS\_COMPONENT\_INFO**](structcuvis_1_1image__t.md) | [**get\_component\_info**](#function-get_component_info) ([**int\_t**](group__typedefs.md#typedef-int_t) id) const<br> |
|  std::string | [**get\_component\_pixel\_format**](#function-get_component_pixel_format) ([**int**](structcuvis_1_1image__t.md) id) const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**get\_dead\_pixel\_correction\_available**](#function-get_dead_pixel_correction_available) () const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**get\_dead\_pixel\_correction\_enabled**](#function-get_dead_pixel_correction_enabled) () const<br> |
|  [**CUVIS\_ACQ\_CONT**](structcuvis_1_1image__t.md) | [**get\_handle**](#function-get_handle) () const<br>_Expert: Return the current handle of the wrapper class._  |
|  [**CUVIS\_ACQ\_CONT**](structcuvis_1_1image__t.md) | [**get\_handle\_copy**](#function-get_handle_copy) () const<br>_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._  |
|  std::optional&lt; [**Measurement**](classcuvis_1_1Measurement.md) &gt; | [**get\_next\_measurement**](#function-get_next_measurement) (std::chrono::milliseconds timeout\_ms=std::chrono::milliseconds(0)) const<br> |
|  [**SessionInfo**](structcuvis_1_1SessionInfo.md) | [**get\_session\_info**](#function-get_session_info) () const<br> |
|  [**hardware\_state\_t**](group__typedefs.md#typedef-hardware_state_t) | [**get\_state**](#function-get_state) () const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**has\_next\_measurement**](#function-has_next_measurement) () const<br> |
|  [**bool**](structcuvis_1_1image__t.md) | [**is\_ready**](#function-is_ready) () const<br> |
|  [**void**](structcuvis_1_1image__t.md) | [**register\_state\_change\_callback**](#function-register_state_change_callback) ([**state\_callback\_t**](classcuvis_1_1AcquisitionContext.md#typedef-state_callback_t) callback, [**bool**](structcuvis_1_1image__t.md) output\_initial\_state=[**true**](structcuvis_1_1image__t.md)) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**reset\_state\_change\_callback**](#function-reset_state_change_callback) () <br> |
|  [**Async**](classcuvis_1_1Async.md) | [**set\_component\_pixel\_format**](#function-set_component_pixel_format) ([**int**](structcuvis_1_1image__t.md) id, std::string format) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_dead\_pixel\_correction\_enabled**](#function-set_dead_pixel_correction_enabled) ([**bool**](structcuvis_1_1image__t.md) enable) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_queue\_size**](#function-set_queue_size) ([**int\_t**](group__typedefs.md#typedef-int_t) size) <br> |
|  [**void**](structcuvis_1_1image__t.md) | [**set\_session\_info**](#function-set_session_info) ([**SessionInfo**](structcuvis_1_1SessionInfo.md) session) <br> |
|   | [**~AcquisitionContext**](#function-acquisitioncontext) () <br> |




























## Public Types Documentation




### typedef component\_state\_t 

```C++
using cuvis::AcquisitionContext::component_state_t =  std::pair<std::string, bool>;
```




<hr>



### typedef mesu\_callback\_t 

```C++
using cuvis::AcquisitionContext::mesu_callback_t =  std::function<void(Measurement)>;
```




<hr>



### typedef state\_callback\_t 

```C++
using cuvis::AcquisitionContext::state_callback_t =  std::function<void(hardware_state_t, std::map<int_t, component_state_info_t>)>;
```




<hr>
## Public Functions Documentation




### function ACQ\_STUB\_0a [1/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    fps,
    cuvis_acq_cont_fps,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0a [2/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    integration_time,
    cuvis_acq_cont_integration_time,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0a [3/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    auto_exp,
    cuvis_acq_cont_auto_exp,
    int_t,
    bool
) 
```




<hr>



### function ACQ\_STUB\_0a [4/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    auto_exp_comp,
    cuvis_acq_cont_auto_exp_comp,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0a [5/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    operation_mode,
    cuvis_acq_cont_operation_mode,
    cuvis_operation_mode_t,
    operation_mode_t
) 
```




<hr>



### function ACQ\_STUB\_0a [6/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    average,
    cuvis_acq_cont_average,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_0a [7/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    bandwidth,
    cuvis_acq_cont_bandwidth,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_0a [8/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    queue_size,
    cuvis_acq_cont_queue_size,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_0a [9/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0a (
    queue_used,
    cuvis_acq_cont_queue_used,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_0b [1/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    fps,
    cuvis_acq_cont_fps,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0b [2/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    integration_time,
    cuvis_acq_cont_integration_time,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0b [3/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    auto_exp,
    cuvis_acq_cont_auto_exp,
    int_t,
    bool
) 
```




<hr>



### function ACQ\_STUB\_0b [4/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    auto_exp_comp,
    cuvis_acq_cont_auto_exp_comp,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_0b [5/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    operation_mode,
    cuvis_acq_cont_operation_mode,
    cuvis_operation_mode_t,
    operation_mode_t
) 
```




<hr>



### function ACQ\_STUB\_0b [6/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    average,
    cuvis_acq_cont_average,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_0b [7/7]

```C++
cuvis::AcquisitionContext::ACQ_STUB_0b (
    continuous,
    cuvis_acq_cont_continuous,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_1a [1/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    component_online,
    cuvis_comp_online,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_1a [2/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    component_gain,
    cuvis_comp_gain,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_1a [3/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    component_integration_time_factor,
    cuvis_comp_integration_time_factor,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_1a [4/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    bandwidth,
    cuvis_comp_bandwidth,
    int_t,
    int
) 
```




<hr>



### function ACQ\_STUB\_1a [5/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    driver_queue_size,
    cuvis_comp_driver_queue_size,
    int_t,
    size_t
) 
```




<hr>



### function ACQ\_STUB\_1a [6/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    driver_queue_used,
    cuvis_comp_driver_queue_used,
    int_t,
    size_t
) 
```




<hr>



### function ACQ\_STUB\_1a [7/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    hardware_queue_size,
    cuvis_comp_hardware_queue_size,
    int_t,
    size_t
) 
```




<hr>



### function ACQ\_STUB\_1a [8/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    hardware_queue_used,
    cuvis_comp_hardware_queue_used,
    int_t,
    size_t
) 
```




<hr>



### function ACQ\_STUB\_1a [9/9]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1a (
    temperature,
    cuvis_comp_temperature,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_1b [1/2]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1b (
    component_gain,
    cuvis_comp_gain,
    double,
    double
) 
```




<hr>



### function ACQ\_STUB\_1b [2/2]

```C++
cuvis::AcquisitionContext::ACQ_STUB_1b (
    component_integration_time_factor,
    cuvis_comp_integration_time_factor,
    double,
    double
) 
```




<hr>



### function AcquisitionContext [1/3]

```C++
cuvis::AcquisitionContext::AcquisitionContext (
    Calibration  const & calib
) 
```




<hr>



### function AcquisitionContext [2/3]

```C++
cuvis::AcquisitionContext::AcquisitionContext (
    SessionFile  const & sess,
    bool simulate=false
) 
```




<hr>



### function AcquisitionContext [3/3]

_Expert: Create a wrapper class around a handle. This only allowed once per handle, otherwise the handle could be freed before all instances of the wrapper class are deleted. This can be useful if a previously a handle has been copied and now should be wrapped at another place in a program. Most of the time this is not necesarry and the wrapper class can be copied just as well._ 
```C++
cuvis::AcquisitionContext::AcquisitionContext (
    CUVIS_ACQ_CONT handle
) 
```




<hr>



### function capture 

```C++
AsyncMesu cuvis::AcquisitionContext::capture () 
```




<hr>



### function capture\_queue 

```C++
void cuvis::AcquisitionContext::capture_queue () 
```




<hr>



### function get\_component\_available\_pixel\_formats 

```C++
std::vector< std::string > cuvis::AcquisitionContext::get_component_available_pixel_formats (
    int_t id
) const
```




<hr>



### function get\_component\_count 

```C++
int_t cuvis::AcquisitionContext::get_component_count () const
```




<hr>



### function get\_component\_info 

```C++
CUVIS_COMPONENT_INFO cuvis::AcquisitionContext::get_component_info (
    int_t id
) const
```




<hr>



### function get\_component\_pixel\_format 

```C++
std::string cuvis::AcquisitionContext::get_component_pixel_format (
    int id
) const
```




<hr>



### function get\_dead\_pixel\_correction\_available 

```C++
bool cuvis::AcquisitionContext::get_dead_pixel_correction_available () const
```




<hr>



### function get\_dead\_pixel\_correction\_enabled 

```C++
bool cuvis::AcquisitionContext::get_dead_pixel_correction_enabled () const
```




<hr>



### function get\_handle 

_Expert: Return the current handle of the wrapper class._ 
```C++
CUVIS_ACQ_CONT cuvis::AcquisitionContext::get_handle () const
```




<hr>



### function get\_handle\_copy 

_Expert: Create a copy of the current handle of the wrapper class and return it. This handle needs to be also freed before the resource will be released by the sdk._ 
```C++
CUVIS_ACQ_CONT cuvis::AcquisitionContext::get_handle_copy () const
```




<hr>



### function get\_next\_measurement 

```C++
std::optional< Measurement > cuvis::AcquisitionContext::get_next_measurement (
    std::chrono::milliseconds timeout_ms=std::chrono::milliseconds(0)
) const
```




<hr>



### function get\_session\_info 

```C++
SessionInfo cuvis::AcquisitionContext::get_session_info () const
```




<hr>



### function get\_state 

```C++
hardware_state_t cuvis::AcquisitionContext::get_state () const
```




<hr>



### function has\_next\_measurement 

```C++
bool cuvis::AcquisitionContext::has_next_measurement () const
```




<hr>



### function is\_ready 

```C++
bool cuvis::AcquisitionContext::is_ready () const
```




<hr>



### function register\_state\_change\_callback 

```C++
void cuvis::AcquisitionContext::register_state_change_callback (
    state_callback_t callback,
    bool output_initial_state=true
) 
```




<hr>



### function reset\_state\_change\_callback 

```C++
void cuvis::AcquisitionContext::reset_state_change_callback () 
```




<hr>



### function set\_component\_pixel\_format 

```C++
Async cuvis::AcquisitionContext::set_component_pixel_format (
    int id,
    std::string format
) 
```




<hr>



### function set\_dead\_pixel\_correction\_enabled 

```C++
void cuvis::AcquisitionContext::set_dead_pixel_correction_enabled (
    bool enable
) 
```




<hr>



### function set\_queue\_size 

```C++
void cuvis::AcquisitionContext::set_queue_size (
    int_t size
) 
```




<hr>



### function set\_session\_info 

```C++
void cuvis::AcquisitionContext::set_session_info (
    SessionInfo session
) 
```




<hr>



### function ~AcquisitionContext 

```C++
cuvis::AcquisitionContext::~AcquisitionContext () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

