from uppercase import s1
"""
fruit='banana'
letter = (fruit[1])
print(letter)

letter = (fruit[0])
print(letter)
#methods=--------
#len- it is used to provide the total no. of characters provided in the string
length=len(fruit)
print(length)"""
#slice function=---
#the func is executed with the help of coloumn operator
#it is used to provide a substring from the string.the left side of the coloumn contains the index value from where we have to start the substring whilw the right side of the coloumn containsthe total no. of char. that we want to display in the substring
# if the left side is not given thn by default sub string will start from (o)th index.if the right side of the coloumn is not gven then it will display all the values given in the string
#string operations (+),(*),([]),([:]),(<string>),for<var> in <string>
s="compute"
print(s.capitalize())
#print(s1+ s1)
#print(s1*3)
#print(s1 *4)
print(s.upper())
print(s.lower())
print(s.title())
print(s.count('1'))
print(s.find('o'))
print(s.rfind('o'))
print(s.lstrip('o'))
print("ok")
print(s.replace('o','*'))

print(s.center(8,'*'))

print(s.rjust(8,'*'))
print(s.ljust(8,'*'))
print(s.count('o'))
print(s.find('o'))
print(s.join('o'))
print(s.replace('o','*'))
print(s.rindex('o'))
print(s.split('-1'))
#print(s.join())





