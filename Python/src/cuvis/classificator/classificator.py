import datetime
import inspect
import warnings
from copy import deepcopy
from pprint import pprint

import numpy as np
import pandas as pd

import cuvis
from .preprocessor import Preprocessor as PreProc
from .postprocessor import Postprocessor as PostProc
from .model import Model as Mod
from .auxiliary import data_from_csv, get_mesu_dict, goodness_of_fit
import os
import time
import os.path
import cv2 as cv
import dill
import json
import yaml


class CuvisClassificator(object):
    _wdir_ = os.getenv("HOME")
    _eval_file_ = None
    _apply_data_ = None
    preprocessor = None
    model = None
    postprocessor = None
    label_dict_numeric = None
    data = None
    original_data = None
    test_data = None
    results = None
    dimensions = {"num_data_cols": 0, "num_label_cols": 0}
    configs = {
        "preprocessor": None,
        "model": None,
        "postprocessor": None}

    def __init__(self, classi_dir=None, **kwargs):

        if classi_dir is not None:
            self._wdir_ = classi_dir
            self._eval_file_ = os.path.join(self._wdir_, "labels", "evaluation.csv")
            data, self.test_data, self.dimensions["num_data_cols"], self.dimensions["num_label_cols"] \
                , orig_image_dimensions, self.label_dict_numeric = data_from_csv(classi_dir)
            self.data = {"data": data,
                         "num_data_cols": self.dimensions["num_data_cols"],
                         "num_label_cols": self.dimensions["num_label_cols"],
                         "orig_image_dimensions": orig_image_dimensions,
                         "label_dict_numeric": self.label_dict_numeric
                         }
            self.original_data = deepcopy(self.data)

        self.configs["preprocessor"] = kwargs.pop("preprocessor_cfg", None)
        self.configs["postprocessor"] = kwargs.pop("postprocessor_cfg", None)
        self.configs["model"] = kwargs.pop("model_cfg", None)

        if not any([val is None for val in list(self.configs.values())]):
            self.build_pipeline()

        pass

    def set_preprocessor(self, preprocessor_dict):
        self.configs["preprocessor"] = preprocessor_dict
        self.preprocessor = None

    def run_preprocessor(self):
        self.preprocessor = PreProc(self.configs["preprocessor"])
        self.preprocessor.fit_and_apply(self.data)

        # subdir = os.path.join(self._wdir_, 'preprocessed')
        # if not os.path.isdir(subdir):
        #    os.mkdir(subdir)
        # self.preprocessor.save(os.path.join(subdir,os.path.splitext(os.path.basename(self.__data_definition__))[0]))
        self.data = self.preprocessor.get_data()
        self.dimensions["num_data_cols"] = self.data["num_data_cols"]
        self.dimensions["num_label_cols"] = self.data["num_label_cols"]

    def set_model(self, model_dict):
        self.configs["model"] = model_dict
        self.model = None

    def set_postprocessor(self, postprocessor_dict):
        self.configs["postprocessor"] = postprocessor_dict
        self.postprocessor = None

    def build_pipeline(self):

        if self.configs["preprocessor"] is None:
            raise NotImplementedError("run 'set_preprocessor' first!")
        if self.configs["model"] is None:
            raise NotImplementedError("run 'set_model' first!")
        if self.configs["postprocessor"] is None:
            raise NotImplementedError("run 'set_postprocessor' first!")

        if self.preprocessor is not None:
            print("Warning: Overwriting preprocessor!")
        if self.model is not None:
            print("Warning: Overwriting model!")
        if self.postprocessor is not None:
            print("Warning: Overwriting postprocessor!")

        self.run_preprocessor()
        t0 = time.time()
        if len(self.configs["model"]["methods"]) > 1:
            raise NotImplementedError("Currently only a single method is supported for models!")
        print("Start fitting model '" + str(list(self.configs["model"]["methods"][0].keys())[0]) + "' on train data...")
        self.make_model()
        self.postprocessor = PostProc(self.configs["postprocessor"])
        tfit = time.time()
        print(
            "Fitted model '" + str(list(self.configs["model"]["methods"][0].keys())[0]) + "' in {:.3} s.".format(
                tfit - t0))

    def make_model(self):
        self.model = Mod(self.configs["model"])
        self.model.set_data(self.data)
        self.model.fit()
        pass

    def predict(self, file_or_object, post_process=True):
        mesu_dict = get_mesu_dict(file_or_object)
        self.results = []
        for name in mesu_dict:
            t0 = time.time()
            print("Start classification on '" + name + "'...")
            self._apply_data_ = mesu_dict[name].Data["cube"]
            self.result = self.model.predict(self._apply_data_, self.preprocessor)
            self.result["image_id"] = name
            self.result["orig_shape"] = (self.data["orig_image_dimensions"][0], self.data["orig_image_dimensions"][1])
            self.result["meta"] = {}
            self.result["meta"]["preprocessor"] = self.configs["preprocessor"]
            self.result["meta"]["model"] = self.configs["model"]
            if post_process:
                t1 = time.time()
                self.result["meta"]["postprocessor"] = self.configs["postprocessor"]
                if len(self.configs["postprocessor"]["methods"]) > 1:
                    raise NotImplementedError("Currently only a single method is supported for postprocessors!")
                print("Start postprocessing with '"
                      + str(list(self.configs["postprocessor"]["methods"][0].keys())[0]) + "' ...")
                self.postprocessor.load_result(self.result)
                self.postprocessor.apply()
                self.result = self.postprocessor.get_final_result()
                tpost = time.time()
                print("Postprocessed with '" + str(list(self.configs["postprocessor"]["methods"][0].keys())[0])
                      + "' in {:.3} s.".format(tpost - t1))
            tclass = time.time()
            print("Classification in {:.3} s.".format(tclass - t0))
            self.results.append(self.result)

        # if visualize:
        #    self._visualize_(results, **kwargs)

        return self.results

    def _predict_test_(self):
        self.results = []
        for loc_dict in self.test_data:
            t0 = time.time()
            print("Start classification on '" + loc_dict["name"] + "'...")
            self._apply_data_ = loc_dict["cube"]
            self.result = self.model.predict(self._apply_data_, self.preprocessor)
            self.result["image_id"] = loc_dict["name"]
            self.result["orig_shape"] = (self.data["orig_image_dimensions"][0], self.data["orig_image_dimensions"][1])
            self.result["meta"] = {}
            self.result["meta"]["preprocessor"] = self.configs["preprocessor"]
            self.result["meta"]["model"] = self.configs["model"]

            t1 = time.time()
            self.result["meta"]["postprocessor"] = self.configs["postprocessor"]
            if len(self.configs["postprocessor"]["methods"]) > 1:
                raise NotImplementedError("Currently only a single method is supported for postprocessors!")
            print("Start postprocessing with '"
                  + str(list(self.configs["postprocessor"]["methods"][0].keys())[0]) + "' ...")
            self.postprocessor.load_result(self.result)
            self.postprocessor.apply()
            self.result = self.postprocessor.get_final_result()
            tpost = time.time()
            print("Postprocessed with '" + str(list(self.configs["postprocessor"]["methods"][0].keys())[0])
                  + "' in {:.3} s.".format(tpost - t1))
            tclass = time.time()
            print("Classification in {:.3} s.".format(tclass - t0))

            self.results.append(self.result)

        return self.results

    def visualize(self, scale=2, alpha=0.25, save_path=None):
        for res in self.results:
            self.postprocessor.load_result(res)
            self.postprocessor.load_measurement(self.postprocessor.image_id)
            self.postprocessor.apply()
            self.postprocessor.show(scale, alpha, save_path)
            cv.waitKey(0)

    def visualizeLive(self, results, mesu, window, scale=2, alpha=0.25, save_path=None):
        for res in results:
            self.postprocessor.load_result(res)
            self.postprocessor.load_measurement(mesu)
            self.postprocessor.apply()
            self.postprocessor.show(scale, alpha, window, save_path)

    def evaluate(self):
        if self.test_data is not None:
            test_results = self._predict_test_()
            adjusted_results = self.postprocessor.visualize_and_adjust(test_results)
            gof = goodness_of_fit(self.test_data, adjusted_results)
            with open(self._eval_file_, "a") as f:
                line = "Classificator evaluation: \n{}\n\n".format(datetime.datetime.now().astimezone())
                f.write(line)
                line = "based on labeling at {}\n\n".format(self._wdir_)
                f.write(line)
                gof.to_csv(f, mode='a', line_terminator='\n', float_format="%.5f")
                line = "\nWith configuration:\n\n"
                f.write(line)
                yaml.dump([el["meta"] for el in adjusted_results][0], f, sort_keys=False)
                f.write("\n{}\n\n".format("".join(["-"] * 25)))
        else:
            warnings.WarningMessage("No test data found, goodness of fit cannot be calculated. \n Classificator "
                                    "available 'as is'.")

        return

    def save(self, filename):
        with open(os.path.join(self._wdir_, filename), 'wb') as handle:
            self._wdir_ = None  # due to DSGVO
            self._apply_data_ = None  # due to DSGVO
            # clean up configuration dictionary
            self.configs = json.loads(json.dumps(self.configs))
            # print("can I pickle? {}".format(dill.pickles(deepcopy(self))))
            # print("------------------------------")
            # pd2xarray_walker(self)
            # print("------------------------------")
            # check_pickle(self)
            dill.dump(self, handle, protocol=dill.HIGHEST_PROTOCOL, recurse=True, byref=True)

    def load(self, filename):
        print("Loading Classificator state from '" + filename + "'")
        with open(filename, 'rb') as handle:
            loaded = dill.load(handle)
        for attrib in dir(self):
            if not attrib.startswith('_') and not callable(getattr(self, attrib)):
                self.__setattr__(attrib, getattr(loaded, attrib))

        if self.model is None:
            self.make_model()
        if len(self.preprocessor.preprocessor_states) == 0:
            self.preprocessor = PreProc(self.configs["preprocessor"])
            self.preprocessor.fit_and_apply(self.original_data)
        if self.postprocessor is None:
            raise NotImplementedError("No alternative, when postprocessor is lost!")
        print("Classificator loaded!")
        pass


