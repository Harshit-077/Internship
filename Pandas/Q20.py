# Calculate the MEAN, and replace any empty values with it:
import pandas as pd
x = pd.read_csv('data.csv')
x.fillna(x['Age'].mean(),inplace=True)
print(x)