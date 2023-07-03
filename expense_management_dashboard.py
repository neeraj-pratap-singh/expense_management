from expense_listing import display_expense_list
from create_expense import add_expense
from sort_expense_list import sort_main
from filter_expense_list import filter_main
from expense_report import expense_report_main
from edit_and_delete import edit_delete_main
from user_authentication import main

def dashboard():
    while True:
        print("\n***********Expense Management Dashboard***********\n")
        print("1. Create an Expense")
        print("2. Expense Listing")
        print("3. Sorting of Listing")
        print("4. Filtering of Listing")
        print("5. Edit and Delete Expense Entries")
        print("6. Report Generation")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            display_expense_list()
        elif choice == '3':
            sort_main()
        elif choice == '4':
            filter_main()
        elif choice == '5':
            edit_delete_main()
        elif choice == '6':
            expense_report_main()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    while True:
        userAuthentication = main()
        if userAuthentication:
            dashboard()
        else:
            print('Please try again')
