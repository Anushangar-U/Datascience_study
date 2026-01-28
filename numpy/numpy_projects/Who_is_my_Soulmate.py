import numpy as np


rating = np.random.randint(1, 11, size=(10, 5))


try:
    position = int(input(f"Enter your position (0-9): "))
    if position < 0 or position >= 10:
        print("Position out of range! Defaulting to 0.")
        position = 0
except ValueError:
    print("Invalid input! Defaulting to 0.")
    position = 0

start = rating[position]


dif = rating - start
dist = np.linalg.norm(dif, axis=1)


mean_dist = np.mean(dist)
similar_mask = dist < mean_dist 


sorted_idx = np.argsort(dist) 
soulmate = sorted_idx[1] 


print("-" * 30)
print("FULL RATINGS MATRIX:\n", rating)
print("-" * 30)
print(f"Distances from Person {position}:", dist.round(2))
print(f"Your #1 Soulmate is at position: {soulmate}")


print(f"Number of people similar to you: {np.sum(similar_mask) - 1}")
print("Their IDs are:", np.where(similar_mask)[0])