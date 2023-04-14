# CUVIS Python SDK

Python Version: 3.9. _This is a strict requirement!_ The Python interpreter must be 3.9.x. Both older and newer versions are not compatible with the provided bindings to the compiled SDK.

## Installing Cuvis Python SDK

In order to install the Python SDK, the Cuvis application must be installed first.

Download the installer for windows (or the .deb files for Ubuntu 20.04) and the `_cuvis_pyil.pyd` file as well as the `cuvis_il.py` file [here](
https://cloud.cubert-gmbh.de/index.php/s/dPycyPcjnvee9F0). On Ubuntu systems these files will be named `_cuvis_pyil.so` and `cuvis_il.py`.

After installing, check out the repository and copy the `_cuvis_pyil` as well as the `cuvis_il.py` file into `Cuvis-SDK\Python\src\cuvis`.

### Virtual Environment Creation

Create a virtual environment with the following commands. This will protect your normal Python programming environment from the specific packages the CUVIS SDK needs to run.
```
cd <<Cuvis-SDK>>/Python/src
python -m venv cubert_env
# Windows
.\cubert_env\Scripts\activate
# Ubuntu
source ./cubert_env/bin/activate
```

As prerequisites for building the package, ensure the system has the appropriate build tools installed: `pip install wheel setuptools==45 setuptools_scm`

Then navigate from within your coding environment to `Cuvis-SDK/Python/src` and run `pip install [--editable] .` in the command line.

## Linux Specific Instructions

Linux requires the application of additional environmental settings. Add the following variables to your `.bashrc` file.

```
export CUVIS="/lib/cuvis"
export CUVIS_DATA="/opt/cuvis"
```
To give cuvis permission to create log files, run this command to set ownership of the Cuvis directory to your user.
```
sudo chown -R <<USER_NAME>> /opt/cuvis/
```
### Running Jupyter Notebooks

Jupyter notebooks are interactive, web-based Python interpreters. There are example notebooks provided in the `notebooks` directory. With your virtual environment active, run the following command to enable interactive controls in the notebooks.

```
jupyter nbextension enable --py widgetsnbextension
```
You are now ready to launch a notebook. `cd notebooks` and run `jupyter-notebook` to start the Jupyter webserver.

In browser, select `Hyperspectral_Data_Exploration.ipynb` to open the notebook. A great beginner guide to Jupyter notebooks is available from [*Python Like You Mean It*](https://www.pythonlikeyoumeanit.com/Module1_GettingStartedWithPython/Jupyter_Notebooks.html).
