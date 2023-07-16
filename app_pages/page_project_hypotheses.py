import streamlit as st


def page_project_hypotheses_content():
    """
    Contents of Project Hypotheses
    """
    st.write("### Project Hypotheses, Validation Methods, and Conclusions")

    st.write("#### Hypothesis 1")

    # Information about hypothesis 1
    st.info(
        f" I suspect that mildew-contained cherry leaves have clear signs on "
        f"their surface to differentiate them from the uninfected leaves. \n\n"
        f"**Validation method** \n"
        f"* An average image and varability image study can help to "
        f"investigate it. \n\n"
        f"**Conclusions** \n"
        f"* The average and variability images show some patterns to "
        f"differentiate one from another. This can be seen by a visual "
        f"difference in the colour pigment of the average and variability "
        f"images for both labels. \n"
        f"* An Image Montage shows that typically a mildew contained leaves "
        f"have clear white powdery spots on the surface and healthy leaves "
        f"have greenish smooth surface. \n"
        f"* Nevertheless, the difference between averages studies did not "
        f"reveal any clear pattern to differentiate one from another.")

    st.write("#### Hypothesis 2")

    # Information about hypothesis 2
    st.info(
        f" I suggest that images of mildew-contained cherry leaves will have "
        f"several differences compared with uninfected leaves in order to "
        f"train the model with an image dataset. \n\n"
        f"**Validation method** \n"
        f"* The dataset will be analysed using train, validation, and test "
        f"techniques to investigate the accuracy of Powdery Mildew Detection. "
        f"\n\n"
        f"**Conclusions** \n"
        f"* ML model performance matrics show that model was trained, "
        f"validated, and tested using the available image dataset. \n"
        f"* ML model performance was evaluated and it differentiates a mildew "
        f"contained leaf and a healthy leaf with at least 97% accuracy in "
        f"both the train and test sets.")

    st.write("#### Hypothesis 3")

    # Information about hypothesis 3
    st.info(
        f" I suggest that binary classification will be the best method to "
        f"determine the difference between infected and uninftected leaves, "
        f"considering that the sample dataset contains images classified as "
        f"infected and uninfected leaves. \n\n"
        f"**Validation method** \n"
        f"* The binary classification will be done to determine the "
        f"difference between infected and uninftected leaves. \n\n"
        f"**Conclusions** \n"
        f"* The difference between healthy and mildew-contained cherry leaves "
        f"was well determined using binary classification.")
