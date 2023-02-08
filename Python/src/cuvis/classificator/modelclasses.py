import numpy as np
from .auxiliary import convert_labels_binary_to_numeric
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import xarray
# from pandarallel import pandarallel
# from collections import OrderedDict
from copy import deepcopy

from pprint import pprint


class BaseMethod(object):
    settings = None
    data = {}
    __min_dict_requirements__ = []
    model = None
    application_data = {}

    def __init__(self, settings=None):
        if settings is None:
            self.settings = {}
        else:
            self.settings = settings
        assert self.__has_min_requirements__(list(settings.keys())), \
            "Some of the keys '{}' are missing.".format(", ".join(self.__min_dict_requirements__))

    def __repr__(self):
        return "{} called with {}".format(self.__class__.__name__, str(self.settings))

    def __make_model__(self):
        self.model = None
        pass

    def predict(self, data):
        return {"data": data}

    def set_data(self, data):
        """
        makes data available to the model maker

        Parameters
        __________
        data : pandas.DataFrame, required
            the dataframe containing pixelwise data and label information.
        """

        self.data = data
        self.__make_model__()
        pass

    def __has_min_requirements__(self, testkeys):
        """
        tests a list of keys to conforming to minimum requirements

        All keys in testkeys will be tested against the self.__min_dict_requirements__ definition.

        Parameters
        __________
        testkeys : list, required
            the keys that are tested against minimum requirements

        Returns
        -------
        bool
            a boolean if minimum requirements are met
        """
        contain = all([key in testkeys for key in self.__min_dict_requirements__])
        return contain


class DIST(BaseMethod):
    __min_dict_requirements__ = ["from"]

    def __make_model__(self):
        data_obj = self.data["data"]
        var_names = list(self.data["data"].variables.keys())
        var_names.remove("index")
        labels_names = var_names[-self.data["num_label_cols"]:]
        labels = self.data["data"][labels_names]

        subsets = {}
        if self.settings["from"] == "mean":
            for i, key in enumerate(labels):
                subset = data_obj.sel(index=data_obj[key].values)
                sub_mean = subset.mean()
                subsets["{}".format(key)] = sub_mean.get(list(sub_mean.keys())[:self.data["num_data_cols"]])
        elif self.settings["from"] == "median":
            for i, key in enumerate(labels):
                subset = data_obj.sel(index=data_obj[key].values)
                sub_median = subset.median()
                subsets["{}".format(key)] = sub_median.get(list(sub_median.keys())[:self.data["num_data_cols"]])

        else:
            raise NotImplementedError("Cannot interpret the given method {}!".format(self.settings.keys()))

        label_functions = {}

        for key in labels:
            def loc_fun(v1, val=subsets[key]):
                return np.linalg.norm(v1.T - val.to_array().values, axis=1)

            label_functions[key] = loc_fun

        self.model = label_functions

    def predict(self, data):
        application_data = data["data"]
        #if data["num_label_cols"]:
        #   test_labels = data["data"].iloc[:, -data["num_label_cols"]:]

        res_labels = pd.DataFrame()
        # pandarallel.initialize()
        for key, val in self.model.items():
            intermediate = application_data.get(list(application_data.keys())[:data["num_data_cols"]])
            res_labels[key] = val(intermediate.to_array().values)


        def min_max_scaling(array_like):
            loc_data = np.asarray(array_like)
            return 1 - (loc_data - np.nanmin(loc_data)) / (np.nanmax(loc_data) - np.nanmin(loc_data))

        def binary(array_like):
            loc_data = np.asarray(array_like)
            return (loc_data == np.nanmax(loc_data)).astype(np.float)

        res_table = np.apply_along_axis(binary, 1, min_max_scaling(res_labels)) * min_max_scaling(res_labels)

        res_labels = pd.DataFrame(res_table, columns=res_labels.columns)

        labeled_img = {"labels": {}}

        for col in res_labels.columns:
            labeled_img["labels"][col] = dict()
            labeled_img["labels"][col]["probabilities"] = res_labels.loc[:, col].to_numpy()

        return labeled_img


