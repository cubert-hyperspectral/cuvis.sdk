import os
import pickle
import typing
from collections import defaultdict
from io import BytesIO
from typing import Dict, List, Optional, Tuple

import cuvis
import cv2
import cv2 as cv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import PySimpleGUI as sg
import webcolors
from PIL import Image

try:
    from . import auxiliary as aux
except:
    import auxiliary as aux

class ClassificatorGUI():
    def __init__(self):
        self.mesu = None
        self.height = 600 # This value might need to be variable
        self.scale = 1.0
        self.classes = set()
        self.colors = {}
        colors = list(webcolors.CSS3_HEX_TO_NAMES.values())
        np.random.shuffle(colors)
        self.all_colors = (n for n in colors)
        self.selected_class = None
        self.labels = defaultdict(lambda: np.zeros((self.height,self.height), dtype=np.uint8))
        self.working_dir = os.path.dirname(os.path.abspath(__file__))
        self.construct_gui()
        self.create_window()

    def construct_gui(self) -> None:
        '''
        Create GUI for classificator life cycle

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # Main theme - change this to agree with the rest of the team's efforts/styling
        sg.theme('LightGray1')
        image_feed = [
            [
                sg.Text('Image Preview', font=('Helvetica 18')),
                sg.Push(),
                # TODO image scaling might eventually be possible
                # sg.Image(filename=os.path.join(self.working_dir,'assets', 'zoom_out.png')),
                # sg.Slider(
                #     range=(100, 300),
                #     default_value=100,
                #     tooltip='Image preview scale factor',
                #     orientation='h',
                #     enable_events=True,
                #     key='scale'
                # ),
                # sg.Image(filename=os.path.join(self.working_dir,'assets', 'zoom_in.png'))
            ],[
                sg.Graph((self.height,self.height), (0, 0), (self.height,self.height), enable_events=True, key='-IMAGE-', drag_submits=True)
            ]
        ]
        # Create column related to controlling the labeling GUI
        control_layout = [
            [
                sg.Text('Data Cube Path', font=('Helvetica 14'), key='load_title'),
                sg.In(size=(25, 1), enable_events=True, key="load_data"),
                sg.FileBrowse(target='load_data', file_types=(("Cubert Datacubes", "*.cu3"),), initial_folder=os.getcwd(), button_color=('black on white'), visible=True, key="file_browse_button"),
            ], [
                sg.HorizontalSeparator()
            ], [
                sg.Text('Image Preview', font=('Helvetica 12')),
                sg.Radio('RGB', 2, key='rgb', enable_events=True, default=True),
                sg.Radio('CIR', 2, key='cir', enable_events=True),
                sg.Radio('Custom', 2, key='custom_bands', enable_events=True),
            ],  [
                sg.Text('Band 1:', font=('Helvetica 12')),
                sg.Combo(['test','test2'], readonly=True, key='band_1', disabled=True, enable_events=True),
                sg.Text('Band 2:', font=('Helvetica 12')),
                sg.Combo(['test','test2'], readonly=True, key='band_2', disabled=True, enable_events=True),
                sg.Text('Band 3:', font=('Helvetica 12')),
                sg.Combo(['test','test2'], readonly=True, key='band_3', disabled=True, enable_events=True)
            ], [
                sg.HorizontalSeparator()
            ], [
                sg.Text('Image Class', font=('Helvetica 12')),
                sg.Radio('Train', 1, key='train', enable_events=True, default=True),
                sg.Radio('Validation', 1, key='validation', enable_events=True),
                sg.Radio('Test', 1, key='test', enable_events=True),
                sg.Radio('Split All', 1, key='all', enable_events=True),
            ], [
                sg.HorizontalSeparator()
            ], [
                sg.Table(values=[[]], headings=['Class Name', 'Color', 'Count'],
                auto_size_columns=True,
                display_row_numbers=False,
                justification='center', key='-TABLE-',
                selected_row_colors='red on yellow',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                enable_click_events=True)            
            ], [
                sg.Text('Class Name', font=('Helvetica 12')),
                sg.In(size=(20, 1), enable_events=True, default_text='', key="class_name"),
                sg.Button('Add', tooltip='Add new class', button_color=('black on white'), font='Helvetica 12', key='add_class'),
                sg.Button('Delete', tooltip='Delete selected class', button_color=('black on white'), font='Helvetica 12', key='delete_class')
            ], [
                sg.HorizontalSeparator()
            ], [
                sg.Text('Save Labels', font=('Helvetica 12')),
                sg.In(size=(25, 1), enable_events=True, key="save_path"),
                sg.FileSaveAs(target='save_path', file_types=(("Pickle Files", "*.pckl"),), initial_folder='./models', button_color=('black on white'), visible=True, key="file_save_button"),
            ], [
                sg.VPush()
            ]
        ]
        # ----- Full layout -----
        self.layout = [
            [sg.Image(key='-IMAGE-HEADER-',filename=os.path.join(self.working_dir,'assets/main_header.png'))],
            [sg.Column(image_feed),
            sg.VSeperator(),
            sg.Column(control_layout, element_justification='c'),]
        ]

    def load_cube(self, values: Dict) -> None:
        '''
        Load data cube from file path

        Parameters
        ----------
        values : Dict, values of all PySimpleGui fields

        Returns
        -------
        None
        '''
        try:
            # Load data
            self.mesu = cuvis.Measurement(values.get('load_data'))
            # Generate cube RGB
            self.curr_img = aux.get_rgb_from_cu3(self.mesu)
            self.curr_img = cv2.resize(self.curr_img, (self.height,self.height), interpolation = cv2.INTER_AREA)
            self.image_elem.draw_image(data=self.array_to_data(self.curr_img),location=(0, self.height))
            # Update the channel values
            self.waves = self.mesu.Data["cube"].wavelength
            r,g,b = aux.find_rgb_idx(self.mesu)
            self.window['band_1'].update(value=self.waves[r],values=self.waves, disabled=True)
            self.window['band_2'].update(value=self.waves[g],values=self.waves, disabled=True)
            self.window['band_3'].update(value=self.waves[b],values=self.waves, disabled=True)
            # render cube
        except Exception as e:
            print('Failed to load data!')

    @staticmethod
    def array_to_data(array: np.ndarray) -> bytearray:
        '''
        Convert image array to bytes object for PySimpleGUI rendering
        Parameters
        ----------
        array : np.ndarray, color image as numpy array, required

        Returns
        -------
        bytearray, encoded png image
        '''
        im = Image.fromarray(array)
        with BytesIO() as output:
            im.save(output, format="PNG")
            data = output.getvalue()
        return data
    
    def modify_class(self, event: str, values: Dict) -> None:
        '''
        Either add or delete class

        Parameters
        ----------
        event : string, triggering event, required
        values : Dict, item values, required

        Returns
        -------
        None
        '''
        if event == 'add_class' and values['class_name'] not in self.classes and len(values['class_name']) > 0:
            # Allocate a new color for the class
            self.colors[values['class_name']] = next(self.all_colors)
            tab_val = self.window['-TABLE-'].get()
            tab_val.append([values['class_name'], self.colors[values['class_name']], 0])
            tab_val = [z for z in tab_val if z]
            self.classes.add(values['class_name'])
            # Add in a new table
            self.window['-TABLE-'].update(values=tab_val)
            # Clear the blank
            self.window['class_name'].update('')
    
        elif event == 'delete_class':
            # Remove the selected class from the table values
            tab_val = self.window['-TABLE-'].get()
            tab_val = [z for z in tab_val if self.selected_class not in z]
            self.classes.remove(self.selected_class)
            self.selected_class = None
            self.window['-TABLE-'].update(values=tab_val)

    def erase_label(self, label, point):
        # TODO Erase drawn pixels
        pass

    def render_bands(self, event: str, values: Optional[Dict] = None):
        '''
        Update the GUI when a new datacube is loaded
        
        Parameters
        ----------
        event : string, triggering event, required
        values : Dict, item values, optional

        Returns
        -------
        None
        '''
        if self.mesu == None:
            print('No measurement loaded!')
            return
        elif event == 'rgb':
            # Generate cube RGB
            self.curr_img = aux.get_rgb_from_cu3(self.mesu)
            r,g,b = aux.find_rgb_idx(self.mesu)
            self.window['band_1'].update(value=self.waves[r],values=self.waves, disabled=True)
            self.window['band_2'].update(value=self.waves[g],values=self.waves, disabled=True)
            self.window['band_3'].update(value=self.waves[b],values=self.waves, disabled=True)
        elif event == 'cir':
            # Generate cube RGB
            self.curr_img = aux.get_cir_from_cu3(self.mesu)
            c,i,r = aux.find_cir_idx(self.mesu)
            self.window['band_1'].update(value=self.waves[c],values=self.waves, disabled=True)
            self.window['band_2'].update(value=self.waves[i],values=self.waves, disabled=True)
            self.window['band_3'].update(value=self.waves[r],values=self.waves, disabled=True)
        elif event in ['custom_bands','band_1','band_2','band_3']:
            # Reslice image from custom bands
            self.curr_img = aux.get_img_from_bands(self.mesu, values['band_1'], values['band_2'], values['band_3'])
            self.window['band_1'].update(disabled=False)
            self.window['band_2'].update(disabled=False)
            self.window['band_3'].update(disabled=False)

        # For both cases update the current image
        self.curr_img = cv2.resize(self.curr_img, (self.height,self.height), interpolation = cv2.INTER_AREA)
        self.image_elem.draw_image(data=self.array_to_data(self.curr_img),location=(0, self.height))

    def create_window(self):
        '''
        Create a window using the provided layout

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # ----- Full layout -----
        self.window = sg.Window(
            'Cubert Classificator',
            self.layout,
            icon = cv2.imencode('.ppm', cv2.imread(os.path.join(self.working_dir,'img', 'cubert.png')))[1].tobytes(),
            location=(0, 0),
            element_justification='c',
            use_default_focus=False,
            no_titlebar=False, 
            finalize=True, 
            debugger_enabled=True
        )
        # locate the elements we'll be updating. Does the search only 1 time
        self.image_elem = self.window['-IMAGE-']
        # Initialize image with blank black square
        data = np.zeros((self.height,self.height,3), dtype=np.uint8)
        font = cv2.FONT_HERSHEY_DUPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 255, 255)
        thickness = 2
        image = cv2.putText(data, 'No Data Loaded!', org, font, fontScale, color, thickness, cv2.LINE_AA)
        self.image_elem.draw_image(data=self.array_to_data(image),location=(0, self.height))
        self.timeout = 1

    def label_image(self, x: int, y: int):
        '''
        Label the image point collected from image canvas click or drag

        Parameters
        ----------
        x : int, row of the image, required
        y : int, column of the image, required

        Returns
        -------
        None
        '''
        if 0 <= x <= self.height and 0 <= y <= self.height:
            # Only allow valid pixels on the canvas
            # Create the label map of the pixels we have drawn
            label_map = self.labels[self.selected_class]
            label_map[x][self.height-y] = 1
            self.labels[self.selected_class] = label_map
            # Draw the pixels on the map
            color = webcolors.name_to_rgb(self.colors[self.selected_class])
            self.curr_img = cv2.circle(self.curr_img, (x, self.height-y), 1, color, -1)
            self.image_elem.draw_image(data=self.array_to_data(self.curr_img),location=(0, self.height))
            # Update the labeled pixel label count
            self.update_labeled_pixels()

    def update_labeled_pixels(self):
        '''
        Update the counts of the labeled pixels

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        tab_val = self.window['-TABLE-'].get()
        # Get index of row
        for index, row in enumerate(tab_val):
            if row[0] == self.selected_class:
                break
        curr_row = tab_val[index]
        curr_row[2] = self.labels[self.selected_class].sum()
        tab_val[index] = curr_row
        self.window['-TABLE-'].update(values=tab_val)

    def save_labels(self, path: str) -> None:
        '''
        Save the image label binary maps in a regular structure
        
        Parameters
        ----------
        path : str, directory to save the files to, required

        Returns
        -------
        None
        '''
        out_data = {}
        out_data['cube_path'] = self.window['load_data'].get()
        out_data['labels'] = dict(self.labels)
        with open(path, 'w') as f:
            pickle.dump(out_data, f)

    def run(self):
        '''
        Main execution loop to listen for events in the GUI window

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        while True:
            event, values = self.window.read(timeout=self.timeout)
            # Process events
            if event in (sg.WIN_CLOSED, sg.WINDOW_CLOSED,'Quit','-Exit', None):
                break
            elif event == '-IMAGE-':
                x, y = values[event]
                if self.selected_class:
                    # Draw a color on the image showing selected pixels
                    self.label_image(x,y)              
            elif event == 'load_data':
                # TODO handle load data, we need a more intelligent data structure here
                print(values)
                self.load_cube(values)
                pass
            elif event in ['rgb','cir','custom_bands','band_1','band_2','band_3']:
                # Update image render
                self.render_bands(event, values)
            elif event in ['add_class', 'delete_class']:
                # Add or delete the classes
                self.modify_class(event, values)
            elif '+CLICKED+' in event and '-TABLE-' in event and event[2][0] is not None:
                # Set the selected class to use for GUI elements
                self.selected_class = self.window['-TABLE-'].get()[event[2][0]][0]
        self.window.close()

if __name__ == '__main__':
    GUI = ClassificatorGUI()
    GUI.run()