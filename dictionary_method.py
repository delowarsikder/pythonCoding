'''spam={'color':'red','age':42}

#print values
print('values of dictionary :')    
for i in spam.values():
    print(i)
    
#print kye
print('kay of dictionary :')    
for i in spam.keys():
    print(i,end=' ')

print('\nall item in dictionary :')    
for i in spam.items():
    print(i)
    
#another way ,all print
print(spam.keys())     #find keys
print(spam.items())    #find item key and vaues
print(spam.values())    #find values

#extract value and key in indivisual
for k,v in spam.items():
    print('Key :',k,'Value :',v)

#check in or not
'color' in spam.keys()
'color' in spam #support for kay
'red' in spam.values() #work
'red' in spam #not support for value

#convert dictionary to list item it work only single

print(list(spam.keys()))
print(list(spam.values()))
print(list(spam.items()))
#convert dictionary to list using single element
li=list(spam.keys())

'''
#get method
