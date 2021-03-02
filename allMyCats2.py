# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:18:49 2020
@author: DelowaR
"""

catName=[]
catNameApp=[]
while True:
    print('Enter the name of cat ' +str(len(catName)+1) +'(or Enter nothing to stop.):')
    name=input()
    if name=='':
        break
    catName=catName+[name] #list concatenation
    catNameApp.append(name)
print ('The cats name are catName list:')
for i in catName:
    print(i,sep=',')
    
print ('The cats name are catNameApp list:')
for i in range(len(catNameApp)):
    print(catNameApp[i],sep=',')

print(type(catName[0]))    
    
    