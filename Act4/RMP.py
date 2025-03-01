import json
from operator import itemgetter

# Load student records from a file
def load_records(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Starting with an empty list.")
        return []

# Save student records to a file
def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

# Calculate final grade
def calculate_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

# Show all student records
def show_all_students(records):
    print("\nStudent Records:")
    for student_id, name, class_standing, major_exam in records:
        final_grade = calculate_grade(class_standing, major_exam)
        print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Final Grade: {final_grade:.2f}")

# Order students by last name
def order_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

# Order students by final grade
def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)

# Find student by ID
def find_student(records, student_id):
    return next((record for record in records if record[0] == student_id), None)

# Add a student record
def add_record(records):
    student_id = input("Enter 6-digit Student ID: ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID format.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing (out of 100): "))
    major_exam = float(input("Enter Major Exam Grade (out of 100): "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added.")

# Edit a student record
def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    student = find_student(records, student_id)
    if student:
        index = records.index(student)
        first_name = input("Enter New First Name: ") or student[1][0]
        last_name = input("Enter New Last Name: ") or student[1][1]
        class_standing = input("Enter New Class Standing (out of 100): ") or student[2]
        major_exam = input("Enter New Major Exam Grade (out of 100): ") or student[3]
        records[index] = (student_id, (first_name, last_name), float(class_standing), float(major_exam))
        print("Record updated.")
    else:
        print("Student not found.")

# Delete a student record
def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    student = find_student(records, student_id)
    if student:
        records.remove(student)
        print("Record deleted.")
    else:
        print("Student not found.")

# Main Menu
def main():
    filename = "students.json"
    records = load_records(filename)
    
    while True:
        print("\nStudent Record Management System")
        print("1. Show All Students")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Add Record")
        print("5. Edit Record")
        print("6. Delete Record")
        print("7. Save File")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_all_students(records)
        elif choice == '2':
            records = order_by_last_name(records)
            show_all_students(records)
        elif choice == '3':
            records = order_by_grade(records)
            show_all_students(records)
        elif choice == '4':
            add_record(records)
        elif choice == '5':
            edit_record(records)
        elif choice == '6':
            delete_record(records)
        elif choice == '7':
            save_records(filename, records)
            print("Records saved.")
        elif choice == '8':
            save_records(filename, records)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()