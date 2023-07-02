import csv
from collections import defaultdict

def generate_expense_report(filename):
    # Initialize dictionaries to store expenses
    category_expenses = defaultdict(float)
    monthly_expenses = defaultdict(float)
    yearly_expenses = defaultdict(float)

    # Read the expense data from the CSV file
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            date = row['Date']
            year, month, _ = date.split('-')

            # Update category-wise expenses
            category_expenses[category] += amount

            # Update monthly expenses
            monthly_expenses[(year, month)] += amount

            # Update yearly expenses
            yearly_expenses[year] += amount

    # Print the expense report
    print("Expense Report - Category-wise:")
    for category, amount in category_expenses.items():
        print(f"{category}: ₹{amount:.2f}")

    print("\nExpense Report - Monthly:")
    for (year, month), amount in monthly_expenses.items():
        print(f"{month}-{year}: ₹{amount:.2f}")

    print("\nExpense Report - Yearly:")
    for year, amount in yearly_expenses.items():
        print(f"{year}: ₹{amount:.2f}")

def expense_report_main():
    filename = 'expense_list.csv'
    generate_expense_report(filename)

# Call the function and provide the filename
if __name__ == '__main__':
    expense_report_main()
