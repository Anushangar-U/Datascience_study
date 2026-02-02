import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,7,8]) 
print(s)

ap = pd.Series([1,3,5,np.nan,7,8], index=['a','b','c','d','e','f'])
print(ap)
print(ap.loc['c']) # label based indexing
print(ap.iloc[2])  # location based indexing
print(ap[ap>5]) # conditional selection  

dates = pd.date_range("20130101",periods=6) 
print(dates)

#dictionary to series
calories = {"Day1":420,"Day2":380,"Day3":390}
s = pd.Series(calories)
print(s)

s.loc['Day2'] = s.loc['Day2'] + 100
print(s)
print(s[s > 400])