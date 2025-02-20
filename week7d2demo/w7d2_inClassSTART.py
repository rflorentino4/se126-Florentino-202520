#W7D2 - Live Class: Review of Binary Search & Bubble Sort + 2D Lists

#This demo uses the file: simple.csv (also named simple-2.csv)

#this start file contains a "shell" program, or a coded outline, for the full working program we will build in class to review bubble sort and binary search, as well as introduce basic processing of 2D lists

#*********************************************************
#we could do binary for name and age bc it's already ordered, but the color IS NOT --that would have to be bubble sorted first ---> KT mentioned that even if two of the three options on the list are sorted, it will still cause issues that the third isn't -> why is that?
#we ran into an issue after doing binary for both + bubble for only colors, because once it runs it sorts colors CHANGING names/their index values, so ---- you must bubble sort BOTH BEFORE binary
#only library needs binary, everything else is sequential
#*********************************************************

import csv 


def menu():
    print("Simple Searching Menu")
    print("1. Search by NAME")
    print("2. Search by NUM")
    print("3. Search by COLOR")
    print("4. EXIT")

    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp


#create your empty 1D parallel lists
names = []
nums = []
colors = []

#we will use the below hand-populated list
valid_menu = ["1", "2", "3", "4"]

with open("week7d2demo\simple-2.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title()) #just for Ray in the morning session ---this capitalizes the first character after a space/start of string
#disconnected from file-----------------------
ans = "y"

while ans == "y":
    choice = menu()

    #if choice != "1" and choice != "2" and choice != "3" and choice != "4": 
    if choice not in valid_menu: #this accomplishes the same thing as the previous line of code -> run this sequence when user choice isn't "1,2,3 or 4 as seen in the valid_menu list"
        print("!INVALID ENTRY!\nPlease try again.\n")

    #if and elif are an either or situation
    elif choice == "1": #search by NAME
        print("\n~Search by NAME~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search --
        for index in range(len(names) - 1):
            for j in range(len(names) - 1): #we do minus 1 bc it works for our if statement?
                if names[j] > names [j + 1]: #if colors at the current position, is greater than the value of current position + 1 index, then swap
                    #SWAP
                    swap(j, colors) #j=index -- colors=list name
                    swap (j, names)
                    swap (j, nums)

        #binary search
        search = input("Enter the NAME you are looking for: ") #always start by asking user
        
        #these will always start the same
        min = 0 #first index
        max = len(names) - 1 #length of list is 7 items but minus one because we need to stop at the last index
        mid = int((min + max) / 2) #middle index

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower(): #if less than what is in the middle, don't look thru upper side of the list
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == names[mid].lower():
            #Found it
            print(f"We found your search for {search}, details below: ")
            print(f"{'NAME':12}   {'NUM':3}   {'COLOR':10}")
            print(f"------------------------------------------------------")
            print(f"{names[mid]:12}   {nums[mid]:3}   {colors[mid]:10}")
            print(f"------------------------------------------------------")

        else:
            print(f"\nYour search for {search} is complete, no matches found ;(\n")


    elif choice == "2": #search by NUM
        print("\n~Search by NUM~")


    elif choice == "3": #search by COLOR
        print("\n~Search by COLOR~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search --
        for index in range(len(colors) - 1):
            for j in range(len(colors) - 1): #we do minus 1 bc it works for our if statement?
                if colors[j] > colors [j + 1]: #if colors at the current position, is greater than the value of current position + 1 index, then swap
                    #SWAP
                    swap(j, colors) #j=index -- colors=list name
                    swap (j, names)
                    swap (j, nums)

        #binary search
        search = input("Enter the NAME you are looking for: ") #always start by asking user
        
        #these will always start the same
        min = 0 #first index
        max = len(colors) - 1 #length of list is 7 items but minus one because we need to stop at the last index
        mid = int((min + max) / 2) #middle index

        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower(): #if less than what is in the middle, don't look thru upper side of the list
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == colors[mid].lower():
            #Found it
            print(f"We found your search for {search}, details below: ")
            print(f"{'NAME':12}   {'NUM':3}   {'COLOR':10}")
            print(f"------------------------------------------------------")
            print(f"{names[mid]:12}   {nums[mid]:3}   {colors[mid]:10}")
            print(f"------------------------------------------------------")

        else:
            print(f"\nYour search for {search} is complete, no matches found ;(\n")


    else:
        print("\n~EXIT~")
        ans = "X" #ans changes from "y" to end the loop (condition will now eval as false)

print("\nThank you for using my program.\n\t\tGOODBYE!\n")


#------2D Lists ----------------------------------------------------------------------------------------------
#2D lists are just lists that contain 1D lists inside of them! 

