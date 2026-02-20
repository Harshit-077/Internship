# Show the relationship between the columns:
import pandas as pd
x = pd.read_csv('data1.csv')
print(x.corr())