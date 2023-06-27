import datetime
import os

from . import cuvis_il
from .cuvis_aux import SDKException, __bit_translate__, __object_declassifier__
from .cuvis_types import DataFormat, ProcessingMode

base_datetime = datetime.datetime(1970, 1, 1)


class Measurement(object):

    def __init__(self, base):
        self.__handle__ = None
        self.__metaData__ = cuvis_il.cuvis_mesu_metadata_allocate()

        self.Data = None

        self.CaptureTime = None
        self.MeasurementFlags = None
        self.Path = None
        self.Comment = None
        self.FactoryCalibration = None
        self.Assembly = None
        self.Averages = None
        self.IntegrationTime = None
        self.SerialNumber = None
        self.ProductName = None
        self.ProcessingMode = None
        self.Name = None
        self.Session = None

        if isinstance(base, int):
            self.__handle__ = base
        elif isinstance(base, str) and os.path.exists(base):
            _ptr = cuvis_il.new_p_int()
            if cuvis_il.status_ok != cuvis_il.cuvis_measurement_load(base,
                                                                     _ptr):
                raise SDKException()
            self.__handle__ = cuvis_il.p_int_value(_ptr)
        else:
            raise SDKException(
                "Could not open Measurement! Either handle not"
                " available or file not found!")
        self.refresh()
        pass

    def load(self, file):
        self.__init__(file)
        pass

    def refresh(self):
        self.Data = {}
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_get_metadata(
                self.__handle__, self.__metaData__):
            raise SDKException

        self.CaptureTime = base_datetime + datetime.timedelta(
            milliseconds=self.__metaData__.capture_time)
        self.MeasurementFlags = self.__metaData__.measurement_flags
        # TODO: Flags should be more and better info!
        self.Path = self.__metaData__.path
        self.Comment = self.__metaData__.comment
        self.FactoryCalibration = base_datetime + datetime.timedelta(
            milliseconds=self.__metaData__.factory_calibration)
        self.Assembly = self.__metaData__.assembly
        self.Averages = self.__metaData__.averages
        self.IntegrationTime = self.__metaData__.integration_time
        self.SerialNumber = self.__metaData__.serial_number
        self.ProductName = self.__metaData__.product_name
        self.ProcessingMode = \
            [key for key, val in ProcessingMode.items() if
             val == self.__metaData__.processing_mode][0]
        self.Name = self.__metaData__.name
        # self.SessionFile = SessionData(self.__metaData__.session_info.name,
        #                           self.__metaData__.session_info.session_no,
        #                           self.__metaData__.session_info.sequence_no)

        pcount = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_get_data_count(
                self.__handle__, pcount):
            raise SDKException()
        for ind in range(cuvis_il.p_int_value(pcount)):
            pType = cuvis_il.new_p_cuvis_data_type_t()
            key = cuvis_il.cuvis_measurement_get_data_info_swig(self.__handle__,
                                                                pType, ind)
            cdtype = cuvis_il.p_cuvis_data_type_t_value(pType)
            if cdtype == cuvis_il.data_type_image:
                data = cuvis_il.cuvis_imbuffer_t()
                cuvis_il.cuvis_measurement_get_data_image(self.__handle__,
                                                          key,
                                                          data)
                # t0 = datetime.datetime.now()
                self.Data.update({key: ImageData(img_buf=data,
                                                 dformat=DataFormat[
                                                     data.__getattribute__(
                                                         "format")])})
                # print("image loading time: {}".format(
                # datetime.datetime.now() - t0))
            elif cdtype == cuvis_il.data_type_string:
                val = cuvis_il.cuvis_measurement_get_data_string_swig(
                    self.__handle__, key)
                self.Data.update({key: val})
            elif cdtype == cuvis_il.data_type_gps:
                gps = cuvis_il.cuvis_gps_t()
                cuvis_il.cuvis_measurement_get_data_gps(self.__handle__, key,
                                                        gps)
                self.Data.update({key: gps})
            elif cdtype == cuvis_il.data_type_sensor_info:
                info = cuvis_il.cuvis_sensor_info_t()
                cuvis_il.cuvis_measurement_get_data_sensor_info(self.__handle__,
                                                                key, info)
                self.Data.update({key: info})
            else:
                self.Data.update({key: "Not Implemented!"})

    def save(self, saveargs):
        ge, sa = saveargs.getInternal()
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_save(
                self.__handle__, ge.export_dir, sa):
            raise SDKException()
        pass

    def setName(self, name):
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_set_name(
                self.__handle__, name):
            raise SDKException()
        self.Name = name
        pass

    def getThumbnail(self):
        thumbnail = [val for key, val in self.Data.items() if "view" in key]
        if len(thumbnail) == 0:
            print("No thumbnail available. Use cube instead!")
            pass
        elif len(thumbnail) == 1:
            return thumbnail[0]
        elif len(thumbnail) > 1:
            shapes = [th.array.shape for th in thumbnail]
            return thumbnail[shapes.index(min(shapes))]

    def getDataInfo(self):
        return_dict = {}
        for att in self.Data["IMAGE_info"].__dir__():
            if not (att.startswith("__") or att.startswith("this")):
                return_dict.update(
                    {att: self.Data["IMAGE_info"].__getattribute__(att)})
        try:
            return_dict["readout_time"] = str(
                base_datetime + datetime.timedelta(
                    milliseconds=return_dict["readout_time"]))
        except:
            print("No human readable readout_time available!")
        return return_dict

    def getCapabilities(self):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_get_capabilities(
                self.__handle__, _ptr):
            raise SDKException()
        return __bit_translate__(cuvis_il.p_int_value(_ptr))

    def getCalibrationID(self):
        _id = cuvis_il.cuvis_measurement_get_calib_id_swig(self.__handle__)
        return _id

    def setComment(self, comment):
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_set_comment(
                self.__handle__, comment):
            raise SDKException()
        self.Comment = comment
        self.__metaData__.comment = comment
        pass

    def getMetadata(self):
        return_MD = __object_declassifier__(self.__metaData__)
        for k, val in return_MD.items():
            if k in ["capture_time", "factory_calibration"]:
                return_MD[k] = str(
                    base_datetime + datetime.timedelta(milliseconds=val))
        return_MD.pop("this")
        return_MD.pop("thisown")
        return return_MD

    def getDataCount(self):  # done
        out = cuvis_il.new_p_int()
        cuvis_il.cuvis_measurement_get_data_count(self.__handle__, out)
        return cuvis_il.p_int_value(out)

    def clearCube(self):
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_clear_cube(
                self.__handle__):
            raise SDKException()
        pass

    def clearImplicitReference(self, ref_type):
        if cuvis_il.status_ok != \
                cuvis_il.cuvis_measurement_clear_implicit_reference(
                    self.__handle__, ref_type):
            raise SDKException()

    def __del__(self):
        _ptr = cuvis_il.new_p_int()
        self.clearCube()
        cuvis_il.p_int_assign(_ptr, self.__handle__)
        cuvis_il.cuvis_measurement_free(_ptr)
        self.__handle__ = cuvis_il.p_int_value(_ptr)

        cuvis_il.cuvis_mesu_metadata_free(self.__metaData__)

        self.Data = {}

        self.CaptureTime = None
        self.MeasurementFlags = None
        self.Path = None
        self.Comment = None
        self.FactoryCalibration = None
        self.Assembly = None
        self.Averages = None
        self.IntegrationTime = None
        self.SerialNumber = None
        self.ProductName = None
        self.ProcessingMode = None
        self.Name = None
        self.Session = None
        pass

    def __deepcopy__(self, memo):
        _ptr = cuvis_il.new_p_int()
        if cuvis_il.status_ok != cuvis_il.cuvis_measurement_deep_copy(
                self.__handle__, _ptr):
            raise SDKException()
        copy = Measurement(cuvis_il.p_int_value(_ptr))
        return copy

        ## failback: detailed copy bit by bit.
        # cls = self.__class__
        # res = cls.__new__(cls)
        # memo[id(self)] = res
        # for k, v in self.__dict__.items():
        #    print("copying: {}".format(k))
        #    try:
        #        setattr(res, k, deepcopy(v, memo))
        #    except:
        #        print("issues with deep copying {}".format(k))
        #        if k == "__metaData__":
        #            setattr(res, k, None)
        #            res.__metaData__ = cuvis_il.cuvis_mesu_metadata_t()
        #            res.__metaData__ = cuvis_il.cuvis_mesu_metadata_allocate()
        #            if cuvis_il.status_ok != \
        #                    cuvis_il.cuvis_measurement_get_metadata(
        #                        res.__handle__,
        #                        res.__metaData__):
        #                raise SDKException()
        #            else:
        #                print("__metaData__ set!")

        #        else:
        #            setattr(res, k, v)
        # return res


