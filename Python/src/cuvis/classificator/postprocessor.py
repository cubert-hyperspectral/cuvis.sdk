import cuvis

try:
    from . import auxiliary as aux
except:
    import auxiliary as aux

import numpy as np
import cv2 as cv
import os
import pprint
import time
from copy import deepcopy


class Postprocessor(object):
    img_raw = None
    img_show = None
    img_bordered = None
    image_id = "No ID!"
    methods = None
    labels = dict()
    meta = dict()
    definity_default = 0.1
    definity = definity_default
    threshold_default = 0.8
    threshold = threshold_default

    dilate_size_default = 0
    dilate_size = dilate_size_default
    dilate_size_max = 21
    dilate_it_default = 1
    dilate_it = dilate_it_default
    dilate_it_max = 5

    erode_size_default1 = 0
    erode_size1 = erode_size_default1
    erode_size_max1 = 21
    erode_it_default1 = 1
    erode_it1 = erode_it_default1
    erode_it_max1 = 5

    erode_size_default2 = 0
    erode_size2 = erode_size_default2
    erode_size_max2 = 21
    erode_it_default2 = 1
    erode_it2 = erode_it_default2
    erode_it_max2 = 5

    scale = 2.0
    alpha = 0.3
    minimal_height = 550
    orig_shape = (0, 0)
    border_left = border_top = border_bottom = 20
    border_right = 500
    show_color = True

    def __init__(self, specification_dict):

        self.methods = deepcopy(specification_dict).pop("methods", None)
        if self.methods is None:
            raise IOError("No methods defined in specification keys:\n{}".format(specification_dict.keys()))
        if len(self.methods) > 1:
            raise NotImplementedError("Currently only only a single method is supported for postprocessors!")
        if "Base" not in self.methods[0].keys():
            raise NotImplementedError("Currently only 'Base' method is supported!")

        for key in specification_dict["methods"][0]["Base"].keys():
            if key == "alpha":
                self.alpha = specification_dict["methods"][0]["Base"][key]
            elif key == "threshold":
                self.threshold = specification_dict["methods"][0]["Base"][key]
            elif key == "definity":
                self.definity = specification_dict["methods"][0]["Base"][key]
            elif key == "erode1":
                self.erode_size1 = specification_dict["methods"][0]["Base"][key]
            elif key == "dilate":
                self.dilate_size = specification_dict["methods"][0]["Base"][key]
            elif key == "erode2":
                self.erode_size2 = specification_dict["methods"][0]["Base"][key]
            else:
                print("Postprocessor could not set '" + str(key) + "'. Ignored.")

    def create_window(self):
        cv.namedWindow('Classification Results')
        cv.createTrackbar("Alpha ", 'Classification Results', int(self.alpha * 100), 100, self.handle_alpha_trackbar)
        cv.createTrackbar("Thresh ", 'Classification Results', int(self.threshold * 100), 100,
                          self.handle_thresh_trackbar)
        cv.createTrackbar("Definity ", 'Classification Results', int(self.definity * 100), 100,
                          self.handle_definity_trackbar)
        cv.createTrackbar("Erode 1", 'Classification Results', self.erode_size1, self.erode_size_max1,
                          self.handle_erode_size1_trackbar)
        cv.createTrackbar("Dilate ", 'Classification Results', self.dilate_size, self.dilate_size_max,
                          self.handle_dilate_size_trackbar)
        cv.createTrackbar("Erode 2", 'Classification Results', self.erode_size2, self.erode_size_max2,
                          self.handle_erode_size2_trackbar)

    def create_window_stripped(self):
        if cv.getWindowProperty('Classification Results', cv.WND_PROP_VISIBLE) > 0:
            cv.destroyAllWindows()
        cv.namedWindow('Classification Results')

    def draw_text(self):
        """

        draws needed information as text onto the img_show_bordered

        Returns
        -------

        """
        start_x = self.img_bordered.shape[1] - self.border_right + 20
        start_y = self.border_top + 20

        self.img_bordered = cv.putText(self.img_bordered, "Measurement: ",
                                       (start_x, start_y),
                                       cv.FONT_HERSHEY_SIMPLEX,
                                       0.6, (255, 255, 255), 1,
                                       cv.LINE_AA)

        print_name = self.image_id
        print_length = 30
        if len(print_name) > print_length:
            print_name = print_name[-print_length:]
            print_name = ".." + print_name[-print_length - 2:]
        self.img_bordered = cv.putText(self.img_bordered, print_name,
                                       (start_x, start_y + 30),
                                       cv.FONT_HERSHEY_SIMPLEX,
                                       0.8, (255, 255, 255), 2,
                                       cv.LINE_AA)

        start_y = start_y + 80

        for idx, key in enumerate(self.labels.keys()):
            start_labels_y = start_y + idx * 40
            start_labels_x = start_x
            if idx > 3:
                start_labels_y = start_y + (idx - 4) * 40
                start_labels_x = start_x + 240
            self.img_bordered = cv.putText(self.img_bordered, key,
                                           (start_labels_x, start_labels_y),
                                           cv.FONT_HERSHEY_SIMPLEX,
                                           0.8, aux.get_new_color(idx), 2,
                                           cv.LINE_AA)

        start_y = self.img_bordered.shape[0] - 200

        instructions = []
        instructions.append("Adjust sliders for best outcome:")
        instructions.append(" ")
        instructions.append("Alpha: Alpha value of the overlay")
        instructions.append("Thresh: Threshold of minimum probability value")
        instructions.append("Definity: Threshold of minimum distance to another label")
        instructions.append("Erosion, then Dilation -> Opening. Reduces noise")
        instructions.append("Dilation, then Erosion -> Closing. Fills holes")
        instructions.append("Press '+' and '-' keys to zoom")
        instructions.append("Press 'c' to switch between b/w and color")
        instructions.append("Press 'm' to print meta data into console")
        instructions.append("Press '<-' and '->' to go through images")
        instructions.append("Press 'f' to save current state.")
        instructions.append("Press 'Esc' or click top right 'X' exit.")
        # todo: add number of visualizable files

        line_spacing = 15

        for i, instruction in enumerate(instructions):
            self.img_bordered = cv.putText(self.img_bordered, instruction,
                                           (start_x, start_y + line_spacing * i),
                                           cv.FONT_HERSHEY_SIMPLEX,
                                           0.4, (255, 255, 255), 1,
                                           cv.LINE_AA)

    def show(self, scale=2, alpha=0.25,window=None, save_path=None):

        if window is None:
            cv.destroyAllWindows()
            window=self.image_id[-80:]
        elif cv.getWindowProperty(window, cv.WND_PROP_VISIBLE) < 1:
            cv.namedWindow(window)
        self.scale = scale
        self.alpha = alpha
        # self.create_window_stripped()
        self.make_img_show()
        self.scale_img_show()
        cv.imshow(window, self.img_show)
        cv.waitKey(1)
        if save_path is not None:
            cv.imwrite(os.path.join(save_path, self.image_id[-20:]) + "_classify.png", self.img_show)
        pass

    def visualize_and_adjust(self, results):

        idx = 0
        size = len(results)
        print(results)
        print(len(results))
        self.load_result(results[idx])
        self.load_measurement(self.image_id)
        if self.img_raw is None:
            raise IOError("Load measurement first!")
        self.create_window()
        while 1:
            self.apply()
            self.make_img_show()
            self.scale_and_border()
            self.draw_text()
            cv.imshow('Classification Results', self.img_bordered)
            ret = self.handle_hotkeys(30)
            if ret == 3:  # finalize
                cv.destroyAllWindows()
                adjusted_results = []
                for res in results:
                    self.load_result(res)
                    self.apply()
                    adjusted = self.get_final_result()
                    adjusted_results.append(adjusted)
                return adjusted_results
            if ret == -1:  # abort
                cv.destroyAllWindows()
                print("Abort. Nothing is going to be saved/returned.")
                return None
            if ret == 1:  # right arrow
                idx = idx + 1
                if idx == size:
                    idx = size - 1
                self.load_result(results[idx])
                self.load_measurement(self.image_id)
                self.create_window()
            if ret == 2:  # left arrow
                idx = idx - 1
                if idx == -1:
                    idx = 0
                self.load_result(results[idx])
                self.load_measurement(self.image_id)
                self.create_window()

    def make_img_show(self):

        self.img_show = self.img_raw.copy()
        if not self.show_color:
            self.img_show = cv.cvtColor(self.img_show, cv.COLOR_BGR2GRAY)
            self.img_show = cv.cvtColor(self.img_show, cv.COLOR_GRAY2BGR)
        merged_color_labels = np.zeros((self.img_show.shape[0], self.img_show.shape[1], 3), np.uint8)
        equal_fraction = 1.0 / len(self.labels.keys())
        for idx, key in enumerate(self.labels.keys()):
            color_label = cv.cvtColor(self.labels[key]["mask"], cv.COLOR_GRAY2BGR)
            color_label[np.where((color_label > [0, 0, 0]).all(axis=2))] = [aux.get_new_color(idx)]
            # color_label=color_label.astype(np.float32)
            # merged_color_labels= merged_color_labels + color_label #* equal_fraction*
            merged_color_labels = cv.addWeighted(merged_color_labels, 1, color_label, 1, 0)
        merged_color_labels = merged_color_labels.astype(np.uint8)
        # merged_color_labels = cv.normalize(merged_color_labels, merged_color_labels, 0, 255, cv.NORM_MINMAX)
        self.img_show = cv.addWeighted(self.img_show, (1 - self.alpha), merged_color_labels, self.alpha, 0)

    def apply(self):

        # 255 is unspecified
        # 0 is label 0, 1 is label 1 and so on
        highest_probability_labels_arr = 255 * np.ones(self.orig_shape, np.uint8)
        # array where every value is the threshold
        highest_probability_arr = self.threshold * np.ones(self.orig_shape, np.float32)
        for idx, key in enumerate(self.labels.keys()):
            morphed_probs = self.labels[key]["probabilities"]
            morphed_probs = self.apply_erosion(key, morphed_probs, 1)
            morphed_probs = self.apply_dilation(key, morphed_probs)
            morphed_probs = self.apply_erosion(key, morphed_probs, 2)

            diff = morphed_probs - highest_probability_arr
            # everything is true that is bigger
            mask_better = diff > 0
            # everything is true that is different enough
            mask_definity = np.absolute(diff) > self.definity

            # remove the previous values that very the highest and replace them
            highest_probability_arr = highest_probability_arr - (highest_probability_arr * mask_better) + (
                    morphed_probs * mask_better)

            # remove the current labels with the highes probs and replace them
            highest_probability_labels_arr = highest_probability_labels_arr - (
                    highest_probability_labels_arr * mask_better * mask_definity) + (
                                                     idx * mask_better * mask_definity)

            # remove labels where previous label was not much different to better label
            highest_probability_labels_arr = highest_probability_labels_arr - (
                    highest_probability_labels_arr * np.invert(mask_definity)) + (255 * np.invert(mask_definity))

        for idx, key in enumerate(self.labels.keys()):
            is_key_mask = highest_probability_labels_arr == idx
            binary = np.ones(self.orig_shape, np.uint8)
            binary = binary * is_key_mask
            # cv.imshow(str(label),binary)
            self.labels[key]["mask"] = binary
            # self.apply_dilation(key)
            # self.apply_erosion(key)

        pass

    def get_final_result(self):

        final_result = {
            "image_id": self.image_id,
            "labels": self.labels,
            "orig_shape": self.orig_shape,
            "meta": self.meta
        }
        final_result["meta"]["postprocessor"] = {"methods": {"Base": {"alpha": self.alpha,
                                                                      "threshold": self.threshold,
                                                                      "definity": self.definity,
                                                                      "erode1": self.erode_size1,
                                                                      "dilate": self.dilate_size,
                                                                      "erode2": self.erode_size2,
                                                                      }}}

        return final_result

    def handle_thresh_trackbar(self, val):
        self.threshold = val * 0.01
        pass

    def handle_definity_trackbar(self, val):
        self.definity = val * 0.01

        pass

    def handle_alpha_trackbar(self, val):
        self.alpha = val * 0.01
        pass

    def handle_erode_size1_trackbar(self, val):
        self.erode_size1 = val
        pass

    def handle_erode_size2_trackbar(self, val):
        self.erode_size2 = val

        pass

    def handle_dilate_size_trackbar(self, val):
        self.dilate_size = val

        pass

    def adjust_scale(self, to_add):
        """
        in-/decrease the scale of the image shown

        In-/Decrease the scale of the shown image by the amount of to_add.
        Lower Limit: 1.0
        Upper Limit: 3.0

        Parameters
        ----------
        to_add : float
            amount by which the scale shall be increased
        Returns
        -------

        """
        self.scale = self.scale + to_add
        if self.scale > 3.0:
            self.scale = 3.0
        if self.scale < 1.0:
            self.scale = 1.0
        # print("Scale adjusted: " + str(lg.scale))

    def scale_and_border(self):
        """

        scales img_show according to the scale variable and adds fixed borders to the scaled image
        to get the _bordered version of the image

        Returns
        -------

        """

        self.scale_img_show()
        self.adjust_borders()
        self.img_bordered = cv.copyMakeBorder(self.img_show, self.border_left, self.border_bottom,
                                              self.border_top, self.border_right, cv.BORDER_CONSTANT,
                                              value=[0, 0, 0])  # blow up label layer so it can be merged

    def scale_img_show(self):

        width_scaled = int(self.img_raw.shape[1] * self.scale)
        height_scaled = int(self.img_raw.shape[0] * self.scale)
        self.img_show = cv.resize(self.img_show, (width_scaled, height_scaled))

    def adjust_borders(self):
        """
        adjusts the border_bottom so that the window shown matches the minimal_height

        Returns
        -------

        """
        current_total_height = self.img_show.shape[0] + self.border_bottom + self.border_top
        if current_total_height < self.minimal_height:
            self.border_bottom = (self.minimal_height - self.img_show.shape[0] + self.border_top)
        elif current_total_height >= self.minimal_height and self.border_bottom > self.border_top:
            self.border_bottom = self.minimal_height - self.img_show.shape[0] - self.border_top
            if self.border_bottom < self.border_top:
                self.border_bottom = self.border_top

    def handle_hotkeys(self, wait_time=0):
        """

        handles the keyboard inputs and executes functions accordingly

        Returns
        -------
        int
        """
        k = cv.waitKeyEx(wait_time)  # & 0xFF
        #print(k)
        if k == 27:  # Escape Key
            # user_input = input("\n Really Exiting? Enter 'y' \n")
            # if user_input == 'y':
            #    print("Exiting...")
            #    exit()
            return -1
        if k == ord('c'):
            self.show_color = not self.show_color
            return 0
        if k == ord('+'):
            self.adjust_scale(0.2)  #
            return 0
        if k == ord('m'):
            printer = pprint.PrettyPrinter(depth=24)
            print("\n Meta data for classification results with ID '" + self.image_id + "' :")
            printer.pprint(self.meta)
            return 0
        if k == ord('-'):
            self.adjust_scale(-0.2)
            return 0
        if k == 2424832:  # left
            return 2
        if k == 2555904:  # right
            return 1
        if k == ord('f'):
            return 3
        if cv.getWindowProperty('Classification Results', cv.WND_PROP_VISIBLE) < 1:
            self.create_window()
            return -1
        else:
            return 0

    def apply_dilation(self, label, input_img):
        if self.dilate_size < 3:
            return input_img
        kernel = np.ones((self.dilate_size, self.dilate_size), np.uint8)
        return cv.dilate(input_img, kernel, iterations=self.dilate_it)

    def apply_erosion(self, label, input_img, nr=1):
        if nr == 1:
            if self.erode_size1 < 3:
                return input_img
            else:
                kernel = np.ones((self.erode_size1,
                                  self.erode_size1), np.uint8)
                return cv.erode(input_img, kernel, iterations=self.erode_it1)
        if nr == 2:
            if self.erode_size2 < 3:
                return input_img
            else:
                kernel = np.ones((self.erode_size2,
                                  self.erode_size2), np.uint8)
                return cv.erode(input_img, kernel, iterations=self.erode_it2)

    def load_measurement(self, mesu):
        measurement = None
        if isinstance(mesu, cuvis.Measurement):
            measurement = mesu
        elif isinstance(mesu, str):
            if os.path.isfile(mesu):
                measurement = cuvis.Measurement(mesu)
        else:
            raise IOError("load_measurement: unknown type")
        self.img_raw = aux.get_rgb_from_cu3(measurement)

    def load_result(self, classification_result):
        if cv.getWindowProperty('Classification Results', cv.WND_PROP_VISIBLE) > 0:
            cv.destroyAllWindows()
        self.labels = {}
        self.image_id = classification_result["image_id"]

        self.orig_shape = classification_result["orig_shape"]

        try:
            self.meta = classification_result["meta"]
        except:
            self.meta = {}
        for key in classification_result["labels"].keys():
            self.labels[key] = {}
            self.labels[key]["probabilities"] = classification_result["labels"][key]["probabilities"].reshape(
                self.orig_shape)
            self.labels[key]["mask"] = np.zeros((self.orig_shape[0], self.orig_shape[1], 3), np.uint8)


