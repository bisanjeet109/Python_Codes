s1="hello python"
for char in s1:
    print(char)
print("end of the loop")

employee = {'empid': 1001,"name":'john','department':'hr'}
for i in employee:
    print(i)      #if u run the for loop in the dictionary itself then it will print only the keys not the whole
print(employee.items())      # it will print all
for i in employee.items():
    print(i)

