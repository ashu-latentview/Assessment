# -*- coding: utf-8 -*-
"""LVADSUSR73_Ashutosh_Q1_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iMKkBY9XphOeTXEQ7aUR5P-NxKsqLmUr
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv('/content/loan_approval.csv')

data.shape

data.info()

data[' education'].value_counts()

data[' self_employed'].value_counts()

data[' loan_status'].value_counts()

le=LabelEncoder()

data[' loan_status']=le.fit_transform(data[' loan_status'])

data[' self_employed']=le.fit_transform(data[' self_employed'])

data[' education']=le.fit_transform(data[' education'])

data.head(10)



sns.boxplot(data[' loan_amount'])

sns.boxplot(data[' income_annum'])

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_data = data[~((data < lower_bound) | (data > upper_bound)).any(axis=1)]

print(cleaned_data)
data=cleaned_data

data.drop('loan_id', axis=1, inplace=True)

data.head()

sns.boxplot(data[' cibil_score'])

data.isnull().sum()

data.duplicated().sum()

x = data.drop(' loan_status', axis=1)
y = data[' loan_status']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

pred=rf.predict(x_test)

print(pred)

from sklearn.metrics import accuracy_score

print("Accuracy without Scaling the dataset",accuracy_score(pred,y_test))

rf2 = RandomForestClassifier()
rf2.fit(x_train_scaled, y_train)

pred2=rf2.predict(x_test)

print("Accuracy with Scaling the dataset",accuracy_score(pred2,y_test))

from sklearn.metrics import confusion_matrix

confusion_matrix(pred,y_test)

cm = confusion_matrix(pred,y_test)


plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(pred,y_test))