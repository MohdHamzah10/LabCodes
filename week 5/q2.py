import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30, 35])

print("Original Array:", arr)

print("Indexing")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Element at index 3:", arr[3])

print("Slicing")
print("Elements from index 1 to 4:", arr[1:5])
print("Elements from start to index 3:", arr[:4])
print("Elements from index 3 to end:", arr[3:])
print("Every second element:", arr[::2])
