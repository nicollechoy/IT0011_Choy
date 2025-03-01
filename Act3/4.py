# Write to the file
with open("students.txt", "a") as file:
    file.write("Last Name: Choy\n")
    file.write("First Name: Nicolle\n")
    file.write("Age: 19\n")
    file.write("Contact Number: 09123456789\n")
    file.write("Course: BSIT-BA\n\n")
print("Student information has been saved to 'students.txt'.\n")

# Read the file
with open("students.txt", "r") as file:
    student_data = file.read()
print("Reading Student Information:\n")
print(student_data)