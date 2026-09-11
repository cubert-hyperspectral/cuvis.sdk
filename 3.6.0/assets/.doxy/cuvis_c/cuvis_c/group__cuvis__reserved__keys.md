

# Group cuvis\_reserved\_keys



[**Modules**](modules.md) **>** [**cuvis\_reserved\_keys**](group__cuvis__reserved__keys.md)





































































## Macros

| Type | Name |
| ---: | :--- |
| define  | [**CUVIS\_MESU\_CUBE\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_cube_key)  `"cube"`<br> |
| define  | [**CUVIS\_MESU\_DARKREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_darkref_key)  `"dark\_ref"`<br>_If this field is present, a dark was set while recording the measurement. This is the dark that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._ |
| define  | [**CUVIS\_MESU\_FLAG\_DARK\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_dark_inttime_key)  `"Flag\_IntegrationTimeMismatchDark"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_DARK\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_dark_temp_key)  `"Flag\_TemperatureMismatchDark"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_OVERILLUMINATED\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_overilluminated_key)  `"Flag\_DataIsOverilluminated"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_PAN\_OVERILLUMINATED\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_pan_overilluminated_key)  `"Flag\_PanDataIsOverilluminated"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_POOR\_REFERENCE\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_poor_reference_key)  `"Flag\_DataUsesPoorReference"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_poor_white_balancing_key)  `"Flag\_PoorWhiteBalancingData"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_whitedark_inttime_key)  `"Flag\_IntegrationTimeMismatchWhiteDark"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_whitedark_temp_key)  `"Flag\_TemperatureMismatchWhiteDark"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITE\_INTTIME\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_white_inttime_key)  `"Flag\_IntegrationTimeMismatchWhite"`<br> |
| define  | [**CUVIS\_MESU\_FLAG\_WHITE\_TEMP\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_flag_white_temp_key)  `"Flag\_TemperatureMismatchWhite"`<br> |
| define  | [**CUVIS\_MESU\_GPS\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_gps_key)  `"GPS\_data"`<br> |
| define  | [**CUVIS\_MESU\_PAN\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_pan_key)  `"pan"`<br> |
| define  | [**CUVIS\_MESU\_PREVIEW\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_preview_key)  `"preview"`<br> |
| define  | [**CUVIS\_MESU\_WHITEDARKREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_whitedarkref_key)  `"white\_dark\_ref"`<br>_If this field is present, a white's dark was set while recording the measurement. This is the white' dark that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._ |
| define  | [**CUVIS\_MESU\_WHITEREF\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_whiteref_key)  `"white\_ref"`<br>_If this field is present, a white was set while recording the measurement. This is the white that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._ |

## Macro Definition Documentation





### define CUVIS\_MESU\_CUBE\_KEY 

```
#define CUVIS_MESU_CUBE_KEY `"cube"`
```



name of the data field for the hyperspectral cube (in all modes except Preview) 


        

<hr>



### define CUVIS\_MESU\_DARKREF\_KEY 

_If this field is present, a dark was set while recording the measurement. This is the dark that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._
```
#define CUVIS_MESU_DARKREF_KEY `"dark_ref"`
```




<hr>



### define CUVIS\_MESU\_FLAG\_DARK\_INTTIME\_KEY 

```
#define CUVIS_MESU_FLAG_DARK_INTTIME_KEY `"Flag_IntegrationTimeMismatchDark"`
```



see [**CUVIS\_MESU\_FLAG\_DARK\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_dark_inttime) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_DARK\_TEMP\_KEY 

```
#define CUVIS_MESU_FLAG_DARK_TEMP_KEY `"Flag_TemperatureMismatchDark"`
```



see [**CUVIS\_MESU\_FLAG\_DARK\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_dark_temp) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_OVERILLUMINATED\_KEY 

```
#define CUVIS_MESU_FLAG_OVERILLUMINATED_KEY `"Flag_DataIsOverilluminated"`
```



