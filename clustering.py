
# coding: utf-8

# In[1]:

import pandas as pd
df = pd.read_csv('file.csv')
from sklearn.cluster import KMeans


# In[2]:


df = df[['MemberId', 'ProductId', 'Quantity']]
df = df.drop_duplicates(['MemberId', 'ProductId'])
df = df.pivot(index='MemberId', columns='ProductId', values='Quantity').fillna(0)


# In[3]:

df.head(10)


# In[4]:

km = KMeans(init='k-means++',n_clusters=5,random_state=0).fit(df)


# In[5]:

print km.labels_


# In[6]:

df['labels'] = km.labels_


# In[7]:

class0 = df[df["labels"]==0]
class1 = df[df["labels"]==1]
class2 = df[df["labels"]==2]
class3 = df[df["labels"]==3]
class4 = df[df["labels"]==4]
print 'density of 1st cluster', len(class0)
print 'density of 2nd cluster', len(class1)
print 'density of 3rd cluster', len(class2)
print 'density of 4th cluster', len(class3)
print 'density of 5th cluster', len(class3)




# In[21]:

class0.to_csv('firstSegment.csv')
class4.to_csv('lastSegment.csv')


# In[33]:

print class0.shape
x= class0.sum(axis=0)
print x.head(5)

cluster_zero = {}
for i, row in enumerate(x.values):
    ind = x.index[i]
    if row!=0:
        cluster_zero[ind] = row
#print cluster_zero

l = sorted(cluster_zero, key=cluster_zero.__getitem__, reverse=True)
print l[:5]
#pd.DataFrame({'index':x.in})


# In[34]:


x= class1.sum(axis=0)
print x.head(5)

cluster_one = {}
for i, row in enumerate(x.values):
    ind = x.index[i]
    if row!=0:
        cluster_one[ind] = row
#print cluster_zero


l = sorted(cluster_one, key=cluster_one.__getitem__, reverse=True)
print l[:5]
#pd.DataFrame({'index':x.in})


# In[31]:

print class2.shape
x= class2.sum(axis=0)
print x.head(5)

cluster_two = {}
for i, row in enumerate(x.values):
    ind = x.index[i]
    if row!=0:
        cluster_two[ind] = row
#print cluster_zero

l = sorted(cluster_two, key=cluster_two.__getitem__, reverse=True)
print l[:5]


# In[ ]:

print class3.shape
x= class3.sum(axis=0)
print x.head(5)

cluster_three = {}
for i, row in enumerate(x.values):
    ind = x.index[i]
    if row!=0:
        cluster_three[ind] = row
#print cluster_zero

l = sorted(cluster_three, key=cluster_three.__getitem__, reverse=True)
print l[:5]


print class4.shape
x= class4.sum(axis=0)
print x.head(5)

cluster_four = {}
for i, row in enumerate(x.values):
    ind = x.index[i]
    if row!=0:
        cluster_three[ind] = row
#print cluster_zero

l = sorted(cluster_four, key=cluster_four.__getitem__, reverse=True)
print l[:5]



