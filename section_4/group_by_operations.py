import pandas as pd
import numpy as np
from numpy.random import randn

print('-'*45, '     START    ', '-'*35)
grp_by = {'Company':['Facebook', 'Google', 'Microsoft','Facebook', 'Google', 'Microsoft' ],
          'Sales':[210,150,23,110,54,32]}
df = pd.DataFrame(data=grp_by)
print(df)
print('.'*80)

print('list of all functions in it', df.describe())

print('grouping a column - Company:\n', df.groupby('Company').sum() )

print('Transpose of that matrix for clarity:\n', df.groupby('Company').sum().transpose())




# the below code shows that string concatenation happens if we perfrom
# sum operation.
grp_by = {'Company':['Facebook', 'Google', 'Microsoft','Facebook', 'Google', 'Microsoft' ],
          'Sales':['210','150','23','110','54','32']}
df = pd.DataFrame(data=grp_by)
print('grouping a column - Company:\n', df.groupby('Company').sum() )


print('-'*45, '     END    ', '-'*35)