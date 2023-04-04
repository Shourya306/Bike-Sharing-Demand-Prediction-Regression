# Bike Sharing Demand Prediction

## Abstract:

I was given a Seoul Bike Sharing Demand Prediction dataset to perform a Regression on. In Seoul, rental bikes are being provided to the public to enhance mobility comfort. It is important to ensure that there are enough bikes available in the streets of Seoul so that the waiting time for bikes by the public is lessened.By building various regression models, we can predict the count of bikes that need to be present in the city at any given time in order to reduce the waiting time for the bikes. And also understand what variables are influencing the model prediction.

## Problem Statement:

The Seoul Bike Sharing Demand Prediction data consists of 14 columns and 8760 rows. The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dew-point, Solar radiation, Snowfall, Rainfall), the count of bikes rented per hour and date information. I am supposed to predict the count of bikes rented per hour. Since the target variable that I need to predict is a continuous numeric variable I have decided to implement Linear Regression Model, Regularised Linear Regression and Random Forest Regressor.

## Attribute Information:

**Date(Year-Month_day)**: This column contains the date on which the observation has occurred.

**Rented Bike Count**: This column contains the number of bikes that are being rented out each hour.

**Hour**: This column contains the hour of the day.

**Temperature**: This column contains the values of temperature that were recorded during that date.

**Humidity**: This column contains the values of humidity that were recorded during that date.

**Windspeed**: This column contains the values of wind speed that were recorded during that date.

**Visibility**: This column contains the values of visibility that were recorded during that date.

**Dew point temperature**: This column contains the values of dew point temperature that were recorded during that date.

**Solar Radiation**: This column contains the values of solar radiation being recorded during that date.

**Rainfall**: The amount of rainfall during that date.

**Snowfall**: The amount of snowfall during that date.

**Seasons**: The various seasons 

**Holiday**: This column informs us whether that particular day was a holiday or not.

**Functional day**: This column informs us whether that particular day was a functioning day or a non-functioning day.

## Introduction:

Currently, the bike-sharing scheme is well-received throughout the world. It is a shared bike service for individuals, which is free of charge and for a short-term basis at a minimal rate. Most bike-sharing systems permit people to borrow and return a bike from a bike station to another station that belongs to the same network.

Bike-sharing involves the provision of a pool of bicycles across a network of strategically positioned ‘bike-sharing stations’, typically distributed in an urban area, which can be accessed by different types of users (i.e., registered members or occasional/casual users) for short-term rentals allowing point-to-point journeys.

Bike-sharing gains a vast range of attention in recent years as a part of initiatives to boost the use of cycles, improve the first mile/last mile link to other modes of transportation, and minimize the negative effect of transport activities on the environment. Bike-sharing has significant impacts on establishing a larger cycling community, increasing the use of transportation, minimizing greenhouse gas emissions, enhancing public health and also traffic troubles

## Models Used: 

1. Linear Regression

Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables. It is mostly used for finding out the relationship between variables and forecasting. Linear regression performs the task to predict a dependent variable value (y) based on a given independent variable (x).

Functional form of linear regression: B0 + B1x1 + B2x2 +…….+ BNxn.

For finding out the coef’s values(B0, B1…) Linear Regression uses Gradient Descent

2. Regularised Regression:

There are 3 regularised linear regressions.

* Lasso Regression - The lasso regression is abbreviated as the linear absolute shrinkage and selection operator. Below is the loss function. The regularised term is called the penalty. The lambda is called the penalty score. This is a hyper-parameter through which you control your penalty on the model. If the penalty score is high then the lasso regression can make the coefficients zero. Hence the name selection operator.

* Ridge Regression - The Ridge Regression unlike Lasso has a different regularised term as you can see below. The penalty term is squared. Even if the penalty score is high the ridge regression never makes the coefficients zero.

* Elastic Net Regression - Elastic Net first emerged as a result of a critique on the lasso, whose variable selection can be too dependent on data and thus unstable. The solution is to combine the penalties of ridge regression and lasso to get the best of both worlds. Elastic Net aims at minimizing the following loss function:

3. Random Forest Regressor

Random Forrest Regressor is used to predict the dependent variable which is continuous in nature. These are non-parametric in nature. This means They don't have any assumptions, unlike linear regression. They use a technique called bootstrap aggregation.

How do they work?
They build multiple decision trees from randomly sampled rows and columns of the dataset. This random sampling of the data is called bootstrap. After building multiple decision trees from the dataset they calculate the average of the values(in case of a regression problem) that have been predicted by all the decision trees. This process of calculating the average prediction by combining all the individual prediction values is called aggregation.

## Deployed:

I have used flask framework to build a website and used AWS EC2 to deploy it. Please find the application link below.

[Website link](http://ec2-65-1-1-208.ap-south-1.compute.amazonaws.com:8080/)
## Conclusion:

After implementing 5 different models on the dataset I came to the conclusion that the data is too complex for linear regression and regularised regression to understand the patterns. One must use complex models like Random Forrest, and XGBoost to get better results. Hence, I used a random forest regressor. The best-performing model among the 4 linear models is Linear Regression. This makes sense because the model that we built was not overfitting in the first place.








