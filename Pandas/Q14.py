# Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd
x = pd.read_csv('data.csv')
print(x.head(10))