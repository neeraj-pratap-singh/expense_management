from expense_listing import read_expense_list

def create_expense():
    # TODO: Implement create expense functionality
    pass

def expense_listing():
    # TODO: Implement expense listing functionality
    # pass
    read_expense_list()

def filtering_of_listing():
    # TODO: Implement filtering of listing functionality
    pass

def edit_expense():
    # TODO: Implement edit expense functionality
    pass

def delete_expense():
    # TODO: Implement delete expense functionality
    pass

def generate_report():
    # TODO: Implement report generation functionality
    pass

def dashboard():
    while True:
        print("\n***********Expense Management Dashboard***********\n")
        print("1. Create an Expense")
        print("2. Expense Listing")
        print("3. Filtering of Listing")
        print("4. Edit and Delete Expense Entries")
        print("5. Report Generation")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            create_expense()
        elif choice == '2':
            expense_listing()
        elif choice == '3':
            filtering_of_listing()
        elif choice == '4':
            edit_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    dashboard()
