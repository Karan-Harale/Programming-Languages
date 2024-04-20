import pandas as pd
print(pd.__version__)

import seaborn as sns
print(sns.__version__)

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier

from sklearn .metrics  import confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
import sklearn

wine=pd.read_csv('Dataframe 1.csv')
print(wine.head())
print(wine.info())
print(wine.isnull().sum())

bins=(2,6.5,8)
groupname=['good','bad']
wine['d']=pd.cut(wine['d'],bins=bins,labels=groupname)
print(wine['d'].unique())

labelquality=LabelEncoder()
wine['d']=labelquality.fit_transform(wine['d'])
print(wine.head(10))

print(wine['d'].value_counts())

print(sns.countplot(wine['d']))

df2['Age_i']=round(pd.to_numeric(df2['Age'],errors='coerce'))
df2.dropna(how='any',inplace=True)

plt.scatter(df2['ChipTime_minutes'],df2['Age_i'])
print(plt.show())

