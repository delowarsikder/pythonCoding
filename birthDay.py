birthDays={'Alice':'Apr 1','Bob':'Dec 12'}
while True:
    print('Enter name :(blank to quit) ')
    name=input()
    if name=='':
        break
    if name in birthDays: #check just key value
        print(birthDays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+name)
        print('What is their birthday ?')
        bday=input()
        birthDays[name]=bday
        print('Birthday database update successfully.')
