

# Struct cuvis::sensor\_spectrum\_t



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**sensor\_spectrum\_t**](structcuvis_1_1sensor__spectrum__t.md)



_An averaged spectrum of raw sensor counts, usable in place of a white reference measurement._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::uint16\_t | [**effective\_bit\_depth**](#variable-effective_bit_depth)   = `0`<br> |
|  [**double**](structcuvis_1_1image__t.md) | [**integration\_time**](#variable-integration_time)   = `0.0`<br> |
|  std::vector&lt; std::uint16\_t &gt; | [**values**](#variable-values)  <br> |
|  std::vector&lt; [**float**](structcuvis_1_1image__t.md) &gt; | [**wavelengths**](#variable-wavelengths)  <br> |












































## Detailed Description


The owning analogue of the C interface's cuvis\_sensor\_spectrum\_t: one struct carries the samples and the acquisition context that makes counts interpretable. Wavelengths are nanometres. Both vectors carry one entry per sample and must be equally long. 


    
## Public Attributes Documentation




### variable effective\_bit\_depth 

```C++
std::uint16_t cuvis::sensor_spectrum_t::effective_bit_depth;
```



bit depth the counts are interpreted against (1 to 16) 


        

<hr>



### variable integration\_time 

```C++
double cuvis::sensor_spectrum_t::integration_time;
```



integration time the counts were recorded with [ms] 


        

<hr>



### variable values 

```C++
std::vector<std::uint16_t> cuvis::sensor_spectrum_t::values;
```



raw sensor counts 


        

<hr>



### variable wavelengths 

```C++
std::vector<float> cuvis::sensor_spectrum_t::wavelengths;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

