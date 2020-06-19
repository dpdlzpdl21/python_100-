#!/usr/bin/env python
# coding: utf-8

# ### 여러개의 파일 가져오기

# In[1]:


import pandas as pd


# In[7]:


path = r'C:\Users\user\Desktop\30107\score\B.csv'


# In[8]:


path


# In[10]:


df=pd.read_csv(path, encoding='cp949')


# In[11]:


df.head()


# In[16]:


import glob 


# In[18]:


data = r'C:\Users\user\Desktop\30107\score\\'


# In[37]:


stu=[]
for file in glob.glob(data+'*.csv') :
    data_stu = pd.read_csv(file, encoding='cp949')
    stu.append(data_stu)


# In[38]:


stu


# In[ ]:


data_stu = pd.read_csv(file. encoding='cp949')
stu.append(data_stu)


# In[28]:


a=[]


# In[29]:


a


# In[30]:


[]


# In[31]:


a.append(3)


# In[32]:


a.append[10]


# In[24]:


a

