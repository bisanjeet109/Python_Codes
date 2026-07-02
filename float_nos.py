"""num1 =float(input("Enter first number: "))
num2 =float(input("enter second number: "))

result1 = num1+num2
print(result1)                                       

result2 = num1-num2
print(result2)
result3 = num1*num2
print(result3)
result4 = num1/num2
print(result4)

"""
#check prime nos or not-----------------

"""num=int(input("enter number: "))
if num==1:
   print("it is not prime")
if num>1:
   for i in range (2,num):
     if num%2==0:
      print("not prime")
      break

     else:
      print("prime")"""


#print prime nos-----------------------
lower=int(input("enter lower limit: "))
upper=int(input("enter upper limit: "))
if lower>1:
    for i in range (lower,upper+1):
        #if i>1:
            for num in range(2,i):
                if i%num==0:
                    print("not prime")
                else:
                    print("prime")

            else:
                print(i)

#1----------------
#for i in range(1,10+1):
 #   print(i)



