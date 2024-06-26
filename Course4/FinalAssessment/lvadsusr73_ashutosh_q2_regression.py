# -*- coding: utf-8 -*-
"""LVADSUSR73_Ashutosh_Q2_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nhRHdOFNqiVV99NQ8L8QZM-EVY1L2nCs
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.linear_model import LinearRegression

data=pd.read_csv('/content/auto-mpg.csv')

data.shape

data.isnull().sum()

data=data.dropna()

data.isnull().sum()

data.duplicated().sum()

data.info()

data.head()

data['horsepower'] = data['horsepower'].str.replace(r'\D', '')
data['horsepower'] = pd.to_numeric(data['horsepower'])

data=data.dropna()

data.info()

sns.boxplot(data)

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_data = data[~((data < lower_bound) | (data > upper_bound)).any(axis=1)]

print(cleaned_data)
data=cleaned_data

plt.figure(figsize=(8, 6))
sns.distplot(data['mpg'])
plt.title('Distribution of Miles per Gallon (mpg)')
plt.xlabel('Miles per Gallon (mpg)')
plt.ylabel('Density')
plt.show()

data.drop('car name',axis=1,inplace=True)

data.head()

data['cylinders'].value_counts()

data['origin'].value_counts()

correlation_matrix = data.corr()

mpg_correlation = correlation_matrix['mpg'].drop('mpg')

print("Correlation with respect to 'mpg' column:")
print(mpg_correlation)

sns.heatmap(data.corr(),annot=True)

sns.pairplot(data[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']])
plt.show()

x=data.iloc[:,1:]
y=data.iloc[:,0]

from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Mean Absolute Error:", mae)

plt.scatter(y_test, y_pred, color='blue', label='Actual vs. Predicted')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Regression Line')
plt.xlabel('Actual mpg')
plt.ylabel('Predicted mpg')
plt.title('Regression Line for Predicted vs. Actual mpg')
plt.legend()
plt.show()