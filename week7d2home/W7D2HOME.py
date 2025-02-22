#W7D2 Searching and Sorting
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. Your program should give your user a specific menu. When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

#this file uses: book_list.csv

#IMPORTS------------------------------
import csv

#FUNCTIONS----------------------------
def byeKT():
    print(f"\n\t\t\t\tHave a good day KT :]\n")

def menu():
    print("\n----------------------------------------------")
    print("\t\tSearching Menu")
    print("----------------------------------------------\n")
    print("1. Show all TITLES")
    print("2. Search by TITLE")
    print("3. Search by AUTHOR")
    print("4. Search by GENRE")
    print("5. Search by LIBRARY NUMBER")
    print("6. Show all AVAILABLE books")
    print("7. Show all UNAVAILABLE/ON LOAN books")
    print("________________")
    print("\n8. **EXIT**\n")

    menu_choice = input("Enter your search type [1-8]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#MAIN EXECUTING CODE------------------

#create empty lists to hold the file data
libraryNumber = []
title = []
author = []
genre = []
pageCount = []
status = []

#hand-populated list to validate user input
validMenu = ["1", "2", "3", "4", "5", "6", "7", "8"]

#open the file and read the data into the lists
with open("week7d2home/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libraryNumber.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3].title())
        pageCount.append(rec[4])
        status.append(rec[5].title())

#disconnected from file-----------------------
ans = "y"

while ans == "y":
    choice = menu()

    if choice not in validMenu:
        print("\n\tINVALID ENTRY!!!! Please try again ;[ \n")

    elif choice == "1":
        print("\n\t\t\t\t\t\t\t~ All Titles ~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search --
        for index in range(len(title) - 1):
            for j in range(len(title) - 1):
                if title[j] > title[j + 1]:
                    #SWAP
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pageCount)
                    swap(j, status)
                    swap(j, libraryNumber)

        #display all titles
        for index in range(0, len(title)):
            print(f"\n{'TITLE':33}   {'AUTHOR':20}   {'GENRE':20}   {'PAGE COUNT':12}   {'STATUS':12}   {'LIBRARY NUMBER':6}")
            print(f"{title[index]:33}   {author[index]:20}   {genre[index]:20}   {pageCount[index]:12}   {status[index]:12}   {libraryNumber[index]:6}")

    elif choice == "2":
        print("\n\t\t\t\t\t\t\t~ Search by TITLE ~")

        found = "x"

        #sequential search
        search = input("Enter the TITLE you are looking for: ")

        for index in range(0, len(title)):
            if search.lower() in title[index].lower():
                found = index

        if found != "x":
            #Found it
                print(f"\nWe found your search for {search}, details below: ")
                print(f"\n{'TITLE':33}   {'AUTHOR':20}   {'GENRE':20}   {'PAGE COUNT':12}   {'STATUS':12}   {'LIBRARY NUMBER':6}")
                print(f"{title[found]:33}   {author[found]:20}   {genre[found]:20}   {pageCount[found]:12}   {status[found]:12}   {libraryNumber[found]:6}")
        
        else:
            print(f"\nYour search for {search} is complete, no matches found ;(\n")

    elif choice == "3":
        print("\n\t\t\t\t\t\t\t~ Search by AUTHOR ~")

        found = []

        #sequential search
        search = input("Enter the AUTHOR you are looking for: ")

        for index in range(0, len(author)):
            if search.lower() in author[index].lower():
                found.append({{title[index]:33}, author[index], genre[index], pageCount[index], status[index], libraryNumber[index]})
        
        for index in range(0, len(found)):
            #Found it
            print(f"\nWe found your search for {search}, details below: ")
            print(f"\n{'TITLE':33}   {'AUTHOR':20}   {'GENRE':20}   {'PAGE COUNT':12}   {'STATUS':12}   {'LIBRARY NUMBER':6}")
            print(f"\t{found[index]}")

            
        if not found: #if the list is empty
            print(f"\nYour search for {search} is complete, no matches found ;(\n")
