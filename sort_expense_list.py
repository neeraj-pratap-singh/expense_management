import csv

EXPENSE_LIST_FILE = 'expense_list.csv'

def read_expenses():
    expenses = []
    with open(EXPENSE_LIST_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses

def sort_expenses(expenses, sort_key, ascending=True):
    return sorted(expenses, key=lambda x: x[sort_key], reverse=not ascending)

def display_expenses(expenses):
    print("Date\t\tCategory\tDescription\t\tAmount")
    for expense in expenses:
        print(f"{expense['Date']}\t{expense['Category']}\t\t{expense['Description']}\t\t{expense['Amount']}")

def sort_main():
    expenses = read_expenses()
    print("Expense List:")
    display_expenses(expenses)
    
    while True:
        print("\n********Sort Options********\n")
        print("1. Sort by Date (Ascending)")
        print("2. Sort by Date (Descending)")
        print("3. Sort by Amount (Ascending)")
        print("4. Sort by Amount (Descending)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            sorted_expenses = sort_expenses(expenses, 'Date', ascending=True)
            display_expenses(sorted_expenses)
        elif choice == '2':
            sorted_expenses = sort_expenses(expenses, 'Date', ascending=False)
            display_expenses(sorted_expenses)
        elif choice == '3':
            sorted_expenses = sort_expenses(expenses, 'Amount', ascending=True)
            display_expenses(sorted_expenses)
        elif choice == '4':
            sorted_expenses = sort_expenses(expenses, 'Amount', ascending=False)
            display_expenses(sorted_expenses)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    sort_main()
