"""a set contains a unique grp of values .
It doesnt store duplicate values in the
group
ususaaly displays values in sorted order only in same datatype
a set is declared with curly brackets

numbers always get top
set is a mutable datatype

"""
s1={1,2,2,4,5,6,7,8,9}
print(s1)
#s2={5,6,"true",8,"pen",9,1.2,}
#print(s2)
s1.remove(8)
print(s1)

s1.add(11)
print(s1)
s2={"eng","hindi","math","science"}
print(s2)
s2.remove("eng")
print(s2)
common_subjects= s1.intersection(s2)
print(common_subjects)


#2 discuss the methods supported by sets
#3 what are the characterstics of the sets.