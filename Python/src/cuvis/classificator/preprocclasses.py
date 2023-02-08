import importlib

import numpy as np
import xarray
from sklearn.decomposition import PCA as PCA_skl
from sklearn.preprocessing import MinMaxScaler
from cv2 import PCACompute2 as PCA_cv
# from tensorflow_transform import pca as PCA_tf

from pprint import pprint


# todo add some kind of "prototype extractor" e.g. via K-means
# https://docs.rapidminer.com/latest/studio/operators/modeling/segmentation/extract_prototypes.html
# with this we should have multiple prototypes per class to check e.g. knn against
# this should be faster, because it has less neighbours to compare to, but better than "distance"
# because we dont just take the median.

class BaseMethod(object):
    settings = None
    data = xarray.Dataset()
    masks = xarray.Dataset()
    __min_dict_requirements__ = []
    internal_state = None

    def __init__(self, settings=None):
        if settings is None:
            self.settings = {}
        else:
            self.settings = settings
        assert self.__has_min_requirements__(list(settings.keys())), \
            "Some of the keys '{}' are missing.".format(", ".join(self.__min_dict_requirements__))

    def __repr__(self):
        return "{} called with {}".format(self.__class__.__name__, str(self.settings))

    def set_data(self, data, num_data_cols=None):
        """
        makes data available to the preprocessor

        Splits data into actual data and mask data based on num_data_cols (number of actual data columns).

        Parameters
        __________
        data : pandas.DataFrame, required
            the dataframe containing pixelwise data and label information.
        num_data_cols : int, optional
            the number of columns at the beginning of the data frame to cut data with.
            If None, all provided data is assumed to be actual data.
        """
        if num_data_cols is not None:
            keys = list(data.keys())
            data_keys = keys[:num_data_cols]
            mask_keys = keys[num_data_cols:]
            self.data = data[data_keys]
            self.masks = data[mask_keys]
        else:
            self.data = data
            self.masks = xarray.Dataset()
        pass

    def fit(self):
        self.internal_state = "do nothing"
        pass

    def set_state(self, state):
        self.internal_state = state
        pass

    def apply(self):
        return xarray.merge([self.data, self.masks], compat='no_conflicts'), len(self.data.variables) - 1

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


class PCA(BaseMethod):
    __min_dict_requirements__ = ["number_of_componenents"]

    def __init__(self, settings=None):
        super().__init__(settings)

    def fit(self):
        num_comp = self.settings["number_of_componenents"]
        this_pca = PCA_skl(n_components=num_comp, svd_solver="full")
        this_pca.fit(self.data.to_array().to_numpy().T)
        print("Using {} components with an explained variance of ~{:.5f}.".format(
            num_comp, np.cumsum(this_pca.explained_variance_ratio_)[num_comp - 1]))
        self.internal_state = this_pca

    def apply(self):
        if self.internal_state is None:
            raise Exception("PCA not configured for application.")
        components = self.internal_state.transform(self.data.to_array().to_numpy().T)
        num_comp = self.settings["number_of_componenents"]
        self.data = self.data.to_array()[:num_comp, :].copy(data=components.T).to_dataset(dim="variable")
        renamed = {}
        [renamed.update({key: "loading_PC{}".format(num)}) for key, num in zip(self.data.keys(), range(num_comp))]
        self.data = self.data.rename(renamed)
        return xarray.merge([self.data, self.masks], compat='no_conflicts'), len(self.data.variables) - 1


class NORM(BaseMethod):
    __min_dict_requirements__ = ["direction"]

    def __init__(self, settings=None):
        super().__init__(settings)

    def apply(self):
        # print(self.data.loc[[2]]) #this prints the unnormed data
        if self.settings["direction"] == "Channel":
            data_arr = self.data.to_array().to_numpy()  # returns a numpy array
            min_max_scaler = MinMaxScaler()
            x_scaled = min_max_scaler.fit_transform(data_arr)
            self.data = self.data.to_array().copy(data=x_scaled).to_dataset(dim="variable")
        elif self.settings["direction"] == "Brightness":
            data_arr = self.data.to_array().to_numpy()  # returns a numpy array
            min_max_scaler = MinMaxScaler()
            x_scaled = min_max_scaler.fit_transform(data_arr.T)
            self.data = self.data.to_array().copy(data=x_scaled.T).to_dataset(dim="variable")
        else:
            raise NotImplementedError("Direction {} not defined!".format(self.settings["direction"]))
        # print(self.data.loc[[2]]) #this prints the normed data
        return xarray.merge([self.data, self.masks], compat='no_conflicts'), len(self.data.variables) - 1


