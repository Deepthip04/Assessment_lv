# -*- coding: utf-8 -*-
"""IA2clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18bfCDjG6LNAApzUBiNvG_II8GDIOCI98
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

df=pd.read_csv('/content/Mall_Customers.csv')

df.head(5)

df.info()

df.describe(include='all')

df['Gender']=df['Gender'].map({'male':1,'female':2})

df.isnull().sum()

mode_income=df['Annual Income (k$)'].mode()[0]
df.fillna(mode_income,inplace=True)

df.isnull().sum()

df.duplicated().sum()

df.columns

cols=['CustomerID','Age', 'Annual Income (k$)',
       'Spending Score (1-100)']
for column in cols:
  sns.boxplot(data=df,x=column)
  plt.title(column)
  plt.show()

sns.scatterplot(data=df,x='Annual Income (k$)',y='Spending Score (1-100)')
plt.show()

encoded_df=df[['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)']]

encoded_df.head(5)

#KMeans(n_clusters=2)

cols=['Annual Income (k$)',	'Spending Score (1-100)']

scaler=StandardScaler()
scaled_df=scaler.fit_transform(df[cols])

inertia=[]
for i in range(1,8):
    kmeans=KMeans(n_clusters=i,random_state=20)
    kmeans.fit(scaled_df)
    inertia.append(kmeans.inertia_)

pd.DataFrame({"cluster":range(1,8),"inertia":inertia})

plt.figure(figsize=(15,8))
plt.plot(range(1,8),inertia,marker='o')
plt.show()

clusters= 5
kmeans = KMeans(n_clusters=clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_df)
plt.figure(figsize=(10,6))
sns.scatterplot(x='Annual Income (k$)',y = 'Spending Score (1-100)',hue='cluster',palette=['blue','green','pink','black','yellow'],legend=True,data=df)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()