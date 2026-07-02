#comma seperated key value pairs enclosed within{}
#{'key1':value,'key2':value}
"""groceries={'milk':60,'biscuits':20,'rice':90,'bread':30}
print(groceries)
#print(type(groceries))
#print(len(groceries))

#dictionaries are mutable--------------------------------------if we can change the value then that is called mutable
groceries['milk']=100
print(groceries)

groceries['wheat']=76
print(groceries)  """                 #dictionaries can be modified
                                  #wwe can add new key to the dictionary

 #LECTURE 2------------------------
student1={'maths':80.5,'eng':54,'phy':66}
#fetch the marks for phy?
#ans---
print(student1['phy'])
print(student1.get('phy'))                  #bothv are the methods tfo fetch
#get()
print(student1.get('chem'))              # uwill get none here
#add
print(student1.get('chem','40'))

#membership operator------(=>)
print('eng' in student1)                   #the membership operator doesnt look for the value ,it look for the key

student2={"maths":55,"phy":34,"bio":93,"sst":77}
student1.update(student2)

print(student1)
student1.pop("eng")
print(student1)