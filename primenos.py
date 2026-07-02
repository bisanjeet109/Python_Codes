a=int(input("Enter a number: "))
print(a)
#f=0
for i in range(2,a  ):
 if(a%i==0):
    #f+=1
#if(f>0):
    print("The number is",a," not prime")
else:
     print("The number is",a," prime")
