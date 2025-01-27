#W4D1 Sequential Search
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: We will continue to work with the class grades csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequental search program which wll allow us to find students in the file, and write data regardig the to a newly created file in our repository.

#this file uses: class_grades.csv

#IMPORTS----------------
import csv

#FUNCTIONS--------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"
    
    return let #"let" value replaces the fnction call in the main executing code

#MAIN EXECUTING CODE----

#create empty lists to hold the file data
fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("week4d1demo\class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropiate lists ---APPEND adds to the END, next available
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file -- can still access the stored data VIA the lists

#process the list data to calc an avg score for each student, and find a letter grade equivalent --process, think FOR LOOP
numAvg = [] #will hold each student's numeric average of test scores
letAvg = [] #will hold each student's letter average of test scores

for index in range(0, len(fName)):
    #calc avg of current student
    a = (test1[index] + test2[index] + test3[index]) / 3
    #add average to numAvg list
    numAvg.append(a) #ORRR, can also do: numAvg.append((test1[index] + test2[index] + test3[index]) / 3)

    l = letter(a) #return value of letter() stored to l
    letAvg.append(l) #can also do: letAvg.append(letter(a)) BUT it is better to do it thi way when you need to reutilize ur vars

#process the lists to display all student data back to the user
print("\n\t\tPART ONE\n")
print (f"{'Fname':12} {'Lname':13} {'T1':5} {'T2':5} {'T3':7}") #header print statements
print("-----------------------------------------")

for index in range(0, len(fName)): #print the data within these vars
    print(f"{fName[index]:10}   {lName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}")

print("\n************************************************************")

print("\n\t\t\tPART TWO\n")
print (f"{'Fname':12} {'Lname':13} {'T1':5} {'T2':5} {'T3':7} {'# Avg:':7} {'L Avg'}") #header print statements
print("------------------------------------------------------------")

for index in range(0, len(fName)): #print the data within these vars
    print(f"{fName[index]:10}   {lName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}   {numAvg[index]:8.2f}   {letAvg[index]}")

print("------------------------------------------------------------")

print(f"\nThere are {len(fName)} students in the file.\n")

#write a program that allows a user to repeatedly search for a stdent by their last name or their letter grade; when a specific user is found, display all data relevant on that user, when not found alert the user. When searching by letter grade, display all of the students' data when found, or alert the user that o student grades fit that description

print("\n\nWelecome to the Student Seach Program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":
    #get search type from user
    print("\n\tSEARCH MENU OPTIONS")
    print("\n1. Search by LAST NAME")
    print("2. Search by FIRST NAME")
    print("3. Search by LETTER GRADE")
    print("4. *EXIT*")

    searchType = input("\nEnter your search type [1-4]\n")

    if searchType == "1":
        print("\t\nSEARCH BY LAST NAME")

        found = -1 #use bc it is an invalid index number, will use to check later to see if a student has been found

        #get search item from user
        searchLast = input("Enter the LAST NAME of the student you are searching for: \n")


        #perform search
        for index in range(0, len(lName)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchLast.lower() == lName[index].lower(): #must emphasize this bc the csv has different casing and human error is inevitable
                #the IF STATEMENT allows for/handles the "search part"
                found = index #make the found var the current index which can be used later 2 display

        #display results
        if found != -1: #if this is true, the last name has been found and can be displayed
            print("test1")
            print(f"Your search for {searchLast} was FOUND!")
            print("test2")
            print(f"{fName[found]:10}   {lName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {numAvg[found]:8.2f}   {letAvg[found]}")
            print("Test3")
        else:
            print(f"Your search for {searchLast} was *NOT* FOUND!")
            print("test4")
            print("Check your spelling and try again.")

    if searchType == "2":
        print("\t\nSEARCH BY FIRST NAME")

        found = -1 #use bc it is an invalid index number, will use to check later to see if a student has been found

        #get search item from user
        searchName = input("Enter the FIRST NAME of the student you are searching for: \n")


        #perform search
        for index in range(0, len(fName)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchName.lower() == fName[index].lower(): #must emphasize this bc the csv has different casing and human error is inevitable
                #the IF STATEMENT allows for/handles the "search part"
                found = index #make the found var the current index which can be used later 2 display

        #display results
        if found != -1: #if this is true, the last name has been found and can be displayed
            print(f"Your search for {searchName} was FOUND!")
            print(f"{fName[found]:10}   {lName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {numAvg[found]:8.2f}   {letAvg[found]}")
        else:
            print(f"Your search for {searchName} was *NOT* FOUND!")
            print("Check your spelling and try again.")

    elif searchType == "3":
        print("\tSEARCH BY LETTER GRADE")

        found = [] #creates empty list to gather and store found index values

        #get search item from user
        searchGrade = input("Enter the LETTER GRADE of the student you are searching for: \n")


        #perform search
        for index in range(0, len(letAvg)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchGrade.upper() == letAvg[index]:
                #the IF STATEMENT allows for/handles the "search part"
                found.append(index) #adds the current index (FOUND), can be used later 2 display

        #display results
        if not found: #this runs if the list is EMPTY MEANING IT DID NOT find anything
            print(f"\tYour search for {searchGrade} was *NOT* FOUND!")
            print("\tCheck your spelling and try again.")
        else:
            print(f"\tYour search for {searchGrade} was FOUND!")
            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            for index in range(0, len(found)):
                print(f"{fName[found[index]]:10}   {lName[found[index]]:10}   {test1[found[index]]:3}   {test2[found[index]]:3}   {test3[found[index]]:3}   {numAvg[found[index]]:8.2f}   {letAvg[found[index]]}")


    elif searchType == "4":
        print("\tEXITING")
        answer = "n"

    else:
        print("test5")
        print("*INVALID ENTRY!!*")


    #build a way out of the loop
    if searchType == "1" or searchType == "2" or searchType =="3": #only used when user doesn't specify 3 to exit
        answer = input("\t\t\nWould you like to search again? [y/n]: \n").lower()