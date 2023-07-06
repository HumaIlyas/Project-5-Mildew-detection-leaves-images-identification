import streamlit as st


def page_project_hypotheses_content():
    """
    Contents of Project Hypotheses
    """
    st.write("### Project Hypotheses, Validation Methods, and Conclusions")
    st.write("#### Hypothesis 1")
    st.info(
        "I suspect that mildew-contained cherry leaves have clear signs on "
        "their surface to differentiate them from the uninfected leaves. \n"
        "* An average image and varability image study can help to "
        "investigate it. \n"
        "* An Image Montage shows that typically a mildew contained leaves "
        "have clear white powdery spots on the surface. \n"
        "* Average Image, Variability Image and Difference between Averages "
        "studies did not reveal any clear pattern to differentiate one from "
        "another.")
    st.write("#### Hypothesis 2")
    st.info(
        "I suggest that images of mildew-contained cherry leaves will have "
        "several differences compared with uninfected leaves in order to "
        "train the model with an image dataset. \n"
        "* The dataset will be analysed using train, validation, and test "
        "techniques to investigate the accuracy of image identification. \n"
        "* ML model performance matrics shows that model was trained, "
        "validated, and tested using the available image dataset.")
    st.write("#### Hypothesis 3")
    st.info(
        "I suggest that binary classification will be the best method to determine "
        "the difference between infected and uninftected leaves, considering that "
        "the sample dataset contains images classified as infected and uninfected "
        "leaves. \n"
        "* The binary classification will be done to determine the "
        "difference between infected and uninftected leaves. \n"
        "* The difference between healthy and mildew-contained cherry leaves "
        "was well determined using binary classification.")
