# CUVIS Python SDK

Python Version: 3.9

## Installing Cuvis Python SDK via setup.py

__In order to install the Python SDK, Cuvis must be installed. 
Download the installer for windows (or the .deb files for Ubuntu 20.04) and the \_cuvis\_pyil file as well as the cuvis\_il.py file here:__
https://cloud.cubert-gmbh.de/index.php/s/dPycyPcjnvee9F0

After installing, check out the repository and copy the *\_cuvis\_pyil* as well as the cuvis\_il.py file into *Cubert-Community-Hub\Python\src\cuvis*.

Then navigate from within your coding environment to *Cubert-Community-Hub\Python\src* and run *pip install . [-e]* in the command line. 

## Python Specific Instructions

Linux will require the application of additional environmental settings. Add the following variables to your `.bashrc` file.

```
export CUVIS="/lib/cuvis"
export CUVIS_DATA="/opt/cuvis"
```
To give cuvis permission to create log files, run this command to set ownership of the Cuvis directory to your user.
```
sudo chown -R <<USER_NAME>> /opt/cuvis/
```
