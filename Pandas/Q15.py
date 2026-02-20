# Print the first 5 rows of the DataFrame:
import pandas as pd
x = pd.read_csv('data.csv')
print(x.head())

# Print the last 5 rows of the DataFrame:
print(x.tail())

# Print information about the data:
print(x.info())