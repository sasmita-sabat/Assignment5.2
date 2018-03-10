
# coding: utf-8

# In[105]:


#Generate sentences with the words in the list.
#Implement a Python program to generate all sentences where subject is in
#["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
#["Baseball","cricket"].

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            s=i+" "+j+" "+k
            print(s)

