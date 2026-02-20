# Return row 0 and 1:
import pandas as pd
data = {
    "data": [1,2,3,4],
    "idx": [7,8,9,10],
}
x = pd.DataFrame(data)
print(x.loc[[0,1]])