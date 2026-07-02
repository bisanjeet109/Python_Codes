"""oop is a concept for write once and use multiple times of a program , with the help of oop we use a large amount of code at multiple places,multiple times,in multiple peices and
with a desired value of arguments.
The oop alows us to create aclasses and use those classes with the help of objects .
A class is a group of variables and functions that provides the str or a blueprint or a template for the object.The objects are instance of a class
: A class is created with the help of class keyword.a class can contain global and local variables and methods .multiple methods can be present inside a class .
: A class is executed with the help of objects .objects are the example of a class.
: A single class may have multiple objects but a single object must belongs to one class only.
: AN object has the capacity to call the function and variables present in the class.
: IT is not necessary for an object to call all the methods of a clasS.


----------------------------- CHARACTERSTICS OF OOPS PROGRAMMING------------------------
Abstraction-----
It is a property that makes a class or a method to be extract from others.i.e- the class or the methods cant be disturbed by any other class or a method.
The abstraction allows the class and the method to standalone and the secure mode.
ENcapsulation-------------
It is a property used to hide and bind the variaBALES and the methods inside a class
in this property the class can work like a rapper for the variables and the mwthod.
Using it the method of one class become a property.for that class and  to use those method we need the class name.
Polymerphism----------------------
It is a property that allows the method to be used in multiple formats .
acc to this property multiple methods can be created with the same name but this methods are diff by the followings--
1>No of args.
2>  Datatypes of args.
3> Datatype of return value.
Inheritance----------------------------------
It is a property to call the functions and the variables of one class by another class.The ANOTHER CLASS MUST BE A SUB CLASS or a child class for that super class or the parent class.
The class that allows to make use of its properties is considered as super class or the psrent clsss.
The class that is calling or using the properties of super class is known as sub class or the child class.
A single class may have multipe subclasses and those subclasses can use or recreate the methods of super class

METHOD OVERRIDING-------------------------------------------------------------------------------

The child classes can be called with the object of child class itself
A child class can create a method or a variable with a new defination just like the parent class.while executing the child class method
the parent class will not get priority and the methods of parent classs can overide by the child class this property is known as method OVERRIDING

REFER TO GOOGLE FOR THE DIAGRAMS AND THE LAYOUT

constructer----------------------
it is a self defined func that can be called automatically with the class object,usually a constructor is used to defibned the global parameters


"""


def faculty_name():
    pass


class University:
    def __init__(self,department,faculty,clubs,hostels):
        self.department=department
        self.faculty=faculty
        self.__clubs=clubs
        self.hostels=hostels

    def get_clubs(self):
        return self.__clubs                           # used to recover or read the encapsulated docs


    def college_details(self):
        print(f"the college which have {self.hostels} is the best")



nit=University("cs","ajeet","gfg","h1")
#print(f"the dept is{nit.department},faculty name is{nit.faculty},clubs present here are{nit.__clubs},best hostel is{nit.hostels}")
IITD=University("mech","aman","dance","h4")
#print(f"the dept is{IITD.department},faculty name is{IITD.faculty},clubs present here are{IITD.__clubs},best hostel is{IITD.hostels}")


nit.college_details()
IITD.college_details()
#print(nit_w.__clubs)
print(nit.get_clubs())                              #encapsulation




