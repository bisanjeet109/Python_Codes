"""when all the length of triangle is known -a,b,c
semi perimeter (s)=(a+b+c)/2
Area = square root of (s*(s-a)*(s-b)*(s-c))
"""
a=float(input("enter first number"))
b=float(input("enter second number"))
c=float(input("enter third number"))

(s)=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is",round(area,2))