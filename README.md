# Image Identification

## Mildew Detection in Cherry Leaves

Mildew Detection in Cherry Leaves is a study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew, and also the capability to predict if a cherry leaf is healthy or contains powdery mildew. [Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) is a fungal disease that affects a wide range of plants, and is caused by many different species of ascomycete fungi in the order Erysiphales. Powdery mildew is one of the easier plant diseases to identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves and stems.

## [View live website](https://project-5.herokuapp.com/)

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

3- The sample dataset contains images classified as infected and uninfected leaves.

- The binary classification will be the best method to determine the difference between infected and uninftected leaves.

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
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
