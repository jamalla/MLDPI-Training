#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[14]:


myreduc = 1
for i in range(1, 6):
    myreduc = myreduc * i
    
print(myreduc)


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[18]:


mylist = [1, 2, 3, 4, 5, 6, 7]
myfilter = 5

for i in mylist:
    if(i == myfilter):
        print("Found")
        break
else:
    print("Itmen Not Found")


# 2.Implement List comprehensions to produce the following lists. 
# Write List comprehensions to produce the following Lists

# In[19]:


# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 


# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


# In[20]:


word = 'ACADGILD'
mylist = [char for char in word]
mylist


# In[21]:


# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']


# In[35]:


original_list = ['x','y','z']
mylist = [ (i*j) for i in original_list for j in range(1,5)]
mylist


# In[36]:


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 


# In[54]:


original_list = [2, 3, 4]
mylist = [ [i+j] for i in original_list for j in range(0,3)]
mylist


# In[55]:


# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]


# In[61]:


original_list = [2, 3, 4, 5]
mylist = [ [i+j for i in original_list] for j in range(0,4)]
mylist

