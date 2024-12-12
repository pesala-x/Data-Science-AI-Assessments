# File to store contacts
FILE_NAME = "file_handling_excersise/contacts.txt"

def display_menu():
    print("\nContact Manager")
    print("1. View Contacts")
    print("2. Add New Contact")
    print("3. Exit")

def read_contacts():
    try:
        file = open(FILE_NAME, "r")
        print("\nContacts:")
        for line in file:
            print(line.strip())
        file.close()
    except FileNotFoundError:
        print("No contacts found.")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    file = open(FILE_NAME, "a")
    file.write(name + ", " + phone + ", " + email + "\n")
    file.close()
    print("Contact added successfully!")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            read_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
