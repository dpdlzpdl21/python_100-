#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=['kor', 'eng', 'math']
b=[30,100,-80]


# In[9]:


import matplotlib.pyplot as plt


# In[11]:


plt.bar(a, b)


# In[13]:


plt.plot(a,b)


# In[14]:


plt.barh(a, b)
plt.ylabel('subject')


# In[15]:


plt.barh(a, b)
plt.ylabel('subject')
plt.xlabel('score')


# In[19]:


plt.barh(a, b,color='red')
plt.ylabel('subject')
plt.xlabel('score')
plt.title('Level')


# In[34]:


plt.plot(a, b,'--')
plt.plot([1,2,3,4,5],[88,50,70,100,90],'o')
t = np.arange(0., 5., 0.2)
plt.xlabel('X name')
plt.ylabel('Y Value')
plt.title('Test')
plt.legend(['A','B'])
plt.show()


# In[27]:


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# In[30]:


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# In[4]:


a


# In[5]:


b


# In[41]:


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('점수들')


# In[46]:


import matplotlib.font_manager as fm
font_list = fm.findSystemFonts()
font_list
from matplotlib import rc


# In[47]:


'GyeonggiTitle'


# In[52]:


rc('font',family='gulim')


# In[53]:


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('계좌')
plt.xlabel('은행명')


# In[ ]:




