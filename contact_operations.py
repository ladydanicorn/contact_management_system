from validation import is_valid_phone, is_valid_email

def add_contact(contacts):
    phone = input("Enter phone number (10 digits): ")
    while not is_valid_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone = input("Enter phone number (10 digits): ")
    
    email = input("Enter email: ")
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter email: ")

    if phone in contacts:
        print("Contact already exists.")
    else:
        name = input("Enter name: ")
        address = input("Enter address: ")
        notes = input("Enter any additional notes: ")
        contacts[phone] = {"name": name, "phone": phone, "email": email, "address": address, "notes": notes}
        print("Contact added successfully.")


def edit_contact(contacts):
    phone = input("Enter phone number of the contact to edit: ")
    while not is_valid_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone = input("Enter phone number (10 digits): ")
    
    if phone in contacts:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        notes = input("Enter new notes: ")
        contacts[phone] = {"name": name, "phone": phone, "email": email, "address": address, "notes": notes}
        print("Contact edited successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    phone = input("Enter phone number to search: ")
    if phone in contacts:
        print(f"Contact found: {contacts[phone]}")
    else:
        print("Contact not found.")

def display_all_contacts(contacts):
    if contacts:
        for phone, details in contacts.items():
            print(f"{phone}: {details}")
    else:
        print("No contacts available.")

def export_contacts(contacts):
    with open('contacts.txt', 'w') as file:
        for phone, details in contacts.items():
            file.write(f"{phone}: {details}\n")
    print("Contacts exported successfully.")

def import_contacts(contacts):
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                phone, details = line.strip().split(': ', 1)
                contacts[phone] = eval(details)  
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("No file found to import contacts.")
