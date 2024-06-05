import pandas as pd
import numpy as np
from numpy.random import randn
#seeding to a value so that it always returns same matrix
np.random.seed(101)

ran_mat = randn(5,4)
print(ran_mat)
#Creating a data frame using pandas
print("*"*80)
df = pd.DataFrame(data=ran_mat)
print(df)

#changing the above data frame indexing from [0,1....4] to some string labels
print("*"*80)
df = pd.DataFrame(data=ran_mat, index=('A B C D E').split())
print(df)

#changing the columns name of df
print("*"*80)
df = pd.DataFrame(data=ran_mat, index=('A B C D E').split(), columns=('W X Y Z').split())
print(df)

#adding a new column to df by referencing it and assigning

print("*"*80)
#if you want to read multiple columns then list is the input to df
print(df[['W', 'X']])
df['NEW'] = df['W'] + df['X']
print(df)

print("*"*80)
#deleting a row and column
print(df.drop('A'))  # row deletion

print("*"*80)
print(df.drop('NEW', axis=1))  # column deletion

df['new_col'] = [1,2,3,4,5]   # adding a new row
print(df)
#generating a subsection of the df
print('*'*80)
print(df.loc[['A', 'B']])  # printing rows of A, B
print(df.loc[['A', 'B'], ['Y', 'Z']])  # printing subsection Y,Z columns for A,B rows
print('*'*80)
print(df.iloc[[0,1]])
print(df.iloc[[0,1], [3,4]])