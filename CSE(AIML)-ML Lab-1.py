#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from statistics import mode

# Dataset
data = np.array([10, 12, 15, 18, 20, 20, 25])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
mode_value = mode(data)

# Variance
variance = np.var(data)

# Standard Deviation
std_dev = np.std(data)

mean, median, mode_value, variance, std_dev


# In[ ]:




