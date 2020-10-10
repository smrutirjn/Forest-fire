#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
from sklearn.feature_selection import RFE



from sklearn.preprocessing import MinMaxScaler



# In[2]:


df=pd.read_csv('forestfires.csv')


# In[3]:



# In[ ]:





# In[4]:


monthdict={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def month2num(month):
    return monthdict[month]

df['month'] = df['month'].apply(month2num)
    


# In[6]:


daydict={'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7}
def day2num(day):
    return daydict[day]
df['day'] = df['day'].apply(day2num)


# In[7]:
X=df.copy()

y = df.iloc[:, -1]
# In[8]:


# y = np.array(y).reshape((len(y), 1))
# #Y.reshape(-1, 1)

# normalize the dataset
scale = MinMaxScaler(feature_range=(0, 1))


# In[9]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[10]:


X_train = scale.fit_transform(X_train)
X_test = scale.transform(X_test)




# In[11]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
regr = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(mean_squared_error(y_pred, y_test))
print(r2_score(y_pred, y_test))


# In[12]:

print(y_test)
print("Training Accuracy = ", regr.score(X_train, y_train))
print("Test Accuracy = ", regr.score(X_test, y_test))

pickle.dump(regr, open('model.pkl','wb'))
# In[ ]:

model = pickle.load(open('model.pkl','rb'))
print(regr.predict([[0.5,0.5,0.6,0.8,0.77,0.48,0.6,0.49,0.66,0.27,0.35,0,1]]))


