# Visuals
#
# python -m utils.visuals


# # Suppress matplotlib user warnings
# # Necessary for newer version of matplotlib
# import warnings
# warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")

# # Display inline matplotlib plots with IPython
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import f1_score, accuracy_score


import utils.configuration as conf
import utils.setup as setu


setu.create_folders()


def distribution(data, transformed=False, plt_show=True):
    """
    Visualization code for displaying skewed distributions of features.

    Parameters:
        data: Data
        transformed: If True the input has been Log-transformed
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    fig = plt.figure(figsize=(11, 5))

    # Skewed feature plotting
    for i, feature in enumerate(['capital-gain', 'capital-loss']):
        ax = fig.add_subplot(1, 2, i+1)
        ax.hist(data[feature], bins=25, color='#00A0A0')
        ax.set_title("'%s' Feature Distribution" % (feature), fontsize=14)
        ax.set_xlabel("Value")
        ax.set_ylabel("Number of Records")

        # old version with static ticks
        # ax.set_ylim((0, 2000))
        # ax.set_yticks([0, 500, 1000, 1500, 2000])
        # ax.set_yticklabels([0, 500, 1000, 1500, ">2000"])

        # Calculate dynamic y-ticks
        max_count = data[feature].value_counts().max()
        # y_ticks = list(range(0, max_count + 1, max(1, max_count // 4)))
        y_ticks = list(np.round(np.quantile(
            np.arange(0, max_count + 1), [0, 0.25, 0.5, 0.75])).astype(int))
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(
            [f">{tick}" if tick == y_ticks[-1] else str(tick) for tick in y_ticks])

    # Plot aesthetics
    if transformed is True:
        fig.suptitle(
            "Log-transformed Distributions of Continuous Census Data Features", fontsize=16, y=0.99)
    else:
        fig.suptitle(
            "Skewed Distributions of Continuous Census Data Features", fontsize=16, y=0.99)

    # fig.tight_layout()
    plt.subplots_adjust(wspace=0.4)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = conf.IMAGES_FOLDER

        if transformed is True:
            output_image_path = output_image_path + 'transformed_'
        else:
            pass
        output_image_path = output_image_path + 'distribution.png'

        plt.savefig(output_image_path)


def evaluate(results, accuracy, f1, plt_show=True):
    """
    Visualization code to display results of various learners.

    Parameters:
        results: Results
        accuracy: The score for the naive predictor
        f1: The score for the naive predictor
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    fig, ax = plt.subplots(2, 3, figsize=(11, 8))

    # Constants
    bar_width = 0.3
    colors = ['#A00000', '#00A0A0', '#00A000']

    # Super loop to plot four panels of data
    for k, learner in enumerate(results.keys()):
        for j, metric in enumerate(['train_time', 'acc_train', 'f_train', 'pred_time', 'acc_test', 'f_test']):
            for i in np.arange(3):

                # Creative plot code
                ax[j//3, j % 3].bar(i+k*bar_width, results[learner]
                                    [i][metric], width=bar_width, color=colors[k])
                ax[j//3, j % 3].set_xticks([0.45, 1.45, 2.45])
                ax[j//3, j % 3].set_xticklabels(["1%", "10%", "100%"])
                ax[j//3, j % 3].set_xlabel("Training Set Size")
                ax[j//3, j % 3].set_xlim((-0.1, 3.0))

    # Add unique y-labels
    ax[0, 0].set_ylabel("Time (in seconds)")
    ax[0, 1].set_ylabel("Accuracy Score")
    ax[0, 2].set_ylabel("F-score")
    ax[1, 0].set_ylabel("Time (in seconds)")
    ax[1, 1].set_ylabel("Accuracy Score")
    ax[1, 2].set_ylabel("F-score")

    # Add titles
    ax[0, 0].set_title("Model Training")
    ax[0, 1].set_title("Accuracy Score on Training Subset")
    ax[0, 2].set_title("F-score on Training Subset")
    ax[1, 0].set_title("Model Predicting")
    ax[1, 1].set_title("Accuracy Score on Testing Set")
    ax[1, 2].set_title("F-score on Testing Set")

    # Add horizontal lines for naive predictors
    ax[0, 1].axhline(y=accuracy, xmin=-0.1, xmax=3.0,
                     linewidth=1, color='k', linestyle='dashed')
    ax[1, 1].axhline(y=accuracy, xmin=-0.1, xmax=3.0,
                     linewidth=1, color='k', linestyle='dashed')
    ax[0, 2].axhline(y=f1, xmin=-0.1, xmax=3.0, linewidth=1,
                     color='k', linestyle='dashed')
    ax[1, 2].axhline(y=f1, xmin=-0.1, xmax=3.0, linewidth=1,
                     color='k', linestyle='dashed')

    # Set y-limits for score panels
    ax[0, 1].set_ylim((0, 1))
    ax[0, 2].set_ylim((0, 1))
    ax[1, 1].set_ylim((0, 1))
    ax[1, 2].set_ylim((0, 1))

    # Create patches for the legend
    patches = []
    for i, learner in enumerate(results.keys()):
        patches.append(mpatches.Patch(color=colors[i], label=learner))

    plt.legend(handles=patches, bbox_to_anchor=(-1.5, 2.75),
               loc='upper center', borderaxespad=0., ncol=3, fontsize='x-large')

    # Aesthetics
    plt.suptitle(
        "Performance Metrics for Three Supervised Learning Models", fontsize=16, y=0.99)

    # plt.tight_layout() # To avoid: UserWarning: Tight layout not applied. tight_layout cannot make Axes width small enough to accommodate all Axes decorations
    plt.subplots_adjust(top=0.8, hspace=0.4, wspace=0.4)
    # fig.set_constrained_layout(True)

    if plt_show is True:
        plt.show()
    else:
        plt.savefig(conf.IMAGES_FOLDER + 'evaluate.png')


def feature_plot(importances, X_train, y_train, plt_show=True):
    """
    Plot feature.

    Parameters:
        importances: Importances
        X_train: X training values
        y_train: Y training values
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    # Display the five most important features
    indices = np.argsort(importances)[::-1]
    columns = X_train.columns.values[indices[:5]]
    values = importances[indices][:5]

    # Creat the plot
    fig = plt.figure(figsize=(11, 8))
    plt.title("Normalized Weights for First Five Most Predictive Features",
              fontsize=16, y=0.99)
    plt.bar(np.arange(5), values, width=0.6, align="center",
            color='#00A000', label="Feature Weight")
    plt.bar(np.arange(5) - 0.3, np.cumsum(values), width=0.2,
            align="center", color='#00A0A0', label="Cumulative Feature Weight")
    plt.xticks(np.arange(5), columns, rotation=45, ha='right')
    plt.xlim((-0.5, 4.5))
    plt.ylabel("Weight", fontsize=12)
    plt.xlabel("Feature", fontsize=12)

    plt.legend(loc='upper center')
    # plt.tight_layout() # To avoid: UserWarning: Tight layout not applied. tight_layout cannot make Axes width small enough to accommodate all Axes decorations

    if plt_show is True:
        plt.show()
    else:
        plt.savefig(conf.IMAGES_FOLDER + 'feature_plot.png')


def heatmap_confusion_matrix(data, title, plt_show=True):
    """
    Confusion matrix heatmap visualization.

    Parameters:
        data: Data
        title: Title
        plt_show: If True the plot will be shown. Otherwise the plot will be saved in IMAGES_FOLDER

    Returns:
        None
    """
    plt.figure()
    sns.heatmap(data, annot=True, annot_kws={
                "size": 30}, cmap='Blues', square=True, fmt='.3f')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.title(title)

    if plt_show is True:
        plt.show()
    else:
        output_image_path = conf.IMAGES_FOLDER

        output_image_path = output_image_path + 'heatmap_confusion_matrix.png'

        plt.savefig(output_image_path)


if __name__ == "__main__":
    print("Visuals")

    test_data_distribution = pd.DataFrame({
        'capital-gain': [0, 0, 0, 0, 5000, 10000, 0, 0, 0, 0, 5000, 0],
        'capital-loss': [0, 0, 0, 2000, 0, 0, 0, 3000, 0, 3000, 0, 0]
    })

    distribution(test_data_distribution, plt_show=False)

    test_results_evaluate = {
        'Learner1': [{'train_time': 1, 'acc_train': 0.8, 'f_train': 0.7, 'pred_time': 0.1, 'acc_test': 0.75, 'f_test': 0.65},
                     {'train_time': 2, 'acc_train': 0.85, 'f_train': 0.75,
                         'pred_time': 0.2, 'acc_test': 0.78, 'f_test': 0.68},
                     {'train_time': 3, 'acc_train': 0.9, 'f_train': 0.8, 'pred_time': 0.3, 'acc_test': 0.8, 'f_test': 0.7}],
        'Learner2': [{'train_time': 1.5, 'acc_train': 0.82, 'f_train': 0.72, 'pred_time': 0.15, 'acc_test': 0.76, 'f_test': 0.66},
                     {'train_time': 2.5, 'acc_train': 0.87, 'f_train': 0.77,
                         'pred_time': 0.25, 'acc_test': 0.79, 'f_test': 0.69},
                     {'train_time': 3.5, 'acc_train': 0.92, 'f_train': 0.82, 'pred_time': 0.35, 'acc_test': 0.82, 'f_test': 0.72}]
    }
    test_accuracy_evaluate = 0.7
    test_f1_evaluate = 0.6
    evaluate(test_results_evaluate, test_accuracy_evaluate,
             test_f1_evaluate, plt_show=False)

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
    feature_plot(test_importances_feature_plot, test_X_train_feature_plot,
                 test_y_train_feature_plot, plt_show=False)

    test_data_heatmap_confusion_matrix = np.random.rand(2, 2)
    heatmap_confusion_matrix(
        test_data_heatmap_confusion_matrix, 'Testing confusion matrix', plt_show=False)
else:
    pass
