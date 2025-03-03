#W9D1 Lab 7 - Dictionaries
#Romina Florentino 
#SE126.04 - 2025
#----------------------------------------------

#this file uses: words.csv

#IMPORTS---------------------------------------
import csv

#FUNCTIONS OR DICTS----------------------------
def byeKT():
    print(f"\n\t\t\t\tHave a good day KT :]\n")

def menu():
    print("\n----------------------------------------------------------------------")
    print("\t\tWelcome to the Searching Menu! :] ")
    print("----------------------------------------------------------------------\n")
    print("1. Show ALL words")
    print("2. SEARCH for a word")
    print("3. ADD a word")
    print("3.5 Show all words ALPHABETICALLY")
    print("________________")
    print("\n4. **EXIT**\n")

    menu_choice = input("Enter your search type [1-3.5]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

wordsDict = {}

#MAIN EXECUTING CODE---------------------------
#list 2 validate user input
validMenu = ["1", "2", "3", "3.5", "4"]

#open file and read data 2 the dict
with open("week9d1home\words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        wordsDict.update({rec[0] : rec[1]})  #similar to .append in lists +  follows same key value pairing to denote it's a dict (so curl braces)

#disconnected from file------------------------
ans = "y"

while ans == "y":
    choice = menu()
    
    if choice not in validMenu:
        print("\n\tINVALID ENTRY!!!! Please try again ;[ ")

    elif choice == "1":
        print("\n\t\t\t\t\t\t~ Show ALL words ~")




    elif choice == "3.5":
        print("\n\t\t\t\t~ Show all words ALPHABETICALLY ~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search --
        for index in range(len(wordsDict) - 1):
            for j in range(len(wordsDict) - 1):
                if wordsDict[j] > wordsDict[j + 1]:
                    #SWAP
                    swap(j, rec[0])
                    swap(j, rec[1])


        #display all titles
        for index in range(0, len(wordsDict)):
            print()