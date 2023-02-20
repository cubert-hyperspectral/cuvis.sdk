import os
import pandas as pd
import warnings
import cuvis
import numpy as np
import cv2 as cv
import typing
from typing import Dict, Tuple, Any, Optional
from operator import truediv
import time
import xarray



class DataLabel(object):
    """
    a class handling data labels

    Handling a pandas dataframe for conforming with the interface requirements in the classificator module.
    Prepares attributes that are relevant for further use.
    Provides read and write functionality.

    Attributes
    ----------
    file : str
        the filename of the interface table to read/write
    table : pandas.Dataframe
        the contents of the interface table
    data_images : list
        a list of all the used images
    all_labels : list
        a list of all the used labels
    has_test : bool
        a check if the table has a test subset

    Methods
    -------
    read()
        reads the specified file
    write()
        writes the specified file
    add(list_dict)
        adds a dictionary entry to the table
    """
    # define minimum table requirements
    __min_table_requirements__ = ["File", "Test"]

    # basic attributes
    file = None
    table = pd.DataFrame()
    data_images = []
    all_labels = []
    has_test = False

    def __init__(self, file):
        """
        initialization

        Basic initialization with file name.

        Parameters
        __________
        file : str, required
            path to a specified file
        """
        self.file = file
        pass

    def read(self):
        """
        read specified file

        Fills the class attributes by reading the specified file.

        Raises
        ------
        WrongInputException
            If read table does not conform minimum requirements.
        FileNotFoundError
            If file is not found.
        """
        # check if file exists and read
        if os.path.isfile(self.file):
            self.table = pd.read_csv(self.file)
            # check if requirements are met
            if not self._has_min_requirements_(self.table.columns):
                print(self)
                raise WrongInputException(self.__min_table_requirements__)
        else:
            raise FileNotFoundError(self.file)
        # extracting attributes
        self._extract_info_()
        pass

    def write(self, overwrite=False):
        """
        writes specified file

        Writes a csv based on the class attributes.

        Parameters
        __________
        overwrite : bool, optional
            Should a file be overwritten if it already exists?

        Raises
        ------
        NoOverwriteException
            If file exists and overwrite is not set.
        """
        # check if file exists and can be overwritten
        if os.path.isfile(self.file):
            if overwrite:
                self.table.to_csv(self.file, index=False)
            else:
                raise NoOverwriteException(
                    "{} cannot be overwritten as overwrite option is not True!".format(self.file))
        else:
            self.table.to_csv(self.file, index=False)
        pass

    def add(self, line_dict):
        """
        adds a dictionary to the table

        Writes a pandas dataframe based on the class attributes.

        Parameters
        __________
        line_dict : dictionary, required
            This dictionary is added to the table of files and labels

        Raises
        ------
        WrongInputException
            If dict does not conform minimum requirements.
        """
        # check for requirements
        if not self._has_min_requirements_(line_dict.keys()):
            print(line_dict)
            raise WrongInputException(self.__min_table_requirements__)
        # make dataframe from dictionary
        loc_table = pd.DataFrame.from_dict([line_dict])
        # append dictionary dataframe to table
        self.table = pd.concat([self.table, loc_table], ignore_index=True)
        # remove duplicates
        self.table.drop_duplicates(inplace=True)
        # extracting attributes
        self._extract_info_()
        pass

    def _has_min_requirements_(self, testkeys):
        """
        tests a list of keys to conforming to minimum requirements

        All keys in testkeys will be tested against the self.__min_table_requirements__ definition.

        Parameters
        __________
        testkeys : list, required
            the keys that are tested against minimum requirements

        Returns
        -------
        bool
            a boolean if minimum requirements are met
        """
        contain = all([key in testkeys for key in self.__min_table_requirements__])
        return contain

    def _extract_info_(self):
        """
        extracts all attributes

        Extracts class attributes from the read table.

        Raises
        ------
        IOError
            If Test column is not boolean.
        """
        # check if Test column is boolean
        test_column = self.table.loc[:, "Test"]
        if test_column.dtype.name != 'bool':
            raise IOError("Expected Test column to be boolean!")
        else:
            self.has_test = any(test_column)
        # get all labels
        self.all_labels = [key for key in self.table.columns if key not in self.__min_table_requirements__]
        # get all image files
        self.data_images = list(self.table.loc[:, "File"])
        pass

    def __repr__(self):
        """
        overwrites standard __repr__ with the representation of the table
        """
        return str(self.table)


