"""
def greeting_someone(name):
    print(f"hello {name}")
    print("it is a beautiful day ")

#calling the function---(without this the output will not show)--------
greeting_someone("gudu")
#if I call the function 3 times then the output will show 3 times also------
greeting_someone("jadhu")

"""

"""                                                                        
def even_odd(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")

even_odd(5)
even_odd(12)
even_odd(23)



def add(num1, num2):
    result= num1 + num2
    print(f"return:{result}")
add(5,8)
add(-25,26)
"""
#returning values---------------------------------
"""
def even_odd(num):
    if num % 2 == 0:
        return"even number"
    else:
        return"odd number"

result=even_odd(5)
result1=even_odd(12)
print(result, )
print(result1, )
"""

"""

#example-------------
def arithmatic(num1,num2):
    add= num1 + num2
    sub= num1 - num2
    mult= num1 * num2

    return add,sub,mult

val1=int(input("enter the first number"))
val2=int(input("enter the second number"))

res1,res2,res3= arithmatic(val1 , val2)
print (f"Addition of {val1} and {val2} is {res1}")

print(f"multiplication of {val1} and {val2} is {res3}")

print(f"subtract of {val1} and {val2} is {res2}")

"""
#types of args in python----------------------------------l4
"""
def add(a,b=10):
    return a+b
result = add(10,12)
print(result)
#the non default args doesnt come after defalt args--------------
result1=add(0,b=40)
print(result1)                   """

#variablelength args-----------------------------------
def add(*args):
   print(args,type(args))

add(10,20,30,40)

#else----------------------------------
"""
def add(*args):
    return sum(args)

result=add(10,20,30,40)
print(result)   """


"""
def student(sid,s_name,*marks):
    percent=sum(marks)/len(marks)
    print(f"{s_name} with id {sid} secured {percent}%")
student(10,"jhonny", 30,40,50,60,70)             """

#another with if else-------------
def student(sid,s_name,*marks):
    if len(marks)==0:
        print(f"{s_name} is absent in all exams")
    else:
     percent=sum(marks)/len(marks)
     print(f"{s_name} with id {sid} secured {percent}%")
student(10,"jhonny", 30,40,50,60,70)
student(11,"sunny")
