#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


ipl=pd.read_csv('matches (1).csv')


# In[3]:


ipl.head()


# In[4]:


ipl.shape


# In[5]:


ipl['winner'].value_counts()


# In[6]:


ipl['player_of_match'].value_counts()


# In[7]:


ipl['result'].value_counts()


# In[ ]:





# In[8]:


ipl['season'].value_counts()


# In[9]:


ipl['player_of_match'].value_counts()[0:20]


# In[10]:


plt.figure(figsize=(5,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]))
plt.show()


# In[11]:


ipl['toss_winner'].value_counts()


# In[12]:


batting_first=ipl[ipl['win_by_wickets']!=0]


# In[13]:


batting_first.head()


# In[14]:


plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.show()


# In[15]:


plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:4].keys()),list(batting_first['winner'].value_counts()[0:4]),color=["red","green","black"])
plt.show()


# In[16]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[17]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[18]:


batting_second.head()


# In[19]:


plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[20]:


batting_second['winner'].value_counts()


# In[21]:


plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["blue","green","orange"])
plt.show()


# In[22]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['player_of_match'].value_counts()[0:6]),labels=list(batting_second['player_of_match'].value_counts()[0:6].keys()),autopct='%0.1f%%')
plt.show()


# In[23]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[24]:


ipl['season'].value_counts()


# In[25]:


ipl['city'].value_counts()


# In[26]:


ipl['venue'].value_counts()


# In[27]:



np.sum(ipl['toss_winner']==ipl['winner'])


# In[28]:



393/756


# In[29]:


deliveries=pd.read_csv('deliveries.csv')


# In[30]:


deliveries.head()


# In[31]:


deliveries['match_id'].unique()


# In[32]:


match_1=deliveries[deliveries['match_id']==1]


# In[33]:


match_1.head()


# In[34]:


match_1.shape


# In[35]:


srh=match_1[match_1['inning']==1]


# In[36]:


srh['batsman_runs'].value_counts()


# In[37]:


srh['dismissal_kind'].value_counts()


# In[38]:


rcb=match_1[match_1['inning']==2]


# In[39]:


rcb['batsman_runs'].value_counts()


# In[40]:


rcb['dismissal_kind'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:




