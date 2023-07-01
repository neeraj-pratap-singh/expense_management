import csv

EXPENSE_LIST_FILE = 'expense_list.csv'

def display_expense_list(expense_list):
    if not expense_list:
        print("No expenses found matching the filters.")
        return

    header = ["Date", "Category", "Description", "Amount"]
    print("{:<12} {:<10} {:<30} {:<8}".format(*header))  # Print header in a formatted manner
    print("-" * 70)  # Print separator line
    for expense in expense_list:
        print("{:<12} {:<10} {:<30} {:<8}".format(*expense))  # Print each expense in a formatted manner

def filter_expenses(expenses, category=None, start_date=None, end_date=None):
    filtered_expenses = []
    for expense in expenses:
        if category and expense[1].lower() != category.lower():
            continue
        if start_date and expense[0] < start_date:
            continue
        if end_date and expense[0] > end_date:
            continue
        filtered_expenses.append(expense)
    return filtered_expenses

def get_user_input(categories):
    print("Available Categories:")
    print(", ".join(categories))
    print()
    category = input("Enter a category to filter (leave blank for no filter): ")
    start_date = input("Enter a start date (YYYY-MM-DD) to filter (leave blank for no filter): ")
    end_date = input("Enter an end date (YYYY-MM-DD) to filter (leave blank for no filter): ")
    return category, start_date, end_date

def filter_main():
    with open(EXPENSE_LIST_FILE, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        expenses = list(reader)

    categories = set(expense[1] for expense in expenses)
    category, start_date, end_date = get_user_input(categories)
    filtered_expenses = filter_expenses(expenses, category, start_date, end_date)
    display_expense_list(filtered_expenses)

if __name__ == '__main__':
    filter_main()
