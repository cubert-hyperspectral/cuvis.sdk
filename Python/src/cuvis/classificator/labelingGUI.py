import cuvis

try:
    from . import auxiliary as aux
except:
    import auxiliary as aux

import numpy as np
import cv2 as cv
import os
import pathlib


class LabelingGUI(object):
    """
     a class allowing a user to generate labels for the cuvis classification workflow

    reads in .cu3 files and a list of labels to be applied
    lets the user label the images via a brush or rect drawing gui
    exports the labels as .png and generates cuvis_labels.csv

    """
    labels = []
    load_path = ""
    label_index = 0
    image_index = 0
    input_images = []
    training_tags = []
    out_dir = ""
    drawing = False  # true if mouse is pressed
    brush = True  # if True, draw rectangle
    current_label = "No Label"
    colors = []
    scale = 2.0
    alpha = 0.3
    minimal_height = 400
    brush_size = 3
    ix, iy = -1, -1
    orig_shape = (0, 0)
    border_left = border_top = border_bottom = 20
    border_right = 500
    img_show = None
    img_show_bordered = None
    layers = []
    current_layer = None
    current_layer_bordered = None
    dataframe = None
    overwrite_enabled = False
    show_color = True

    def load_images(self, load_path):
        """
        loads images (cubes) from directory

        Looks for .cu3-files in load_path and appends them to the input_images list. Also creates test/training tag.
        Exits when no files are found.

        Parameters
        ----------
        load_path : string, required
            folder path where .cu3-filey are

        Returns
        -------

        """
        print("\nSearching .cu3-files in " + load_path + "...")
        self.load_path = load_path
        for file in os.listdir(load_path):
            filename = os.fsdecode(file)
            if filename.endswith(".cu3"):  # or filename.endswith(".cu3s"):
                print("Found " + os.path.join(load_path, filename))
                self.input_images.append(filename)
                self.training_tags.append(True)
                continue
            else:
                continue
        if len(self.input_images) == 0:
            print("No Files where found. Exiting...")
            exit()
        pass

    def get_labels(self, labels_string):
        """
        makes label list

        Generates a list of labels without spaces from the comma seperated labels_string.
        Exits when no labels are present.

        Parameters
        ----------
        labels_string : string, required
            input string with comma seperated labels
        Returns
        -------

        """
        labels_string = labels_string.replace(' ', '')
        self.labels = labels_string.split(",")
        if len(self.labels) == 0:
            print("No labels given. Exiting...")
            exit()
        if len(self.labels) > 8:
            print("Too many labels! Maximum is 8. Exiting...")
            exit()
        for label in self.labels:
            if len(label) > 16:
                print("Label '" + label + "' is too long. \n 16 char. max. \n Exiting...")
                exit()
        print("Following labels can be applied: ")
        print(self.labels)

        for label_idx, label in enumerate(self.labels):
            self.colors.append(aux.get_new_color(label_idx))

    def adjust_brush(self, to_add):
        """
        in-/decrease the brush size

        In-/Decrease the brush by the amount of to_add.
        Lower Limit: 1
        Upper Limit: 15

        Parameters
        ----------
        to_add : int
            amount by which the scale shall be increased
        Returns
        -------
        """
        self.brush_size = self.brush_size + to_add
        if self.brush_size > 15:
            self.brush_size = 15
        if self.brush_size < 1:
            self.brush_size = 1

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

    def adjust_borders(self):
        """
        adjusts the border_bottom so that the window shown matches the minimal_height

        Returns
        -------+

        """
        current_total_height = self.current_layer.shape[0] + self.border_bottom + self.border_top
        if current_total_height < self.minimal_height:
            self.border_bottom = (self.minimal_height - self.current_layer.shape[0] + self.border_top)
        elif current_total_height >= self.minimal_height and self.border_bottom > self.border_top:
            self.border_bottom = self.minimal_height - self.current_layer.shape[0] - self.border_top
            if self.border_bottom < self.border_top:
                self.border_bottom = self.border_top

    def adjust_alpha(self, to_add):
        """

        in-/decrease the alpha value of the label layer overlay

        In-/Decrease the alpha value of the label layer overlay by the amount of to_add.
        Lower Limit: 0.1
        Upper Limit: 0.9

        Parameters
        ----------
        to_add: float

        Returns
        -------

        """
        self.alpha = self.alpha + to_add
        if self.alpha > 0.9:
            self.alpha = 0.9
        if self.alpha < 0.1:
            self.alpha = 0.1
        # print("Alpha adjusted: " + str(lg.alpha))

    def store_layer(self, image_index, label_index):
        """

        resets the scale to 1.0 and stores the current_layer at the right place in the layers list

        Parameters
        ----------
        image_index : uint8, required
        label_index :  uint8, required

        Returns
        -------

        """

        self.scale_images(1.0)
        self.layers[image_index][label_index] = self.current_layer.copy()

    def finish(self):
        """
        finishes the labeling process and saves the acquired labels accordingly

        Creates the out_dir in the same directory where the cu3-files were loaded. Checks if existing labels should be
        overwritten. Saves the label layers as .png. Creates cuvis_labels.csv.
        Returns
        -------

        """
        # todo: How to handle if one pixel has multiple labels?
        self.out_dir = os.path.join(self.load_path, "labels")
        self.dataframe = aux.DataLabel(os.path.join(self.out_dir, "{}_labels.csv".format("cuvis")))
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        else:
            while (1):
                user_input = input("\nLabels already exist. Enter 'y' to overwrite labels or 'n' to exit: \n")
                if user_input == 'y':
                    self.overwrite_enabled = True
                    break
                elif user_input == 'n':
                    print("\nLabels used in " + self.out_dir)
                    print("\nExiting Labeling GUI...")
                    raise LabelingDone

        for image_idx, image in enumerate(self.input_images):
            image_folder = os.path.join(self.out_dir, image)
            if not os.path.exists(image_folder):
                os.mkdir(image_folder)
            new_Line = {
                "File": image,
                "Test": not self.training_tags[image_idx]  # in the .csv the column is called "Test"
            }
            sum = 0
            for label_idx, label in enumerate(self.labels):
                label_layer = aux.convert_to_binary(self.layers[image_idx][label_idx])
                sum = sum + np.sum(label_layer)
                cv.imwrite(os.path.join(image_folder, label) + ".png", label_layer)
                new_Line[label] = os.path.join(image, label) + ".png"
            if sum == 0:
                user_input = input("\n" + image + " has no labels. Will be excluded from further processing. OK? Enter"
                                                  " 'y' \n")
                if user_input != 'y':
                    print("\n Continue Labeling. Label Data may be corrupted until saving is completed. ")
                    return None
            else:
                self.dataframe.add(new_Line)

        try:
            self.dataframe.write(self.overwrite_enabled)
            print("\nLabels saved to " + self.out_dir)
            print("\nExiting Labeling GUI...")
        except:
            raise LabelingDone
        raise LabelingDone

    def mark_test(self):
        """

        toggles between test/training for the currently shown image

        Returns
        -------

        """
        self.training_tags[self.image_index] = not self.training_tags[self.image_index]

    def undo_layer(self):
        """

        removes the currently shown label layer

        Returns
        -------

        """
        self.current_layer = np.zeros((self.orig_shape[0], self.orig_shape[1], 3), np.uint8)
        self.store_layer(self.image_index, self.label_index)

    def handle_hotkeys(self):
        """

        handles the keyboard inputs and executes functions accordingly

        Returns
        -------
        int
        """
        k = cv.waitKeyEx(1)  # & 0xFF
        # print(k)
        if k == ord('m'):
            self.brush = not self.brush
        if k == ord('+'):
            self.adjust_scale(0.2)
        if k == ord('-'):
            self.adjust_scale(-0.2)
        if k == ord('w'):
            self.adjust_alpha(0.1)
        if k == ord('q'):
            self.adjust_alpha(-0.1)
        if k == ord('c'):
            self.store_layer(self.image_index, self.label_index)
            self.show_color = not self.show_color
            return -1
        if k == ord('f'):
            self.store_layer(self.image_index, self.label_index)
            user_input = input("\n Really Finishing? Enter 'y' \n")
            if user_input == 'y':
                self.finish()
        if k == ord('u'):
            self.undo_layer()
        if k == ord('t'):
            self.mark_test()
        if k == ord('a'):
            self.adjust_brush(-1)
        if k == ord('s'):
            self.adjust_brush(1)
        if k == 2490368:  # up
            self.store_layer(self.image_index, self.label_index)
            self.label_index = self.label_index + 1
            if self.label_index > (len(self.labels) - 1):
                self.label_index = len(self.labels) - 1
            # print("Label Index : " + str(self.label_index))
            return -1
        if k == 2621440:  # down
            self.store_layer(self.image_index, self.label_index)
            self.label_index = self.label_index - 1
            if self.label_index < 0:
                self.label_index = 0
            # print("Label Index : " + str(self.label_index))
            return -1

        if k == 2424832:  # left
            self.store_layer(self.image_index, self.label_index)
            self.image_index = self.image_index - 1
            if self.image_index < 0:
                self.image_index = 0
            # print("Image Index : " + str(self.image_index))
            return -1
        if k == 2555904:  # right
            self.store_layer(self.image_index, self.label_index)
            self.image_index = self.image_index + 1
            if self.image_index > (len(self.input_images) - 1):
                self.image_index = len(self.input_images) - 1
            # print("Image Index : " + str(self.image_index))
            return -1

        elif k == 27:  # Escape Key
            user_input = input("\n Really Exiting? Enter 'y' \n")
            if user_input == 'y':
                print("Exiting...")
                exit()
            return -1

    def next_label(self, index):
        """

        sets the label_index to the index provided

        Parameters
        ----------
        index: int, required

        Returns
        -------
        int

        """
        self.label_index = index
        return self.label_index

    def next_image(self, index):
        """
        sets the image_index to the index provided

        Parameters
        ----------
        index: int, required

        Returns
        -------
        int
        """
        self.image_index = index
        return self.image_index

    def init_layers(self):
        """

        opens all the .cu3 files in the directory and creates label layers for each image and label, which are appended
        to layers (list of lists)

        Returns
        -------

        """
        if len(self.input_images) == 0:
            print("Load images first! Exiting...")
            exit()
        if len(self.labels) == 0:
            print("Load labels first! Exiting...")
            exit()
        for image in self.input_images:
            image_path = os.path.join(self.load_path, self.input_images[self.image_index])
            print("Trying to open " + image_path + " ...")
            mesu = cuvis.Measurement(image_path)

            img_layers = []
            for label in self.labels:
                img_layers.append(
                    np.zeros((mesu.Data["cube"].array.shape[0], mesu.Data["cube"].array.shape[1], 3), np.uint8))
            self.layers.append(img_layers)

    def run(self):
        """

        this is where the magic happens

        Runs the labeling GUI in an endless loop, receives input from mouse and keyboard and generates visual output.

        Returns
        -------

        """
        self.init_layers()
        try:
            while (1):
                label = self.labels[self.label_index]
                image_path = os.path.join(self.load_path, self.input_images[self.image_index])
                # print("Trying to open " + image_path + " ...")
                mesu = cuvis.Measurement(image_path)
                self.img_show = aux.get_rgb_from_cu3(mesu)
                if not self.show_color:
                    self.img_show = cv.cvtColor(self.img_show, cv.COLOR_BGR2GRAY)
                    self.img_show = cv.cvtColor(self.img_show, cv.COLOR_GRAY2BGR)
                height, width, channels = self.img_show.shape  # get shape of original image
                self.orig_shape = (height, width)
                self.img_show_bordered = cv.copyMakeBorder(self.img_show, self.border_left, self.border_bottom,
                                                           self.border_top,
                                                           self.border_right, cv.BORDER_CONSTANT,
                                                           value=[0, 0, 0])  # make bordered image to get writing space
                self.current_layer = self.layers[self.image_index][self.label_index]

                cv.namedWindow('Cuvis Labeling Tool')
                cv.setMouseCallback('Cuvis Labeling Tool', self.draw_shape)
                while (1):
                    # cv.imshow('layer', self.current_layer)
                    self.scale_images(self.scale)
                    self.adjust_borders()
                    merged = cv.addWeighted(
                        self.img_show_bordered[self.border_top:self.border_top + self.current_layer.shape[0],
                        self.border_left:self.border_left + self.current_layer.shape[1]], (1 - self.alpha),
                        self.current_layer, self.alpha,
                        0)  # stack images

                    self.img_show_bordered = cv.copyMakeBorder(merged, self.border_left, self.border_bottom,
                                                               self.border_top, self.border_right, cv.BORDER_CONSTANT,
                                                               value=[0, 0, 0])  # blow up label layer so it can be merged
                    self.draw_text()
                    cv.imshow('Cuvis Labeling Tool', self.img_show_bordered)

                    if self.handle_hotkeys() == -1:
                        break;

                cv.destroyAllWindows()

        except LabelingDone:
            cv.destroyAllWindows()
            pass

    def draw_shape(self, event, x, y, flags, param):
        """

        OpenCV callback function that draws the labels onto the image shown

        The callback function for mouse events checks if the cursor is currently over the image to be labeled and then
        draws either circles or rectangles onto the current_layer

        Parameters
        ----------
        event: see cv2, required
        x: int, required
        y: int, required
        flags: optional
        param: optional

        Returns
        -------

        """

        label_layer_bordered_height = self.current_layer_bordered.shape[0]
        label_layer_bordered_width = self.current_layer_bordered.shape[1]

        if aux.check_in_boundary((x, y), (self.border_left, self.border_top), (
                label_layer_bordered_width - self.border_right, label_layer_bordered_height - self.border_bottom)):
            if event == cv.EVENT_LBUTTONDOWN:
                self.drawing = True
                self.ix, self.iy = x, y
            elif event == cv.EVENT_MOUSEMOVE:
                if self.drawing == True:
                    if self.brush == False:
                        cv.rectangle(self.current_layer, (self.ix - self.border_left, self.iy - self.border_top),
                                     (x - self.border_left, y - self.border_top), self.colors[self.label_index], -1)
                    else:
                        cv.circle(self.current_layer, (x - self.border_left, y - self.border_top),
                                  int(self.brush_size * self.scale), self.colors[self.label_index], -1)
            elif event == cv.EVENT_LBUTTONUP:
                self.drawing = False
                if self.brush == False:

                    cv.rectangle(self.current_layer, (self.ix - self.border_left, self.iy - self.border_top),
                                 (x - self.border_left, y - self.border_top), self.colors[self.label_index], -1)
                else:
                    cv.circle(self.current_layer, (x - self.border_left, y - self.border_top),
                              int(self.brush_size * self.scale), self.colors[self.label_index], -1)

    def draw_text(self):
        """

        draws needed information as text onto the img_show_bordered

        Returns
        -------

        """
        label = self.labels[self.label_index]
        line_spacing = 35
        column_spacing = 270
        start_y = self.border_top
        start_x = self.img_show_bordered.shape[1] - self.border_right + 20

        self.img_show_bordered = cv.putText(self.img_show_bordered, "Please label the class:",
                                            (start_x, start_y + line_spacing),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            0.5, (255, 255, 255), 1,
                                            cv.LINE_AA)
        self.img_show_bordered = cv.putText(self.img_show_bordered, label, (start_x, start_y + line_spacing * 3),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            1.3, self.colors[self.label_index], 2,
                                            cv.LINE_AA)

        text = "Label " + str(self.label_index + 1) + r"/" + str(len(self.labels))
        self.img_show_bordered = cv.putText(self.img_show_bordered, text,
                                            (start_x, start_y + line_spacing * 4),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            0.5, (255, 255, 255), 1,
                                            cv.LINE_AA)

        color = (255, 0, 128)
        if self.training_tags[self.image_index] == True:
            text = "Marked as Training"
        else:
            text = "Marked as Test"
            color = (128, 0, 255)
        self.img_show_bordered = cv.putText(self.img_show_bordered, text,
                                            (start_x + column_spacing, start_y + line_spacing * 2),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            0.5, color, 1,
                                            cv.LINE_AA)

        text = self.input_images[self.image_index]
        print_length = 30
        if len(text) > print_length:
            text = text[-print_length:]
            text = ".." + text[-print_length - 2:]
        self.img_show_bordered = cv.putText(self.img_show_bordered, text,
                                            (start_x + column_spacing, start_y + line_spacing * 3),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            0.4, (255, 255, 255), 1,
                                            cv.LINE_AA)

        text = "Image " + str(self.image_index + 1) + r"/" + str(len(self.input_images))
        self.img_show_bordered = cv.putText(self.img_show_bordered, text,
                                            (start_x + column_spacing, start_y + line_spacing * 4),
                                            cv.FONT_HERSHEY_SIMPLEX,
                                            0.5, (255, 255, 255), 1,
                                            cv.LINE_AA)

        instructions = []
        instructions.append("Hold the left mouse button down to label with the brush")
        instructions.append("Press 'm' to toggle between brush and rect-labeling mode")
        instructions.append("Press 'left' and 'right' arrow keys to go through images")
        instructions.append("Press 'up' and 'down' arrow keys to go through labels")
        instructions.append("Press 't' to mark image either as 'Training' or  'Test'")
        instructions.append("Press 'u' to undo a label")
        instructions.append("Press '+' and '-' keys to zoom")
        instructions.append("Press 'q' and 'w' to adjust the alpha value of the labels (for visibility)")
        instructions.append("Press 'a' and 's' to adjust the brush size")
        instructions.append("Press 'c' to switch between b/w and color")
        instructions.append("Press 'f' to finish the labeling")
        instructions.append("Press 'Esc' to exit")

        line_spacing = 15
        start_y = self.img_show_bordered.shape[0] - 190

        for i, instruction in enumerate(instructions):
            self.img_show_bordered = cv.putText(self.img_show_bordered, instruction,
                                                (start_x, start_y + line_spacing * i),
                                                cv.FONT_HERSHEY_SIMPLEX,
                                                0.4, (255, 255, 255), 1,
                                                cv.LINE_AA)

    def scale_images(self, new_scale):
        """

        scales img_show and current_layer according to the new_scale variable and adds fixed borders to the scaled images
        to get the _bordered version of the image

        Parameters
        ----------
        new_scale: int, required

        Returns
        -------

        """
        width_scaled = int(self.orig_shape[1] * new_scale)
        height_scaled = int(self.orig_shape[0] * new_scale)

        self.img_show = cv.resize(self.img_show, (width_scaled, height_scaled))
        self.img_show_bordered = cv.copyMakeBorder(self.img_show, self.border_left, self.border_bottom, self.border_top,
                                                   self.border_right, cv.BORDER_CONSTANT,
                                                   value=[0, 0, 0])  # make borderd image to get writing space
        self.current_layer = cv.resize(self.current_layer, (width_scaled, height_scaled))
        self.current_layer_bordered = cv.copyMakeBorder(self.current_layer, self.border_left, self.border_bottom,
                                                        self.border_top, self.border_right,
                                                        cv.BORDER_CONSTANT,
                                                        value=[0, 0, 0])  # blow up label layer so it can be merged


class LabelingDone(Exception):
    pass


if __name__ == "__main__":
    lg = LabelingGUI()
    lg.load_images(input("This is the the Cuvis Labeling Tool. \nTo get started,"
                         "please provide the path to the folder containing .cu3-files you want to label: "))
    # lg.load_images(r"C:\Users\robert.briegel\Documents\Cubert\2022_05_30\session_000")

    labels_string = input("\nPlease provide a comma seperated list of all labels you want to use."
                          "Example: 'background, apple, orange, pineapple' \nYour lables: ")
    # labels_string = r"Fruits,Background, Wood, Plastic, Paper, Metal"
    lg.get_labels(labels_string)
    lg.run()
