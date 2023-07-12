import csv
import re

EXPENSE_LIST_FILE = 'expense_list.csv'
DEFAULT_CATEGORIES = ['Food', 'Travel', 'Household', 'Health', 'Education', 'Gift', 'Bill Payment']

def is_valid_date(date):
    # Date validation: check if it matches the format (YYYY-MM-DD)
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        return True
    return False

def is_valid_category(category):
    # Category validation: check if it is not empty
    if category:
        return True
    return False

def is_valid_description(description):
    # Description validation: check if it is not empty
    if description:
        return True
    return False

def is_valid_amount(amount):
    # Amount validation: check if it is a positive number
    if amount.isdigit() and int(amount) > 0:
        return True
    return False

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def add_expense():
    date = get_valid_input("Enter the date (YYYY-MM-DD): ", is_valid_date)
    
    # Show default categories with an option to create a new category
    print("Default Categories:")
    for i, category in enumerate(DEFAULT_CATEGORIES, start=1):
        print(f"{i}. {category}")
    print(f"{len(DEFAULT_CATEGORIES)+1}. Create a new category")
    
    # Prompt for category selection
    category_choice = get_valid_input("Select a category (enter the number): ", lambda x: x.isdigit() and 1 <= int(x) <= len(DEFAULT_CATEGORIES)+1)
    category_choice = int(category_choice)
    
    # If user selects a default category
    if 1 <= category_choice <= len(DEFAULT_CATEGORIES):
        category = DEFAULT_CATEGORIES[category_choice - 1]
    # If user chooses to create a new category
    elif category_choice == len(DEFAULT_CATEGORIES) + 1:
        category = get_valid_input("Enter your own category: ", is_valid_category).capitalize()
    
    description = get_valid_input("Enter the description: ", is_valid_description)
    amount = get_valid_input("Enter the amount: ", is_valid_amount)

    with open(EXPENSE_LIST_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
        writer.writerow([date, category, description, amount])

    print("Expense added successfully.")

if __name__ == '__main__':
    add_expense()