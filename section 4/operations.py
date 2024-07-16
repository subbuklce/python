import pandas as pd 
import numpy as np

np.random.seed(101)

my_mat = np.random.randn(5,4)
print('my_mat is:\n', my_mat)

df = pd.DataFrame(data=my_mat, columns=['W', 'X', 'Y', 'Z'])
print('data frame is:\n', df)

#the list of operations 
"""

df['col_name'].unique() - Prints all unique values from that license
df['col_name'].nunique() - prints number of unique values
df['col_name'].value_counts() - how many times each value appeared in that column

"""
def multiply_two(number):
    return 2 * number

df['New']=df['Z'].apply(multiply_two)
print("After applying the function on each element of column\n",
      df)
print("all collumns\n", df.columns)
print("Only rows:\n", df.index)
print("complete info:\n", df.describe())
print("known info\n", df.info())
print("*"*45 ,"  END ", "*"*25)

