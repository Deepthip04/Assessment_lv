# -*- coding: utf-8 -*-
"""InternalAssessmentexpenses.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MLT3SMeQtMlWhS28uhtsu9mWvor3pBV9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

df=pd.read_csv('/content/expenses.csv')

df.head(5)

df.shape

df.info()

df.describe(include='all')

"""Checking for null values"""

df.isnull().sum()

"""found null values in bmi column, filling the null values with mode of bmi column"""

bmi_mode=df['bmi'].mode()[0]
df['bmi']=df['bmi'].fillna(bmi_mode)
print(df['bmi'])

df.isnull().sum()

"""Handling Duplicate Values"""

df.duplicated().sum()

df[df.duplicated()]

df=df.drop_duplicates()

df.duplicated().sum()

"""Univariate Analysis"""

numerical_columns=df.select_dtypes(include=['int64','float64']).columns
print(numerical_columns)
categorical_columns=df.select_dtypes(include=['object']).columns
print(categorical_columns)

for column in numerical_columns:
  plt.figure(figsize=(10,4))
  sns.histplot(df[column])
  plt.title(f'Histogram of {column}')
  plt.show()

for column in categorical_columns:
  plt.figure(figsize=(10,4))
  df[column].value_counts().plot(kind='bar')
  plt.title(f'Bar chart of {column}')
  plt.show()

"""Bivariate Analysis"""

correlation_matrix=df[numerical_columns].corr()
print('Correlation matrix for numerical columns is:',correlation_matrix)

plt.figure(figsize=(10,4))
sns.heatmap(correlation_matrix,annot=True,fmt='.2f')
plt.title('heatmap of correlation matrix')
plt.show()

#scatter plots between different numerical values

for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

"""outliers detection"""

for column in numerical_columns:
  plt.figure(figsize=(10,4))
  sns.boxplot(x=df[column])
  plt.title(f'boxplot of {column}')
  plt.show()

#we can see outliers in columns bmi and charges,let's remove outliers
new_df=df[numerical_columns]
q1=new_df.quantile(0.25)
q3=new_df.quantile(0.75)
iqr=q3-q1
outliers=((new_df>q3+1.5*iqr)|(new_df<q1-1.5*iqr)).any(axis=1)
print(outliers)
new_df=new_df[~outliers]
print(new_df)

df['age']=new_df['age']
df['bmi']=new_df['bmi']
df['children']=new_df['children']
df['charges']=new_df['charges']

#encoding categorical values
#categorical_columns= sex,smoker,region

df['sex'].value_counts()

df['smoker'].value_counts()

df['region'].value_counts()

encoded_df=pd.get_dummies(df,columns=['sex','smoker','region'],dtype='int')
print(encoded_df)

x=encoded_df.drop(columns=['charges'])
y=encoded_df['charges']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=40)

scaler = MinMaxScaler()
x_train=pd.DataFrame(scaler.fit_transform(x_train[list(x.columns)]),
                                    columns=x.columns)
X_test=pd.DataFrame(scaler.transform(x_test[list(x.columns)]),
                                    columns=x.columns)

model=LinearRegression()
model=model.fit(x_train,y_train)
y_pred=model.predict(y_test)

print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))
print(mean_squared_error(y_test,y_pred,squared=False))