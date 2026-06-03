

# Struct cuvis\_gps\_t



[**ClassList**](annotated.md) **>** [**cuvis\_gps\_t**](structcuvis__gps__t.md)



_The gps data structure._ 

* `#include <cuvis.h>`





















## Public Attributes

| Type | Name |
| ---: | :--- |
|  double | [**altitude**](#variable-altitude)  <br> |
|  double | [**latitude**](#variable-latitude)  <br> |
|  double | [**longitude**](#variable-longitude)  <br> |
|  [**CUVIS\_TIMESTAMP**](cuvis_8h.md#define-cuvis_timestamp) | [**time**](#variable-time)  <br> |












































## Public Attributes Documentation




### variable altitude 

```C++
double cuvis_gps_t::altitude;
```



gps altitude in meters 


        

<hr>



### variable latitude 

```C++
double cuvis_gps_t::latitude;
```



gps latitude in decimal degrees 


        

<hr>



### variable longitude 

```C++
double cuvis_gps_t::longitude;
```



gps longitude in decimal degrees 


        

<hr>



### variable time 

```C++
CUVIS_TIMESTAMP cuvis_gps_t::time;
```



the timestamp (UTC) while recoding the gps. 


        

<hr>

------------------------------
The documentation for this class was generated from the following file `docs/_api_sources/cuvis.h`

