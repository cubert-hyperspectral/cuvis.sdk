import datetime
import PySimpleGUI as sg
import cuvis
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# set color theme of gui
sg.theme('LightBrown13')

# flex dir cam_settings:
IMG_dir_base = r"C:\Users\benjamin.mueller\Documents\CUVIS\Images"
img_dir = "session\image"
SETTINGS_dir = r"C:\Program Files\cuvis\user\settings"
CALIB_dir = r"C:\Program Files\CubertFuchsia\Bin\factory"


# initialize global variables
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False,
         'mesu': None,
         'white': None,
         'dark': None,
         'dist': None,
         'img_name': "img",
         'sess_name': "session"}

# define the buttons
buttons = [
    [sg.Text('cam_settings location', size=(15, 1)),
     sg.InputText(r"C:\Program Files\cuvis\user\settings", key="-cam_settings-", size=(15, 1)),
     sg.Button("set", key="-setsettings-")],
    [sg.Text('init location', size=(15, 1)),
     sg.InputText(r"C:\Users\benjamin.mueller\Documents\dstl\IR20_fixed_Mono\calib", key="-init-", size=(15, 1)),
     sg.Button("(re)set", key="-setinit-")],
    [sg.Button("Update View", key="-view-", size=(30, 2))],
    [sg.Text(size=(15, 1))],
    [sg.Text('integration time [ms]', size=(15, 1)),
     sg.InputText("100", key="-inttime-", size=(15, 1)),
     sg.Button("set", key="-setinttime-")],
    [sg.Button("Capture Dark", key="-dark-", size=(15, 1)),
     # sg.Text(size=(9, 1)),
     sg.Button("set", key="-setdark-")],
    [sg.Button("Capture White", key="-white-", size=(15, 1)),
     # sg.Text(size=(9, 1)),
     sg.Button("set", key="-setwhite-")],
    [sg.Text('distance [mm]', size=(15, 1)),
     sg.InputText("500", key="-distmm-", size=(15, 1)),
     sg.Button("set", key="-setdistance-")],
    [sg.Text(size=(15, 1))],
    [sg.Text('Filename', size=(15, 1)),
     sg.InputText("session\image", key="-imgname-", size=(15, 1)),
     sg.Button("set", key="-setimgdir-")],
    [sg.Button("Save Image to Cube", key="-save-", size=(30, 2))],
    [sg.Text(size=(10, 2))],
    [sg.Button("Exit", key="-exit-", size=(30, 2))],
]

# define view window (canvas)
image_viewer_column = [
    [sg.Canvas(key="-IMAGE-")],
]

# define layout
layout = [
    [
        sg.vtop(sg.Column(buttons)),
        sg.VSeperator(),
        sg.vtop(sg.Column(image_viewer_column)),
    ]
]

# set lobal gui variable
_VARS['window'] = sg.Window('CUVIS Simple GUI',
                            layout,
                            margins=(10, 10),
                            finalize=True,
                            resizable=False,
                            size=(900, 500),
                            element_justification="left")

# cuvis contexts
cuvis.General(SETTINGS_dir)
calibration = cuvis.Calibration(CALIB_dir)
processingContext = cuvis.ProcessingContext(calibration)
acquisitionContext = cuvis.AcquisitionContext(calibration)

# define image export
general_settings = cuvis.GeneralExportSettings(ExportDir=IMG_dir_base + os.sep + _VARS["sess_name"],
                                               ChannelSelection="all",
                                               SpectraMultiplier=1.0,
                                               PanScale=0.0,
                                               PanSharpeningInterpolationType="NearestNeighbour",
                                               PanSharpeningAlgorithmType="Noop",
                                               AddPan=False,
                                               AddFullscalePan=False,
                                               Permissive=False)

cube_settings = cuvis.CubertSaveArgs(AllowOverride=False, AllowFragmentation=False, AllowSessionFile=False)
cubeExporter = cuvis.CubeExporter(general_settings, cube_settings)

