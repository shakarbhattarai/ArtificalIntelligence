# -*- coding: utf-8 -*-
#The relevant data for red wine is found in red.csv
import pandas as pd
import quandl as Quandl,math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn import tree
df=pd.read_csv("red.csv",parse_dates=True,sep=';')
X=np.array(df.drop(['quality'],1))
y=np.array(df['quality'])
print df.tail()
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
clf=tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)
accuracy=clf.score(X_test,y_test)

df['forecast']=clf.predict(X)
df['error']=df['quality']-df['forecast']

df['error'].plot()


