# Contact Management System

## Author
Danielle Bronson

## School
Coding Temple

## GitHub Repository
[Contact Management System](https://github.com/ladydanicorn/contact_management_system)

## Project Overview
The **Contact Management System** is a Python command-line application that helps you manage your contacts efficiently. You can add, edit, delete, search, and display contacts using this program. In addition, you can export and import contacts from a file, making it easy to back up or transfer your data.

This project reinforces key Python concepts, including dictionaries, file handling, user interaction, input validation, and error handling.

## Features

1. **Add a new contact**  
   Create a new contact by entering details such as name, phone number, email address, and other additional information (like address or notes).
   
2. **Edit an existing contact**  
   Modify the details of an existing contact, including the name, phone number, and other contact information.

3. **Delete a contact**  
   Remove a contact from the system.

4. **Search for a contact**  
   Find and display a contact’s details by searching using their phone number or email address.

5. **Display all contacts**  
   Show all contacts stored in the system.

6. **Export contacts to a text file**  
   Save your contacts in a structured format into a text file.

7. **Import contacts from a text file (Bonus)**  
   Load contacts from a text file into the system to restore or merge contact information.

8. **Quit**  
   Exit the application.

## Data Storage
Contacts are stored in nested Python dictionaries. Each contact is identified by a unique phone number or email address as the key, and the corresponding value contains the following details:
- Name
- Phone number
- Email address
- Additional information (address, notes, etc.)

Example of contact data format:
```python
contacts = {
    '1234567890': {
        'name': 'Bob', 
        'phone': '1234567890', 
        'email': 'bob@bob.com', 
        'address': '123 Bob St', 
        'notes': 'Friend'
    },
    '1234567891': {
        'name': 'Diane', 
        'phone': '1234567891', 
        'email': 'diane@neopets.com', 
        'address': '123 Apfel Lane', 
        'notes': 'Enemy'
    }
}
```
For more example contact data, refer to the provided `contacts.txt` file.

## User Interface
The system operates through a command-line interface (CLI) with an intuitive menu:

```
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file (Bonus)
8. Quit
```

## Input Validation
The system validates user inputs using regular expressions to ensure proper formatting of phone numbers and email addresses. Incorrect inputs trigger user-friendly error messages, helping users provide correct information.

## Error Handling
The program includes robust error handling through `try`, `except`, `else`, and `finally` blocks. It manages file errors, invalid input, and general execution issues gracefully, preventing the program from crashing unexpectedly.

## How to Run the Project

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ladydanicorn/contact_management_system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd contact_management_system
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to add, edit, delete, search, or manage contacts.

## Bonus Feature
If you want to import contacts from a text file, ensure that your file format follows the pattern shown in the `contacts.txt` file.