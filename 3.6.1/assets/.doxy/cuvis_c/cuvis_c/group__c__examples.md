

# Group c\_examples



[**Modules**](modules.md) **>** [**c\_examples**](group__c__examples.md)



[More...](#detailed-description)


































































## Detailed Description


There are several examples delivered with the SDK


## Overview



Under Windows you can find the examples in your installation directory (Default: "C:\Program Files\Cuvis\sdk\cuvis\_c\examples" or "C:\Program Files\Cuvis\sdk\cuvis\_cpp\examples"), under Linux they can be found in "/lib/cuvis/cuvis\_c/examples" or "/lib/cuvis/cuvis\_cpp/examples" . Each Example comes with the precompiled binary, a short .sh-script to run the application and the source code file. The .sh-script requires the bash console. Under windows we recommend to use Git Bash.


Examples 01-04 and 07 require the "sample\_data" folder to be present in the installation directory ( Windows: "C:\Program Files\Cuvis\sdk\sample\_data" , Linux: "/lib/cuvis/sample\_data"). Examples 05-06 require a camera to be installed and connected.



## Compiling examples



Instead of using the precompiled examples, you can use the provided source code to compile it yourself. Under Linux this is quite simple.



```
sudo apt install gcc
sudo gcc -o 0X_example main.c  -L/lib/cuvis -lcuvis
```



or



```
sudo apt install g++
sudo g++ -o 0X_example main.cpp  -L/lib/cuvis -lcuvis -std=c++17
```
 



    

------------------------------


