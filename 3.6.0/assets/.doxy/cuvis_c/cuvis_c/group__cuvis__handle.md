

# Group cuvis\_handle



[**Modules**](modules.md) **>** [**cuvis\_handle**](group__cuvis__handle.md)



_The SDK is handle-based, i.e to access an internal data object you will require a handle._ [More...](#detailed-description)


































































## Detailed Description


The main concepts of the SDK which use handles are the [**Measurement**](group__cuvis__mesu.md), the [**Calibration**](group__cuvis__calib.md), the [**Session File**](group__cuvis__session.md), the [**Acquisition Context**](group__cuvis__acq.md), the [**Processing Context**](group__cuvis__proc.md), the [**Viewer**](group__cuvis__viewer.md), the [**Export API**](group__cuvis__exporter.md) and the [**Worker**](group__cuvis__worker.md). On how to obtain a handle of the individual components of the SDK, see the respective Pages for the individual components.


For example, a handle wich represents a [**Measurement**](group__cuvis__mesu.md) can be obtained by either loading ([**cuvis\_measurement\_load**](group__cuvis__mesu.md#function-cuvis_measurement_load)) or by recording ([**cuvis\_acq\_cont\_capture**](group__cuvis__acq.md#function-cuvis_acq_cont_capture) or [**cuvis\_acq\_cont\_get\_next\_measurement**](group__cuvis__acq.md#function-cuvis_acq_cont_get_next_measurement)) a measurement. 
A measurement is equivalent to a data-cube and would be called a frame in a traditional Camera-Setup. The handle then refers to measurement in the SDK context.


Each handle should be freed after it is no longer needed. This can be done via the respective free function. Calling the free-function does not necessarily free up the used memory immediately, because there could be multiple handles referring to the same object. 


    

------------------------------


