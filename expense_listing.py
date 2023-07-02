import csv

EXPENSE_LIST_FILE = 'expense_list.csv'

def display_expense_list():
    with open(EXPENSE_LIST_FILE, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print("{:<12} {:<10} {:<30} {:<8}".format(*header))  # Print header in a formatted manner
        print("-" * 70)  # Print separator line
        for row in reader:
            print("{:<12} {:<10} {:<30} {:<8}".format(*row))  # Print each row in a formatted manner

if __name__ == '__main__':
    display_expense_list()