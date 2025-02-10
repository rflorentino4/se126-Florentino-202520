#W5D2 Midterm
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu

#this file uses: westeros.csv
#prompt choice: #1

#IMPORTS------------------------------
import csv
import random

#FUNCTIONS----------------------------
def byeKT():
    print(f"\n\t\t\t\tHave a good day KT :]\n")

#MAIN EXECUTING CODE------------------

#create empty lists to hold the file data
fName = []
lName = []
email = []
department = []
phoneExt = []

#this list is for the office # that must be generated, start at 100 and do not exceed 200 -> SO USE 199 MINA
officeNumber = []

#connected to file
with open("week5MIDTERM/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append file data to appropriate list
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        department.append(rec[3])
        phoneExt.append(rec[4])
        
        #generate random number for each employee to receive a office #
        number = random.randint(100, 199)
        officeNumber.append(number)

#header print statements
print (f"\n{'First':10} {'Last':12} {'Email':32} {'Department':25} {'Ext':8} {'Office'}")
print("--------------------------------------------------------------------------------------------------")

#print the data in the lists
for index in range(0, len(fName)):
    print(f"{fName[index]:8}   {lName[index]:10}   {email[index]:30}   {department[index]:23}   {phoneExt[index]:6}   {officeNumber[index]}")

print("--------------------------------------------------------------------------------------------------")    

#write the data to a new file
file = open('midterm_choice1.csv', 'w')

#process for every record in the csv file
for index in range(0, len(fName)):
#check if it's the last record in the csv file
    if index != len(fName) - 1:
        #create a new line for each record
        file.write(f"{fName[index]},{lName[index]},{email[index]},{department[index]},{phoneExt[index]},{officeNumber[index]}\n")
#this is the LAST RECORD in the csv file
    else:
        #NO NEW LINE for the last record
        file.write(f"{fName[index]},{lName[index]},{email[index]},{department[index]},{phoneExt[index]},{officeNumber[index]}")

file.close()    

#print total number of records
print(f"\nTotal Records in file: {len(fName)}")

print("\n\n\tWelecome to the Seach Program :]\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":
    #get search type from user
    print("\n\tSEARCH MENU OPTIONS")
    print("\n1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. *EXIT*")

    searchType = input("\nEnter your search type [1-3]\n")

    if searchType == "1":
        print("\t\nSEARCH BY EMAIL")

        found = -1 #checks if record has been located

        #get search item from user
        searchEmail = input("\nEnter the EMAIL of the person you are searching for: \n")

        
        #perform search
        for index in range(0, len(email)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchEmail.lower() == email[index].lower(): #must emphasize this bc the csv has different casing and human error is inevitable
                #the IF STATEMENT allows for/handles the "search part"
                found = index #make the found var the current index which can be used later 2 display

        #display results
        if found != -1: #if this is true, the last name has been found and can be displayed
            print(f"\n\tYour search for {searchEmail} was FOUND!")
            print (f"\n{'First':12} {'Last':12} {'Email':34} {'Department':30} {'Ext':8} {'Office'}")
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"{fName[found]:10}   {lName[found]:10}   {email[found]:32}   {department[found]:28}   {phoneExt[found]:6}   {officeNumber[found]}")

        else:
            print(f"\tYour search for {searchEmail} was *NOT* FOUND!")
            print("\tCheck your spelling and try again.")


    elif searchType == "2":
        print("\t\nSEARCH BY DEPARTMENT")

        found = []

        #get search item from user
        searchDepartment = input("\nEnter the DEPARTMENT of the person you are searching for: \n")


        #perform search
        for index in range(0, len(department)):
            #the FOR LOOP allows for/handles the "sequence" part -> from the beginning to the end
            if searchDepartment.lower() in department[index].lower(): #I'm using "in" so that the user can type something somewhat similar and get the results they intended
                #the IF STATEMENT allows for/handles the "search part"
                found.append(index) #make the found var the current index which can be used later 2 display

         #display results
        if not found: #this runs if the list is EMPTY MEANING IT DID NOT find anything
            print(f"\tYour search for {searchDepartment} was *NOT* FOUND!")
            print("\tCheck your spelling and try again.")

        else:
            print(f"\t\nYour search for {searchDepartment} was FOUND!")
            print (f"\n{'First':12} {'Last':12} {'Email':34} {'Department':27} {'Ext':8} {'Office'}")
            print("--------------------------------------------------------------------------------------------------------")

            #found is a list with multiple pieces of data - must use a FOR LOOP to see all
            for index in range(0, len(found)):
                print(f"\n{fName[found[index]]:10}   {lName[found[index]]:10}   {email[found[index]]:32}   {department[found[index]]:25}   {phoneExt[found[index]]:8}   {officeNumber[found[index]]}")

    elif searchType == "3":
        print("\tEXITING\n")
        byeKT()
        answer = "n"

    else:
        print("\n\t*INVALID ENTRY!!*")    

        #build a way out of the loop
    if searchType == "1" or searchType == "2": #only used when user doesn't specify "3" to exit
        answer = input("\t\t\nWould you like to search again? [y/n]: \n").lower()