class NoOverwriteException(FileExistsError):
    pass


class WrongInputException(IOError):
    def __init__(self, req):
        super(WrongInputException, self).__init__(
            "Input needs to meet the availability of the required columns: {}!".format(", ".join(req)))

    pass


def cu3s_from_dir(load_path):
    files = []
    for file in os.listdir(load_path):
        filename = os.fsdecode(file)
        if filename.endswith(".cu3"):  # or filename.endswith(".cu3s"):
            # print("Found " + os.path.join(load_path, filename))
            files.append(os.path.join(load_path, filename))
            continue
        else:
            continue
    if len(files) == 0:
        raise IOError("No .cu3s found in : {}".format(load_path))
    return files


def data_from_csv(classi_dir):
    """
    prepares data based on a LUT of labels

    prepares a pandas.DataFrame from a labels LUT with pixel based cube data, followed by the mask data for the labels

    Parameters
     __________
        classi_dir : str, required
            classification directory that defines where the  cuvis_labels.csv from the labeling GUI is

    Returns
    -------
    data
        the training data pandas.DataFrame
    test_data
        the testing data pandas.DataFrame
    dlen
        the data length (number of columns in the pandas.DataFrame, start)
    llen
        the label length (number of columns in the pandas.DataFrame, end)
    """

    interface_file = os.path.join(classi_dir, r"labels", r"cuvis_labels.csv")
    print("Start configuring from " + interface_file + " ...")
    labels = DataLabel(interface_file)
    labels.read()

    # initialize returns
    data = pd.DataFrame()
    test_data = pd.DataFrame()
    dlen = 0
    llen = 0
    orig_image_dimensions = [0, 0, 0]

    ##### help functions

    # reshaping an array to pixelorder
    def img_reshape(array):
        reshaped = np.moveaxis(array, -1, 0).reshape(array.shape[-1], -1)
        return reshaped

    # get mask values
    def get_masks(row, labels, classi_dir):
        mask_dict = {}
        for lbl in labels:
            mask_data = cv.imread(os.path.join(os.path.join(classi_dir, "labels"), row[lbl]), 0)
            mask_data = mask_data.reshape(np.prod(mask_data.shape))
            mask_data = mask_data > 128
            mask_dict.update({lbl: mask_data})
        return mask_dict

    #####

    # check for test data
    if not labels.has_test:
        print("Test data not found! No independent analysis of goodness of fit will be available.")

    # else:
    # print("Test data found!")

    # set cuvis settings
    gen = cuvis.General(r"C:\Program Files\cuvis\user\settings")
    print(gen.getVersion())

    res_test_data = []
    res_data = xarray.Dataset()

    # read cubes
    for file in np.unique(labels.data_images):
        mesu_path = os.path.join(classi_dir, file)
        if os.path.isfile(mesu_path):
            # read spectra
            mesu_cube = cuvis.Measurement(mesu_path).Data["cube"]
            orig_image_dimensions = mesu_cube.array.shape
            spectra = img_reshape(mesu_cube.array)
            dlen = len(mesu_cube.wavelength)
            # read masks
            file_rows = labels.table[labels.table["File"] == file]
            for rid, f_row in file_rows.iterrows():
                if f_row["Test"]:
                    # add spectra and masks
                    mask_dict = get_masks(f_row, labels.all_labels, classi_dir)
                    llen = len(mask_dict.keys())
                    masks = pd.DataFrame(mask_dict).to_xarray()
                    res_test_data.append({"cube": mesu_cube, "labels": masks, "name": mesu_path})
                else:
                    # add spectra and masks
                    mask_dict = get_masks(f_row, labels.all_labels, classi_dir)
                    llen = len(mask_dict.keys())
                    data = pd.DataFrame(spectra.T, columns=["{} nm".format(wl) for wl in mesu_cube.wavelength])
                    masks = pd.DataFrame(mask_dict)
                    data = pd.concat([data, masks], axis=1).to_xarray()
                    try:
                        try:
                            data["index"] = data["index"] + np.max(res_data["index"].values)+1
                        except:
                            0
                        res_data = xarray.concat([res_data, data], dim="index")
                    except ValueError:
                        res_data = data
        else:
            raise IOError("File not found: {}".format(file))

    if len(test_data.columns):
        assert (dlen + llen) == len(res_test_data.columns), "The test dimensions do not fit, something went wrong! "
    if len(data.keys()):
        assert (dlen + llen) == len(res_data.keys()), "The data dimensions do not fit, something went wrong! "

    label_dict = get_label_dict(list(res_data.keys())[-llen:])
    return res_data, res_test_data, dlen, llen, orig_image_dimensions, label_dict


