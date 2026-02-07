import pandas as pd
import numpy as np

df = pd.read_csv("python/ds_study/pandas/pokemon.csv")

#drop irrelevant columns
df = df.drop(columns=["Type2", "Generation", "Legendary"])
print(df.head())

#handle missing values
df = df.dropna(subset=["Type2"])#drop rows with missing values in "Type2" column
print(df.head())

df = df.fillna({"Type2":"None"})#fill missing values in "Type2" column with "Unknown"
print(df.head())

#fix inconsistent data
df["Type1"] = df["Type1"].replace({"Grass":"Plant","Bug":"Insect"})#replace "Grass" with "Plant" and "Bug" with "Insect" in "Type1" column
print(df.head())

#standardize data
df["Name"] = df["Name"].str.capitalize()
print(df.head())

#fix data types
df["Legendary"] = df["Legendary"].astype(bool) #convert "Legendary" column to boolean type
print(df.head())

#remove duplicates
df = df.drop_duplicates() #drop duplicate rows