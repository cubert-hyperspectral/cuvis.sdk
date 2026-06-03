

# Group cuvis\_info\_layer



[**Modules**](modules.md) **>** [**cuvis\_info\_layer**](group__cuvis__info__layer.md)



[More...](#detailed-description)

































































## Macros

| Type | Name |
| ---: | :--- |
| define  | [**CUVIS\_MESU\_CUBE\_INFO\_KEY**](group__cuvis__info__layer.md#define-cuvis_mesu_cube_info_key)  `"cube\_info\_layer"`<br> |
| define  | [**CUVIS\_MESU\_INFO\_BAD\_PIXEL**](group__cuvis__info__layer.md#define-cuvis_mesu_info_bad_pixel)  `2`<br> |
| define  | [**CUVIS\_MESU\_INFO\_INCOMPLETE**](group__cuvis__info__layer.md#define-cuvis_mesu_info_incomplete)  `64`<br> |
| define  | [**CUVIS\_MESU\_INFO\_OK**](group__cuvis__info__layer.md#define-cuvis_mesu_info_ok)  `0`<br> |
| define  | [**CUVIS\_MESU\_INFO\_OVERILLUMINATED**](group__cuvis__info__layer.md#define-cuvis_mesu_info_overilluminated)  `1`<br> |
| define  | [**CUVIS\_MESU\_INFO\_OVERILLUMINATED\_REFERENCE**](group__cuvis__info__layer.md#define-cuvis_mesu_info_overilluminated_reference)  `4`<br> |
| define  | [**CUVIS\_MESU\_INFO\_REFERENCE\_CALC\_OVERFLOW**](group__cuvis__info__layer.md#define-cuvis_mesu_info_reference_calc_overflow)  `32`<br> |
| define  | [**CUVIS\_MESU\_INFO\_UNDERFLOW\_MEASUREMENT\_MIN\_DARK**](group__cuvis__info__layer.md#define-cuvis_mesu_info_underflow_measurement_min_dark)  `8`<br> |
| define  | [**CUVIS\_MESU\_INFO\_UNDERFLOW\_WHITE\_MIN\_DARK**](group__cuvis__info__layer.md#define-cuvis_mesu_info_underflow_white_min_dark)  `16`<br> |
| define  | [**CUVIS\_MESU\_PAN\_INFO\_KEY**](group__cuvis__info__layer.md#define-cuvis_mesu_pan_info_key)  `"pan\_info\_layer"`<br> |

## Detailed Description


The info layer can be retrieved with the function [**cuvis\_measurement\_get\_data\_image**](group__cuvis__mesu.md#function-cuvis_measurement_get_data_image) Though is appears to be an image and will also be exported and fragmented as an image it is actually a set of flags. Each position of the a info-layer pixel represents a data flag for a respective cube (or pan image).


E.g. if a cube ([**CUVIS\_MESU\_CUBE\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_cube_key)) has the size of 410x410x164 (W x H x Chn), the respective info layer ([**CUVIS\_MESU\_CUBE\_INFO\_KEY**](group__cuvis__info__layer.md#define-cuvis_mesu_cube_info_key)) will have a size of 410x410. The info\_layer value at position x,y contains the flags for the whole spectrum at position x,y in the cube.


The same is true for the pan-chromatic image (([**CUVIS\_MESU\_CUBE\_INFO\_KEY**](group__cuvis__info__layer.md#define-cuvis_mesu_cube_info_key)) and [**CUVIS\_MESU\_CUBE\_INFO\_KEY**](group__cuvis__info__layer.md#define-cuvis_mesu_cube_info_key), respectively)


The info layer pixel value is retrieved by binary operation.




**Note:**

The info layer may not be available on all devices.


Example:



```
// mesu is a measurement already loaded
// load the info channel to cube_info_layer_buffer
CUVIS_IMBUFFER cube_info_layer_buffer;
cuvis_measurement_get_data_image(mesu, CUVIS_MESU_CUBE_INFO_KEY, &cube_info_layer_buffer);
//now load pixel x=15, y=17' s flag information
int x = 15, y = 17;
uint16_t info_ptr = (const uint16_t*)(cube_info_layer_buffer.raw);
cube_info_layer_buffer pixel_info = IMBUFFER_GET(info_ptr, x, y, 0, imbuf);
//check if the pixel is ok
if (pixel_info == CUVIS_MESU_INFO_OK)
    printf("pixel 15|17 ok \n");
else
{
    // multiple flags can be set
    if ((pixel_info  & CUVIS_MESU_INFO_BAD_PIXEL) != 0)
        printf("pixel 15|17 is over-illuminated \n");

    if ((pixel_info  & CUVIS_MESU_INFO_OVERILLUMINATED) != 0)
        printf("pixel 15|17 is a bad pixel \n");
    // ...
}
```
 


    
## Macro Definition Documentation





### define CUVIS\_MESU\_CUBE\_INFO\_KEY 

```
#define CUVIS_MESU_CUBE_INFO_KEY `"cube_info_layer"`
```



name of the info channel of its respective cube. 


        

<hr>



### define CUVIS\_MESU\_INFO\_BAD\_PIXEL 

```
#define CUVIS_MESU_INFO_BAD_PIXEL `2`
```



the pixel is marked bad, eg. a pixel of the respective spectrum is dead 


        

<hr>



### define CUVIS\_MESU\_INFO\_INCOMPLETE 

```
#define CUVIS_MESU_INFO_INCOMPLETE `64`
```



the spectrum at this position is incomplete, e.g by a bad / too close distance calibration 


        

<hr>



### define CUVIS\_MESU\_INFO\_OK 

```
#define CUVIS_MESU_INFO_OK `0`
```



no flag set, only valid, if pixel value is equal 0 


        

<hr>



### define CUVIS\_MESU\_INFO\_OVERILLUMINATED 

```
#define CUVIS_MESU_INFO_OVERILLUMINATED `1`
```



one or more channels of the spectrum are over-exposed / the pan image is over-exposed at this position 


        

<hr>



### define CUVIS\_MESU\_INFO\_OVERILLUMINATED\_REFERENCE 

```
#define CUVIS_MESU_INFO_OVERILLUMINATED_REFERENCE `4`
```



one or more channels of the spectrum of the white reference that was used to calculate this position was over-exposed 


        

<hr>



### define CUVIS\_MESU\_INFO\_REFERENCE\_CALC\_OVERFLOW 

```
#define CUVIS_MESU_INFO_REFERENCE_CALC_OVERFLOW `32`
```



the reflectance value exceeded the maximum value possible by the data format (i.e. the value reflectance reached or exceeded 655.35% (uint16 value of 65535) 


        

<hr>



### define CUVIS\_MESU\_INFO\_UNDERFLOW\_MEASUREMENT\_MIN\_DARK 

```
#define CUVIS_MESU_INFO_UNDERFLOW_MEASUREMENT_MIN_DARK `8`
```



the meausurement was darker then the dark reference at this position (underflow) 


        

<hr>



### define CUVIS\_MESU\_INFO\_UNDERFLOW\_WHITE\_MIN\_DARK 

```
#define CUVIS_MESU_INFO_UNDERFLOW_WHITE_MIN_DARK `16`
```



the white reference was darker then the dark reference at this position (underflow) 


        

<hr>



### define CUVIS\_MESU\_PAN\_INFO\_KEY 

```
#define CUVIS_MESU_PAN_INFO_KEY `"pan_info_layer"`
```



name of the info channel of its respective pan image. 


        

<hr>

------------------------------


