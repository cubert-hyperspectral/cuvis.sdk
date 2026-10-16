

# Struct cuvis\_pansharpening\_settings\_t



[**ClassList**](annotated.md) **>** [**cuvis\_pansharpening\_settings\_t**](structcuvis__pansharpening__settings__t.md)



_general export settings_ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**add\_pan**](#variable-add_pan)  <br> |
|  [**CUVIS\_CHAR**](cuvis_8h.md#define-cuvis_char) | [**channel\_selection**](#variable-channel_selection)  <br> |
|  [**CUVIS\_PAN\_SHAPRENING\_ALGORITHM\_TYPE**](cuvis_8h.md#define-cuvis_pan_shaprening_algorithm_type) | [**pan\_algorithm**](#variable-pan_algorithm)  <br> |
|  [**CUVIS\_PAN\_SHAPRENING\_INTERPOLATION\_TYPE**](cuvis_8h.md#define-cuvis_pan_shaprening_interpolation_type) | [**pan\_interpolation\_type**](#variable-pan_interpolation_type)  <br> |
|  double | [**pan\_scale**](#variable-pan_scale)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**pre\_pan\_sharpen\_cube**](#variable-pre_pan_sharpen_cube)  <br> |
|  float | [**spectra\_multiplier**](#variable-spectra_multiplier)  <br> |












































## Public Attributes Documentation




### variable add\_pan 

```C++
CUVIS_INT cuvis_pansharpening_settings_t::add_pan;
```



add pan to exported image / cube.


If applicable, the pan image is scaled to target pan-sharpening resolution. 


        

<hr>



### variable channel\_selection 

```C++
CUVIS_CHAR cuvis_pansharpening_settings_t::channel_selection[CUVIS_MAXBUF];
```



The export channel selection 



Use "all" or "full" for all available channels


Use ranges for wavelength range start-end or start:end or start:step:end ; All values in Nanometers. Examples: 450:10:550 or 450-550 


        

<hr>



### variable pan\_algorithm 

```C++
CUVIS_PAN_SHAPRENING_ALGORITHM_TYPE cuvis_pansharpening_settings_t::pan_algorithm;
```



method for calculating the weights 


        

<hr>



### variable pan\_interpolation\_type 

```C++
CUVIS_PAN_SHAPRENING_INTERPOLATION_TYPE cuvis_pansharpening_settings_t::pan_interpolation_type;
```



for pansharpening use this interpolation type to scale up the cube before adjusting the weights


As a first step to pan-sharpening the spectral data needs to be re-sampled to the target resolution This parameter determines the method for this resampling. 


        

<hr>



### variable pan\_scale 

```C++
double cuvis_pansharpening_settings_t::pan_scale;
```



amount of pan-sharpening


The value is relative to the pan image size, give a value between 0 and 1 


        

<hr>



### variable pre\_pan\_sharpen\_cube 

```C++
CUVIS_INT cuvis_pansharpening_settings_t::pre_pan_sharpen_cube;
```



pansharpen cube before calculating user plugin


Normally pan sharpening is applied after calculating the user plugin. Prepansharpening can be used to get a pansharpened cube when no real userplugin shall be applied. Prepansharpening is calculated on the whole spectral cube which is heavy on performance. 


        

<hr>



### variable spectra\_multiplier 

```C++
float cuvis_pansharpening_settings_t::spectra_multiplier;
```



multiply spectrum by fixed factor before exporting


This is most usefull for bitshifting the data - especially when the pan image is also added to the export. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

