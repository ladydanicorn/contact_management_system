from contact_operations import (add_contact, edit_contact, delete_contact, search_contact, display_all_contacts)
from file_operations import export_contacts, import_contacts

def display_menu():
    contacts = {} 
    print("Welcome to the Contact Management System!")

    while True:
        print("""\nMenu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file 
    8. Quit""")
        
        choice = input("Please select an option 1-8: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            import_contacts(contacts)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number 1-8: ")



if __name__ == "__main__":
    display_menu() 