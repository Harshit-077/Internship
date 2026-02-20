import pandas as pd
x = pd.read_csv('data.csv')
print(x.duplicated())
x.drop_duplicates(inplace=True)