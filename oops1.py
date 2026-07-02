"""#create a class----------------
class MyClass:
    pass

#create an object---------------
obj1=MyClass()
obj2=MyClass()
#obj1,obj2 are the objects of my class

l1=[10,20,30]
print(type(l1))

print(type(obj1))
print(type(obj2))       #__main__;the underscore is called dunder
"""




"""
class Student:
  
    pass
s1=Student()
s2=Student()
#doc string----------------------------==__doc__
print(Student.__doc__)
print(help(Student))

"""




#A T T R I B U T E S----------------------------------------

class Student:
    pass
student1=Student()
student2=Student()

student1.name="gudu"
student1.roll=100

print(student1.name)
print(student1.roll)
print(student1.__dict__)