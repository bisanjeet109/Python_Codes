import copy

l1=[1,2.3,[10,20,30],'python']
print(type(l1))
#shallow copy----------------
l2=copy.copy(l1)
print(l2)
l1[0]=100 #l2 value is not chaging
l1[2][1]=50   #l2 is also changed because this is the direct element of l1 ,it is and external element of so-------
print(f"l1->{l1}",id(l1))
print(f"l2->{l2}",id(l2))

