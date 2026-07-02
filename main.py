print("hello world")

a=[[1,2,3],
   [3,4,5],
   [4,5,6]]
b=[[5,6,7,2],
   [7,8,9,3],
   [6,7,8,9]]


result=[[0,0,0,0], [0,0,0,0],[0,0,0,0]]
for i in range(3):
    for j in range(4):
        for k in range(3):
         result[i][j]+=a[i][k]*b[k][j]
for i in result:
         print(i)

