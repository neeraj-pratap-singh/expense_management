import csv
import os
import re

USER_DATABASE_FILE = 'user_database.csv'

def is_valid_username(username):
    # Username validation: alphanumeric characters only
    if re.match(r'^[a-zA-Z0-9]+$', username):
        return True
    return False

def is_valid_password(password):
    # Password validation: at least 6 characters long
    if len(password) >= 6:
        return True
    return False

def register():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if not is_valid_username(username):
            print("Invalid username. Username must contain only alphanumeric characters.")
        elif not is_valid_password(password):
            print("Invalid password. Password must be at least 6 characters long.")
        else:
            break

    with open(USER_DATABASE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Registration successful.")

def login():
    if not os.path.exists(USER_DATABASE_FILE):
        print("User database file not found. Please register an account first.")
        return

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(USER_DATABASE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful.")
                # Continue with dashboard or other actions
                return True

    print("Invalid username or password.")
    return False

def main():
    while True:
        print("1. Register")
        print("2. Login")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            register()
        elif choice == '2':
            isSuccess = login()
            return isSuccess
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
