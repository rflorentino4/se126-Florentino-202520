#W9D1 Lab 7 - Dictionaries
#Romina Florentino 
#SE126.04 - 2025
#----------------------------------------------
#PROGRAM PROMPT: 
#Create a dictionary to store the data from the file. Once the dictionary has been fully populated with file data, create a menu system that allows the user to search for a word, add a word, show all words, or show all words alphabetically. The program should not end unless the user chooses option 4 to exit. All searches should not be case sensitive.

#this file uses: words.csv

#IMPORTS---------------------------------------
import csv

#FUNCTIONS OR DICTS----------------------------
def byeKT():
    print(f"\n\t\t\t\t\t   Have a good day KT :]\n")

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
with open("week9d1home/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        key = rec[0] #word
        value = rec[1] #definition
        wordsDict[key] = value #add 2 dict

#disconnected from file------------------------
ans = "y"

while ans == "y":
    choice = menu()
    
    if choice not in validMenu:
        print("\n\tINVALID ENTRY!!!! Please try again ;[ ")

    elif choice == "1":
        print("\n\t\t\t\t\t\t\t~ Show ALL words ~ ")

        print("\n~ Words - Definitions ~ ")
        #print all words + corresponding definitions
        for key in wordsDict:
            print(f"\n{key} - {wordsDict[key]}")

    elif choice == "2":
        print("\n\t\t\t\t\t\t~ SEARCH for a word ~ ")

        search = input("\nEnter the word you're looking for: ")

        #sequential search
        found = "x"
        for key in wordsDict:
            if search.lower() == key.lower():
                found = key

        if found != "x":
            print("\nYour word was found! :] ")
            print("\n~ Words - Definitions ~ ")
            print(f"\n{found} - {wordsDict[found]}")

        else:
            print("\nYour word was NOT found ;[ ")
            print("Please double check your spelling and try again... ")

    elif choice == "3":
        print("\n\t\t\t\t\t\t~ ADD a word ~")

        newWord = input("\nEnter the word you would like to add: ")
        newDef = input(f"Enter the definition of '{newWord}': ")

        wordsDict[newWord] = newDef #add new word 2 dict ---> no need 4 update() Mina
            
    elif choice == "3.5":
        print("\n\t\t\t\t~ Show all words ALPHABETICALLY ~")

        #make the dict a list 4 sorting
        wordsList = list(wordsDict.items())

        #BUBBLE SORT
        for index in range(0,len(wordsList) - 1):
            for j in range(0,len(wordsList) - 1 - index):
                if wordsList[j][0] > wordsList[j + 1][0]:
                    swap(j, wordsList)

        #convert back 2 dict
        wordsDict = dict(wordsList)

        print("\n~ Words - Definitions ~ ")
        #print all words + corresponding definitions ALPHABETICALLY now
        for key in wordsDict:
            print(f"\n{key} - {wordsDict[key]}")
        
    elif choice == "4":
        print("\n\t\t\t\t\t\t~ EXITING ~")
        ans = "n"
        byeKT()