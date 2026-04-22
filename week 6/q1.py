import random

arr = [random.randint(1,100) for _ in range(10)]

print("Array: ",arr)

max_val = max(arr)
min_val = min(arr)

print("Maximum = ",max_val)
print("Minimum = ",min_val)

