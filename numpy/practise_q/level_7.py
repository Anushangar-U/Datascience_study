#The Scenario:You are building a tiny AI that predicts whether a house will sell.
#You have 4 houses (samples) and each house has 3 features (Size, Bedrooms, Age). 
#You also have 2 neurons that represent different ways of looking at the data.

import numpy as np

houses = np.random.randint(size=(4,3))
weights = np.random.randint(size=(2,3))

result = houses@weights.T

print(result)
