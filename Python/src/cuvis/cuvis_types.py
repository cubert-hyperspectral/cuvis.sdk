import numpy as np

from . import cuvis_il

MeasurementFlag = dict({
    ("POOR_REFERENCE", cuvis_il.CUVIS_MESU_FLAG_POOR_REFERENCE_KEY),
    ("OVERILLUMINATED", cuvis_il.CUVIS_MESU_FLAG_OVERILLUMINATED_KEY),
    ("POOR_WHITE_BALANCING", cuvis_il.CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY),
    ("DARK_INTTIME", cuvis_il.CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY),
    ("DARK_TEMP", cuvis_il.CUVIS_MESU_FLAG_DARK_TEMP_KEY),
    ("WHITE_INTTIME", cuvis_il.CUVIS_MESU_FLAG_WHITE_INTTIME_KEY),
    ("WHITE_TEMP", cuvis_il.CUVIS_MESU_FLAG_WHITE_TEMP_KEY),
    ("WHITEDARK_INTTIME", cuvis_il.CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY),
    ("WHITEDARK_TEMP", cuvis_il.CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY),
})

__CuvisProcessingMode__ = dict({
    ("Preview", cuvis_il.Preview),
    ("Cube_Raw", cuvis_il.Cube_Raw),
    ("Cube_DarkSubtract", cuvis_il.Cube_DarkSubtract),
    ("Cube_Reflectance", cuvis_il.Cube_Reflectance),
    ("Cube_SpectralRadiance", cuvis_il.Cube_SpectralRadiance)
})

__CuvisDataType__ = dict({
    ("data_type_unsupported", cuvis_il.data_type_unsupported),
    ("data_type_image", cuvis_il.data_type_image),
    ("data_type_gps", cuvis_il.data_type_gps),
    ("data_type_string", cuvis_il.data_type_string),
    ("data_type_sensor_info", cuvis_il.data_type_sensor_info),
})

__CuvisReferenceType__ = dict({
    ("Reference_Dark", cuvis_il.Reference_Dark),
    ("Reference_White", cuvis_il.Reference_White),
    ("Reference_WhiteDark", cuvis_il.Reference_WhiteDark),
    ("Reference_SpRad", cuvis_il.Reference_SpRad),
    ("Reference_Distance", cuvis_il.Reference_Distance),
})

__CuvisSessionItemType__ = dict({
    ("all_frames", cuvis_il.session_item_type_frames),
    ("no_gaps", cuvis_il.session_item_type_frames_no_gaps),
    ("references", cuvis_il.session_item_type_references)
})

DataFormat = dict({
    (1, np.uint8),
    (2, np.uint16),
    (3, np.uint32),
    (4, np.float32)
})

PanSharpeningInterpolationType = dict({
    ("NearestNeighbour",
     cuvis_il.pan_sharpening_interpolation_type_NearestNeighbor),
    ("Linear", cuvis_il.pan_sharpening_interpolation_type_Linear),
    ("Cubic", cuvis_il.pan_sharpening_interpolation_type_Cubic),
    ("Lanczos", cuvis_il.pan_sharpening_interpolation_type_Lanczos),
})

PanSharpeningAlgorithm = dict({
    ("Noop", cuvis_il.pan_sharpening_algorithm_Noop),
    ("CubertMacroPixel", cuvis_il.pan_sharpening_algorithm_CubertMacroPixel),
})

ProcessingMode = dict({
    ("Preview", __CuvisProcessingMode__["Preview"]),
    ("Raw", __CuvisProcessingMode__["Cube_Raw"]),
    ("DarkSubtract", __CuvisProcessingMode__["Cube_DarkSubtract"]),
    ("Reflectance", __CuvisProcessingMode__["Cube_Reflectance"]),
    ("SpectralRadiance", __CuvisProcessingMode__["Cube_SpectralRadiance"])
})

ReferenceType = dict({
    ("White", __CuvisReferenceType__["Reference_White"]),
    ("Dark", __CuvisReferenceType__["Reference_Dark"]),
    ("WhiteDark", __CuvisReferenceType__["Reference_WhiteDark"]),
    ("SpRad", __CuvisReferenceType__["Reference_SpRad"]),
    ("Distance", __CuvisReferenceType__["Reference_Distance"]),
})

