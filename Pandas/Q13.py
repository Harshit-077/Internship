# Load the JSON file into a DataFrame:
import pandas as pd
x = pd.read_json('data.json')
print(x.to_string())