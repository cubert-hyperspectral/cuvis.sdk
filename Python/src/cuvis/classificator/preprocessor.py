import importlib
import os.path

import xarray

import cuvis

import pandas as pd
from .auxiliary import DataLabel, data_from_csv
from copy import deepcopy
import numpy as np
import time


class Preprocessor(object):
    """
    the preprocessor class of the classificator module

    The Preprocessor class is initialized with a stp by step definition of the used preprocessors.
    The Preprocessor class can apply the defined preprocessors to the available data

    Attributes
    ----------
    methods : dict
        the dictionary the preprocessor is initialized with
    method_names : list
        the names of the methods defined in the dict
    num_data_cols : int
        the number of columns that are designated for data
    num_label_cols : int
        the number of columns that are designated for masks
    data : pandas.DataFrame
        the data frame designated for training/inference


    Methods
    -------
    apply(interface_file)
        applies the defined preprocessors based on the interface file (from auxiliary.DataLabel)
    save(base_filename)
        saves a csv for the applied data (pandas.DataFrame)
    """
    methods = {}
    method_names = []
    num_data_cols = 0
    num_label_cols = 0
    orig_image_dimensions = [0, 0, 0]
    data = xarray.Dataset()
    preprocessor_states = []
    label_dict_numeric = {}

    # todo: Should we make labels unique? i.e. can a pixel have multiple labels?

    def __init__(self, specification_dict):
        """
        initialization

        Basic initialization with specification dictionary.

        Parameters
        __________
        specification_dict : dict, required
            dictionary containing the preprocessor options (see preprocclasses.py)
        """
        self.methods = deepcopy(specification_dict).pop("methods", None)

        if self.methods is None:
            raise IOError("No methods defined in specification keys:\n{}".format(specification_dict.keys()))
        else:
            self.method_names = [list(dct.keys())[0] for dct in self.methods]
        pass

    def fit_and_apply(self, data):
        """
        applies the defined preprocessors based on the interface file (from auxiliary.DataLabel)

        Basic initialization with file name.

        Parameters
        __________
        interface_file : str, required
            file specification for a DataLabel readable file that defines the interface from the labeling GUI

        Returns
        -------
        dictionary of data and test_data
        """

        self.data = data["data"]
        self.num_data_cols = data["num_data_cols"]
        self.num_label_cols = data["num_label_cols"]
        self.orig_image_dimensions = data["orig_image_dimensions"]
        self.label_dict_numeric = data["label_dict_numeric"]
        self._apply_preprocessors_()
        return

    def apply(self, data):
        """
        applies the defined preprocessors based on the interface file (from auxiliary.DataLabel)

        Basic initialization with file name.

        Parameters
        __________
        interface_file : str, required
            file specification for a DataLabel readable file that defines the interface from the labeling GUI

        Returns
        -------
        dictionary of data and test_data
        """

        wls = ["{} nm".format(dwl) for dwl in data.wavelength]
        data = np.reshape(data.array, (np.prod(data.array.shape[:-1]), data.array.shape[-1]))
        data = pd.DataFrame(data, columns=wls).to_xarray()
        self.data = data
        self._apply_preprocessors_(refit=False)
        return

    def _apply_preprocessors_(self, refit=True):
        """
        applies the defined preprocessors in order of the specification

        Wrapper function for the different preprocessors.
        Changes the data and testing_data in place.
        """

        for ind, meth in enumerate(self.method_names):
            t0 = time.time()
            pp_class = getattr(importlib.import_module('.preprocclasses', package="cuvis.classificator"), meth)
            loc_pp = pp_class(self.methods[ind][meth])
            loc_pp.set_data(self.data, num_data_cols=self.num_data_cols)
            if refit:
                print("Start fitting preprocessing step '" + pp_class.__name__ + "' on train data...")
                loc_pp.fit()
                self.preprocessor_states.append(loc_pp.internal_state)
            else:
                loc_pp.set_state(self.preprocessor_states[ind])
                loc_pp.set_data(self.data)
            print("Start preprocessing step '" + pp_class.__name__ + "' ...")
            self.data, num_data_cols = loc_pp.apply()
            #if len(self.test_data.columns):
            #    loc_pp.set_data(self.test_data, num_data_cols=self.num_data_cols)
            #    print("Start preprocessing step '" + pp_class.__name__ + "' on test data...")
            #    self.test_data, num_data_cols_test = loc_pp.apply()

            #    # check data length
            #    assert num_data_cols == num_data_cols_test, "Something went wrong, test_data and data are of different " \
            #                                                "column length. "
            pp_time = time.time()
            print("Preprocessed with '" + pp_class.__name__ + "' in {:.3} s.".format(pp_time - t0))
            self.num_data_cols = num_data_cols
            pass

    def save(self, base_filename):
        """
        saves a csv for the applied data (pandas.DataFrame)

        Basic initialization with file name.

        Parameters
        __________
        base_filename : str, required
            file specification for a file to be read by the classification algorithm (simple pandas.Dataframe by pixel)
        """
        self.data.to_csv(base_filename + "_data.csv")
        pass

    def get_data(self):
        return {"data": self.data,
                "num_data_cols": self.num_data_cols,
                "num_label_cols": self.num_label_cols,
                "orig_image_dimensions": self.orig_image_dimensions,
                "label_dict_numeric": self.label_dict_numeric
                }  # dimensions of the orig input image eg. (275x290)
