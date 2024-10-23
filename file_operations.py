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