# ML-Model-Deployment
This project is a demonstration of a machine learning model deployment using Flask and Heroku on a simple dataset.
App Link: https://car-sp-prediction-app.herokuapp.com
## Objective:
#### Predicting the selling price of a car given features like kms driven, transmission type, year bought, present price etc.

## Dataset: 
#### The dataset's was collected from cardekho.com  was provided bdataset.
Link: https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho
* No of features: 9
* No of observations: 301

## Packages:
* Numpy, Pandas, Matplotlib, Flask, Pickle, sklearn

## Preprocessing:
* **Null Values** : There are no null values in the dataset.
* **Feature Elimination**: The 'Car_Name' feature was removed as it would not contribute in a beneficial way. The 'Year' feature was also removed.
* **Feature Engineering**: The 'car_age' feature was computed by calculating the difference between 'Year' variable and current year.
* **Encoding**: The categorical features 'Fuel_Type', 'Seller_Type', 'Transmission' were one-hot encoded.

## Predictive Modelling:
* **ML ALgorithms*: Random Forest was used for the training process.

## Evaluation:
* **Metrics**: R<sup>2</sup>, adjusted  R<sup>2</sup>, negative mean squared error.

## Performance (Random Forest):
* R<sup>2</sup>: 0.9477
* adjusted R<sup>2</sup>: 0.9300
* neg mean squared error:  -2.44

## Deployment: 
