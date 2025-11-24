# Exercise 3: Biography (Advanced)

# Step 1: Get input from user
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Step 2: Handle possible input errors for age
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number for age.")
    age = 0  # default value

# Step 3: Store info in a dictionary
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 4: Print the information
print("\n--- Biography ---")
print("Name:", biography["name"])
print("Hometown:", biography["hometown"])
print("Age:", biography["age"])
