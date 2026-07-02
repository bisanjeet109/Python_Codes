"""import numpy as np
#a=np.array([12,23,34,45,56,67])
#print(a)
a2=np.array([[12,23,34],[98,87,76],[12,23,32]])
print(a2,"\n")
print(a2[-1])
upper_triangle=a2.max(axis=0)
print(upper_triangle)"""
class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        print("car is good")

s1=car("honda",1200)
print (s1.brand,s1.price)

s2=car("maruti",1300)
print(s2.brand,s2.price)


