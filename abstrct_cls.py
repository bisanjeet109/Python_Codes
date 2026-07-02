#abstract class----------------------------------
from abc import ABC, abstractmethod

# Abstract Class
class University(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def courses(self):
        pass

    @abstractmethod
    def fees(self):
        pass



class vit(University):

    def courses(self):
        return "B.Tech, M.Tech"

    def fees(self):
        return 150000


# Child Class 2
class MedicalCollege(University):

    def courses(self):
        return "MBBS, MD"

    def fees(self):
        return 300000


# Usage
eng = vit("ABC Engineering College")
med = MedicalCollege("XYZ Medical College")

print("Engineering College:", eng.name)
print("Courses:", eng.courses())
print("Fees:", eng.fees())

print("\nMedical College:", med.name)
print("Courses:", med.courses())
print("Fees:", med.fees())
