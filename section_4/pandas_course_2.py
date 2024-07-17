import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
print('-'*45, '     START    ', '-'*35)
mat_ran = randn(5,4)
df = pd.DataFrame(data=mat_ran, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

print('.'*80)
print(df > 0)
print(df[df>0])

#adding conditional filtering to df
print('.'*80)
cond1 = df['W'] > 0
cond2 = df['Y'] > 1
print(df[ (cond1) & (cond2)])   # and/or keywords does not work in pandas bool type
print('.'*80)
print(' Condition filter, display if W col values > 0')
print(df[ df['W']>0])
print('Displaying with addtional cond:\n', df[ df['W']>0])

print('Displaying with addtional cond & row A only:\n', df[ df['W']>0].loc['A'])
print('.'*80)
#reset index and set a new column as index
new_idx = 'BG HY CH BO DL'.split()
df['Capitals'] = new_idx
print(df)
df.reset_index()
print(df)

df.set_index('Capitals', inplace=True)  # this will ensure the df is persistent
print(df)



print('-'*45, '     END    ', '-'*35)