def get_test_cu3s(classi_dir):
    interface_file = os.path.join(classi_dir, r"labels", r"cuvis_labels.csv")
    labels = DataLabel(interface_file)
    labels.read()
    files = []
    for file in np.unique(labels.data_images):
        mesu_path = os.path.join(classi_dir, file)
        if os.path.isfile(mesu_path):
            file_rows = labels.table[labels.table["File"] == file]
            for rid, f_row in file_rows.iterrows():
                if f_row["Test"]:
                    files.append(os.path.join(classi_dir, file))
    return files


def convert_to_binary(input_image):
    """
    converts 3 channel BGR input_image to single channel gray image, where every pixel greater than 0 is converted
    to the value of 255 (binarizing)

    Parameters
    ----------
    input_image: Mat, required

    Returns
    -------
    Mat

    """
    binary = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(binary, 1, 255, cv.THRESH_BINARY)
    return binary


def check_in_boundary(point, upper_left, lower_right):
    """

    checks if point is in bounds of the rectangle defined by the two points upper_left and lower_right

    Parameters
    ----------
    point: tuple(int, int), required
    upper_left: tuple(int, int), required
    lower_right: tuple(int, int), required

    Returns
    -------
    bool

    """
    inside = upper_left[0] < point[0] < lower_right[0] and upper_left[1] < point[1] < lower_right[1]
    return inside


def find_rgb_idx(mesu):
    """

    finds the indexes of the channels closest to the colors red, green and blue

    Parameters
    ----------
    mesu : cuvis_measurement, required

    Returns
    -------
    uint8

    """
    mesu_wl = mesu.Data["cube"].wavelength
    mesu_wl = np.asarray(mesu_wl)

    r = (np.abs(mesu_wl - 660)).argmin()  # red=630-700
    g = (np.abs(mesu_wl - 520)).argmin()  # green=490-560
    b = (np.abs(mesu_wl - 480)).argmin()  # blue= 470-490
    return r, g, b


def get_rgb_from_cu3(mesu):
    """

    generates a rgb image from a given cube (cu3)

    Generates a rgb image from a given cube (cu3) by selecting 3 channels closest to the desired colors (red,
    green, blue), stacking the channels and converting and scaling them to uint8.

    Parameters
    ----------
    mesu : cuvis_measurement, required

    Returns
    -------
        np.array(x,y,3)
    """
    r, g, b = find_rgb_idx(mesu)
    cube = mesu.Data["cube"].array
    rgb = np.stack((cube[:, :, b], cube[:, :, g], cube[:, :, r]), axis=2)  # rgb to bgr
    rgb = cv.convertScaleAbs(rgb, alpha=(255.0 / 4096.0))  # convert between 12 bit and 8 bit

    return rgb

