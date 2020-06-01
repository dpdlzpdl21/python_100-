#!/usr/bin/env python
# coding: utf-8

# for_list_format

# In[1]:


num = [1,2,3,4,5]
print(num)


# In[4]:


type(num)


# In[10]:


for  i in num:
    print('%d번'%i,   end = ' ')


# In[13]:


i=1
if i==0:
   print('i는 0이다.')
else:
   print('i는 0이 아니다')


# In[14]:


i=1
if i%2==0 :
   print('i는 짝수이다.')
else:
   print('i는 홀수이다')


# In[18]:


i = int(input('숫자입력>>> '))
if i%2==0 :
   print('i는 0이다.')
else:
   print('i는 0이 아니다')


# In[35]:


sub = ['국', '영', '수', '정보']
for i, s in enumerate(sub):
    print(sub[i], end=' ')


# In[ ]:





# In[36]:


sub = ['국', '영', '수', '정보']
for i, s in enumerate(sub):
    if sub[i] == '정보' :
        print(i+1,'교시', sub[i], '합격')
    else:
        print(i+1,'교시', sub[i], '해당없음')


# In[39]:


for i in range(1,11) :
    if i % 2==0 :
        print('파이썬')
    else :
        print('야~ 나도 파이썬 할 수 있어')


# ## List 활용

# In[43]:


juso  = '    인천광역시 중구 참외전로 116 창의관'
juso, type(juso), len(juso)


# In[46]:


juso=juso.strip()


# In[47]:


juso, len(juso)


# In[48]:


addr=juso.split()


# In[49]:


addr, len(addr), type(addr)


# In[50]:


addr[:2], addr[3:]


# In[51]:


juso.startswith('인천')


# In[52]:


juso.endswith('동')


# In[53]:


'인천광역시' in addr


# In[54]:


'인천' in juso


# In[86]:


info_1 = '학교: {}, 학번:{}, 이름:{}'
pr = info_1.format('인천정보',30107, '박준아')
print(pr)


# ### [문제1] 30부터 50까지 중에서 홀수만 출력

# In[5]:


for i in range(30,50):
    if i%2 !=0 :
        print(i)


# ### [문제2] 아이디(문자)를 입력받아 동일하면 회원 아니면 회원가입하세요.
# 

# In[6]:


id = input('아이디 입력')
if id == 'imddyd' :
    print('안녕하세요 회원님')
else :
    print('회원가입하세요.')


# ### [문제3] 

# In[ ]:


stu=list(map(str, input('내용 입력>>>').split('/')))


# In[16]:


print('학교명',stu[0])
print('학번',stu[1])
print('이름',stu[2])


# ### [문제4] 숫자 데이터 5개를 입력받아
# - 합계
# - 평균

# In[10]:


num =list(map(int,input('숫자 5개 입력: ').split(' ')))
print('합계: ',sum(num))
print('평균: ',(sum(num)/len(num)))

