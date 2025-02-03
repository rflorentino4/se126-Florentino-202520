#W4D2 Parallel List Processing
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: This is a two-part program where you will work on creating and populating parallel lists based on file data, then create and write data to a file.

#this file uses: got_emails.csv

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
age = []
email = []
department = []
phoneExt = []

#initialize counting variables
researchCount = 0
salesCount = 0
marketingCount = 0
hrCount = 0
accountingCount = 0
auditCount = 0

#connected to file
with open("week4d2home\got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropiate lists ---APPEND adds to the END, next available
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(int(rec[2]))
        screenName = rec[3]
        house = rec[4]

        #create the email address
        email.append(f"{screenName}@westeros.net")

        #assign the department and extension BASED on the house
        if house == "House Stark":
            department.append("Research & Development")
            extension = random.randint(100, 199)  #Random extension between 100 and 199
            researchCount += 1
        elif house == "House Targaryen":
            department.append("Marketing")
            extension = random.randint(200, 299)  #Random extension between 200 and 299
            marketingCount += 1
        elif house == "House Tully":
            department.append("Human Resources")
            extension = random.randint(300, 399)  #Random extension between 300 and 399
            hrCount += 1
        elif house == "House Lannister":
            department.append("Accounting")
            extension = random.randint(400, 499)  #Random extension between 400 and 499
            accountingCount += 1
        elif house == "House Baratheon":
            department.append("Sales")
            extension = random.randint(500, 599)  #Random extension between 500 and 599
            salesCount += 1
        elif house == "The Night's Watch":
            department.append("Auditing")
            extension = random.randint(600, 699)  #Random extension between 600 and 699
            auditCount += 1
        
        #add the chosen extension to the list so we can keep track of them all
        phoneExt.append(extension)


#disconnected from file -- can still access the stored data VIA the lists
print("\n\t\t\t\t\tPART ONE\n")
print (f"{'First':10} {'Last':12} {'Email':32} {'Department':25} {'Ext':3}") #header print statements
print("--------------------------------------------------------------------------------------")

#print the data in the lists
for index in range(0, len(fName)):
    print(f"{fName[index]:8}   {lName[index]:10}   {email[index]:30}   {department[index]:23}   {phoneExt[index]:3}")

print("--------------------------------------------------------------------------------------")

#write the data to a new file
file = open('westeros.csv', 'w')

#for loop so it will run for every record in the csv file
for index in range(0, len(fName)):
#check if it's the last record in the csv file
    if index != len(fName) - 1:
        #create a new line for each record
        file.write(f"{fName[index]:8}   {lName[index]:10}   {email[index]:30}   {department[index]:23}   {phoneExt[index]:3}\n")
#this is the LAST RECORD in the csv file
    else:
        #NO NEW LINE for the last record
        file.write(f"{fName[index]:8}   {lName[index]:10}   {email[index]:30}   {department[index]:23}   {phoneExt[index]:3}")

file.close()

#display ending statements + the total number of records + employees in each department
print("\n\t\t\t\t\tPART TWO\n")
print("File created as:'westeros.csv'\n")
print(f"Total Employees: {len(fName)}")
print(f"\nResearch & Development Employees: {researchCount}")
print(f"\nSales Employees: {salesCount}")
print(f"\nMarketing Employees: {marketingCount}")
print(f"\nHuman Resources Employees: {hrCount}")
print(f"\nAccounting Employees: {accountingCount}")
print(f"\nAuditing Employees: {auditCount}")

byeKT()