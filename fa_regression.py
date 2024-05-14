# -*- coding: utf-8 -*-
"""FA_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BbIogzklVPIUttRmFbQJ6cFSN3h9t4s5
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import mean_squared_error,r2_score

df=pd.read_csv('/content/Fare prediction.csv')

df.head(5)

df.info()

df.shape

df.describe(include='all')

df.isnull().sum()

#no null values observed in data
#key is not an important factor for fare analysis. so, we will remove the column
df.drop(columns=['key'],axis=1,inplace=True)

df.duplicated().sum()

numerical_columns=df.select_dtypes(include=['int64','float64']).columns

correlation_matrix=df[numerical_columns].corr()
print(correlation_matrix)

plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix,annot=True,fmt='.2f')

#dropoff_longitude has o correlation with fare price
df.drop('dropoff_longitude',axis=1,inplace=True)

numerical_columns=df.select_dtypes(include=['int64','float64']).columns

#finding outliers
for column in numerical_columns:
  plt.figure(figsize=(10,8))
  sns.boxplot(df[column])
  plt.show()

#removing outliers
new_df=df[numerical_columns]
q1=new_df.quantile(0.25)
q3=new_df.quantile(0.75)
iqr=q3-q1

outliers=(df[(new_df>q3+1.5*iqr)|(new_df<q1-1.5*iqr)]).any(axis=1)
print(outliers)
new_df=new_df[~outliers]

df['pickup_datetime'].value_counts()

le=LabelEncoder()
df['pickup_datetime']=le.fit_transform(df['pickup_datetime'])

df.head(2)

x=df.drop('fare_amount',axis=1)
y=df['fare_amount']

x.head(4)

y.head(2)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=40)

scaler = MinMaxScaler()
X_train=pd.DataFrame(scaler.fit_transform(x_train[list(x.columns)]),
                                    columns=x.columns)
X_test=pd.DataFrame(scaler.transform(x_test[list(x.columns)]),
                                    columns=x.columns)

model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

y_pred[:5]

print(mean_squared_error(y_pred,y_test))
print(r2_score(y_pred,y_test))
print('Root mean square error:',mean_squared_error(y_pred,y_test,squared=False))