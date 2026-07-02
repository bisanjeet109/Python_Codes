#IT IS a function that called automatically with the object of  aclass.there is no need of explicit calls  of  the constructor function . usually threse functions are used to define something or to provide a welcome message while creation of the object.
#the constructor methofds in python are created with the function __init__ havoing the underscorre on the preeciding and behind level.In python all the functipns including the constructors take the default args that is--(self)

class Books:
    def __init__(self,value):
        self.books_code=value
        print("book value is:",self.books_code)
        print("we are in the books section")
    def computer(self,name):


vitlibrary=Books(title="black",author="jbjvj")
vitlibrary.books_code

vitlibrary.books_code
vitlibrary.author
vitlibrary.title



#create a class where there is constructor and user defined function both in one frame/
class Books:
    def __init__(self):
        self.books_code=[100]
    def vitlibrary(self):
        print("we are in the books section")