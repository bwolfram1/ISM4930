# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:36:50 2019

@author: brand
"""
#https://www.kaggle.com/uciml/biomechanical-features-of-orthopedic-patients#column_2C_weka.csv

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df = pd.read_csv('C:/Users/brand/Downloads/biomechanical-features-of-orthopedic-patients/column_2C_weka.csv')

df['Type'] = np.where(df['class'] == 'Normal',0,1)
df = df.drop('class',axis=1)

print(df.describe())

corr = df.corr()
sns.heatmap(corr)
plt.figure()

sns.pairplot(df,hue='Type')
plt.figure()

sns.distplot(df['pelvic_incidence'])
plt.figure()
sns.distplot(df['pelvic_tilt numeric'])
plt.figure()
sns.distplot(df['lumbar_lordosis_angle'])
plt.figure()
sns.distplot(df['sacral_slope'])
plt.figure()
sns.distplot(df['pelvic_radius'])
plt.figure()
sns.distplot(df['degree_spondylolisthesis'])
plt.figure()

X = df.iloc[:,:6]
y = df['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=13)

clf = LogisticRegression()
clf = clf.fit(X_train,y_train)
print(clf)


y_pred = clf.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
sns.heatmap(cnf_matrix,annot = True)
plt.figure()

print(" -----------")
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("F1:",metrics.f1_score(y_test, y_pred))