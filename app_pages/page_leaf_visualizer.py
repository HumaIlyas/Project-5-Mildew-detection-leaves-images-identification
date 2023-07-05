import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaf_visualizer_content():
    """
    Contents of Leaf Visualiser
    """
    st.write("### Leaf Visualiser")
    st.info(
        f"* The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one that contains powdery "
        f"mildew."
    )
    version = 'v1'
    # Checkbox for the difference betweeen average and variability image
    if st.checkbox("Difference betweeen average and variability image"):
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")

        # Warning message
        st.warning(
            f"* The average and variability images did not show patterns to "
            f"intuitively differentiate one from another. However, a small "
            f"difference in the colour pigment of the average images is seen "
            f"for both labels.")

        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.image(avg_mildew, caption='Infected Leaf - Average and Variability')
        st.write("---")

    # Checkbox for the differences between average healthy and average infected Leaves
    if st.checkbox("Differences between average healthy and average infected Leaves."):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        # Warning message
        st.warning(
            f"* This study didn't show patterns to intuitively differentiate "
            f"average healthy and average infected leaves from another.")
        st.image(diff_between_avgs, caption='Difference between average images')

    # Checkbox for image montage
    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/mildew_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    Create image montage
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class to display
    if label_to_display in labels:

        # Check if montage space is greater than subset size
        # Number of images in the folder
        image_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(image_list):
            img_idx = random.sample(image_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(image_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        
        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        
        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
