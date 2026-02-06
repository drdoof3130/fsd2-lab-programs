#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Attribute Selection


# In[1]:


import pandas as pd
import numpy as np

# Create dataset
df = pd.DataFrame({
    "Age": [25, 30, np.nan, 45, 28],
    "Income": [50000, np.nan, 60000, 120000, 52000],
    "Experience": [2, 5, 7, 30, 3]
})

print("Original Dataset")
print(df)


# In[ ]:


#Attribute Selection


# In[2]:


df_selected = df[["Age", "Income", "Experience"]]


# In[ ]:


#Handling Missing Values


# In[3]:


df_selected["Age"].fillna(df_selected["Age"].mean(), inplace=True)
df_selected["Income"].fillna(df_selected["Income"].mean(), inplace=True)

print("After Handling Missing Values")
print(df_selected)


# In[ ]:


#Discretization


# In[4]:


bins = [20, 30, 40, 50]
labels = ["Young", "Middle", "Senior"]

df_selected["Age_Group"] = pd.cut(df_selected["Age"], bins=bins, labels=labels)

df_selected


# In[ ]:


#Outlier Elimination (IQR Method)


# In[5]:


Q1 = df_selected["Income"].quantile(0.25)
Q3 = df_selected["Income"].quantile(0.75)

IQR = Q3 - Q1

df_no_outliers = df_selected[
    (df_selected["Income"] >= Q1 - 1.5 * IQR) &
    (df_selected["Income"] <= Q3 + 1.5 * IQR)
]

df_no_outliers


# In[ ]:




