import numpy as np


class base_index(object):
    wavelengths = []
    num_wls = 0

    def __init__(self):
        pass

    def get_function(self):
        def do_nothing(*args):
            pass

        return do_nothing

    def __repr__(self):
        return "{} based on wavelengths: {} nm.".format(self.__class__.__name__, self.wavelengths)


class simple_difference(base_index):

    def __init__(self):
        super().__init__()
        self.wavelengths = [2000, 0]

    def get_function(self):
        self.num_wls = 2

        def diff(wls):
            return wls[0] - wls[1]

        return diff


class NDVI(base_index):

    def __init__(self):
        super().__init__()
        self.wavelengths = [800, 670]

    def get_function(self):
        self.num_wls = 2

        def ndvi(wls):
            return (wls[0] - wls[1]) / (wls[0] + wls[1])

        return ndvi


class hNDVI(base_index):

    def __init__(self):
        super().__init__()
        self.wavelengths = [827, 668]

    def get_function(self):
        self.num_wls = 2

        def hndvi(wls):
            return (wls[0] - wls[1]) / (wls[0] + wls[1])

        return hndvi


class simple_integral(base_index):

    def __init__(self):
        super().__init__()
        self.wavelengths = [500, 600]
        self.resolution = 8
        start = np.min(self.wavelengths)
        stop = np.max(self.wavelengths)
        self.wavelengths = [start]
        while self.wavelengths[-1] < stop:
            self.wavelengths.append(self.wavelengths[-1] + self.resolution)

    def get_function(self):
        self.num_wls = len(self.wavelengths)

        def integral(wls, res=self.resolution):
            subints = np.convolve(wls, np.ones(2) / 2, mode='valid') * res
            return np.sum(subints)

        return integral
