import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation (arr1^2)")

choice = input("Enter your choice (1-6): ")

if choice == "1":
    print("Addition:", arr1 + arr2)
elif choice == "2":
    print("Subtraction:", arr1 - arr2)
elif choice == "3":
    print("Multiplication:", arr1 * arr2)
elif choice == "4":
    print("Division:", arr1 / arr2)
elif choice == "5":
    print("Modulus:", arr1 % arr2)
elif choice == "6":
    print("Exponentiation:", arr1 ** 2)
else:
    print("Invalid choice! Please enter a number from 1 to 6.")
