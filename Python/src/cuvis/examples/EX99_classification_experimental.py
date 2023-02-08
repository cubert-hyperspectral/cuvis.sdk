import cuvis.classificator as cuvClass
import os
from pprint import pprint

if __name__ == '__main__':
    Labeling = True
    classi_dir = input("This is the Cuvis Classification Tool."
                       " \nTo get started please provide the path to the folder containing .cu3-files you want to label: ")
    # classi_dir = r'M:\Evaluations\2022_08_18_Effilux_LED_Foods\cornflakes_and_noodles_000'


    if os.path.exists(os.path.join(classi_dir, "labels", "cuvis_labels.csv")):
        Labeling = False

    if Labeling:
        lg = cuvClass.LabelingGUI()
        lg.load_images(classi_dir)
        labels_string = input("\nPlease provide a comma seperated list of all labels you want to use."
                              "Example: 'background, apple, orange, pineapple' \nYour lables: ")
        # labels_string = r"Fruits,Background, Wood, Plastic, Paper, Metal"
        lg.get_labels(labels_string)
        lg.run()

    preprocessor_dict = {
        "methods": [
            # {"INDICES": {
            #     "indices": ["simple_difference", "NDVI", "hNDVI", "simple_integral"],
            #     "choice": "closest",
            # }},
            {"NORM": {
                "direction": "Brightness"
            }},
            # {"NORM": {
            #     "direction": "Channel"
            # }},
            # {"SUBSET": {
            #     "wavelengths": [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820,
            #                     840, 860],
            #     "choice": "closest"
            # }},
            {"PCA": {
                "number_of_componenents": 3
            }},
        ],
    }

    model_dict = {"methods":
                  # [{"RndForrest": {"max_depth": 2,"random_state": 0, "n_jobs": -1}}]
                  # [{"DIST": {"from": "median"}}]
                      [{"KNN": {"k": 5, "weights": "distance", "algorithm": "auto", "n_jobs": -1}}]

                  }

    postprocessor_dict = {"methods":
                              [{"Base": {"alpha": 0.3,
                                         "threshold": 0.5,
                                         "definity": 0.05,
                                         "erode1": 0,
                                         "dilate": 0,
                                         "erode2": 0,
                                         }}]}

    CC = cuvClass.CuvisClassificator(classi_dir=classi_dir)
    CC.set_preprocessor(preprocessor_dict)
    CC.set_model(model_dict)
    CC.set_postprocessor(postprocessor_dict)
    CC.build_pipeline()
    CC.evaluate()

    CC.save("CuvisClassificator.pckl")

    CC2 = cuvClass.CuvisClassificator()
    CC2.load(os.path.join(classi_dir, "CuvisClassificator.pckl"))

    res = CC2.predict(
        r"C:\Users\benjamin.mueller\Documents\strawberries4brezel"
        r"\strawberries_black_flat_angled_lights_foreign_000_007_snapshot.cu3")

    CC2.visualize(alpha=0.75,
                  scale=2.5,
                  save_path=r"C:\Users\benjamin.mueller\Documents\strawberries4brezel"
                            r"\strawberries_black_flat_angled_lights_foreign_000_007_snapshot.png")

    # pprint(res)

    # val = np.zeros(res[0]["orig_shape"]) - 999
    # prob = np.zeros(res[0]["orig_shape"]) + 0.9 # threshold
    # for ind, i in enumerate(res[0]["labels"].items()):
    #    resprobs = i[1]["probabilities"]
    #    resprobs = resprobs.reshape(res[0]["orig_shape"])
    #    val[prob < resprobs] = ind
    #    prob = np.maximum(prob, resprobs)

    # val = np.zeros(res[0]["orig_shape"])
    # for ind, i in enumerate(res[0]["labels"].items()):
    #    val = val + i[1]["mask"] * ind#

    # val[val == -999] = np.nan

    # plt.imshow(val, origin="lower", interpolation='nearest')
    # plt.colorbar()
    # plt.show()

    # results = CC.predict("new_image", post_process=False)
