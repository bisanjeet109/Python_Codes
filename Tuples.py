#Tuple  #datatype
#(item1,item2,.........)
#sequence of items as a collection
"""
t1=("python",10,1.5,True,[1,2,4],[10,20])
print(len(t1))
print(t1[0])
print(t1[-1])
print(type(t1))


#concatenation, repetition,membership=======================
#count,index
# min,max,sum

#concatenation-----------
student_detail1=(1001,"john")
student_detail2=(78.5,91.0,83.5,79.5)
student_details=student_detail1+student_detail2
print(student_details)

#* ------
t1=("class 5",5000)
print(t1*3)

"""

student_detail1=(1001,"john")
student_detail2=(78.5,91.0,83.5,79.5)
# in , not in
print(91.0 in student_detail2)
print(99.0 in student_detail2)

# not in -------
print(91.0 not in student_detail2)
print(99.0 not in student_detail2)

# we cant add or remove an element from a tupple but we can do some read operations on tuple

#count-------------------
t1=(10,4,1,9,0,3,1)
#tuple.index(element)
print(t1.index(0))   #what is the index of item 4 in t1 tuple?

#min(tuple)
#max(tuple)
#sum(tuple)------------

print(f"smallest number:{min(t1)}")
print(f"biggest number:{max(t1)}")
print(f"total:{sum(t1)}")
