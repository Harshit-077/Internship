# Create a simple Pandas Series from a dictionary:
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}

x = pd.Series(calories)

print(x)