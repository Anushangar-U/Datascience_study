import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(f"stats array:\n{stats}")

#mean
mean_stats = np.mean(stats, axis=0)
print(f"Mean of stats along axis 0: {mean_stats}")

#sum
sum_stats = np.sum(stats, axis=1)
print(f"Sum of stats along axis 1: {sum_stats}")

#standard deviation
std_stats = np.std(stats)
print(f"Standard Deviation of stats: {std_stats}")

#variance
var_stats = np.var(stats)
print(f"Variance of stats: {var_stats}")

#minimum
min_stats = np.min(stats)
print(f"Minimum value in stats: {min_stats}")

#maximum
max_stats = np.max(stats)
print(f"Maximum value in stats: {max_stats}")