from traceback import print_tb  #sets are non-sequential collection of items


l1=[10,2.5,10,30,10]
print(l1,type(l1))                         # comma seperated elements enclosed within {}
s1={10,2.5,10,30,10}
print(s1,type(s1))                          #sets do not allow duplicate elements

nums=(1,3,5,10,0,-1)
print(0 in nums)
print(10 in nums)
print(3 not in nums)
#concatination---------
#nums1={1,3,2,0,-1}
#nums2={3,5}
#print(nums1 + nums2)              #cant do
#weekdays=("mon","tue","wed","thu","fri")
#weekdays=set(weekdays)
#print(weekdays,type(weekdays))

#are sets re mutable or immutable?

set1={2,0,-1}
print(set1)
set1.add(5)
print(set1)

#operations on set------
st1={"english","bio","science"}
st2={"english","odia","chemistry"}
st3={"sanskrit"}
print(st1)
print(st2)
common_subjects=st1.intersection(st2)#/st1&st2 also works for 2 if works for 3 sets and no common it will show empty set
print(common_subjects)
all_subjects=st1.union(st2,st3 )
print(all_subjects)
all1_subjects=st1 | st2 | st3
print(all1_subjects)



days={"mon","tue","wed","thur","fri","sat","sun"}
weekdays={"sat","sun"}

#weekends=days-weekdays
       #or
weekends=days.difference(weekdays)
print(weekdays)