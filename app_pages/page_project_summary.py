import streamlit as st


def page_project_summary_content():
    """
    Contents of Project Summary
    """
    st.write("### Project Summary")
    st.info(
        f"**General Information**\n"
        f"* [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) is "
        f"a fungal disease that affects a wide range of plants, and can "
        f"result in a low fruit yield in the case of Cherry Trees. This "
        f"disease is caused by many different species of ascomycete fungi in "
        f"the order Erysiphales. Powdery mildew is one of the easier plant "
        f"diseases to identify, as its symptoms are quite distinctive. "
        f"Infected plants display white powdery spots on the leaves and "
        f"stems.\n\n"
        f"* Currently, the process is to manually verify if a given cherry "
        f"tree contains powdery mildew or not. An employee spends around 30 "
        f"minutes in each tree, taking a few samples of tree leaves and "
        f"verifying visually if the leaf tree is healthy or contains powdery "
        f"mildew."
        f"**Project Dataset**\n"
        f"* The available dataset contains 4+ thousand images of cherry "
        f"leaves taken from the client's crop fields: \n"
        f"* 2104 images of cherry leaves which are healthy \n"
        f"* 2104 images of cherry leaves containing powdery mildew \n"
        f"* For additional information about the dataset, please visit "
        f"[Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/HumaIlyas/Project-5-Mildew-detection-leaves-images-identification/blob/main/README.md).")

    st.success(
        f"**Business requirements**\n"
        f"* The project has two business requirements:\n"
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains "
        f"powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew.")
