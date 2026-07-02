"""
1-write a python program to create a class(university)
  the class should have following functions
  a-library()
  b-exam()
  c-placement()

  the library function should ask for issue or deposite of the books.it must include the issue date and the return date .if the return date is
  more than 15 days of issue date,then there will be a fine of 0 for rupees for each extended day

2-the exam function should ask for the sem,class and the registration number and then display the exam schedule [class catagories are ug,pg,ARCHIT]

3-the placement() should ask for registration no. and cgpa and should display the details  of the upcomming training schedule acccording to your cgpa [cgpa catagories are [8,9,10]]


"""

"""
#1st questian----------

class University:
    def library (self):
        print("library section")
        choice=input("do you want to deposite or issue a book?")
        if choice=="yes":
            issue_date=int(input("enter issue date"))
            return_date=int(input("enter return date"))
            days_diff=(int(return_date - issue_date).days)
            print(days_diff)
        if days_diff<15:
            print("no fine ! ")
        else:
            print("fine of rs 100500")

    def exam (self):
        print("exam section")
        choice=input("do you want to take exam?")
        if choice=="yes":
            print("you will take exam")
        else:
            print("you will not take exam")

    def placement (self):
        print("placement section")
        choice=input("do you want to take placement?")
        if choice=="yes":
            print("you will take placement")
        else:
            print("you will not take placement")

University=University()
University.library()
University.exam()
University.placement()"""



"""
for A library function a list of 10 books is available . each of these books are having 5 copies. A singkle book can be issued by 5 members at a time, if any other user wants to issue the same book then it should reflect the message the book will be availabble on the retun date.
this return date must be caluculated as the 15 dat after the issue date 

"""

"""
the university class should contain 3 more functions all the 3 functions should have a same name fees collection.the functions are seperated with their arguments
1-one function should take reg no,password to display the balance of fees amount
2-2nd one should take name and dob to display the balance of fees amount
3-the 3rd fnctn must take name ,reg no and dob to display the same


"""

class library:
    def Book(self,):
        print("book section")
        choice=input("do you want to take a book?")
        if choice=="yes":
            print("you will take book")
        else:
            print("you will not take book")
library=library()
library.Book()

#C O N S T R U C T O R S-------------------------------------------------




