import pandas as pd
import numpy as np

df = pd.read_csv("python/ds_study/pandas/pokemon.csv", index_col="Name")
print(df.to_string())

tall_pokemon = (df[df["Height"] >= 2])
print = tall_pokemon