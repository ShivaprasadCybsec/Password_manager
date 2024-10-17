
import hashlib
import getpass

# Dictionary to store usernames and their hashed passwords
password_manager = {}

def create_account():
    """Create a new account with a username and hashed password."""
    username = input("Enter your desired username: ")
    
    # Check if username already exists
    if username in password_manager:
        print("Username already exists. Please choose another.")
        return

    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Store the hashed password
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    """Login by verifying username and password."""
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the credentials match
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    """Main function with a loop to create accounts or login."""
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