def find_cir_idx(mesu) -> typing.Tuple:
    """

    finds the indexes of the channels closest to the colors red, green and blue

    Parameters
    ----------
    mesu : cuvis_measurement, required

    Returns
    -------
    Tuple of index values

    """
    mesu_wl = mesu.Data["cube"].wavelength
    mesu_wl = np.asarray(mesu_wl)

    c = (np.abs(mesu_wl - 842)).argmin()
    i = (np.abs(mesu_wl - 682)).argmin()
    r = (np.abs(mesu_wl - 562)).argmin()
    return c,i,r

def get_cir_from_cu3(mesu):
    """

    generates a CIR image from a given cube (cu3)

    Generates a rgb image from a given cube (cu3) by selecting 3 channels closest to the desired colors (red,
    green, blue), stacking the channels and converting and scaling them to uint8.

    Parameters
    ----------
    mesu : cuvis_measurement, required

    Returns
    -------
        np.array(x,y,3)
    """
    c, i, r = find_cir_idx(mesu)
    cube = mesu.Data["cube"].array
    cir = np.stack((cube[:, :, i], cube[:, :, c], cube[:, :, r]), axis=2)  # rgb to bgr
    cir = cv.convertScaleAbs(cir, alpha=(255.0 / 4096.0))  # convert between 12 bit and 8 bit

    return cir

def get_img_from_bands(mesu, band1, band2, band3):
    """

    generates a band image from a given cube (cu3)

    Generates a rgb image from a given cube (cu3) by selecting 3 channels closest to the desired colors, stacking the channels and converting and scaling them to uint8.

    Parameters
    ----------
    mesu : cuvis_measurement, required

    Returns
    -------
        np.array(x,y,3)
    """
    cube = mesu.Data["cube"].array
    b1 = mesu.Data["cube"].wavelength.index(band1)
    b2 = mesu.Data["cube"].wavelength.index(band2)
    b3 = mesu.Data["cube"].wavelength.index(band3)
    img = np.stack((cube[:, :, b1], cube[:, :, b2], cube[:, :, b3]), axis=2)
    img = cv.convertScaleAbs(img, alpha=(255.0 / 4096.0))  # convert between 12 bit and 8 bit

    return img

def convert_labels_binary_to_numeric(labels_binary):
    label_no = []
    labels_names = list(labels_binary.variables.keys())
    labels_names.remove("index")
    for idx, label in enumerate(labels_names):
        label_no.append(idx + 1)

    label_no = np.array(label_no)
    summed_labels = np.apply_along_axis(sum, 0, labels_binary.to_array().values)
    num_duplicate = np.sum(summed_labels > 1)
    num_no_label = np.sum(summed_labels == 0)

    labels_numeric = np.apply_along_axis(lambda x: (label_no * x).sum(), 0, labels_binary.to_array().values)  # multiply false,true...
    # with numbers from 1 to 8
    labels_numeric[summed_labels != 1] = 0  # set to 0 if no label or multiple
    return labels_numeric, num_duplicate, num_no_label


def convert_labels_numeric_to_binary(labels_numeric, label_dict):
    labels_binary = pd.DataFrame()
    for label, item in label_dict.items():
        loc_dict = {label: labels_numeric == item}  # array with True/False if condition is true
        loc_dict = pd.DataFrame.from_dict(loc_dict)
        labels_binary = pd.concat([labels_binary, loc_dict], axis=1)
    return labels_binary


def get_label_dict(labels_binary):
    label_dict = dict()
    for idx, label in enumerate(labels_binary):
        label_dict.update({label: idx + 1})
    return label_dict


def get_new_color(id):
    """

    gives b, g, e values for different colors according to the index given from 0-5

    Parameters
    ----------
    id : int, required

    Returns
    -------
        tuple(int)

    """

    if id < 0 or id > 9:
        return (-1, -1, -1)
    if id == 0:  # red
        return (0, 0, 255)
    if id == 1:  # green
        return (0, 255, 0)
    if id == 2:  # blue
        return (255, 0, 0)
    if id == 3:  # magenta
        return (255, 0, 255)
    if id == 4:  # lightblue
        return (255, 255, 0)
    if id == 5:  # yellow
        return (0, 255, 255)
    if id == 6:  # brown
        return (23, 91, 191)
    if id == 7:  # orange
        return (0, 127, 255)


