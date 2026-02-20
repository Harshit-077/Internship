# Replace NULL values with the number 130:
import pandas as pd
x = pd.read_csv('data.csv')
x.fillna(130,inplace=True)
print(x)