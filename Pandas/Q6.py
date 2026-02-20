# Create a Series using only data from "day1" and "day2":
import pandas as pd
data = {"day1": 420, "day2": 380, "day3": 390}
x = pd.Series(data, index = ["day1", "day2"])

print(x)