# basic setting of processing context
processingContext.setRecalib(False)
processingContext.setProcessingMode("Raw")

# waiting for camera
print("Waiting for Camera to come online")
while 1:
    state = acquisitionContext.getState()
    if state == "Online":
        print("Camera online")
        break
    if state == "PartiallyOnline":
        print("Camera partially online")
        break
    time.sleep(1)
    print(".")

# basic setting of acquisition context
acquisitionContext.setIntegrationTime(100)
acquisitionContext.setOperationMode("Software")


def draw_figure(canvas, figure):
    '''draws the figure onto canvas (view)'''
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def Cuvis_Capture():
    '''capture image and return an img preview
    gives frownie face, when no measurement (when camera gets stuck)
    gives 2x2 grid when no data at all => refresh necessary
    '''
    am = acquisitionContext.capture()
    res = am.get(datetime.timedelta(milliseconds=500))
    if res["Measurement"] is not None:
        mesu = res["Measurement"]
        mesu.set_name("img_{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
        # print("viewing img_{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
        processingContext.apply(mesu)
        _VARS['mesu'] = mesu
        img = np.asarray([[1, 0], [0, 1]])
        for key, obj in mesu.Data.items():
            if key == "cube":
                spec = len(obj.wavelength)
                # preview is average of inner 50% of spectral layers
                img = np.mean(obj.array[:, :, int(0.25*spec):int(0.75*spec)], axis=2)
                img = np.rot90(img, 2)
                print("max count: {}".format(np.max(obj.array, axis=(0, 1, 2,))))
    else:
        print("no measurement, please retry....")
        img = np.asarray(
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 2, 0, 0, 2, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 3, 3, 0, 0, 1, 0],
             [0, 1, 0, 3, 0, 0, 3, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    return img


def drawChart():
    """provides preview image onto canvas"""
    _VARS['pltFig'] = plt.figure()
    img = Cuvis_Capture()
    plt.imshow(img, cmap="YlOrBr_r")
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.margins(x=0)
    plt.tight_layout()
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['-IMAGE-'].TKCanvas, _VARS['pltFig'])


def updateChart():
    '''updates the data in preview'''
    _VARS['fig_agg'].get_tk_widget().forget()
    img = Cuvis_Capture()
    plt.cla()
    plt.clf()
    plt.imshow(img, cmap="YlOrBr_r")
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.margins(x=0)
    plt.tight_layout()
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['-IMAGE-'].TKCanvas, _VARS['pltFig'])


def get_session_image(name):
    '''split name from image specification'''
    name = os.path.normpath(name)
    sections = name.split(os.sep)
    image = sections[-1]
    if len(sections) == 1:
        session = ""
    else:
        session = os.sep.join(sections[:-1])
    return session, image


### start an event loop

# draw first image
drawChart()

