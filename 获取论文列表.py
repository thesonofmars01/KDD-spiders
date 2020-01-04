#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# In[2]:


url='https://dl.acm.org/topic/conference-collections/kdd?sortBy=downloaded&startPage=1&pageSize=100'
res = requests.get(url)
res.encoding = 'utf-8'  ##设置编码
soup = BeautifulSoup(res.text, 'html.parser')
papers = soup.select('#fitvid0 , .table-bordered a')


# In[4]:


print(soup)


# In[36]:


temp=soup.select('.issue-item__title .hlFld-Title')
print(len(temp))


# In[22]:


re_url=re.search('"/doi.*"',str(temp[0]))
print(re_url.group().strip('"'))


# In[23]:


temp_str="https://dl.acm.org"


# In[37]:


url_list=[]
for i in range(51):
    url='https://dl.acm.org/topic/conference-collections/kdd?sortBy=downloaded&startPage='+str(i)+'&pageSize=100'
    res = requests.get(url)
    res.encoding = 'utf-8'  ##设置编码
    soup = BeautifulSoup(res.text, 'html.parser')
    temp=soup.select('.issue-item__title .hlFld-Title')
    for j in range(len(temp)):
        re_url=re.search('"/doi.*">',str(temp[j]))
        dizhi=temp_str+re_url.group().strip('>').strip('"')
        url_list.append(dizhi)
print("nadaole!")
print(len(url_list))


# In[38]:


print(len(url_list))
print(url_list)


# In[41]:


pred_url_list=[]
for i,j in enumerate(url_list):
    if re.search('abs',j) is not None:
        pred_url_list.append(j)
print(len(pred_url_list))


# In[42]:


fileObject = open('kdd_url.txt', 'w')
for ip in pred_url_list:
    fileObject.write(ip)
    fileObject.write('\n')
fileObject.close()