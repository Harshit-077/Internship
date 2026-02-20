# Remove all rows with NULL values:
import pandas as pd
x = pd.read_csv('data.csv')
x.dropna(inplace=True)
print(x.to_string())