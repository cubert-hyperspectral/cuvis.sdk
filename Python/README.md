# CUVIS Python SDK

Python Version: 3.9

## Installing Cuvis Python SDK via setup.py

__In order to install the Python SDK, Cuvis must be installed. 
Download the installer for windows (or the .deb files for Ubuntu 20.04) and the \_cuvis\_pyil file as well as the cuvis\_il.py file here:__
https://cloud.cubert-gmbh.de/index.php/s/dPycyPcjnvee9F0

After installing, check out the repository and copy the *\_cuvis\_pyil* as well as the cuvis\_il.py file into *Cubert-Community-Hub\Python\src\cuvis*.

### Virtual Environment Creation

Create a virtual environment with the following commands. This will protect your normal Python programming environment from the specific packages the CUVIS SDK needs to run.
```
cd <<Cubert-Community-Hub>>/Python/src
python -m venv cubert_env
./cubert_env/Scripts/activate
```

Then navigate from within your coding environment to *Cubert-Community-Hub\Python\src* and run *pip install . [-e]* in the command line.

## Linux Specific Instructions

Linux will require the application of additional environmental settings. Add the following variables to your `.bashrc` file.

```
export CUVIS="/lib/cuvis"
export CUVIS_DATA="/opt/cuvis"
```
To give cuvis permission to create log files, run this command to set ownership of the Cuvis directory to your user.
```
sudo chown -R <<USER_NAME>> /opt/cuvis/
```
### Running Jupyter Notebooks

Jupyter notebooks are an interactive, web-based Python interpreter. There are example notebooks provided in the `notebooks` directory. With your virtual environment active, run the following command to enable interactive controls in the notebooks.

```
jupyter nbextension enable --py widgetsnbextension
```
You are now ready to launch a notebook. `cd notebooks` and run `jupyter-notebook` to start the Jupyter webserver.