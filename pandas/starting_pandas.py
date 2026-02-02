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