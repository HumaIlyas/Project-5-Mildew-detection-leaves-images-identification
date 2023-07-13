import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics_content():
    """
    Contents of ML Performance Metrics
    """
    st.write("### ML Performance Metrics")
    version = 'v1'

    # Labels distribution on train, validation, and test sets
    st.write("### Train, Validation, and Test Sets: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation, and Test Sets')

    # Number of images in train, validation, and test sets
    st.info(
        f" **Number of images in train, validation, and test sets**\n"
        f"* Train - healthy: 1472 images\n"
        f"* Train - powdery_mildew: 1472 images\n"
        f"* Validation - healthy: 210 images\n"
        f"* Validation - powdery_mildew: 210 images\n"
        f"* Test - healthy: 422 images\n"
        f"* Test - powdery_mildew: 422 images")

    st.write("---")

    # To display model histroy
    st.write("### Model History")

    # Information about the graphical representation
    st.info(
        f" **Graphical representation of the learning cycle for the ML "
        f"model**\n"
        f"* The graphs show the model training accuracy and loss plots.\n"
        f"* It is evident from these graphs that it is a normal learning "
        f"curve.\n"
        f"* The model is neither overfitting nor underfitting.")

    # To display plots for graphical representation
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.write("---")

    # To display the generalised performance on test Set
    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Loss', 'Accuracy']))

    # The success message about the model performance
    st.success(
        f"**The general accuracy of ML model is 99.29%!!** ")
    load_test_evaluation(version)