class KNN(BaseMethod):
    __min_dict_requirements__ = ["k", "weights", "algorithm", "n_jobs"]

    def __make_model__(self):
        var_names = list(self.data["data"].variables.keys())
        var_names.remove("index")
        labels_names = var_names[-self.data["num_label_cols"]:]
        labels = self.data["data"][labels_names]
        # label_dict = self.data["label_dict_numeric"]
        labels_numeric, num_duplicate, num_no_label = convert_labels_binary_to_numeric(labels)
        if num_duplicate > 0:
            print(str(num_duplicate) + " pixels had more than one label assigned. Those are ignored.")

        data_names = var_names[:self.data["num_data_cols"]]
        datapoints = self.data["data"][data_names]

        datapoints = datapoints.sel(index=datapoints["index"][labels_numeric != 0])

        labels_numeric = labels_numeric[labels_numeric != 0]
        k = self.settings["k"]
        algo = self.settings["algorithm"]
        j = self.settings["n_jobs"]
        if self.settings["weights"] != "uniform" and self.settings["weights"] != "distance":
            try:
                knn = KNeighborsClassifier(n_neighbors=k,
                                           weights=eval(self.settings["weights"]),
                                           algorithm=algo,
                                           n_jobs=j)
            except:
                raise IOError("Cannot interpret the given attribute {}!".format(self.settings["weights"]))
        else:
            knn = KNeighborsClassifier(n_neighbors=k,
                                       weights=self.settings["weights"],
                                       algorithm=algo,
                                       n_jobs=j)

        # first is data, second is labels
        knn.fit(datapoints.to_array().values.T.tolist(), labels_numeric.tolist())

        self.model = knn

    def predict(self, data):
        var_names = list(data["data"].variables.keys())
        var_names.remove("index")
        data_names = var_names[:data["num_data_cols"]]
        datapoints = data["data"][data_names]
        knn = self.model
        probs = knn.predict_proba(datapoints.to_array().values.T.tolist())
        # print(probs)
        # print(probs.shape)
        # labels=knn.predict(datapoints.values.tolist())

        # labels_binary=aux.convert_labels_numeric_to_binary(labels,decData["label_dict_numeric"])
        labels_prob = deepcopy(data["label_dict_numeric"])
        for label, idx in labels_prob.items():
            labels_prob[label] = probs[:, idx - 1]

        labeled_img = {"labels": {}}

        for label, array in labels_prob.items():
            labeled_img["labels"][label] = dict()
            labeled_img["labels"][label]["probabilities"] = array

        return labeled_img


class RndForrest(BaseMethod):
    __min_dict_requirements__ = ["max_depth", "random_state", "n_jobs"]

    def __make_model__(self):
        var_names = list(self.data["data"].variables.keys())
        var_names.remove("index")
        labels_names = var_names[-self.data["num_label_cols"]:]
        labels = self.data["data"][labels_names]

        label_dict = self.data["label_dict_numeric"]
        labels_numeric, num_duplicate, num_no_label = convert_labels_binary_to_numeric(labels)
        if num_duplicate > 0:
            print(str(num_duplicate) + " pixels had more than one label assigned. Those are ignored.")

        data_names = var_names[:self.data["num_data_cols"]]
        datapoints = self.data["data"][data_names]
        datapoints = datapoints.sel(index=datapoints["index"][labels_numeric != 0])
        labels_numeric = labels_numeric[labels_numeric != 0]
        maximum_depth = self.settings["max_depth"]
        rnd_state = self.settings["random_state"]
        j = self.settings["n_jobs"]

        clf = RandomForestClassifier(max_depth=maximum_depth, random_state=rnd_state, n_jobs=j)
        # first is data, second is labels
        clf.fit(datapoints.to_array().values.T.tolist(), labels_numeric.tolist())

        self.model = clf

    def predict(self, data):
        var_names = list(data["data"].variables.keys())
        var_names.remove("index")
        data_names = var_names[:data["num_data_cols"]]
        datapoints = data["data"][data_names]
        clf = self.model
        probs = clf.predict_proba(datapoints.to_array().values.T.tolist())
        # print(probs)
        # print(probs.shape)
        # labels=knn.predict(datapoints.values.tolist())

        # labels_binary=aux.convert_labels_numeric_to_binary(labels,decData["label_dict_numeric"])
        labels_prob = deepcopy(data["label_dict_numeric"])
        for label, idx in labels_prob.items():
            labels_prob[label] = probs[:, idx - 1]

        labeled_img = {"labels": {}}

        for label, array in labels_prob.items():
            labeled_img["labels"][label] = dict()
            labeled_img["labels"][label]["probabilities"] = array

        return labeled_img
