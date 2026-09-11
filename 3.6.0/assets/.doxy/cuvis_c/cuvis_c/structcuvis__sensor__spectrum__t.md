

# Struct cuvis\_sensor\_spectrum\_t



[**ClassList**](annotated.md) **>** [**cuvis\_sensor\_spectrum\_t**](structcuvis__sensor__spectrum__t.md)



_An averaged spectrum of raw sensor counts._ [More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  uint32\_t | [**count**](#variable-count)  <br> |
|  uint16\_t | [**effective\_bit\_depth**](#variable-effective_bit_depth)  <br>_how many bits of each count are significant, 1 to 16_  |
|  double | [**integration\_time**](#variable-integration_time)  <br> |
|  uint16\_t const  \* | [**values**](#variable-values)  <br> |
|  float const  \* | [**wavelengths**](#variable-wavelengths)  <br> |












































## Detailed Description


The spectrum analogue of cuvis\_imbuffer\_t: one struct carries the samples and the acquisition context (bit depth, integration time) that makes counts interpretable, and the setter and the getter both speak it. Used as the white reference for reflectance calculation in place of a full white measurement, see [**cuvis\_proc\_cont\_set\_reference\_white\_spectrum**](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference_white_spectrum).


Filled by a getter, the pointers reference SDK memory and are valid as long as the processing context is valid and the reference slot unchanged, i.e. until the reference is set again, cleared, or the context freed - the same contract as [**cuvis\_imbuffer\_t**](structcuvis__imbuffer__t.md). Copy the arrays out to keep them longer. 


    
## Public Attributes Documentation




### variable count 

```C++
uint32_t cuvis_sensor_spectrum_t::count;
```



number of samples 


        

<hr>



### variable effective\_bit\_depth 

_how many bits of each count are significant, 1 to 16_ 
```C++
uint16_t cuvis_sensor_spectrum_t::effective_bit_depth;
```



4095 off a 12 bit sensor is full scale; off a 16 bit one it is a sixteenth of it, so counts are meaningless without the depth. A count above the full scale this depth implies is rejected. 


        

<hr>



### variable integration\_time 

```C++
double cuvis_sensor_spectrum_t::integration_time;
```



integration time in milliseconds the counts were recorded with 


        

<hr>



### variable values 

```C++
uint16_t const* cuvis_sensor_spectrum_t::values;
```



raw sensor counts, array of length [**count**](structcuvis__sensor__spectrum__t.md#variable-count) 


        

<hr>



### variable wavelengths 

```C++
float const* cuvis_sensor_spectrum_t::wavelengths;
```



wavelengths in nanometers, array of length [**count**](structcuvis__sensor__spectrum__t.md#variable-count) 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