see [**CUVIS\_MESU\_FLAG\_OVERILLUMINATED**](cuvis_8h.md#define-cuvis_mesu_flag_overilluminated) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_PAN\_OVERILLUMINATED\_KEY 

```
#define CUVIS_MESU_FLAG_PAN_OVERILLUMINATED_KEY `"Flag_PanDataIsOverilluminated"`
```



see [**CUVIS\_MESU\_FLAG\_OVERILLUMINATED**](cuvis_8h.md#define-cuvis_mesu_flag_overilluminated) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_POOR\_REFERENCE\_KEY 

```
#define CUVIS_MESU_FLAG_POOR_REFERENCE_KEY `"Flag_DataUsesPoorReference"`
```



see [**CUVIS\_MESU\_FLAG\_POOR\_REFERENCE**](cuvis_8h.md#define-cuvis_mesu_flag_poor_reference) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING\_KEY 

```
#define CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY `"Flag_PoorWhiteBalancingData"`
```



see [**CUVIS\_MESU\_FLAG\_POOR\_WHITE\_BALANCING**](cuvis_8h.md#define-cuvis_mesu_flag_poor_white_balancing) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME\_KEY 

```
#define CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY `"Flag_IntegrationTimeMismatchWhiteDark"`
```



see [**CUVIS\_MESU\_FLAG\_WHITEDARK\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_whitedark_inttime) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP\_KEY 

```
#define CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY `"Flag_TemperatureMismatchWhiteDark"`
```



see [**CUVIS\_MESU\_FLAG\_WHITEDARK\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_whitedark_temp) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITE\_INTTIME\_KEY 

```
#define CUVIS_MESU_FLAG_WHITE_INTTIME_KEY `"Flag_IntegrationTimeMismatchWhite"`
```



see [**CUVIS\_MESU\_FLAG\_WHITE\_INTTIME**](cuvis_8h.md#define-cuvis_mesu_flag_white_inttime) 


        

<hr>



### define CUVIS\_MESU\_FLAG\_WHITE\_TEMP\_KEY 

```
#define CUVIS_MESU_FLAG_WHITE_TEMP_KEY `"Flag_TemperatureMismatchWhite"`
```



see [**CUVIS\_MESU\_FLAG\_WHITE\_TEMP**](cuvis_8h.md#define-cuvis_mesu_flag_white_temp) 


        

<hr>



### define CUVIS\_MESU\_GPS\_KEY 

```
#define CUVIS_MESU_GPS_KEY `"GPS_data"`
```



name of the GPS data field, if available 


        

<hr>



### define CUVIS\_MESU\_PAN\_KEY 

```
#define CUVIS_MESU_PAN_KEY `"pan"`
```



name of the pan image (pixels registered to [**CUVIS\_MESU\_CUBE\_KEY**](group__cuvis__reserved__keys.md#define-cuvis_mesu_cube_key)) 


        

<hr>



### define CUVIS\_MESU\_PREVIEW\_KEY 

```
#define CUVIS_MESU_PREVIEW_KEY `"preview"`
```



name of the generate preview image, if available. The preview will be generated by the [**cuvis\_proc\_cont\_apply**](group__cuvis__proc.md#function-cuvis_proc_cont_apply) function 


        

<hr>



### define CUVIS\_MESU\_WHITEDARKREF\_KEY 

_If this field is present, a white's dark was set while recording the measurement. This is the white' dark that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._
```
#define CUVIS_MESU_WHITEDARKREF_KEY `"white_dark_ref"`
```




<hr>



### define CUVIS\_MESU\_WHITEREF\_KEY 

_If this field is present, a white was set while recording the measurement. This is the white that is implicitly loaded when a processing context is created with the current measurement and used, if a dark is needed (unless overwritten by_ [_**cuvis\_proc\_cont\_set\_reference**_](group__cuvis__proc.md#function-cuvis_proc_cont_set_reference) _) The reference file should be located in ../Calibration/&lt;reference-name&gt;.cu3 or the precise path defined by the string value of the data tag._
```
#define CUVIS_MESU_WHITEREF_KEY `"white_ref"`
```




<hr>

------------------------------


