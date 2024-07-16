import pandas as pd

#df = pd.read_csv('/Users/subrahmanyamgundimeda/Documents/PytorchDeepLearning/PYTORCH_NOTEBOOKS/00-Crash-Course-Topics/01-Crash-Course-Pandas')
df = pd.read_csv('./data/example.csv')
print(df)
df = pd.read_csv('./data/bank.csv')
print("bank data is:\n", df)
print("\n num of rows:\t", len(df['age']))

print("Printing first five rows of data set")

print(df[:5])

print("\n mean avg of age is:\t", df['age'].mean())
llist = df['age'].sort_values()
print("llist top values are:\n", llist[:2])
print("llist indexes of those two rows are:\n", llist[:2].index)
idx = llist[:1].index   # returns the index of first row
print("llist data is:: \n", llist.loc[idx])
print("youngest person marital status is {0} , age is {1}, index is {2}\n", df.loc[idx]['marital'], df.loc[idx]['age'], idx)
#print("\n youngest person age is:\n", df.loc[19]['marital'])