

# Struct cuvis::PanSharpeningArgs



[**ClassList**](annotated.md) **>** [**cuvis**](namespacecuvis.md) **>** [**PanSharpeningArgs**](structcuvis_1_1PanSharpeningArgs.md)



_Settings defining Pansharpening and channel selection for all exporters._ [More...](#detailed-description)

* `#include <cuvis.hpp>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**bool**](structcuvis_1_1image__t.md) | [**add\_pan**](#variable-add_pan)  <br>_Add the pan image to the output (default: false)_  |
|  std::string | [**channel\_selection**](#variable-channel_selection)  <br>_The selection of spectral channels to be exproted. (default : "all")_  |
|  [**pan\_sharpening\_algorithm\_t**](group__typedefs.md#typedef-pan_sharpening_algorithm_t) | [**pan\_algorithm**](#variable-pan_algorithm)  <br>_The pansharpening algorithm (default: pan\_sharpening\_algorithm\_CubertMacroPixel)_  |
|  [**pan\_sharpening\_interpolation\_type\_t**](group__typedefs.md#typedef-pan_sharpening_interpolation_type_t) | [**pan\_interpolation\_type**](#variable-pan_interpolation_type)  <br>_The pansharpening interpolation type (default: pan\_sharpening\_interpolation\_type\_Linear)_  |
|  [**double**](structcuvis_1_1image__t.md) | [**pan\_scale**](#variable-pan_scale)  <br>_amount of pan-sharpening (default: 0)_  |
|  [**bool**](structcuvis_1_1image__t.md) | [**pre\_pan\_sharpen\_cube**](#variable-pre_pan_sharpen_cube)  <br> |
|  [**uint8\_t**](structcuvis_1_1image__t.md) | [**spectra\_multiplier**](#variable-spectra_multiplier)  <br>_Multiply the spectrum before exporting._  |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PanSharpeningArgs**](#function-pansharpeningargs) () <br> |
|   | [**operator cuvis\_pansharpening\_settings\_t**](#function-operator-cuvis_pansharpening_settings_t) () const<br> |




























## Detailed Description


The options of this structure can be set for any [**Exporter**](classcuvis_1_1Exporter.md). However, not all options are respected by the [**Exporter**](classcuvis_1_1Exporter.md). 


    
## Public Attributes Documentation




### variable add\_pan 

_Add the pan image to the output (default: false)_ 
```C++
bool cuvis::PanSharpeningArgs::add_pan;
```




<hr>



### variable channel\_selection 

_The selection of spectral channels to be exproted. (default : "all")_ 
```C++
std::string cuvis::PanSharpeningArgs::channel_selection;
```




<hr>



### variable pan\_algorithm 

_The pansharpening algorithm (default: pan\_sharpening\_algorithm\_CubertMacroPixel)_ 
```C++
pan_sharpening_algorithm_t cuvis::PanSharpeningArgs::pan_algorithm;
```




<hr>



### variable pan\_interpolation\_type 

_The pansharpening interpolation type (default: pan\_sharpening\_interpolation\_type\_Linear)_ 
```C++
pan_sharpening_interpolation_type_t cuvis::PanSharpeningArgs::pan_interpolation_type;
```




<hr>



### variable pan\_scale 

_amount of pan-sharpening (default: 0)_ 
```C++
double cuvis::PanSharpeningArgs::pan_scale;
```




<hr>



### variable pre\_pan\_sharpen\_cube 

```C++
bool cuvis::PanSharpeningArgs::pre_pan_sharpen_cube;
```




<hr>



### variable spectra\_multiplier 

_Multiply the spectrum before exporting._ 
```C++
uint8_t cuvis::PanSharpeningArgs::spectra_multiplier;
```




<hr>
## Public Functions Documentation




### function PanSharpeningArgs 

```C++
cuvis::PanSharpeningArgs::PanSharpeningArgs () 
```



Constructor to create default parameters 


        

<hr>



### function operator cuvis\_pansharpening\_settings\_t 

```C++
cuvis::PanSharpeningArgs::operator cuvis_pansharpening_settings_t () const
```



convert to C - SDK settings structure 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `cuvis.cpp/interface/cuvis.hpp`

