#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("C:/Users/Ramya/Desktop/ethereum_price.csv")
df.head()


# In[11]:


plt.boxplot(df['High'])
plt.show()


# In[12]:


plt.boxplot(df['Low'])
plt.show()


# In[13]:


plt.hist(df['Open'])
plt.show()


# In[17]:


plt.scatter(df['Open'], df['Low'])
plt.show()


# In[18]:


plt.scatter(df['Close'], df['Low'])
plt.show()


# In[ ]:





# In[ ]:




