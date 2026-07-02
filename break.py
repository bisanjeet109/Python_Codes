"""x = 2
while True:
    is_prime = True

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print(x, end=" ")

    if x ==23:
       break
    x+= 1"""
from operator import index

l1=[2,3,"computer",4.5]
print(l1)
print(l1[-1])
#wap to contain the name of 10 fruits now display it
#fruit available on the first no.
#fruit value available on thed last no.
#fruits available on the seconfd last no.
#first 3 n
#list of first3 and last 5 fruits
#provide the index no. of the fruit mango

"""append() Adds an element at the end of the list

⚫ clear() Removes all the elements from the list

copy() Returns a copy of the list

⚫ count() Returns the number of elements with the specified value

extend() Add the elements of a list (or any iterable), to the end of the current lis

Index() Returns the index of the first element with the specified value

Insert() Adds an element at the specified position

pop() Removes the element at the specified position

⚫ remove() Removes the item with the specified value

reverse() Reverses the order of the list

sort() Sorts the list

to search

Desktop



l1=["mango","banana","apple","watermelon","grapes","cherry",]
print(l1)
print(l1[0])
print(l1[-1])
print(l1[-2])
print(l1[0:5])
print(l1[0:3])

index=l1.index("mango")
print(index)

print(l1.append("lemon"))
print(l1)

print(l1.insert(3,"guava"))
print(l1)

sort=sorted(l1)
print(sort)

print(l1.count("mango"))



print(l1.remove("banana"))
print(l1)

l1.reverse()
print(l1)

l1.remove("apple")
print(l1)

old_list=l1
newlist=l1.copy()
print(newlist)
newlist.append("brinjal")
print(newlist)
list=["pea","fig","onion"]
print(list)"""
#  defibe the list
# discuss any 5 method of the list with proper example
# displat the list elements acc. to the given index no and program rltd to the list

#
k1=("pen","pencil","4.5","carrot","raddish","bike")
print(k1)
#display the kast and the first element present in the tuple

#display first 3 element preseent in the tuple
#display 2nd to 5th element present in the tuple
print(k1[0])
print(k1[-1])
print(k1[1:4])
print(k1.count("pencil"))
k1.index("pencil")
print(k1.max)




























