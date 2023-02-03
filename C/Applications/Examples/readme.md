## 01_loadMeasurement
Load measurement from disk and print the value (count) for all available channels (wavelength) for one specific pixel.

## 02_reprocessMeasurement
Load measurement as well as references (dark, white, distance) from disk and reprocess the measurement to e.g. reflectance.

## 03_exportMeasurement
Load measurement from disk and save to different file formats.

## 04_changeDistance
Load measurement from disk and reprocess to a new distance.

## 05_recordSingleImages
Setup camera and record measurements via software trigger, aka "single shot mode" or "software mode".

## 06_recordVideo
Setup camera and record measurements via internal clock triggering, aka "video mode". In this example the worker is used to make use of multithreading (cuvis_worker_create).