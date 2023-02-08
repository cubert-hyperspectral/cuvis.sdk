import importlib
import os.path
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from copy import deepcopy
import time

try:
    from . import auxiliary as aux
except:
    import auxiliary as aux


class Model(object):
    settings = None
    basic_data = None
    model = None
    method = None

    def __init__(self, settings):
        self.settings = settings
        pass

    def set_data(self, ppData):
        if isinstance(ppData, dict):
            self.basic_data = ppData  # todo check all internals ("data", "num_label_cols", etc)
        else:
            raise NotImplementedError("Cannot interpret the given model data {}!".format(type(ppData)))

    def fit(self):
        if len(self.settings["methods"]) > 1:
            raise NotImplementedError("Currently only a single method is supported for models!")
        meth = list(self.settings["methods"][0].keys())
        if len(meth) != 1:
            raise NotImplementedError("fit only works with one single fit method, currently.")
        self.method = meth[0]

        try:
            mm_class = getattr(importlib.import_module('.modelclasses', package="cuvis.classificator"), self.method)
        except:
            raise NotImplementedError("Cannot interpret the given method {}!".format(self.method))

        self.model = mm_class(self.settings["methods"][0][self.method])
        self.model.set_data(self.basic_data)

    def get_model(self):
        return self.model

    def predict(self, data, preproc=None):

        if preproc is not None:
            preproc.apply(data)
            preprocessed = preproc.get_data()
            t0 = time.time()
            labeled_img = self.model.predict(preprocessed)
        else:
            t0 = time.time()
            labeled_img = self.model.predict(data)
        predtime = time.time()
        print("Predicted with '" + self.method + "' in {:.3} s.".format(predtime - t0))
        return labeled_img
