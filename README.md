# Image Identification

## Mildew Detection in Cherry Leaves

Mildew Detection in Cherry Leaves is a study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew, and also the capability to predict if a cherry leaf is healthy or contains powdery mildew. [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) is a fungal disease that affects a wide range of plants, and is caused by many different species of ascomycete fungi in the order Erysiphales. Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves and stems.

## [View live website](https://project-5-image-identification-4f5afac6ab95.herokuapp.com/)

---

## Table of contents

- [Image Identification](#image-identification)
  - [Mildew Detection in Cherry Leaves](#mildew-detection-in-cherry-leaves)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypotheses and Validation Methods](#hypotheses-and-validation-methods)
  - [The Rationale to Map the Business Requirements](#the-rationale-to-map-the-business-requirements)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
    - [Project Summary](#project-summary)
    - [Leaf Visualiser](#leaf-visualiser)
    - [Mildew Detection](#mildew-detection)
    - [Project Hypotheses](#project-hypotheses)
    - [ML Performance Metrics](#ml-performance-metrics)
- [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Data Analysis and Machine Learning Libraries](#data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

---

## Dataset Content

The main contents of the dataset are disussed in this section.

- The dataset is taken from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves), and it is provided by Code Institute for the purpose of this portfolio project. I have created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. About 50% of the images show healthy cherry leaves and 50% of the images show the cherry leaves containing powdery mildew. Powdery mildew a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio; therefore, the company is concerned about supplying the market with a compromised quality product.

---

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

The business requirements are:<br>
1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.<br>
2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

---

## Hypotheses and Validation Methods

Project hypotheses and the methods to validate them are described below. The detailed validation process will be displayed in the dashboad.<br>
1- I suspect that mildew-contained cherry leaves have clear signs on their surface to differentiate them from the uninfected leaves.

- An average image and varability image study can help to investigate it.

2- I suggest that images of mildew-contained cherry leaves will have several differences compared with uninfected leaves in order to train the model with an image dataset.

- The dataset will be analysed using train, validation, and test techniques to investigate the accuracy of image identification.

3- I suggest that binary classification will be the best method to determine the difference between infected and uninftected leaves, considering that the sample dataset contains images classified as infected and uninfected leaves.

- The binary classification will be done to determine the difference between infected and uninftected leaves.

---

## The Rationale to Map the Business Requirements

### The rationale to map the business requirements to the Data Visualisations and ML tasks

The business requirements of image identification and a rationale to map them to the Data Visualisations and ML tasks are provided below.

- **Business Requirement 1**: Data Visualization

  - I will display the "mean" and "standard deviation" images for infected and uninfected leaves.
  - I will display the difference between an average infected leaf and an average uninfected leaf.
  - I will display an image montage for either infected or uninfected leaves.

- **Business Requirement 2**: Classification
  - I want to predict if a given leaf is infected or not with powdery mildew.
  - I want to build a binary classifier and generate reports.

---

## ML Business Case

- I want a ML model to predict if a leaf is infected with powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
- My ideal outcome is provide the Farmy foods team a faster method of determining if a plant is infected with powdery mildew or not.
- The model success metrics are:
  - Accuracy of 97% on the train set as well as on the test set.
- The model output is defined as a flag, indicating if the leaf is infected with powdery mildew or not and the associated probability of being infected or not. The Farmy foods staff will do the inspection of the leaf as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
- **Heuristics:** Currently, the process is to manually verify if a given cherry tree contains powdery mildew or not. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. Although the staff require some training to detect the occurrance of disease in detail, the image analysis, sample collection, and processing will be faster and could be performed by staff with less expertise.
- The training data to fit the model come from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset contains about +4 thousand images.
  - Train data - target: infected or not; features: all images.

---

## Dashboard Design

## Streamlit App User Interface

The dashboard is consisted of five pages provided below.

### Project Summary

This page will provide general information about the project, dataset used for data visualization and prediction, link for the additional information, and business requirements.

- **General Information**
  - [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) is a fungal disease that affects a wide range of plants, and can result in a low fruit yield in the case of Cherry Trees. This disease is caused by many different species of ascomycete fungi in the order Erysiphales. Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves and stems.
  - Currently, the process is to manually verify if a given cherry tree contains powdery mildew or not. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or contains powdery mildew.
- **Project Dataset**
  - The available dataset contains +4 thousand images of cherry leaves taken from the client's crop fields:
  - 2104 images of cherry leaves which are healthy
  - 2104 images of cherry leaves containing powdery mildew
  - For additional information about the dataset, please visit [Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
- **Link to additional information**
  - Link will be provided for the additional information about the project.
- **Business requirements**
  The project has two business requirements:<br>
  - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Leaf Visualiser

This page will provide the details for the answer to business requirement 1- "The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew."<br>

- Checkbox 1 - Difference between average and variability image
- Checkbox 2 - Differences between average infected and average uninfected leaves.
- Checkbox 3 - Image Montage

### Mildew Detection

This page will provide information about business requirement 2- "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."<br>

- Link to download a set of infected and uninfected leaves for live prediction.
- User Interface with a file uploader widget. The user should upload multiple leaf sample images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement.
- Table with image name and prediction results.
- Download button to download table.

### Project Hypotheses

This page will provide block for each project hypothesis, conclusions, and methods used to validate the hypothesis.

### ML Performance Metrics

This page will provide the details for the answer to business requirement 2.<br>

- Label Frequencies for Train, Validation, and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result

---

## Unfixed Bugs

- No unfixed bugs

[Back to Table of contents](#table-of-contents)

---

# Deployment

- The Image Identification was deployed using Code Institute's mock terminal for Heroku.

## Heroku

The steps for deployment were as follows:

1. Fork or clone this repository
2. Log in to Heroku and create an App
3. At the Deploy tab, select GitHub as the deployment method.
4. Select your repository name and click Search. Once it is found, click Connect.
5. Select the branch to be deployed, then click Deploy Branch.
6. The deployment process should happen smoothly if all deployment files are fully functional
7. Click now the button Open App on the top of the page to access your App.

## [View live website](https://project-5-image-identification-4f5afac6ab95.herokuapp.com/)

---

# Data Analysis and Machine Learning Libraries

Main list of the libraries used in the project of Image Identification and some examples of how these libraries were used is provided below.
* numpy
* pandas
* matplotlib
* seaborn
* plotly
* streamlit
* scikit-learn
* tensorflow-cpu
* keras
* keras-tuner
* protobuf

**matplotlib** is used to plot graphs<br>
**streamlit** is used to design the dashboard for mildew detector app<br>
**keras-tuner** is used to to create Keras tuning model for hyperparameter optimization

---

# Credits

To complete the contents of Image Identification: Mildew Detection in Cherry Leaves, I learned coding and collected the information from different sources.

- Learned Python coding from [Code Institute](https://learn.codeinstitute.net/)
- Used Code Institute student template [template](Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves)
- Collected information on good and bad coding practices from:
  - [Documenting Python Code](https://realpython.com/documenting-python-code/)
- The description on the malaria detection in blood cells provided by the tutor of the Code Institute with [Malaria Detection](Code-Institute-Solutions/WalkthroughProject01) and app [Malaria Detector](https://malaria-predictor.onrender.com/) was useful as well as an inspiration to design [Image Identification](https://github.com/HumaIlyas/mildew-detection-image-identification).
- The information on how to build keras tuning model for hyperparameter optimization was collected from [Tensorflow](https://www.tensorflow.org/tutorials/keras/keras_tuner) and [KerasTuner](https://keras.io/keras_tuner/)

## Content

- The cherry with leaf icon in the dashboard.py file was taken from [Cherry Emoji](https://emojicombos.com/cherry).
- The details about the powdery mildew were found at [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew)

## Acknowledgements

- I acknowledge all the tutors and fellow students at [Slack](https://app.slack.com/client/T0L30B202/D03PENWED0F) for their guidance and assistance to complete Image Identification.
- I acknowledge [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for mentor support and finishing touches.

[Back to Table of contents](#table-of-contents)