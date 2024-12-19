import json
import numpy as np

FILE_NAME = "file_handling_excersise_2/students.json"

def display_menu():
    print("\nStudent Manager")
    print("1. View Students")
    print("2. View Students scored more than 75 marks")
    print("3. Add Students")
    print("4. Exit")

def read_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
            print("\nStudents:")
            for student in students:
                print(f"Name: {student['name']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("No students found.")
    # except json.JSONDecodeError:
    #     print("Error reading JSON file. It may be empty")

def high_grade():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
            print("\nStudents with grades more than 75:")
            for student in students:
                if int(student['grade']) > 75:
                    print(f"Name: {student['name']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("No students found.")
    # except json.JSONDecodeError:
    #     print("Error reading JSON file. It may be empty or corrupted.")

def add_contact():
    name = input("Enter name: ")
    grade = input("Enter grade: ")

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    # except json.JSONDecodeError:
    #     students = []

    students.append({"name": name, "grade": grade})

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully!")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            read_contacts()
        elif choice == "2":
            high_grade()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()
