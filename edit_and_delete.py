#read csv file
#show csv file to user
#ask user to edit or delete the entry
#ask user to delete or edit which entry

import csv
import os

def read_expense_list():
    if not os.path.exists('expense_list.csv'):
        print("\nExpense list file does not exist.\n")
        return
    data = []
    with open('expense_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            print(row)
    return data
    # with open('expense_list.csv', 'r') as file:
    #     reader = csv.reader(file)

    #     for row in reader:
    #         print(row)
    #     expenses = list(reader)
    #     print(expenses, type(expenses))
    #     return expenses

def modify_expense(expenses):
    entry = int(input("Enter the entry number you want to modify: "))
    if entry < 1 or entry > len(expenses):
        print(entry)
        print("Invalid entry number.")
        return
    new_amount = input("Enter the new amount: ")
    expenses[entry-1][3] = new_amount
    save_expenses(expenses)
    print("Expense modified successfully.")

def delete_expense(expenses):
    entry = int(input("Enter the entry number you want to delete: "))
    if entry < 1 or entry > len(expenses):
        print("Invalid entry number.")
        return
    expenses.pop(entry-1)
    save_expenses(expenses)
    print("Expense deleted successfully.")

def save_expenses(expenses):
    with open('expense_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

def edit_delete_main():
    expenses = read_expense_list()
            
    user_input = input("Do you want to edit or delete an entry? (E for edit, D for delete, any other key to continue): ")
    if user_input.upper() == 'E':
        modify_expense(expenses)
    elif user_input.upper() == 'D':
        delete_expense(expenses)
    
if __name__ == '__main__':
    edit_delete_main()

