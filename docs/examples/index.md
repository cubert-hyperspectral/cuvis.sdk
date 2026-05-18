# Examples

The following examples demonstrate the core workflows of the Cuvis SDK.
Each example is available in Python (Jupyter notebook), C, and C++.

Use the language tabs within each example to switch between implementations.
Clicking a tab (e.g. **C++**) syncs all code blocks on the page to that language.

!!! note "Prerequisites"
    All examples require:

    - A Cuvis SDK installation
    - Camera settings files (provided with your camera and the SDK)
    - For examples 2–5: a recorded measurement file (`.cu3s`) or the
      [demo dataset](https://cloud.cubert-gmbh.de/s/SDKSampleData)

| Example | Description |
|---|---|
| [1 – Take Snapshot](example_1_take_snapshot.md) | Connect to a camera and capture a single measurement |
| [2 – Load Measurement](example_2_load_measurement.md) | Load a recorded `.cu3s` file and inspect its data |
| [3 – Reprocess](example_3_reprocess.md) | Re-apply spectral processing to a stored measurement |
| [4 – Exporters](example_4_exporters.md) | Export measurements to common file formats |
| [5 – Record Video](example_5_record_video.md) | Continuously record a video stream of measurements |
