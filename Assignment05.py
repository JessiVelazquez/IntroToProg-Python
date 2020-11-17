# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JVelazquez,11.13.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = ""   # A task entered by the user
strPriority = "" # A priority entered by the user
strRemove = "" # User request to remove an item from the list/table


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# Text File "ToDoList.txt" is loaded into a Python list of dictionary rows.
objFile = open(objFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
print("Task Manager Program")
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Task"], dicRow["Priority"], sep="|")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        strPriority = input("Enter its Priority (High/Med/Low): ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("What task would you like to remove? ")
        for dicRow in lstTable:
            if strRemove in dicRow["Task"]:
                lstTable.remove(dicRow)
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("File Saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program Closed. Bye Bye, Butterfly.")
        break  # and Exit the program
