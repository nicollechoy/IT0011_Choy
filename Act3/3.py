# Input
last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

# Formatting the student information
student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n\n"

# Writing to the file
with open("students.txt", "a") as file:
    file.write(student_info)

# Confirmation message
print("Student information has been saved to 'students.txt'.")