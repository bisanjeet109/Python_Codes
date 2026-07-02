"""name="john"
age=22
percent=85.5

student=["john,22,85.5"]
print(type(student))
print(student)
days_of_week=["mon","tue","wed","thur","fri","sat","sun"]
print(days_of_week[0])
print(days_of_week[4])
print(f"last day of week is {days_of_week[6]}")

# Length of a list => the number of items/elements in the list
print(len(days_of_week))
print(f"last day of week is {days_of_week[-1]}")
print(days_of_week[8])   #canoot be done error will occur



# list slicing --------
l1=[3,8,1,0,4,9,7,3,6]
print(l1[1:6:1])
print(l1[2:7:2])


#concatenation in lists---------
l1=[1,7,2]
l2=[0,5]
print(l1+l2)
print(l2+l1)



# Repetition of lists  (*) operator is used
l1=[1,7,2]
l2=[0,5]
print(l1*3)       # repeting 3 times




#append()
#adds an item to the end of the list
# DIFF BETWEEN STRING AND LISTS:
# in strings it creates a new string or replace a string and gives the output    but    in list where the append function is used it only modifies and dont give the output
fruits=["mango","apple","banana"]
print (fruits)
fruits.append("orange")
print (fruits)              # we have to write the print fnctn again



# if i want something to be added in the middle we have to use (insert)
# adds an element before the specified index
#syntax:list.insert(index,item
fruits.insert(3,"watermelon")
print (fruits)



#extend()
#remove()
#pop()

#extend--------------------
#fruits=["apple","mango","banana"]
#fruits.append("orange","grapes")   #it gives error coz append ony add 1 more element thats why we use extend function
#print(fruits)o"]


fruits=["apple","mango","banana"]
fruits.extend(["orange","grapes"])   #brackets are impportant here  it shows the list[]  if i add all using append with braces onn then it will show as one element bcoz it takes the list as one
print(fruits)                          # if [] is used and append also then it add the whole list as one element in the present list
print(len(fruits))    #it shows 4 with append and with extend it shows 5




#remove function
fruits.remove("orange")
print(fruits)


#pop()---------
fruits.pop(2)
print(fruits)   #it is used to remove the element from any place
fruits.pop()        # if there is no index inside the brackets then the last element got deleted
print(fruits)


days_of_week=["mon","tue","wed","thur","fri","sat","sun"]
print(days_of_week)

#Reverse-----------
days_of_week.reverse()
print(days_of_week)



#Sort-----------
nums=[4,9,8,1,2,8]
nums.sort()
print("sorted list:",nums)

# in using reverse-----
nums=[4,9,8,1,2,8]
nums.sort(reverse=True)
print("Reverse sorted list:",nums)



#count()--------------
numbers=[0,1,3,4,1,2,2,4,4,4,5,6,6,7,8,8,8,8,8,9]
print(numbers.count(8))

#dynamically make by doing-----
numbers=[0,1,3,4,1,2,2,4,4,4,5,6,6,7,8,8,8,8,8,9]
print(f"the list is:{numbers}")
item_to_count=int(input("enter the number to be counted:"))
c=numbers.count(item_to_count)
print(f"occurance of {item_to_count} is {c}")


#membership operator (in)-----------------------
language=["python","java","c++","python"]
print("python"in language)

language=["python","java","c++","python"]
print("sql"in language)

# for reverse use {not} in instead of {in}





# NUMERICAL OPERATIONS------------
#MIN()------  {SMALLEST NUMBER IN THE LIST}
numbers=[10,4,5.5,7,1]
print(min(numbers))

#biggest number in the list
#max()----
print(f"biggest number: {max(numbers)}")

#total
#sum()-----
print(f"total: {sum(numbers)}")

                                       """

#LIST INSIDE LIST {NESTED LIST}---------------
l1=[5,1.5,"python", True, None,[1,2,3]]
#print(len(l1))
print(l1[-1][2])     # to find list inside list and find elements inside the list inside list it is used
l2=[[1,2], [3,4], [5,6,[0,1]]]
print(len(l2))
print(l2[-1][-1][1])












