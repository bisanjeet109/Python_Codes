#mutability & imutability
#lists are mutable
#tuples and strings are immutable

s1="python is fun"
s1.replace("python","java")
print(s1)
s2=s1.replace("python","java")      #it creates a new string not in the same string
print(s2)


l1=["mango" , "orange" , "banana"]
l1.append("apple")
print(l1)            #it works because list are mutable


#to know the memory address we use the id function
l1=["mango" , "orange" , "banana"]
print(id(l1))
l1.append("apple")
print(l1)
print(id(l1))                   #it is done to prove the list are mutable


l1=["mango" , "orange" , "bana"]
print(l1)
l1[-1]="banana"
print(l1)   #mutability
#tuples and lists cannot do this
