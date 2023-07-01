import csv
import os

def read_expense_list():
    if not os.path.exists('expense_list.csv'):
        print("\nExpense list file does not exist.\n")
        return

    with open('expense_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Call the function to read and display the expense list
# read_expense_list()
