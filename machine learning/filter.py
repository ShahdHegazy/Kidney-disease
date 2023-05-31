#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df= pd.read_csv ("cars93.csv")
df


# In[4]:


df[df.Price > 20]


# In[5]:


df[df.Type > 'Midsize']


# In[6]:


df[(df.Price >5) & (df.Type=='Small')]


# In[19]:





# In[7]:


df.query('Price >5 and Type=="Van"')


# In[8]:


df.nlargest(3, 'Price')


# In[9]:


df.nsmallest(3, 'Price')


# In[21]:


df.iloc[3:5, :] #rows 3 and 4, all columns


# In[26]:





# In[11]:


# select columns by name
df.filter(items=['Type', 'Price'])


# In[12]:


# select rows containing 'Man'
df.filter(like='Man', axis=1)


# In[14]:


df["Manufacturer"].isin(["Acura","BMW"])


# In[15]:


df["Manufacturer"].str.startswith("A")


# In[16]:


df["Manufacturer"].str.endswith("W")


# In[17]:


df["Manufacturer"].str.contains("s")


# In[18]:


df.filter(items=['Model', 'Type'])


# In[19]:


filtered = df[~(df['Model'] == 'Legend')]
print(filtered)


# In[ ]:




