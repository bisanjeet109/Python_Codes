import numpy as np
"""arr=np.array([10,20,30,40,50])
print(arr)
x=arr<45
print(x)


arr=np.array([3,4,6,10,24,89,45,43,46,99,100])
print(arr)
x=arr[(arr%3==0)]
print(x)
x=arr[arr%5==0]
print(x)
y=arr[(arr%3==0) & (arr%5==0)]
print(y)

#create an array with 10 values and display the values present on even positons
#display the last 3 values
#display the values from 3 to 6 position

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[-3:])
print(arr[::2])
print(arr[3:6])
print(arr[0:11:2])


#one optional parameter that is the steps that indicates the increment of stacks in the indexing. for an ex- if we want to display the values from begining to end with the increment of 2,2 values then we should use this optional parameter
# fancy indexing is a process to provide thebpseudo index no. or the false index no. to the array values.for this we can assign a list of pseudo numbers
#to the array and these pseudo no. will work as the fancy indexing

#sorting------------
x=np.array([0,11,20,33,54,25,67,17,80,49])
a=[2,4,6]
print(x[a])
print(np.sort(x))

"""
# the numpy array gives us the facility to display the values in a group.Suppose we need the name,reg.no.and the marks for one student and to display all those things for a group of students then we need a structued array.then the structured array works like a dictionary where we are having a group of values ,assigned with a  key values

#y=np.array([('rex',9,81.0),('fido',3,27,0)]) dtype=[('name','U10'),('age','<i4'),('weight','<f4')]

#create a structured arr that have name ,regno,total marks of 5 students ,display them with fancy indexing
#z=np.array([('rex',9,81.0),('fido',3,27,0)])
#print(z)
arr=np.array( [('gudu',25,76)],[('aman',26,55)],[('name','reg no.','marks')])

