# Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd
x = pd.read_csv('data.csv')
x.fillna({"Age": 130}, inplace=True)
print(x)