def check_pickle(obj):
    if any([isinstance(obj, el) for _, el in inspect.getmembers(cuvis.classificator, inspect.isclass)]) or \
            isinstance(obj, cuvis.ImageData):
        for attrib in dir(obj):
            if not attrib.startswith('_') and not callable(getattr(obj, attrib)):
                print("Checking {}.{}.{}!".format(obj.__class__.__module__, obj.__class__.__name__, attrib))
                try:
                    check_pickle(getattr(obj, attrib))
                except:
                    if not dill.pickles(getattr(obj, attrib), exact=True, safe=True):
                        print("Cannot pickle: {}".format(attrib))
    elif isinstance(obj, list):
        for i in obj:
            check_pickle(i)
    elif isinstance(obj, dict):
        for i in obj.values():
            check_pickle(i)
    else:
        print("Checking {}.{}!".format(obj.__class__.__module__, obj.__class__.__name__))
        if not dill.pickles(obj, exact=True, safe=True):
            print("Cannot pickle: {}".format(obj))


def pd2xarray_walker(obj):
    if any([isinstance(obj, el) for _, el in inspect.getmembers(cuvis.classificator, inspect.isclass)]) or \
            isinstance(obj, cuvis.ImageData):
        for attrib in dir(obj):
            if not attrib.startswith('_') and not callable(getattr(obj, attrib)):
                try:
                    print(attrib)
                    pd2xarray_walker(getattr(obj, attrib))
                except:
                    print(type(obj))
                    if isinstance(obj, pd.DataFrame):
                        xobj = obj.to_xarray()
                        print(xobj)
    elif isinstance(obj, list):
        for i in obj:
            pd2xarray_walker(i)
    elif isinstance(obj, dict):
        for i in obj.values():
            pd2xarray_walker(i)
    else:
        print(type(obj))
        if isinstance(obj, pd.DataFrame):
            xobj = obj.to_xarray()
            print(xobj)
    pass


def xarray2pd_walker(obj):
    pass
