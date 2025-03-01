# Input
first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")

# String manipulations
full_name = first_name + " " + last_name
sliced_name = first_name[:4]
greeting = f"Hello, {sliced_name}! Welcome. You are {age} years old."

# Output
print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting:", greeting)
