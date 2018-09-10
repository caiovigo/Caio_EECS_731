
# coding: utf-8

# # This is Caio's notebook for Data Science EECS?

# In[1]:


import pandas as pd
import numpy as np


# ## AAII Investor Sentiment Data
# 
# Data from: https://www.quandl.com/data/AAII/AAII_SENTIMENT-AAII-Investor-Sentiment-Data
# 
# REFRESHED
# 3 days ago, on 6 Sep 2018
# FREQUENCY
# Weekly
# DESCRIPTION
# The AAII Investor Sentiment Survey measures the percentage of individual investors who are bullish, bearish, and neutral on the stock market for the next six months; individuals are polled from the ranks of the AAII membership on a weekly basis. Only one vote per member is accepted in each weekly voting period.

# In[15]:


my_data_AAII=pd.read_csv('C:/Users/Caio Laptop/OneDrive - The University of Kansas/Documents/PhD/11. Courses/19. EECS 731 - Introduction to Data Science/1.Datasets/AAII-AAII_SENTIMENT.csv')


# ## University of Michigan Consumer Survey, Index of Consumer Sentiment
# 
# Data from: https://www.quandl.com/data/UMICH/SOC1-University-of-Michigan-Consumer-Survey-Index-of-Consumer-Sentiment
# 
# 
# REFRESHED
# 2 hours ago, on 9 Sep 2018
# FREQUENCY
# Monthly
# DESCRIPTION
# Reproduced with Permission. Publisher's terms of use at www.sca.isr.umich.edu/agreement.php Data points for the most recent 6 months are unofficial; they are sourced from articles in the Wall Street Journal. The script that produces this dataset can be found at https://github.com/tammer/scrapers/blob/master/umich_consumer_sentiment.rb

# In[16]:


my_data_UMICH=pd.read_csv('C:/Users/Caio Laptop/OneDrive - The University of Kansas/Documents/PhD/11. Courses/19. EECS 731 - Introduction to Data Science/1.Datasets/UMICH-SOC1.csv')


# In[17]:


my_data_AAII


# In[18]:


my_data_UMICH


# ### Testing data

# In[31]:


my_data_AAII.loc[[0],['Bullish']]


# In[27]:


my_merged_data=pd.merge(my_data_AAII,my_data_UMICH,how='inner',on='Date')


# In[28]:


my_merged_data

