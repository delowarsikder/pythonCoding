# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:45:07 2020

@author: DelowaR
"""
li=[1,3,4,5]
#print(li[2])
spam=[['cat','bat'],[10,20,30,45],['a',3,3.20]]
#print(spam[-2][-1])
#print(li[0:2])
#print(len(spam))
li=li+['A','a','f']
#print(li)
del li[2]
#print(li)
print('print list')
for i in  range(len(li)):
    print(li[i])

li.insert(0,6)
print('another format of print')    
for i in li:
    print(i)