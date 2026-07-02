import pnds1 as pd
"""
dropna()
drop()
deop_duplicate()
cocat()
sort_values()
fillna()
head()
tail()
nunique()
count()
describe()
groupby()
    
"""
#Creating a dataset from excel sheet------------------------------------
#my_data=pd.read_csv('book1.csv')
#print(my_data)
#print(my_data.head())
#print(my_data.tail())
"""
                read                                save
csv         pd.read_csv()                   df.to_csv()
json        pd.read_json()                  df.to_json()
excel       pd.read_excel()                 df.to_excel()
hdf         pd.read_hdf()                   df.to_hdf()
sql         pd.read_sql()                   df.to_sql()

series can hold 1 d dataset.that 1d dataset can contain heterogenous values 
creating  aa series with numpy array

"""
import numpy as np
data=np.array(['a','b','c','d'])
S=pd.Series(data)
S=pd.Series(data,index=[100,101,102,103])
print(S)
