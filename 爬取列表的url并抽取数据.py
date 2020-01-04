#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import json


# In[59]:


url_list=[]
with open('kdd_url.txt','r')as f:
    for line in f:
        url_list.append(line.strip('\n'))
print(len(url_list))


# In[72]:


dict_list=[]
for url in url_list:
#for i in range(1198,1906):
    print(i)
    url=url_list[i]
    res = requests.get(url)
    res.encoding = 'utf-8'  ##设置编码
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)
    dict={}

    temp=soup.select(".border-bottom.clearfix .citation__title")
    title=re.search('>.*<',str(temp))
    if title is not None:
        title=title.group().strip('>').strip('<')
    else:
        title=""
    #print(title)
    dict['title']=title
    #print(dict)

    temp=soup.select(".border-bottom.clearfix .epub-section__date")
    #print(temp)
    year=re.search('[0-9]+',str(temp))
    if year is not None:
        year=int(year.group().strip('>').strip('<'))
    else:
        year=-1#未读到
    #print(year)
    dict['year']=year
    #print(dict)

    temp=soup.select(".hlFld-Abstract p")
    #print(temp)
    abstract=re.search('>.*<',str(temp))
    if abstract is not None:
        abstract=abstract.group().strip('>').strip('<')
    else:
        abstract=''
    #print(abstract)
    dict['abstract']=abstract
    #print(dict)

    temp=soup.select(".badge-type")
    #print(temp)
    keyword=[]
    for i,j in enumerate(temp):
        tmp=re.search("title=\".*\"",str(j))
        if tmp is not None:
            tmp=tmp.group().strip("title=\"").strip("\"")
        else:
            tmp=''
        keyword.append(tmp)
    #print(keyword)
    dict['keywords']=keyword
    #print(dict)

    temp1=soup.select(".auth-info a")
    temp2=soup.select(".auth-info .info--text")
    authors=[]
    dict['authors']=authors
    for i in range(len(temp1)):
        author_dict={}
        name=temp1[i]
        org=temp2[i]
        name=re.search(">.*<",str(name))
        if name is not None:
            name=name.group().strip('<').strip('>')
        else:
            name=''
        org=re.search("\n.*\n",str(org))
        if org is not None:
            org=org.group().strip('\n').strip('\r').strip(' ')
        else:
            org=''
        author_dict['name']=name
        author_dict['organization']=org
        authors.append(author_dict)

    dict_list.append(dict)


# In[73]:


print(len(dict_list))


# In[74]:


print(dict_list[-1])


# In[75]:


for item in dict_list:
    authors=item['authors']
    for author in authors:
        tmp=[]
        tmp.append(author['organization'])
        author['organization']=tmp


# In[76]:


print(dict_list[0])


# In[77]:


print(dict_list[-1])


# In[79]:


with open("KDD_result.txt","w")as f:
    for item in dict_list:
        json_str=json.dumps(item)
        f.write(json_str+'\n')


# In[ ]:




