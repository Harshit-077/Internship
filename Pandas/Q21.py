# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd
x = pd.read_csv('data.csv')
x.fillna(x['Age'].median(),inplace=True)
print(x)