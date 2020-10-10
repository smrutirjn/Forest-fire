#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pickle
import numpy as np
import pandas as pd

from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesRegressor

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error


# In[2]:


df=pd.read_csv('forestfires.csv')


# In[3]:


df.head()


# In[ ]:





# In[4]:


monthdict={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def month2num(month):
    return monthdict[month]

df['month'] = df['month'].apply(month2num)
    
df.head()


# In[5]:


daydict={'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7}
def day2num(day):
    return daydict[day]
df['day'] = df['day'].apply(day2num)
df.head()


# In[6]:


X = df.drop(columns=['area']).copy()
y = df['area']


# In[7]:


X.head()


# In[8]:


y = np.array(y).reshape((len(y), 1))
#Y.reshape(-1, 1)

# normalize the dataset
scale = MinMaxScaler(feature_range=(0, 1))


# In[9]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[10]:


X_train = scale.fit_transform(X_train)
X_test = scale.transform(X_test)


# In[20]:

np.set_printoptions(threshold=np.inf)
#X_train.head()


# In[14]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(mean_squared_error(y_pred, y_test))
print(mean_absolute_error(y_pred, y_test))
print(r2_score(y_pred, y_test))


# In[15]:

print(y_train)
print("Training Accuracy = ", regr.score(X_train, y_train))
print("Test Accuracy = ", regr.score(X_test, y_test))


# In[ ]:


#!jupyter nbconvert --to script forestfirefinal.ipynb


# In[16]:


re = ExtraTreesRegressor(n_estimators =10,criterion='mae',random_state=0)
re.fit(X_train,y_train)


# In[17]:


y_pred = re.predict(X_test)


# In[18]:


re.score(X_test, y_test)


# In[ ]:


# plt.figure(figsize=(10, 6))
# #plt.plot(X_test, f(X_test), "b")
# plt.scatter(X_train, y_train, c="b", s=20)
# plt.plot(X_test, regr.predict(X_test), "r", lw=2)
# plt.xlim([-5, 5])


# In[53]:


row = [[0.5,0.5,0.6,0.8,0.77,0.48,0.6,0.49,0.57,0.77,0.78,0.0]]
yhat = re.predict(row)
print('Prediction: %d' % yhat[0])

pickle.dump(re,open('model.pkl','wb'))
# In[ ]:





# In[ ]:




