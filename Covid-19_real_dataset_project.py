#!/usr/bin/env python
# coding: utf-8

# # (A part of Big Data Analysis)
# 
# 

# #     COVID-19 SMALL DATASET

# We have a taken a small dataset of covid-19,The dataset used here till 29 April 2020.
# 
# I am Analyzing this data using pandas DataFrame. 

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("/Users/arshlannadeem/Desktop/covid_19_data.csv")


# In[3]:


data


# In[4]:


#1.
#df.count()
#df.isnull().sum()


# In[5]:


data.count()

#Null Values means missing values.


# In[6]:


data.isnull()


# In[7]:


data.isnull().sum()


# In[8]:


pip install seaborn


# In[9]:


#2.
#import seaborn as sns
#import matplotlib.plt as plt
#sns.heatmap(df.isnull())
#plt.show()


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


sns.heatmap(data.isnull())
plt.show()


# # Q.1)Show the number of Confirmed,Deaths and Recovered cases in each Region.

# In[12]:


#df.groupby('Region').sum().head(30)
#df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(30)
#df.groupby('Region')['Deaths'].sum()
#df.groupby('Region')['Recovered'].sum()


# In[13]:


data.head(2)


# In[14]:


data.groupby('Region').sum()


# In[15]:


data.groupby('Region').sum().head(20)


# In[16]:


data.groupby('Region')['Confirmed'].sum()


# In[17]:


data.groupby('Region')['Deaths'].sum()


# In[18]:


data.groupby('Region')['Recovered'].sum()


# # Q.2)Remove all the records where Confirmed cases is less than 10.

# In[19]:


#df.Confirmed<10
#df[df.Confirmed<10]
#df[~(df.confirmed<10)]
#df = df[~(df.confirmed<10)]


# In[20]:


data.head(2)


# In[21]:


data[data.Confirmed<10]


# In[22]:


data[~(data.Confirmed<10)]


# In[23]:


data


# In[24]:


data=data[~(data.Confirmed<10)]


# In[25]:


data.head(50)


# # Q.3)In Which Region,maximum number of Confirmed cases were recorded?

# In[26]:


#df.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(50)


# In[27]:


data.head(2)


# In[28]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False)


# In[29]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(30)


# # Q.4)In Which Region,minimum number of Death cases were recorded?

# In[30]:


#df.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50)


# In[31]:


data.head(2)


# In[32]:


data.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50)


# # Q.5)How many Confirmed,Deaths and Recovered cases were reported from India till 29 April 2020?

# In[33]:


#df[df.region=='Country_name']


# In[34]:


data.head(2)


# In[35]:


data[data.Region=='India']


# In[36]:


data[data.Region=='US']


# # Q.6-A)Sort the entire data with respect to No.of Confirmed cases in ascending order. 

# In[37]:


#df.sort_values(by=['Confirmed'],ascending=True)


# In[38]:


data.head(2)


# In[39]:


data.sort_values(by=['Confirmed'],ascending=True)


# In[40]:


data.sort_values(by=['Confirmed'],ascending=True).head(50)


# # Q.6-B)Sort the entire data with respect to No.of Confirmed cases in descending order.

# In[41]:


#df.sort_values(by=['Recovered'],ascending=False)


# In[42]:


data.sort_values(by=['Recovered'],ascending=False)


# In[43]:


data.sort_values(by=['Recovered'],ascending=False).head(50)


# 
# 
# 
# 
# 
# 
#      By - Mohd Arshlan Nadeem 
