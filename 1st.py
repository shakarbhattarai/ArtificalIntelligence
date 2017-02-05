# -*- coding: utf-8 -*-
import pandas as pd
import quandl as Quandl,math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df=Quandl.get('WIKI/GOOGl')

df=df[['Adj. Open','Adj. Close','Adj. High','Adj. Low','Adj. Volume']]
df['HL_PCNT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Low']
df['PCNT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']
df=df[['Adj. Close','HL_PCNT','PCNT_change','Adj. Volume']]

forecastcol='Adj. Close'

forecast_out=int(math.ceil(0.01*len(df)))

df['label']=df[forecastcol].shift(-forecast_out)
X = np.array(df.drop(['label'],1))
X=preprocessing.scale(X)
X_predict=X[-forecast_out:]
df.dropna(inplace=True)
X = X[:-forecast_out]
y=np.array(df['label'])



X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=LinearRegression()
clf.fit(X_train,y_train)
accuracy=clf.score(X_test,y_test)
answer=clf.predict(X_predict)

df['Forecast']=np.nan

last_date=df.iloc[-1].name
ld_unix=(pd.to_datetime(last_date).value)/ 1000000000
print ld_unix

next_unix=ld_unix+86400 
print df.tail()

for i in answer:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix=next_unix+86400
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1) ]+[i]


df['Adj. Close'].plot()
df['Forecast']. plot()