class ImageData(object):
    def __init__(self, img_buf=None, dformat=None):

        if img_buf is None:

            self.width = None
            self.height = None
            self.channels = None
            self.array = None
            self.wavelength = None

        elif isinstance(img_buf, cuvis_il.cuvis_imbuffer_t):

            if dformat is None:
                raise TypeError("Missing format for reading image buffer")

            if img_buf.__getattribute__("format") == 1:
                self.array = cuvis_il.cuvis_read_imbuf_uint8(img_buf)
            elif img_buf.__getattribute__("format") == 2:
                self.array = cuvis_il.cuvis_read_imbuf_uint16(img_buf)
            elif img_buf.__getattribute__("format") == 3:
                self.array = cuvis_il.cuvis_read_imbuf_uint32(img_buf)
            elif img_buf.__getattribute__("format") == 4:
                self.array = cuvis_il.cuvis_read_imbuf_float32(img_buf)
            else:
                raise SDKException()

            self.width = img_buf.__getattribute__("width")
            self.height = img_buf.__getattribute__("height")
            self.channels = img_buf.__getattribute__("channels")

            if img_buf.__getattribute__("wavelength") is not None:
                self.wavelength = [
                    cuvis_il.p_unsigned_int_getitem(
                        img_buf.__getattribute__("wavelength"), z) for z
                    in
                    range(self.channels)]

            # print("got image of size {}.".format(self.array.shape))

        else:
            raise TypeError(
                "Wrong data type for image buffer: {}".format(type(img_buf)))
