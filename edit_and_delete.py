import csv
import os


def read_show_expense_list():
    if not os.path.exists('expense_list.csv'):
        print("Expense list file does not exist.")
        return []

    expenses = []
    with open('expense_list.csv', 'r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if not expenses:
        print("Expense list is empty.")
        return []

    print("Expense List:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {', '.join(expense)}")

    return expenses


def modify_expense(expenses):
    entry = int(input("Enter the entry number you want to modify: ")) - 1

    if not (0 <= entry < len(expenses)):
        print("Invalid entry number.")
        return

    print("Select the fields you wish to edit:")
    print("1. Date")
    print("2. Category")
    print("3. Description")
    print("4. Amount")
    choices = input("Enter the field numbers separated by commas (e.g., 1, 3, 4): ").split(",")

    for choice in choices:
        choice = choice.strip()
        if choice == '1':
            new_date = input("Enter the new date: ")
            expenses[entry][0] = new_date
        elif choice == '2':
            new_category = input("Enter the new category: ")
            expenses[entry][1] = new_category
        elif choice == '3':
            new_description = input("Enter the new description: ")
            expenses[entry][2] = new_description
        elif choice == '4':
            new_amount = input("Enter the new amount: ")
            expenses[entry][3] = new_amount
        else:
            print(f"Invalid choice: {choice}")

    save_expenses(expenses)
    print("Expense modified successfully.")


def delete_expense(expenses):
    entry = int(input("Enter the entry number you want to delete: ")) - 1

    if not (0 <= entry < len(expenses)):
        print("Invalid entry number.")
        return

    expenses.pop(entry)

    save_expenses(expenses)
    print("Expense deleted successfully.")


def save_expenses(expenses):
    with open('expense_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)


def edit_delete_main():
    expenses = read_show_expense_list()

    if not expenses:
        return

    user_input = input("Do you want to edit or delete an entry? (E for edit, D for delete, any other key to continue): ")

    if user_input.upper() == 'E':
        modify_expense(expenses)
    elif user_input.upper() == 'D':
        delete_expense(expenses)


if __name__ == '__main__':
    edit_delete_main()
