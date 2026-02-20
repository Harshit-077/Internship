# Return a new Data Frame with no empty cells:
import pandas as pd
x = pd.read_csv('data.csv')
xy = x.dropna()
print(xy.to_string())