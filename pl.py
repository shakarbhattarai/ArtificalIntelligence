# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:59:40 2016

@author: shakar
"""

import pandas as pd

import quandl as Quandl,math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
final=pd.DataFrame();
dictionary=[
            [{"Chelsea":6,"Man United":1,"Man City":18,"Liverpool":3,"Arsenal":2}],
            [{"Chelsea":6,"Man United":3,"Man City":0,"Liverpool":2,"Arsenal":1}],
            [{"Chelsea":4,"Man United":1,"Man City":9,"Liverpool":5,"Arsenal":2}],
            [{"Chelsea":2,"Man United":3,"Man City":16,"Liverpool":4,"Arsenal":1}],
            [{"Chelsea":1,"Man United":3,"Man City":8,"Liverpool":5,"Arsenal":2}],
            [{"Chelsea":1,"Man United":2,"Man City":15,"Liverpool":3,"Arsenal":4}], 
            [{"Chelsea":2,"Man United":1,"Man City":14,"Liverpool":3,"Arsenal":4}],
            [{"Chelsea":2,"Man United":1,"Man City":9,"Liverpool":4,"Arsenal":3}],
            [{"Chelsea":3,"Man United":1,"Man City":10,"Liverpool":2,"Arsenal":4}],
            [{"Chelsea":1,"Man United":2,"Man City":5,"Liverpool":7,"Arsenal":3}],
            [{"Chelsea":2,"Man United":1,"Man City":3,"Liverpool":6,"Arsenal":4}],
           
            [{"Chelsea":6,"Man United":2,"Man City":1,"Liverpool":8,"Arsenal":3}],
            [{"Chelsea":3,"Man United":1,"Man City":2,"Liverpool":7,"Arsenal":4}],
            [{"Chelsea":3,"Man United":7,"Man City":1,"Liverpool":2,"Arsenal":4}],
            [{"Chelsea":1,"Man United":4,"Man City":2,"Liverpool":6,"Arsenal":3}],
            [{"Chelsea":10,"Man United":5,"Man City":4,"Liverpool":8,"Arsenal":2}],
             
            
            ]
for filename in [j for j in range(0,17)]:
    df=pd.read_csv(str(filename)+".csv",error_bad_lines=False)
    """df.drop(df.columns[23:], axis=1, inplace=True)
    df.drop(['Div','Date','Referee'], axis=1, inplace=True)
    df.drop(['HTR','FTR'], axis=1, inplace=True)"""
        
    df=df[['HomeTeam','AwayTeam','HTHG','HTAG','FTAG','FTHG','HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR']]
   
    
    #df.div((df.sum(axis=0,numeric_only=True)))
    df2=df[df.columns[2:]]
    df2=df2.div((df.sum(axis=0,numeric_only=True)))
    
    df[df.columns[2:]]=df2[df2.columns[:]]
    year=str(2000+int(filename))
    
    #df_che=df.loc[df'HomeTeam'] == 'Chelsea' & df['AwayTeam'] == 'Chelsea']
    for team in ['Chelsea','Man United', 'Man City', 'Liverpool', 'Arsenal']:
                
        if filename<=15:
            rank=dictionary[filename][0][team]
        else:
            rank=None
        df_che_ho=df[(df.HomeTeam == team)]
        df_che_aw=df[(df.AwayTeam == team)]
        
        che=pd.DataFrame({
             'Team': team,
             'Year': year,
             'Rank': rank,
             'HTHGS': [df_che_ho['HTHG'].sum()],
             'HTHGC': [df_che_ho['HTAG'].sum()],
             'FTHGC': [df_che_ho['FTAG'].sum()],
             'FTHGS': [df_che_ho['FTHG'].sum()],
        
             'HTAGS': [((df_che_aw['HTAG']).sum())],
             'HTAGC': [((df_che_aw['HTHG']).sum())],
             'FTAGC': [((df_che_aw['FTHG']).sum())],
             'FTAGS': [((df_che_aw['FTAG']).sum())],     
             
             'HS':[((df_che_ho['HS']).sum())],
             'HSC':[((df_che_ho['AS']).sum())],
             'AS':[((df_che_aw['AS']).sum())],
             'ASC':[((df_che_aw['HS']).sum())],
              
             
             'SOTH':[((df_che_ho['HST']).sum())],
             'SOTCH':[((df_che_ho['AST']).sum())],
             'SOTA':[((df_che_aw['AST']).sum())],
             'SOTCA':[((df_che_aw['HST']).sum())],
    
           
    
             'CoH':[((df_che_ho['HC']).sum())],
             'CoHC':[((df_che_ho['AC']).sum())],
             'CoA':[((df_che_aw['AC']).sum())],
             'CoAC':[((df_che_aw['HC']).sum())],
    
             
             'FAH':[((df_che_ho['HF']).sum())],
             'FAHC':[((df_che_ho['AF']).sum())],
             'FAA':[((df_che_aw['AF']).sum())],
             'FAAC':[((df_che_aw['HF']).sum())],
        
          
    
             'YCAH':[((df_che_ho['HY']).sum())],
             'YCAHC':[((df_che_ho['AY']).sum())],
             'YCA':[((df_che_aw['AY']).sum())],
             'YCAC':[((df_che_aw['HY']).sum())],
    
             
             'RCAH':[((df_che_ho['HR']).sum())],
             'RCAHC':[((df_che_ho['AR']).sum())],
             'RCA':[((df_che_aw['AR']).sum())], 
             'RCAC':[(df_che_aw['HR']).sum()]
             
    
    
        })
        final=final.append(che)
    final.fillna(0,inplace=True)
print final.head()
topredict=final[-5:]
final=final[:-5]

#print final.tail()
#print topredict.tail()
X=np.array(final.drop(['Rank','Team','Year'],1))
y=np.array(final['Rank'])
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.4)
clf=AdaBoostClassifier()
clf.fit(X_train,y_train)
print clf.score(X_test,y_test)
answer=clf.predict(np.array(topredict.drop(['Rank','Team','Year'],1)))
print topredict['Team'],answer