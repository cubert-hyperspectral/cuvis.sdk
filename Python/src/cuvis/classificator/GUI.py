import PySimpleGUI as sg
import cv2 as cv
import math
import os
import cuvis
import time
import signal
import typing
import warnings
import cv2
import threading
import traceback
import numpy as np
import pandas as pd
import matplotlib as mpl
from typing import Tuple, List, Dict, Optional
import matplotlib.pyplot as plt
try:
    from . import auxiliary as aux
except:
    import auxiliary as aux

class ClassificatorGUI(object):
    def __init__(self):
        self.working_dir = os.path.dirname(os.path.abspath(__file__))
        self.construct_gui()
        self.create_window()

    def construct_gui(self):
        '''
        Create GUI for classificator life cycle
        '''
        # Main theme - change this to agree with the rest of the team's efforts/styling
        sg.theme('LightGray1')
        image_feed = [
            [
                sg.Text('Image Preview', font=('Helvetica 18'))
            ],[
                sg.Image(key='-IMAGE-')
            ]
        ]
        # Create column related to controlling the labeling GUI
        control_layout = [
            [
                sg.Text('Data Cube Path', font=('Helvetica 14'), key='load_title'),
                sg.In(size=(25, 1), enable_events=True, key="load_data"),
                sg.FileBrowse(target='load_data', file_types=(("Cubert Datacubes", "*.cu3"),), initial_folder=os.getcwd(), visible=True, key="file_browse_button"),
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
            ], [
                sg.HorizontalSeparator()
            ], [
                sg.Listbox(values=[''],select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, size=(50,10), key='class_selection')
            ],[
                sg.Text("Class Name"),
                sg.In(size=(10, 1), enable_events=True, default_text='', key="class_name"),
                sg.Button('Add', tooltip='Add new class', button_color=('black on white'), font='Helvetica 12', key='add_class'),
                sg.Button('Delete', tooltip='Delete selected class', button_color=('black on white'), font='Helvetica 12', key='delete_class')
            ], [
                sg.Text("Policy File"),
                sg.In(size=(25, 1), enable_events=True, key="policy-path"),
                sg.FileBrowse(target='policy-path', file_types=(("NPY files", "*.npy"),), initial_folder='./models', visible=False, key="file_browse_button"),
                sg.FileSaveAs(target='policy-path', file_types=(("NPY files", "*.npy"),), initial_folder='./models', visible=True, key="file_save_button")
            ]
        ]
        # ----- Full layout -----
        self.layout = [
            [sg.Image(key='-IMAGE-HEADER-',filename=os.path.join(self.working_dir,'assets/main_header.png'))],
            [sg.Column(image_feed),
            sg.VSeperator(),
            sg.Column(control_layout, element_justification='c'),]
        ]

    def load_cube(self, values: Dict):
        '''
        ADADad
        '''
        try:
            # Load data
            self.mesu = cuvis.Measurement(values.get('load_data'))
            # Generate cube RGB
            self.curr_img = aux.get_rgb_from_cu3(self.mesu)
            imgbytes = cv.imencode('.ppm', self.curr_img)[1].tobytes()
            self.image_elem.update(imgbytes)
            # Update the channel values
            self.waves = self.mesu.Data["cube"].wavelength
            r,g,b = aux.find_rgb_idx(self.mesu)
            self.window['band_1'].update(value=self.waves[r],values=self.waves, disabled=True)
            self.window['band_2'].update(value=self.waves[g],values=self.waves, disabled=True)
            self.window['band_3'].update(value=self.waves[b],values=self.waves, disabled=True)
            # render cube
        except Exception as e:
            print('Failed to load data!')

    def render_bands(self, event: str, values: Optional[Dict] = None):
        '''
        Update the GUI when a new datacube is loaded
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
        imgbytes = cv.imencode('.ppm', self.curr_img)[1].tobytes()
        self.image_elem.update(imgbytes)
    
    def create_window(self):
        '''
        Create a window using the provided layout
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
        data = np.zeros((600,600,3))
        font = cv2.FONT_HERSHEY_DUPLEX
        org = (50, 50)
        fontScale = 1
        color = (255, 255, 255)
        thickness = 2
        image = cv2.putText(data, 'No Data Loaded!', org, font, fontScale, color, thickness, cv2.LINE_AA)
        imgbytes = cv.imencode('.ppm', image)[1].tobytes()
        self.image_elem.update(imgbytes)
        self.timeout = 1000//60 # time in ms to use for window reads

    def run(self):
        while True:
            event, values = self.window.read(timeout=self.timeout)
            # Process events
            if event in (sg.WIN_CLOSED, sg.WINDOW_CLOSED,'Quit','-Exit', None):
                break
            elif event == '-IMAGE-':
                # TODO handle image clicks
                pass
            elif event == 'load_data':
                # TODO handle load data, we need a more intelligent data structure here
                print(values)
                self.load_cube(values)
                pass
            elif event in ['rgb','cir','custom_bands','band_1','band_2','band_3']:
                # Update image render
                self.render_bands(event, values)
            time.sleep(0.01)
        self.window.close()

if __name__ == '__main__':
    GUI = ClassificatorGUI()
    GUI.run()