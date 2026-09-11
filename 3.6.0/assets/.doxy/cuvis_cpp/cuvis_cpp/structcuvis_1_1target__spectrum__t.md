

# Struct cuvis::target\_spectrum\_t



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**target\_spectrum\_t**](structcuvis_1_1target__spectrum__t.md)



_The reflectivity curve of the white target used for reflectance calculation._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  std::vector&lt; [**float**](structcuvis_1_1image__t.md) &gt; | [**values**](#variable-values)  <br> |
|  std::vector&lt; [**float**](structcuvis_1_1image__t.md) &gt; | [**wavelengths**](#variable-wavelengths)  <br> |












































## Detailed Description


Wavelengths are nanometres; values are reflectivity as a fraction, 1.0 meaning 100 percent. Both vectors carry one entry per sample and must be equally long. 


    
## Public Attributes Documentation




### variable values 

```C++
std::vector<float> cuvis::target_spectrum_t::values;
```




<hr>



### variable wavelengths 

```C++
std::vector<float> cuvis::target_spectrum_t::wavelengths;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