while True:
    event, values = _VARS['window'].read(timeout=200)
    # updateChart() # activate for "live view"

    # event management based on buttons
    if event == "-exit-" or event == sg.WIN_CLOSED:
        break

    if event == "-view-":
        updateChart()

    if event == "-setinttime-":
        # sets new integration time
        acquisitionContext.setIntegrationTime(int(values["-inttime-"]))
        print("inttime set to {}".format(int(values["-inttime-"])))
        updateChart()

    if event == "-setsettings-":
        # sets settings directory
        cuvis.General(values["-cam_settings-"])
        print("cam_settings set to {}".format(values["-cam_settings-"]))
        updateChart()

    if event == "-setinit-":
        # sets init containing directory and refreshes contexts based on the new directory
        del acquisitionContext
        del processingContext
        time.sleep(3)
        calibration = cuvis.Calibration(values["-init-"])
        processingContext = cuvis.ProcessingContext(calibration)
        acquisitionContext = cuvis.AcquisitionContext(calibration)
        processingContext.setRecalib(False)
        processingContext.setProcessingMode("Raw")

        while 1:
            state = acquisitionContext.getState()
            if state == "Online":
                print("Camera online")
                break
            if state == "PartiallyOnline":
                print("Camera partially online")
                break
            time.sleep(1)
            print(".")
        acquisitionContext.setIntegrationTime(100)
        acquisitionContext.setOperationMode("Software")
        _VARS.update({'white': None})
        _VARS.update({'dark': None})
        _VARS.update({'dist': None})
        print("init location set to {} and contexts reset".format(values["-init-"]))
        updateChart()

    if event == "-setimgdir-":
        # sets image dir based, relative to ~/Documents/CUVIS/Images/
        session_name, image_name = get_session_image(values["-imgname-"])
        _VARS["img_name"] = image_name
        _VARS["sess_name"] = session_name
        general_settings.ExportDir = IMG_dir_base + os.sep + session_name
        cubeExporter = cuvis.CubeExporter(general_settings, cube_settings)
        print("img dir set to {}".format(general_settings.ExportDir))
        updateChart()

    if event == "-setdistance-":
        # sets measured distance
        processingContext.calcDistance(int(values["-distmm-"]))
        print("distance set to {}".format(int(values["-distmm-"])))
        updateChart()

    if event == "-save-":
        # saves image to disk. Uses maximal available mode.
        mode = "Preview"
        name = "{}_{}".format(_VARS["img_name"], datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        _VARS["mesu"].set_name(name)
        print("Processing mode set to {}.".format(processingContext.getProcessingMode()))
        isCapable = processingContext.isCapable(_VARS["mesu"], mode, False)
        if isCapable:
            processingContext.apply(_VARS["mesu"])
            cubeExporter.apply(_VARS["mesu"])
            print("Measurement saved to {}!".format(general_settings.ExportDir + os.sep + name + ".cu3"))
        else:
            print("Could not save measurement. Irregular mode...")

    if event == "-white-":
        # captures white reference
        white = "white_{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        _VARS["mesu"].set_name(white)
        cubeExporter.apply(_VARS["mesu"])
        _VARS["white"] = {"file": IMG_dir_base + os.sep + _VARS["sess_name"] + os.sep + white + ".cu3", "set": False}
        print("White saved!")

    if event == "-dark-":
        # captures dark reference
        dark = "dark_{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        _VARS["mesu"].set_name(dark)
        cubeExporter.apply(_VARS["mesu"])
        _VARS["dark"] = {"file": IMG_dir_base + os.sep + _VARS["sess_name"] + os.sep + dark + ".cu3", "set": False}
        print("Dark saved!")

    if event == "-dist-":
        # captures distance reference from image (not used)
        dist = "dist_{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        _VARS["mesu"].set_name(dist)
        cubeExporter.apply(_VARS["mesu"])
        _VARS["dist"] = IMG_dir_base + os.sep + _VARS["sess_name"] + os.sep + dist + ".cu3"

    if event == "-setdark-":
        # sets dark reference
        dark = cuvis.Measurement(_VARS["dark"]["file"])
        processingContext.setReference(dark, "Dark")
        if _VARS["white"] is not None and _VARS["white"]["set"]:
            processingContext.setProcessingMode("Reflectance")
        else:
            processingContext.setProcessingMode("DarkSubtract")
        _VARS["dark"]["set"] = True
        print("dark set to {}".format(_VARS["dark"]["file"]))
        updateChart()

    if event == "-setwhite-":
        # sets white reference
        dark = cuvis.Measurement(_VARS["white"]["file"])
        processingContext.setReference(dark, "White")
        if _VARS["dark"] is not None and _VARS["dark"]["set"]:
            processingContext.setProcessingMode("Reflectance")
        _VARS["white"]["set"] = True
        print("white set to {}".format(_VARS["white"]["file"]))
        updateChart()

_VARS['window'].close()
