#W10 - Course Project
#Romina Florentino
#SE126.04 - 2025

#---------------------------------------------
#PROGRAM PROMPT:

#IMPORTS--------------------------------------
import csv

#create lists for the following:

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

#CONNECTED TO FILE----------------------------

#create empty lists
uniqueID = []
amount = []
category = []
date = []

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

#while loop to continue entering transactions
while promptUser == "y":
    newID = len(uniqueID) + 1
    newAmount = float(input("Enter the amount (as a float): "))
    newCategory = input("Enter the category (withdrawl or deposit): ")
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