DataType = dict({
    ("unsupported", __CuvisDataType__["data_type_unsupported"]),
    ("image", __CuvisDataType__["data_type_image"]),
    ("gps", __CuvisDataType__["data_type_gps"]),
    ("string", __CuvisDataType__["data_type_string"]),
    ("sensor_info", __CuvisDataType__["data_type_sensor_info"]),
})

TiffCompressionMode = dict({
    ("None", cuvis_il.tiff_compression_mode_None),
    ("LZW", cuvis_il.tiff_compression_mode_LZW),
})

TiffFormat = dict({
    ("Single", cuvis_il.tiff_format_Single),
    ("MultiChannel", cuvis_il.tiff_format_MultiChannel),
    ("MultiPage", cuvis_il.tiff_format_MultiPage),
})

HardwareState = dict({
    ("Online", cuvis_il.hardware_state_online),
    ("PartiallyOnline", cuvis_il.hardware_state_partially_online),
    ("Offline", cuvis_il.hardware_state_offline),
})

OperationMode = dict({
    ("External", cuvis_il.OperationMode_External),
    ("Internal", cuvis_il.OperationMode_Internal),
    ("Software", cuvis_il.OperationMode_Software),
    ("UNDEFINED", cuvis_il.OperationMode_Undefined),
})

ComponentType = dict({
    ("ImageSensor", cuvis_il.component_type_image_sensor),
    ("MiscSensor", cuvis_il.component_type_misc_sensor),
})

AsyncResult = dict({
    ("overwritten", 2),
    ("timeout", 1),
    ("done", 0),
    ("deferred", 3),
})

CUVIS_imbuffer_format = dict({
    ("imbuffer_format_uint8", cuvis_il.imbuffer_format_uint8),
    ("imbuffer_format_uint16", cuvis_il.imbuffer_format_uint16),
    ("imbuffer_format_uint32", cuvis_il.imbuffer_format_uint32),
    ("imbuffer_format_float", cuvis_il.imbuffer_format_float),
})

CUVIS_capabilities = dict({
    ("AcquisitionCapture", cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_CAPTURE),
    ("AcquisitionTimelapse",
     cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_TIMELAPSE),
    ("AcquisitionContinuous",
     cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_CONTINUOUS),
    (
        "AcquisitionSnapshot",
        cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SNAPSHOT),
    ("AcquisitionSetIntegrationtime",
     cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SETINTEGRATIONTIME),
    ("AcquisitionSetGain", cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_SETGAIN),
    ("AcquisitionAveraging",
     cuvis_il.CUVIS_MODE_CAPABILITY_ACQUISITION_AVERAGING),
    ("ProcessingSensorRaw",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SENSOR_RAW),
    ("ProcessingCubeRaw", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_RAW),
    ("ProcessingCubeRef", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_REF),
    ("ProcessingCubeDarkSubtract",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_DARKSUBTRACT),
    ("ProcessingCubeFlatFielding",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_FLATFIELDING),
    ("ProcessingCubeSpectralRadiance",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CUBE_SPECTRALRADIANCE),
    ("ProcessingSaveFile", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SAVE_FILE),
    ("ProcessingClearRaw", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CLEAR_RAW),
    ("ProcessingCalcLive", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_CALC_LIVE),
    ("ProcessingAutoExposure",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_AUTOEXPOSURE),
    ("ProcessingOrientation",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_ORIENTATION),
    ("ProcessingSetWhite", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_WHITE),
    ("ProcessingSetDark", cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DARK),
    ("ProcessingSetSprad",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_SPRADCALIB),
    ("ProcessingSetDistanceCalib",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCECALIB),
    ("ProcessingSetDistanceValue",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_SET_DISTANCE_VALUE),
    ("ProcessingUseDarkSpradcalib",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_USE_DARK_SPRADCALIB),
    ("ProcessingUseWhiteSpradCalib",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_USE_WHITE_SPRADCALIB),
    ("ProcessingRequireWhiteDarkReflectance",
     cuvis_il.CUVIS_MODE_CAPABILITY_PROCESSING_REQUIRE_WHITEDARK_REFLECTANCE),
    ("UNDEFINED", 2 ** 26),

})
