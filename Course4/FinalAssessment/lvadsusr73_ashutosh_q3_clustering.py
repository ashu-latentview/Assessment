# -*- coding: utf-8 -*-
"""LVADSUSR73_Ashutosh_Q3_Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fk2pd_Jzcvf44nX41Ayx8oUbi3oAXSI5
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

data= pd.read_csv('/content/seeds.csv')
data.head()

data.shape

data.info()

data.isnull().sum()

data=data.dropna()

data.isnull().sum()

for col in data.columns:
    if data[col].dtype == 'object' and '?' in data[col].unique():
        data = data[data[col] != '?']
    data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert columns to numeric if they were object type

data.dropna(inplace=True)

plt.figure(figsize=(12, 8))
for i, col in enumerate(data.columns, 1):
    plt.subplot(3, 3, i)
    sns.histplot(data[col], kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()

x = data.copy()
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

inertia = []
silhouette_scores = []
range_values = range(2, 10)
for i in range_values:
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(x_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(x_scaled, kmeans.labels_))

plt.plot(range_values, inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

plt.show()

plt.plot(range_values, silhouette_scores, marker='o')
plt.title('Silhouette Scores')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.show()

optimal_clusters = 3
kmeans_final = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans_final.fit(x_scaled)

data['Cluster'] = kmeans_final.labels_

pca = PCA(n_components=3)
pca_x = pca.fit_transform(x_scaled)
sns.scatterplot(x=pca_x[:, 0], y=pca_x[:, 1], hue=kmeans_final.labels_, palette='viridis', s=100, alpha=0.6)
plt.title('Cluster Visualization with PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster')
plt.show()