"""
a database is a group of rows and coloumns  any coloumn value can be access with the help of rows as well as any row value can be access with the help of coloumns .
The row and coloumn str is provided by multiple data structures in python.
for example,series,list,dictionary,arrays,represent a group of row and coloumns. To make them a database we should use pandas library

in pandas lib the one of the major func. is the dATA FRAME it is useed to create a database or to convert a group of values in database

"""
#a data frame is a two dimensional data str,that is, aligned in a tabular form of rows and coloummns
import pnds1 as pd
data=[1,2,3,4,5]
d1=pd.DataFrame(data)
print(d1)



