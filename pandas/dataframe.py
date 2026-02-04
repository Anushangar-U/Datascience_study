import pandas as pd
import numpy as np

data = {"Name":["spongebob","patrick","squidward"],
        "age":[20,21,22]
        }
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['emp1','emp2','emp3'])
print(df)
print(df.loc['emp1']) # label based indexing
print(df.iloc[1])  # location based indexing

#adding new column
df ["job"] = ["developer","manager","accountant"]
print(df)

# adding new row
new_row = pd.DataFrame({"Name":["sandy"], "age":[23], "job":["scientist"]}, index=['emp4'])
df = pd.concat([df, new_row])
print(df)