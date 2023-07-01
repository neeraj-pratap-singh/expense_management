import os
from is_valid_date import is_valid_date
from is_valid_number import is_valid_number

def createFile():
    if not os.path.exists("expense_list.csv"):
        fileObject = open("expense_list.csv",'w')
        data = "Date\t Category\t Description\t Amount"
        fileObject.write(data)
    else:
        print("File already exist!")


def takeInput():
    createFile()
    while True:
        date = input("Enter Date in yyyy-mm-dd: ")
        if is_valid_date(date):
            break
        else:
            print("Invalid Date Format..!! Please enter in yyyy-mm-dd format.")

    while True:
        category = input("Mention Category: ")
        if category == "":
            print("Category Required..!!")
        else:
            break
    
    while True:
        description = input("Add Description: ")
        if description == "":
            print("Description Required..!!")
        else:
            break
    
    while True:
        amount = input("What is Amount: ")
        if is_valid_number(amount):
            break
        else:
            print("Amout Required..!!")

    #return date, category, description, amount
    writeFile(date, category, description, amount)

def writeFile(date, category, description, amount):
    fileObject = open("expense_list.csv",'a') 
    data = "\n" + date + "\t " + category + "\t " + description + "\t " + str(amount)
    fileObject.write(data)

#date, category, description, amount=takeInput()

