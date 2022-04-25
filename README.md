<h1>PREDICT MELANOMA</h1>

####
[Download Dataset](https://www.kaggle.com/aquib5559/machine-hack-house-price) <br>
Generally collecting data that fits your application is one of the most difficult steps in developing
a machine learning application, so for developing the Melanoma tumour size prediction
application, the required dataset has been taken from [kaggle](https://www.kaggle.com/).

## PROBLEM STATEMENT  <img src='https://img.shields.io/badge/Dataset-Kaggle-pink'>
<p>The objective of the application is to predict the Melanoma Tumour size based on various attributes regarding tumour e.g. damage size, exposed area ration of malign skin to the normal skin etc.</p>

## DISCOURSE 
Melanoma is the most invasive skin cancer with the highest risk of death. While it’s a serious skin cancer as it makes up a majority of skin cancer deaths, it’s highly curable if caught early.
Before recommending treatment, doctors first need to learn about the melanoma (e.g. shape, size or thickness etc.)
Melanomas present in many different shapes, sizes, and colours. That’s why it’s tricky to provide a comprehensive set of warning signs. Knowing the warning signs of skin cancer can help ensure that cancerous changes are detected and treated and hence it is needed to get some predictions of the melanoma tumour size based on various attributes.
Once doctors have collected all the information they can about the tumour, they can assign a stage. The stage gives doctor and patient a common language to understand how advanced the cancer is, where it is located and which treatment options are available.

The dataset contains 9,146 rows for each patient, with 10 columns mass_npea, size_npear,
malign_ratio, damage_size, exposed_area, std_dev_malign, err_malign, malign_penalty,
damage_ratio, tumor_size, most features are numerical continuous except the malign_penalty
which is a discrete one.

<h4>DATASET DESCRIPTION</h4>

- mass_npea: the mass of the area understudy for melanoma tumor
- size_npear: the size of the area understudy for melanoma tumor
- malign_ratio: ration of normal to malign surface understudy
- damage_size: unrecoverable area of skin damaged by the tumor
- exposed_area: total area exposed to the tumor
- std_dev_malign: standard deviation of malign skin measurements
- err_malign: error in malign skin measurements
- malign_penalty: penalty applied due to measurement error in the lab
- damage_ratio: the ratio of damage to total spread on the skin
- tumor_size: size of melanoma_tumor

<h4>ANALYZATION AND VISUALIZATION OF THE DATASET</h4>

For analyzation and visualization, I started loading the dataset and then I imported
required libraries e.g. pandas, numpy, matplotlib, pyplot, seaborn.
- I have used data.info() function to get the idea of datatypes and missing value and I have found that there is no missing value in the dataset.
- I have used data.isnull().sum() function to check for null values and found none.
- For visualization I have used heat map to get the idea about correlation between the features.

<h4>TRAINING THE MODEL USING FEATURE ENGINEERING, ENSEBLING AND STACKING</h4>

- I applied feature engineering which is quite helpful in training the model which has high accuracy. 
- I have created 13 new features and done log transformation of one feature which can improve my cross validation score.
- To calculate Loss I have used defined metrics by using RMSE.
- Finally trying out different regressors such as, ExtraTreeRegrssor, XGBoostRegressor and RandomForestRegressor and done hyperparametric tuning of the respective regressors using Bayesian optimization. Optimizer is used to minimize the loss function so that the model tries to predict accurately next time.
- The major step which boosted my score was using Stack Ensemble by combining 3 different regression models that were least correlated with each other.


## Prerequisites
 - Python
 - Pandas
 - Scikit Learn
 - Xgboost 
 - Bayesian optimization
 
 
 ## Dialogflow
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://www.drupal.org/files/project-images/dialogflownpng.png" alt="Dialogflow"></a>
</p>
<p align="center">
    <em>Lifelike conversational AI with state-of-the-art virtual agents.</em>

---

**Documentation**: <a href="https://cloud.google.com/dialogflow/es/docs" target="_blank">https://cloud.google.com/dialogflow/es/docs</a>

---

<p>Dialogflow is a service powered by Google Cloud Platform, enabling business-customer conversations, either by voice or text and built on natural language processing (NLP). Given its breadth of possibilities for integration, it seems a good fit for any kind of business.</p>
<p>Dialogflow provides better UX owing to the use of machine learning. The present-day trial version (ideal for non-commercial projects) is free of charge and likely a good choice when starting your experience with chatbots and voice apps.</p>






### Wanna Contribute?
- Clone/pull/download this repository.
- Create a virtualenv and install dependencies.
- Make relevant changes and Create Pull request

Comment your feedbacks, and do drop a ⭐ on the Github Repository.









