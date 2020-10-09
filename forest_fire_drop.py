#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle

from sklearn.feature_selection import RFE
# from sklearn.ensemble import ExtraTreesRegressor

# import seaborn as sns

# import matplotlib.pyplot as plt
# from pandas.plotting import scatter_matrix

from sklearn.preprocessing import MinMaxScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Ridge
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import ElasticNet
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.svm import SVR
# from sklearn.metrics import explained_variance_score
# from sklearn.metrics import mean_absolute_error


# In[2]:
# days = {'Mon':0,'Tues':1,'Weds':2,'Thurs':3,'Fri':4,'Sat':5,'Sun':6}
mon={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

dff=pd.read_csv('forestfires.csv')
dff['month'] = dff['month'].apply(lambda x: mon[x])

# In[3]:




# In[4]:


df = dff.drop(columns=['X','Y','FFMC','DMC','DC','ISI','rain']).copy()

df['month'] = df['month'].apply(lambda x: mon[x])

# In[5]:


# df.head()


# In[6]:


target='area'


# In[7]:


# sns.heatmap(df.corr(),annot=True)


# In[8]:


X = df.iloc[:, 0:5].values
y = df.iloc[:, 5].values


# In[9]:


# display(X)


# In[10]:


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 2]) #For month
labelencoder_X_2 = LabelEncoder()
X[:, 1] = labelencoder_X_2.fit_transform(X[:, 3]) #For weekday


# In[11]:
print(X)


# display(X)


# In[14]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

sc = MinMaxScaler(feature_range=(0, 1))
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[15]:


# display(X_train)


# # In[16]:


# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn import metrics
# from sklearn.metrics import accuracy_score


# # In[17]:


# et = ExtraTreesRegressor(n_estimators =10,criterion='mse',random_state=0)
# et.fit(X_train,y_train)


# # In[19]:


# y_pred = et.predict(X_test)


# # In[20]:


# et.score(X_test, y_test)


# In[29]:


from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
# print(mean_squared_error(y_pred, y_test))
# print(r2_score(y_pred, y_test))
#print(explained_variance_score(y_pred, y_test))


# In[27]:


# from sklearn.tree import DecisionTreeRegressor as dtr
# reg = dtr(random_state = 42)
# reg.fit(X_train, y_train)
# y_pred = reg.predict(X_test)
# print(mean_squared_error(y_pred, y_test))
# print(r2_score(y_pred, y_test))


# In[30]:

# pickle.dump(regr, open('model.pkl','wb'))

# In[ ]:




