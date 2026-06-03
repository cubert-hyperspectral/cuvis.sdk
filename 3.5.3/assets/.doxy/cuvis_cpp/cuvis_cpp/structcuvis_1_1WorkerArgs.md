

# Struct cuvis::WorkerArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**WorkerArgs**](structcuvis_1_1WorkerArgs.md)



[More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**can\_drop\_results**](#variable-can_drop_results)  <br> __ |
|  [**bool**](structcuvis_1_1image__t.md) | [**can\_skip\_measurements**](#variable-can_skip_measurements)  <br> __ |
|  [**bool**](structcuvis_1_1image__t.md) | [**can\_skip\_supplementary\_steps**](#variable-can_skip_supplementary_steps)  <br> __ |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**input\_queue\_size**](#variable-input_queue_size)  <br> __ |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**mandatory\_queue\_size**](#variable-mandatory_queue_size)  <br> __ |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**output\_queue\_size**](#variable-output_queue_size)  <br> __ |
|  [**size\_t**](structcuvis_1_1image__t.md) | [**supplementary\_queue\_size**](#variable-supplementary_queue_size)  <br> __ |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**WorkerArgs**](#function-workerargs) () <br> |
|   | [**operator cuvis\_worker\_settings\_t**](#function-operator-cuvis_worker_settings_t) () const<br>_convert to C - SDK settings structure_  |




























## Detailed Description


settings for the worker 


    
## Public Attributes Documentation




### variable can\_drop\_results 

 __
```C++
bool cuvis::WorkerArgs::can_drop_results;
```




 


        

<hr>



### variable can\_skip\_measurements 

 __
```C++
bool cuvis::WorkerArgs::can_skip_measurements;
```




 


        

<hr>



### variable can\_skip\_supplementary\_steps 

 __
```C++
bool cuvis::WorkerArgs::can_skip_supplementary_steps;
```




 


        

<hr>



### variable input\_queue\_size 

 __
```C++
size_t cuvis::WorkerArgs::input_queue_size;
```




 


        

<hr>



### variable mandatory\_queue\_size 

 __
```C++
size_t cuvis::WorkerArgs::mandatory_queue_size;
```




 


        

<hr>



### variable output\_queue\_size 

 __
```C++
size_t cuvis::WorkerArgs::output_queue_size;
```




 


        

<hr>



### variable supplementary\_queue\_size 

 __
```C++
size_t cuvis::WorkerArgs::supplementary_queue_size;
```




 


        

<hr>
## Public Functions Documentation




### function WorkerArgs 

```C++
cuvis::WorkerArgs::WorkerArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_worker\_settings\_t 

_convert to C - SDK settings structure_ 
```C++
cuvis::WorkerArgs::operator cuvis_worker_settings_t () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