if __name__ == "__main__":

    binarized = []
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Fruits.png"))
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Background.png"))
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Wood.png"))
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Plastic.png"))
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Paper.png"))
    binarized.append(cv.imread(r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\labels"
                               r"\session_000_015_snapshot.cu3\Metal.png"))

    pseudo_labels = {
        "Fruits": {"probabilities": binarized[0]},
        "Background": {"probabilities": binarized[1]},
        "Wood": {"probabilities": binarized[2]},
        "Plastic": {"probabilities": binarized[3]},
        "Paper": {"probabilities": binarized[4]},
        "Metal": {"probabilities": binarized[5]}
    }

    for key in pseudo_labels.keys():
        pseudo_labels[key]["probabilities"] = pseudo_labels[key]["probabilities"].astype(np.float32)
        # scale it so it will 1.0
        pseudo_labels[key]["probabilities"] /= 255.
        pseudo_labels[key]["probabilities"] = cv.cvtColor(pseudo_labels[key]["probabilities"], cv.COLOR_BGR2GRAY)

    labeled_img_data = {
        "image_id": r"C:\Users\robert.briegel\Documents\Cubert\2022_06_29\session_000\session_000_015_snapshot.cu3",
        "labels": pseudo_labels,
        "meta": {
            "preproc_config": {
                "methods": {
                    "SUBSET": {
                        "wavelengths": [450, 531, 623, 751, 834, 1011],
                        "choice": "closest"
                    },
                    "PCA": {
                        "explained_variance": 0.9995
                    },
                },
            },
        }
    }

    pp = Postprocessor()

    while (1):
        t1 = time.time()
        pp.load_result(labeled_img_data)
        pp.load_measurement_from_file(pp.image_id)
        pp.make_img_show(30)
        final_result = pp.get_final_result()
        # print(final_result)
        t2 = time.time()

        # print(t2-t1)
