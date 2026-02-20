# Calculate the MODE, and replace any empty values with it:
import pandas as pd
x = pd.read_csv('data.csv')
x.fillna(x['Age'].mode(),inplace=True)
print(x)