def closest_hlp(mywl, wl_list):
    diff = [np.abs(mywl - wl_el) for wl_el in wl_list]
    myind = diff.index(np.min(diff))
    return wl_list[myind]


def closest_hlp_old(mywl, wl_list):
    diff = [np.abs(mywl - wl_el) for wl_el in wl_list]
    check = [False] * len(wl_list)
    myind = diff.index(np.min(diff))
    check[myind] = True
    return check


def exact_hlp(mywl, wl_list):
    if mywl in wl_list:
        return mywl
    else:
        return None


def exact_hlp_old(mywl, wl_list):
    check = [mywl == wl_el for wl_el in wl_list]
    return check


class SUBSET(BaseMethod):
    __min_dict_requirements__ = ["wavelengths", "choice"]

    def __init__(self, settings=None):
        super().__init__(settings)

    def fit(self):
        self.internal_state = self.settings
        pass

    def apply(self):
        data_wls = list(self.data.variables.keys())
        data_wls.remove("index")
        data_wls_int = [int(el.strip("nm")) for el in data_wls]

        settings_ch = self.internal_state["choice"]

        subset_cases = {"closest": closest_hlp,
                        "exact": exact_hlp}

        try:
            subset_fun = subset_cases[settings_ch]
        except:
            raise NotImplementedError("subset choice '{}' not defined.".format(settings_ch))

        list_of_used_wls = []
        for wl in self.internal_state["wavelengths"]:
            list_of_used_wls.append(subset_fun(wl, data_wls_int))

        variable_name_subset = []
        for ind, el in enumerate(data_wls):
            if data_wls_int[ind] in list_of_used_wls:
                variable_name_subset.append(el)

        if len(variable_name_subset) != len(self.internal_state["wavelengths"]):
            print("Not all wavelengths could be found. Used '{}' only.".format(", ".join(variable_name_subset)))
        else:
            print("Used wavelengths: {}.".format(", ".join(variable_name_subset)))

        self.data = self.data[variable_name_subset]

        return xarray.merge([self.data, self.masks], compat='no_conflicts'), len(self.data.variables) - 1


class INDICES(BaseMethod):
    __min_dict_requirements__ = ["indices", "choice"]

    def __init__(self, settings=None):
        super().__init__(settings)

    def fit(self):
        self.internal_state = self.settings
        pass

    def apply(self):

        indices = []

        for ind in self.internal_state["indices"]:
            index_def = getattr(importlib.import_module('.indices', package="cuvis.classificator"), ind)()
            print("Using index: {}".format(index_def))

            data_wls = list(self.data.variables.keys())
            data_wls.remove("index")
            data_wls_int = [int(el.strip("nm")) for el in data_wls]

            settings_ch = self.internal_state["choice"]

            subset_cases = {"closest": closest_hlp,
                            "exact": exact_hlp}

            try:
                subset_fun = subset_cases[settings_ch]
            except:
                raise NotImplementedError("subset choice '{}' not defined.".format(settings_ch))

            list_of_used_wls = []
            for wl in index_def.wavelengths:
                list_of_used_wls.append("{} nm".format(subset_fun(wl, data_wls_int)))

            if len(list_of_used_wls) != len(index_def.wavelengths) or "None nm" in list_of_used_wls:
                raise IOError("Not all wavelengths could be found.")
            else:
                print("Used wavelengths: {}.".format(", ".join(np.unique(list_of_used_wls))))

            subset = self.data[list_of_used_wls].astype(float)
            subset = subset.to_array().values
            index = np.apply_along_axis(index_def.get_function(), 0, subset)

            indices.append(index)
        indices = np.array(indices)
        self.data = self.data.to_array()[:len(indices), :].copy(data=indices).to_dataset(dim="variable")
        renamed = {}
        [renamed.update({key: self.settings["indices"][num]}) for key, num in zip(self.data.keys(), range(len(indices)))]
        self.data = self.data.rename(renamed)

        return xarray.merge([self.data, self.masks], compat='no_conflicts'), len(self.data.variables) - 1
