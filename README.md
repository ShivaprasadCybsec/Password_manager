Password Manager 


Code Breakdown

1. Importing Required Modules![IMG_20241017_132937](https://github.com/user-attachments/assets/91c63b7f-0d6b-49de-b556-cf9ac8e14bd0)
hashlib: A library for hashing (converting data into a fixed-length hash value) to secure passwords.
getpass: Allows users to enter passwords without displaying them on the screen, providing security during input.



2. Creating a Dictionary to Store Credentials
![IMG_20241017_133200](https://github.com/user-attachments/assets/64c557dd-6732-4df8-abda-0d0c05274dee)
This is a dictionary that will store usernames as keys and their corresponding hashed passwords as values.

Note: Currently, the data is stored in memory and will not persist after the program exits.



3. create_account() Function: Creating a New User Account
![IMG_20241017_133409](https://github.com/user-attachments/assets/16baf11c-dedb-4ae5-b3d2-cb794b2bef22)
Explanation:

input(): Asks the user to enter a desired username.

Check for Duplicate Username: If the username already exists in the dictionary, it prints a message and exits the function.

getpass.getpass(): Prompts the user to enter a password securely (the input is hidden).

password.encode(): Converts the password from a string to bytes (required for hashing).

hashlib.sha256(): Hashes the password using the SHA-256 algorithm.

hexdigest(): Converts the hash into a hexadecimal string.


Storing the Hashed Password: Adds the username and its hashed password to the dictionary.



4. login() Function: Logging in with Stored Credentials
![IMG_20241017_133541](https://github.com/user-attachments/assets/f0b48612-285a-41f6-99e3-70a550c9eb21)
Explanation:

input(): Prompts the user to enter their username.

getpass.getpass(): Securely asks the user to enter their password.

hashlib.sha256(): Hashes the entered password using SHA-256.

Credential Validation:

Checks if the username exists in the dictionary.

Compares the stored hashed password with the newly hashed password.


Output: If the credentials match, it prints a success message; otherwise, it prints an error.



5. main() Function: User Interface for Account Management
![IMG_20241017_133711](https://github.com/user-attachments/assets/a6dc980b-24d6-490c-9539-b5b4624ddbcb)
Explanation:

Infinite Loop: The program runs continuously inside a while True loop until the user exits.

input(): Asks the user to choose between:

1. Creating an account.


2. Logging in.


3. Exiting the program.



if-elif-else Statements:

Depending on the input, it calls the appropriate function (create_account() or login()).

If the user enters 0, the loop breaks, and the program exits.

For any other input, it prints "Invalid choice."




6. Program Entry Point
![IMG_20241017_133838](https://github.com/user-attachments/assets/ddfeea6f-b096-4a5d-89bd-4f5550c4abe0)
Explanation:
if __name__ == "__main__": is a common Python idiom to ensure that the code inside it runs only when the script is executed directly (and not when imported as a module).

It calls the main() function, starting the program’s execution.



How the Code Works (Summary)

1. Creating an Account:

User selects option 1 from the menu.

Enters a username and password.

Password is hashed and stored in the password_manager dictionary.



2. Logging In:

User selects option 2 from the menu.

Enters their username and password.

The entered password is hashed and compared with the stored hash.

If they match, login is successful.



3. Exiting:

User selects option 0 to exit the program.
![IMG_20241017_134121](https://github.com/user-attachments/assets/c0eeffe5-dbd7-48bc-970a-86f9bd1cded6)
