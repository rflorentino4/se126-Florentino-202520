#W10 - Course Project
#Romina Florentino
#SE126.04 - 2025

#---------------------------------------------
#PROGRAM PROMPT: I have created a personal finance tracker that allows users to input their transactions (withdrawals and deposits) and view them in a sorted manner. The program will allow users to enter new transactions, view all transactions sorted by date (newest to oldest), and filter transactions by category.

#IMPORTS--------------------------------------
import csv

#FUNCTIONS------------------------------------
def header():
    print()
    print(f"{'ID':4}   {'Amount':6}   {'Category':10}   {'Date':12}")
    print("-" * 40)

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

def bubbleSort():
    #bubble sort the lists by date - most recent to least recent
    for index in range(0,len(date) - 1):
        for j in range(0,len(date) - 1): #HAS to be a DIFFERENT iterator, NOT INDEX
            if date[j] < date[j+1]:
                #now need to swap places!
                swap(j, uniqueID) #current index, and the list get swapped
                swap(j, amount)
                swap(j, category)
                swap(j, date)

def categorySort():
        found = []

        #get search item from user
        searchCategory = input("\nEnter the category you would like to view (withdrawal or deposit): ")

        #perform search
        for index in range(0, len(category)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchCategory.lower() == category[index].lower(): 
                #the IF STATEMENT allows for/handles the "search part"
                found.append(index) #make the found var the current index which can be used later 2 display

        if found:
            header()

            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            for index in range(0, len(found)):
                print(f"\n{uniqueID[found[index]]:<4}   {amount[found[index]]:6.2f}   {category[found[index]]:10}   {date[found[index]]}")

#show menu options
def menuOptions():
    print("\nWelcome to the Transaction Tracker! ")
    print("\n1. View by Date (descending) ")
    print("2. View by Category ")
    print("3. Exit")

    menuChoice = input("\nPlease enter a valid menu option (1-3): ")
    return menuChoice

#CONNECTED TO FILE----------------------------
validChoices = ["1", "2", "3"]

#create empty lists
uniqueID = []
amount = []
category = []
date = []

#read the csv file and append to lists
with open("week10d1_courseProject\data.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        uniqueID.append(rec[0])
        amount.append(rec[1])
        category.append(rec[2])
        date.append(rec[3])

#DISCONNECTED TO FILE-------------------------

#header print statements
header()
bubbleSort()

#print full lists to start
for rec in range(len(uniqueID)):
    amount[rec] = float(amount[rec])
    print(f"{uniqueID[rec]:<4}   {amount[rec]:6.2f}   {category[rec]:10}   {date[rec]}")

#prompt user to enter a new transaction
promptUser = input("\nWould you like to enter a new transaction? (y/n): ")

#while loop to get user information on transactions + append to lists
while promptUser == "y":
    newID = len(uniqueID) + 1
    newAmount = float(input("Enter the amount (as a float): "))
    newCategory = input("Enter the category (withdrawal or deposit): ")
    newDate = input("Enter the date as (yyyy-mm-dd): ")

    #append new transaction to lists
    uniqueID.append(newID)
    amount.append(newAmount)
    category.append(newCategory)
    date.append(newDate)

    header()
    bubbleSort()

    for rec in range(len(uniqueID)):
        print(f"{uniqueID[rec]:<4}   {amount[rec]:6.2f}   {category[rec]:10}   {date[rec]}")
    
    rePrompt = input("\nWould you like to enter a new transaction? (y/n): ")

    #if user does not want to enter a new transaction, exit the loop using "n"
    if rePrompt == "n":
        promptUser = "n"

ans = "y"
while ans =="y":
    choice = menuOptions()

    #if choice != "1" and choice != "2" and choice != "3": 
    if choice not in validChoices: #this accomplishes the same thing as the previous line of code -> run this sequence when user choice isn't "1,2,3"
        print("!INVALID ENTRY!\nPlease try again.\n")

    #date sort (descending)
    elif choice == "1":
        print("\n~View by Date (descending)~")
        header()
        bubbleSort()

        for rec in range(len(uniqueID)):
            amount[rec] = float(amount[rec])
            print(f"{uniqueID[rec]:<4}   {amount[rec]:6.2f}   {category[rec]:10}   {date[rec]}")

    #category sort
    elif choice == "2":
        categorySort()

    #exit
    elif choice == "3":
        print("Thank you for using the Transaction Tracker! ")
        print("\nThank you for a wonderful term KT :] ")
        ans = "n"