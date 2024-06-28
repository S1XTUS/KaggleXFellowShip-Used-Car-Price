# Used Car Price Prediction


## Overview
This is based on the KaggleX Fellowship Skill Assessment challenge. The goal is to predict the prices of used vehicles

## Dataset
The dataset for this competition (both train and test) was generated from a deep learning model fine-tuned on the [Used Car Price Prediction Dataset dataset](#kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset). 
Feature distributions are close to, but not exactly the same, as the original. Feel free to use the original dataset as part of this competition,
both to explore differences as well as to see whether incorporating the original in training improves model performance, but that is not required.


**Brand & Model:** Identify the brand or company name along with the specific model of each vehicle.  
**Model Year:** Discover the manufacturing year of the vehicles, crucial for assessing depreciation and technology advancements.  
**Mileage:** Obtain the mileage of each vehicle, a key indicator of wear and tear and potential maintenance requirements.  
**Fuel Type:** Learn about the type of fuel the vehicles run on, whether it's gasoline, diesel, electric, or hybrid.  
**Engine Type:** Understand the engine specifications, shedding light on performance and efficiency.  
**Transmission:** Determine the transmission type, whether automatic, manual, or another variant.  
**Exterior & Interior Colors:** Explore the aesthetic aspects of the vehicles, including exterior and interior color options.  
**Accident History:** Discover whether a vehicle has a prior history of accidents or damage, crucial for informed decision-making.  
**Clean Title:** Evaluate the availability of a clean title, which can impact the vehicle's resale value and legal status.  
**Price:** Access the listed prices for each vehicle, aiding in price comparison and budgeting.  

## Model Training
For this , I used **Grid Search Cross-Validation for XGBoost** to achieve the best results. The model training process involved:
- **Data Preprocessing**: Cleaning and preparing the dataset for training.
- **Feature Engineering**: Creating and selecting relevant features for the model.
- **Hyperparameter Tuning**: Using Grid Search Cross-Validation to find the optimal hyperparameters for the XGBoost model.
- **Model Evaluation**: Assessing the performance of the model using various metrics.(Competition Criteria was rmse)
