#!/usr/bin/env python
# coding: utf-8

#                                       Exploratory Data Analysis
#                                       
# * Discover the data for better understanding 
# * Check for anomalies in the data
# * Look for relationships between variables 
# * We can either explore data using graohs or through some python functions 
# * In the non-graphical approach, you will be using functions such as shape, describe, isnull, info, datatypes and more
# * In the graphical approach, you will be using plots such as scatter, box, bar, density and correlation plots
# 

#                            Importing Necessary Libraries 
#                                    

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') 


#                                Reading the CSV File 

# In[2]:


df= pd.read_csv ("kidney_disease.csv")
df


# * Shap Function : returns the number of rows and columns

# In[3]:


df.shape


# * Describe Function :computes a summary of statistics pertaining to the Dataset columns. This function gives the mean, std 
#  (إحصاء)

# In[4]:


df.describe()


# * isnull().sum() : returns the number of missing values in the dataset

# In[5]:


df.isnull().sum() 


# * dtypes function : This returns a Series with the data type of each column in the dataset

# In[6]:


df.dtypes


# * Hadling missing values :
# _ To insert the median value of each column into its missing rows ( only numeric ) 

# In[6]:


df.fillna(df.median(numeric_only=True), inplace=True)
df.isnull().sum() 


# *  To handle Categorical (the data  that is a string(object) or numeric, which needs to be converted to numerical variables),It  is preferred to use the Mode methode

# In[7]:


# df=pd.get_dummies(df)
# df
# Dummy Encode Method
dummies = pd.get_dummies(df)
dummies


# 
#  * Hadling missing values : _ To insert the mode value of each column into its missing rows 
# 

# In[8]:


#  df.fillna(df.mode() , inplace = True)
# df['rbc'].fillna(df['rbc'].mode() [0],inplace=True)
# df['pc'].fillna(df['pc'].mode() [0],inplace=True)
# df['pcc'].fillna(df['pcc'].mode() [0],inplace=True)
# df['ba'].fillna(df['ba'].mode() [0],inplace=True)
# df['pcv'].fillna(df['pcv'].mode() [0],inplace=True)
# df['wc'].fillna(df['wc'].mode() [0],inplace=True)
# df['rc'].fillna(df['rc'].mode() [0],inplace=True)
# df['htn'].fillna(df['htn'].mode() [0],inplace=True)
# df['dm'].fillna(df['dm'].mode() [0],inplace=True)
# df['cad'].fillna(df['cad'].mode() [0],inplace=True)
# df['appet'].fillna(df['appet'].mode() [0],inplace=True)
# df['pe'].fillna(df['pe'].mode() [0],inplace=True)
# df['ane'].fillna(df['ane'].mode() [0],inplace=True)
def handle_values (column_name):
    df[column_name].fillna(df[column_name].mode() [0],inplace=True)
handle_values("rbc")
handle_values("pc")
handle_values("pcc")
handle_values("ba")
handle_values("pcv")
handle_values("wc")
handle_values("rc")
handle_values("htn")
handle_values("dm")
handle_values("cad")
handle_values("appet")
handle_values("pe")
handle_values("ane")


# In[10]:


df.isnull().sum()


# * A Box Plot is the visual representation of the statistical five number summary of a given data set(
#   Minimum
#   First Quartile
#   Median (Second Quartile)
#   Third Quartile
#   Maximum)

# In[13]:


def boxplot (column_name):
    
    sns.boxplot(df[column_name])
boxplot("age")
# boxplot("bp")
# boxplot("sg")
# # boxplot("al")
# # boxplot("su")
# # boxplot("rbc")
# # boxplot("pc")
# boxplot("pcc")
# boxplot("ba")
# boxplot("wc")
# boxplot("rc")
# boxplot("htn")
# boxplot("dm")
# boxplot("cad")
# boxplot("appet")
# boxplot("pe")
# boxplot("ane")
# boxplot("classification")
# boxplot("bgr")
# boxplot("bu")
# boxplot("sc")
# boxplot("sod")
# boxplot("pot")
# boxplot("hemo")
# boxplot("pcv")



# In[14]:


boxplot("bp")


# * A histogram is a graph showing frequency distributions.
#   It is a graph showing the number of observations within each given interval.

# In[15]:


boxplot("sg")


# In[16]:


boxplot("al")


# In[17]:


boxplot("su")


# In[31]:


boxplot("bgr")


# In[32]:


boxplot("bu")


# In[33]:


boxplot("sc")


# In[34]:


boxplot("sod")


# In[35]:


boxplot("pot")


# In[36]:


boxplot("hemo")


# In[38]:


df['age'].hist()
#df['age'].plot(kind='hist')


# * A Distplot or distribution plot: depicts the variation in the data distribution

# In[13]:


sns.distplot(df['bp'])


# * A bar graph shows comparisons among discrete categories. One axis of the chart shows the specific categories being compared, and the other axis represents a measured value. The bars can be plotted vertically or horizontally.

# In[14]:


df['pc'].value_counts().plot(kind='bar',color=['salmon','lightblue'],title="Count of Diagnosis of kidney disease")


# In[15]:


df['su'].plot.pie()


# * A correlation matrix allows us to identify how well, or not so well, features within a dataset correlate with each other as  well as whether that correlation is positive or negative.

# In[16]:


df.corr()


# * A heatmap : is a two-dimensional graphical representation of data where the individual values that are contained in a matrix are represented as colours

# In[17]:


corr = df.corr()
sns.heatmap(corr,annot=True)


# In[ ]:




