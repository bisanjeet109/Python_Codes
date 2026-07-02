""" a function is a set of instructi0n that can perform any specific tasks.
yhere are 2 type of functions
1-library functions
2-user defined functions
the library functions are inbuilyt functions and usually displayed in lower case in python. we cxan access any of the library functiuon with the help of the member operator i.e dot(.)
example -
sysntax-:
lbraryname.function Name ()
class Name-function Name()
eg---np.array()
df.array()
python provides a facility to define a function where the user a define a specific task and use it accordinlgly,.user defined function are also known as (functions)
the useer defined function can defined any value as well as they can take many no. of argum,ents

in python a user defined func is created with the help of (f) keyword.the func can return any value with the help of return keyword
"""


"""
crerating a function
def function name(arg1,arg2):
function body
return
"""


"""
syntax for calling a function
1--function name()
2--variable=functionname()
variable ---to hold the return values
"""


def first():
    print("hello")


    #wap to input the numbers as an arguments

def add(a,b):
    a = 2
    b = 5
    c=a+b
    return c

#LAMBDA FUNCTION=-------------------------------------
"""
General functions are declared with the def keyword, give them a name, and then add the list of arguments surrounded by round parenthesis. There could be many lines of code, with as many statements and expressions inside a function.

1. Lambda functions are anonymous functions that can contain only one expression.

2. Lambda is considered as nameless function for a short period of time.

3. We can say a function with only one expression inside.

3. We can say a function with only one expression inside.

Syntax:

lambda arguments: expression

4. Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.

5. The lambda function is defined where it is used, in this way there is not a named function in memory.
6. we can return a lambda fubc from a function
"""

double= lambda x: x*2
print(double(4))

multiply= lambda x,y: x*y
print(multiply(5,5))
#wap to display 1 tp 10
#wap highest among three no.