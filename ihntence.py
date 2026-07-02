
# it a property to call a functn of one class by the another clas.the class that can call the function of another class is known as child class or the sub class,while the class that provides its properties is kown as parent class or super class,
#python provides 3 types of inheritence  i.e--- single ,multilevel,multiple inheritance.
# syntax of single inheritance
"""
class BaseClass:
    body of base classs
derived class:
    body of derived class
    """
from oop import university

"""
class University:
    def school(self ):
        print("this is school of science")
class Department(University):
    def Science(self):
        print("MCA","FR,SCIENCE","CS")
        


OBJECT = Department()
OBJECT.school()
OBJECT.Science()

"""


class University:
    def __init__(self):
        self.university = University()
        print("this is school of science")


class Department(University):
    def __init__(self):
        self.Department = Department()
        super(University).__init__()
        print("MCA", "FR,SCIENCE", "CS")



obj=Department()


"""
syntax of multiple inheritance

class Baseclasss-1:
     body of base class
class baseclass-2:
     body of base class
class baseclass-3:
     body of base class
class derivedclass(baseclass-1,baseclass-2,baseclass-3):
      body of derived class


"""

class computers:
    def java(self):
        print("this is java of computers")
class ems:
    def statics(comp,cms,ems):
        print(comp,cms,ems)
class student:
    def degree(self):
        print("this is student of degree")
obj=student()
obj.degree()
obj.statics()
obj.java()


# hi rarchical=--------------
#create a class university having function exam conduction,the admission office must provide reg no. to every admitted student. the exam function muszt provide the exam dates amnd responsible fror degree distribution
#theree are various colleges affilated by the university.college bun provideds only the sign subject i.e phy,chem,bot,zool, for the admitted wstudents .the another afilated student of the same unoversity provides admisssion in arts subject like hindi,eng,geo,hist.
# create a python prog that allows the adddmisiion of the student acc to the choice of affilatwed colleges 







