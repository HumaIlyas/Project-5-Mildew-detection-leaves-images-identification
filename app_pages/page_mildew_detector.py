import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities)


def page_mildew_detector_content():
    """
    Contents of Mildew Detection
    """
    st.write("### Mildew Detection")

    # Second business requirement
    st.info(
        f"**Business Requirement 2** \n"
        f"* The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew.")

    # Link to download a set of healthy and mildew contained cherry leaves
    st.write(
        f"* You can download a set of healthy and mildew contained cherry "
        f"leaves for live prediction. "
        f"You can download the images from "
        f"[kaggle] "
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)")

    st.write("---")

    # Upload of cherry leaf image samples for live predictions
    st.write(
        f" **Upload cherry leaf image samples for live predictions. You may "
        f"select more than one.**")

    images_buffer = st.file_uploader(' ',
                                     accept_multiple_files=True)

    # Button to make live prediction
    st.write(
        f" For prediction results click on the **Make Live Prediction** "
        f"button")
    predict_button = st.button("Make Live Prediction")

    if predict_button:
        make_live_prediction(images_buffer)


def make_live_prediction(images_buffer):
    """
    Function to upload images and make live predictions
    """
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample Image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_prob, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_prob, pred_class)

            df_report = df_report.append({"Name": image.name,
                                         'Result': pred_class},
                                         ignore_index=True)

        # Table with the image name and prediction results
        # Download button to download the analysis
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
