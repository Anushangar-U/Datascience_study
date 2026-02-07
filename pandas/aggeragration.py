import pandas as pd
import numpy as np

df = pd.read_csv("python/ds_study/pandas/pokemon.csv")

#whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

#specific column
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())

#grouping
grouped = df.groupby("Type1")
print(grouped["Height"].mean())
print(grouped.count())
