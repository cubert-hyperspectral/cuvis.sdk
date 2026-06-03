

# Struct cuvis\_save\_args\_t



[**ClassList**](annotated.md) **>** [**cuvis\_save\_args\_t**](structcuvis__save__args__t.md)



_options for saving as cu3/cu3s files_ [More...](#detailed-description)

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**allow\_drop**](#variable-allow_drop)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**allow\_info\_file**](#variable-allow_info_file)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**allow\_overwrite**](#variable-allow_overwrite)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**allow\_session\_file**](#variable-allow_session_file)  <br> |
|  double | [**fps**](#variable-fps)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**full\_export**](#variable-full_export)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**hard\_limit**](#variable-hard_limit)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**max\_buftime**](#variable-max_buftime)  <br> |
|  [**CUVIS\_SESSION\_MERGE\_MODE**](cuvis_8h.md#define-cuvis_session_merge_mode) | [**merge\_mode**](#variable-merge_mode)  <br> |
|  [**CUVIS\_OPERATION\_MODE**](cuvis_8h.md#define-cuvis_operation_mode) | [**operation\_mode**](#variable-operation_mode)  <br> |
|  [**CUVIS\_INT**](cuvis_8h.md#define-cuvis_int) | [**soft\_limit**](#variable-soft_limit)  <br> |












































## Detailed Description


The cube exporter works asynchronically. For


## offline saving to session file



When processing sesion files (allow\_session\_file=true) offline, the option [**allow\_drop**](structcuvis__save__args__t.md#variable-allow_drop) should be set to false. In this case measurements are added to the internal buffer until the size given by [**hard\_limit**](structcuvis__save__args__t.md#variable-hard_limit) is reached. 
 In this mode, the options [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) and [**max\_buftime**](structcuvis__save__args__t.md#variable-max_buftime) are ignroed.



## online saving to session file



When recording sesion files (allow\_session\_file=true) live, the options [**allow\_drop**](structcuvis__save__args__t.md#variable-allow_drop) should be set to true.


When a new measurement is added to the cube exporter, the following strategy is applied:



* The internal buffer has a total limit of size [**hard\_limit**](structcuvis__save__args__t.md#variable-hard_limit). If the buffer is full, it will be dropped (end).
* If the buffer is not full, the [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) is checked. If it is reachd, the ordering of the frame numbers is ignored and the measurement with the lowest sequence nubmer is stored to the disk directly. (This can mess up the order of the frames set [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) = [**hard\_limit**](structcuvis__save__args__t.md#variable-hard_limit) to disable this behaviour)
* All meausurements in the internal buffer are checked: If they are held in the buffer for longer then the time given by [**max\_buftime**](structcuvis__save__args__t.md#variable-max_buftime), they are saved to disk directly. (This can mess up the order of the frames set [**max\_buftime**](structcuvis__save__args__t.md#variable-max_buftime) to a higher value allow for longer hold time intervals.) 





    
## Public Attributes Documentation




### variable allow\_drop 

```C++
CUVIS_INT cuvis_save_args_t::allow_drop;
```



allow to drop files, if output buffers are full


This options controlls the export behaviour. If internal write buffers are full, new measurements are either dropped or kept.


The policy to drop measurements on full buffer (allow\_drop=true) is recommended for online opration. The idea is to rather drop measurements and thus allow the acquisition to continue without slowing down. When this policy is set, the [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) and the [**max\_buftime**](structcuvis__save__args__t.md#variable-max_buftime) options are also used (see there).


If new measurements are forced to be kept (allow\_drop=true), the exporter will wait until the measurement can be written. This polocy is recommended for batch-processing measurements (offline). The options [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) and [**max\_buftime**](structcuvis__save__args__t.md#variable-max_buftime) are ignored.




**Note:**

This option only applies, if allow\_session\_file=true. 





        

<hr>



### variable allow\_info\_file 

```C++
CUVIS_INT cuvis_save_args_t::allow_info_file;
```



save additional info file.


The info file is written to the same path as the export files. It is a plain text file and consits of the a header showing the recoridng FPS and mode and a body, where each frame number from 0 till the last frame written is shown by their name. Missing frames are noted as "dropped".




**Note:**

The output of this file is not flushed until the exporter writes to a different file or is closed. Thus, it is not suited to be used as a way to monitor frame drops during live acquisiton.


This option is ignored, when [**allow\_session\_file**](structcuvis__save__args__t.md#variable-allow_session_file) is set to false. 


        

<hr>



### variable allow\_overwrite 

```C++
CUVIS_INT cuvis_save_args_t::allow_overwrite;
```



allow to overwrite an existing file. 



This option anables to allow to ovewrite files on the disk, if they exist.




**Note:**

When exporting to legacy format of version 2.x (allow\_session\_file=false and allow\_fragmentation=true), only the existance of the \*.cu3 file is checked, existing \*.tiff files are neither cleaned up nor checked if they exist prior overwriting. 





        

<hr>



### variable allow\_session\_file 

```C++
CUVIS_INT cuvis_save_args_t::allow_session_file;
```



save files of same session number to a single cu3s file. If allow\_fragmentation is set, cu3s fill be split by measurement. Default in Wrappers: True 


        

<hr>



### variable fps 

```C++
double cuvis_save_args_t::fps;
```



the fps used in operation\_mode video


only used if allow\_session\_file=true and operation\_mode=Internal. 


        

<hr>



### variable full\_export 

```C++
CUVIS_INT cuvis_save_args_t::full_export;
```



Whether processing results are also saved in the export.


If enabled, all cube data and accompanying meta-data are stored in the exported file as well. This vastly increases file size and the time and processing resources needed for the export.


If disabled, only the raw image from the camera and raw data from any additional devices are stored. This in turn requires the data to be reprocessed when loading it again. 


        

<hr>



### variable hard\_limit 

```C++
CUVIS_INT cuvis_save_args_t::hard_limit;
```



Maximum number of elements in output cache


The hard limit is only used if allow\_session\_file=true.


The output cache has a maximum size of [**hard\_limit**](structcuvis__save__args__t.md#variable-hard_limit). If more measurements are added, adding another measurment is not possible. Adding a measurement will lock the calling function if [**allow\_drop**](structcuvis__save__args__t.md#variable-allow_drop) is set to false. If [**allow\_drop**](structcuvis__save__args__t.md#variable-allow_drop) is set to true, the added frame is directrly dropped and not stored.




**Note:**

This behaviour also applies when using the exproter within a worker. 





        

<hr>



### variable max\_buftime 

```C++
CUVIS_INT cuvis_save_args_t::max_buftime;
```



Any frame is forced to be written after this time (in ms), latest.


The maximum buffer time option is only used if allow\_drop=true and allow\_session\_file=true.


The time a buffer is held in the exporter's cache is tracked. If the time given by the max\_buftime is exceeded, a measuremnt is written to disk.


This option also helps to guarantee a measurements to be serialized to a permanent storage and avoid data loss upon power or abnormal program termination.


This option will overwrite the [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) for this frame, if needed. 


        

<hr>



### variable merge\_mode 

```C++
CUVIS_SESSION_MERGE_MODE cuvis_save_args_t::merge_mode;
```



allow to split file to multiple files.


When exporting to a cu3s file (allow\_session\_file=true) the merge mode (previous allow\_fragmentation flag) controlles if all measurements (of the same session name) are written as they are present in the input directory (set to 0) or if each measurement is saved to a separate cu3s file (set to 1). The latter option generates substantial overhead. If the merge mode is merging (set to 2)all measurements are written to one file even if they are present as multiple files on the disk. Different references will still result in additional session files being written.


When exporting to a (legacy) cu3 file (allow\_session\_file=false), the merge mode fragmentation (previous allow\_fragmentation flag) will lead to multiple files exported: a &lt;name&gt;.cu3 file, followed by &lt;name&gt;\_&lt;postfix&gt;.tiff files. These come as a tuple and must be kept together, else the file will be corrupted. This export option is intended for legacy programs that were deisnged to read raw data with the previous software verison 2.x. 


        

<hr>



### variable operation\_mode 

```C++
CUVIS_OPERATION_MODE cuvis_save_args_t::operation_mode;
```



give the current operation mode.


Save the operation mode used while recording. Only used if [**allow\_session\_file**](structcuvis__save__args__t.md#variable-allow_session_file) is set. 


        

<hr>



### variable soft\_limit 

```C++
CUVIS_INT cuvis_save_args_t::soft_limit;
```



Out-of-order frames are sorted within the cache, as long as the cache useage is below this limit.


The soft limit is only used if allow\_drop=true and allow\_session\_file=true.


The internal chache may hold up to [**soft\_limit**](structcuvis__save__args__t.md#variable-soft_limit) number of frames that are out of sequence.


For example: Let the the seqence number of the measurement written last be #14, and let the internal cache hold the frames #16,#17,...#24 (9 images in chache) and let the soft limit be 10 If we assume the next frame to be #25, the 10 images in cache reached the soft limit, forcing the first frame with the lowest nubmer (#16) to be written (#15 is makred as 'dropped'). If the next image actually is #15, this image is then written out of sequence, resulting in the order #14, #16, #15.


Theese are the states of the example avove.



> write to disk: #14 

> cache: #16,#17,...#24 [soft limit: 10] 

> insert: #25 

> write to disk: #16 

> cache: #17,...#24, #25 [soft limit: 10] 

> insert: #15 

> write to disk: #15 

> cache: #17,...#24, #25 [soft limit: 10] 
This behaviour is a compromise between keeping the seuqence in order and at the same time not storing too many images if a frame was acutally dropped. Increase the soft\_limit to a value same or grater the [**hard\_limit**](structcuvis__save__args__t.md#variable-hard_limit) to disable this behaviour. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

