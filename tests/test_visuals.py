# Test configuration
#
# python test_configuration.py

import os
import numpy as np
import pandas as pd


import configuration
import visuals as vs


def test_distribution():
    test_data_distribution = pd.DataFrame({
        'capital-gain': [0, 0, 0, 0, 5000, 10000, 0, 0, 0, 0, 5000, 0],
        'capital-loss': [0, 0, 0, 2000, 0, 0, 0, 3000, 0, 3000, 0, 0]
    })

    vs.distribution(test_data_distribution, plt_show = False)

    output_image_path = configuration.IMAGES_FOLDER  + 'distribution.png'

    test_result = os.path.exists(output_image_path)
    os.remove(output_image_path)
    assert test_result


def test_evaluate():
    test_results_evaluate = {
        'Learner1': [{'train_time': 1, 'acc_train': 0.8, 'f_train': 0.7, 'pred_time': 0.1, 'acc_test': 0.75, 'f_test': 0.65},
                     {'train_time': 2, 'acc_train': 0.85, 'f_train': 0.75, 'pred_time': 0.2, 'acc_test': 0.78, 'f_test': 0.68},
                     {'train_time': 3, 'acc_train': 0.9, 'f_train': 0.8, 'pred_time': 0.3, 'acc_test': 0.8, 'f_test': 0.7}],
        'Learner2': [{'train_time': 1.5, 'acc_train': 0.82, 'f_train': 0.72, 'pred_time': 0.15, 'acc_test': 0.76, 'f_test': 0.66},
                     {'train_time': 2.5, 'acc_train': 0.87, 'f_train': 0.77, 'pred_time': 0.25, 'acc_test': 0.79, 'f_test': 0.69},
                     {'train_time': 3.5, 'acc_train': 0.92, 'f_train': 0.82, 'pred_time': 0.35, 'acc_test': 0.82, 'f_test': 0.72}]
    }
    test_accuracy_evaluate = 0.7
    test_f1_evaluate = 0.6
    vs.evaluate(test_results_evaluate, test_accuracy_evaluate, test_f1_evaluate, plt_show = False)

    output_image_path = configuration.IMAGES_FOLDER  + 'evaluate.png'

    test_result = os.path.exists(output_image_path)
    os.remove(output_image_path)
    assert test_result


def test_feature_plot():
    test_importances_feature_plot = np.array([0.2, 0.1, 0.4, 0.15, 0.05, 0.1])
    test_X_train_feature_plot = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'feature6': [16, 17, 18]
    })
    test_y_train_feature_plot = np.array([0, 1, 0])
    vs.feature_plot(test_importances_feature_plot, test_X_train_feature_plot, test_y_train_feature_plot, plt_show = False)

    output_image_path = configuration.IMAGES_FOLDER  + 'feature_plot.png'

    test_result = os.path.exists(output_image_path)
    os.remove(output_image_path)
    assert test_result