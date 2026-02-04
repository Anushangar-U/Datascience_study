import pandas as pd
import numpy as np

#setting a column as  a index
df = pd.read_csv("python/ds_study/pandas/pokemon.csv", index_col="Name")
print(df.to_string())

#slection by column
#print(df["Name"].to_string())

#slection of multiple columns
print(df[["No","Legendary"]])

#selecting using indexing a column
print(df.loc["Pikachu"])

#adding row
new_row = pd.DataFrame({"No":[152], "Type 1":["Water"], "Type 2":["Dark"], "Legendary":[False]}, index=["Greninja"])
df = pd.concat([df, new_row])
print(df.loc["Greninja"])

#adding column
df["Region"] = "Kanto"
print(df.loc["Greninja"])

#editing a cell
df.at["greninja","Region"] = "kalos"
print(df.loc["greninja"])

#slicing
print(df.iloc[0:5])