#  def __split_test_train__(self, lut):
#      if lut.has_test:
#          print("Test data found!")
#          self.train_data = lut.table[np.logical_not(lut.table["Test"])]
#          self.test_data = lut.table[lut.table["Test"]]
#      else:
#          self.train_data = lut.table
#      pass##

#  def __gather_data__(self):
#      self.train_data = datafromlut(self.train_data)
#      self.test_data = datafromlut(self.test_data)

def goodness_of_fit(test_data, res_labels):

    gofs = []

    for ind, td in enumerate(test_data):
        classes = list(td["labels"].keys())

        gof = pd.DataFrame(columns=pd.MultiIndex.from_product([["original"], classes]),
                           index=pd.MultiIndex.from_product([["classification"], list(classes) + ["unlabeled"]]))

        for iind in range(len(classes)):
            for jind in range(len(classes)+1):
                key1 = classes[iind]
                key2 = (list(classes) + ["unlabeled"])[jind]
                # print("calculating gof for {} - {}".format(key1, key2))
                orig = td["labels"][key1].to_numpy()
                if key2 == "unlabeled":
                    gen_mask = 0
                    for val in res_labels[ind]["labels"].values():
                        loc_mask = val["mask"]
                        gen_mask = loc_mask + gen_mask
                    trained = np.array(gen_mask).astype(np.bool)
                    trained = trained.reshape(np.prod(trained.shape))
                    gof.loc[("classification", key2), ("original", key1)] = np.sum(np.logical_not(trained)[orig])
                else:
                    trained = np.array(res_labels[ind]["labels"][key2]["mask"]).astype(np.bool)
                    trained = trained.reshape(np.prod(trained.shape))
                    gof.loc[("classification", key2), ("original", key1)] = np.sum(trained[orig])

        gofs.append(gof)

    gof = sum(gofs)

    def prec_rec_f1(loc_gof):
        tp = np.diag(gof.to_numpy())
        rec = list(map(truediv, tp, np.sum(loc_gof, axis=0)))
        prec = list(map(truediv, tp, np.sum(loc_gof, axis=1)))
        np.seterr(invalid='ignore')
        f1 = list(np.divide(2 * (np.array(prec) * np.array(rec)), (np.array(prec) + np.array(rec))))
        return {"precision": prec, "recall": rec, "f1-score": f1}

    for key, val in prec_rec_f1(gof).items():
        gof[key] = val + [np.nan]

    with pd.option_context('display.max_rows', None, 'display.max_columns', None, "display.precision", 3):
        print(gof)
        pass

    return gof


def get_mesu_dict(file_or_object):
    if not isinstance(file_or_object, list):
        mesu_list = [file_or_object]
    else:
        mesu_list = file_or_object
    mesu_dict = {}
    for el in mesu_list:
        t0 = time.time()
        name = ""
        mesu = None
        if isinstance(el, cuvis.Measurement):
            name = el.Name
            print("Loading Measurement: " + el.Name)
            mesu = el
        elif isinstance(el, str):
            if os.path.isfile(el):
                print("Loading Measurement: " + el)
                name = el
                mesu = cuvis.Measurement(el)
        else:
            raise NotImplementedError("Can not predict on data with type : {}".format(type(el)))
        mesu_dict[name] = mesu
        tloading = time.time()
        print("Loading in {:.3} s.".format(tloading - t0))
    return mesu_dict


if __name__ == "__main__":
    dl = DataLabel(r"C:\Users\benjamin.mueller\Documents\dev_test_files\DataLabel.csv")
    dl.read()
    my_line = {
        "File": "anotherfile.cu3",
        "Test": False,
        "label1": "label1_1.png",
        "label3": "label3_1.png",
    }
    dl.add(my_line)
    print(dl)
    print(dl.data_images)
    print(dl.all_labels)
    print(dl.has_test)
    # dl.write(overwrite=True)
