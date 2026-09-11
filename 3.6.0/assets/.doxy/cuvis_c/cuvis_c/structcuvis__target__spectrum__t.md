

# Struct cuvis\_target\_spectrum\_t



[**ClassList**](annotated.md) **>** [**cuvis\_target\_spectrum\_t**](structcuvis__target__spectrum__t.md)



_The reflectance spectrum of the white target used in the scene._ [More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  uint32\_t | [**count**](#variable-count)  <br> |
|  float const  \* | [**values**](#variable-values)  <br> |
|  float const  \* | [**wavelengths**](#variable-wavelengths)  <br> |












































## Detailed Description


Values are fractions: 0.0 for 0% and 1.0 for 100% reflectivity. A dimensionless curve, so it carries no acquisition context. Pointer validity as in [**cuvis\_sensor\_spectrum\_t**](structcuvis__sensor__spectrum__t.md). Used as the target reference, see [**cuvis\_proc\_cont\_set\_reference\_target\_spectrum**](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference_target_spectrum). 


    
## Public Attributes Documentation




### variable count 

```C++
uint32_t cuvis_target_spectrum_t::count;
```



number of samples 


        

<hr>



### variable values 

```C++
float const* cuvis_target_spectrum_t::values;
```



reflectance values as fractions (1.0 for 100%), array of length [**count**](structcuvis__target__spectrum__t.md#variable-count) 


        

<hr>



### variable wavelengths 

```C++
float const* cuvis_target_spectrum_t::wavelengths;
```



wavelengths in nanometers, array of length [**count**](structcuvis__target__spectrum__t.md#variable-count) 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

