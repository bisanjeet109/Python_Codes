"""s1="hello world"
print(s1)
print(len(s1))
print("first char",s1[0])
print("last char",s1[-1])

basic stuffs .......
syntax of indexing:string [index]

syntax of slicing: string [start:end:step]

start : starting index at which the slicing starts
end: ending index at which the slicing ends(excluded)
step: integer that specifies the step for the slicing


----in the end index dont take the last one the final element----
"""

s1="hello world"
print(s1[2:10:2])


print(s1[1:22:1])
#here if the end index is more than the total no. of letters
#it ALways takes the last letter if it falls,acc to the steps or the gaps, more then one from the last index,and if the total is 10 and we put 10 then it always show -1 from the final index
#another exampple-----
print(s1[1:14:4])












