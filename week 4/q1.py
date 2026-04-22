# Create dictionary
students = {
    "Maaz": 85,
    "Ahmad": 72,
    "Saif": 90,
    "Hamzah": 68,
    "Yash": 78
}

# Display students scoring above 75
print("Students scoring above 75:")
for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)
