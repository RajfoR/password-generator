# Password Manager

Password Manager is an application for managing passwords that allows you to generate random passwords and store them in a Keepass file. It also provides functionality to search and update existing entries.

## Requirements

The application relies on the following dependencies:

- tkinter: Library for creating user interfaces in Python.
- pyperclip: Library for copying text to the clipboard.
- json: Library for handling JSON format.
- pykeepass: Library for working with Keepass files.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd password-manager
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application by executing the following command:
```
python password_manager.py
```

## Instructions

### Generating a Password

- Click the "Generate Password" button to open the password options window.
- Enter the password length (default is 16 characters).
- Select the types of characters to include in the password by checking the corresponding checkboxes.
- Click the "Generate" button to generate a random password.
- The generated password will be displayed in the "Password" field and copied to the clipboard.

### Saving/Updating a Password

- Enter the website name in the "Website" field.
- Enter the email/username in the "Email/Username" field.
- Enter the password in the "Password" field.
- Click the "Add/Update" button to add a new entry or update an existing one.

### Searching for a Password

- Enter the website name in the "Website" field.
- Click the "Search" button to search for an entry for the given website.
- If an entry exists for the website, the email/username and password will be displayed in their respective fields.

## Notes

- Before using the application, you need to provide correct values for the `keepass_file` and `keepass_password` variables in the `save_to_keepass()` function.
- Make sure the logo.png file is located in the same directory as the password_manager.py file.
