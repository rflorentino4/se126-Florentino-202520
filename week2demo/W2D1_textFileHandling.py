#W2D1 
#name: Text Filing Intro Demo

#Step 1: import the csv (comma separated value )library
import csv

totalRecords = 0 #holds total number of records in the file

#----conneted to file--------------------------------
#include relative file paths in open()
#make sure \ switches to /
with open("week2demo\simple.csv") as csvfile:
    #make sure to indent inside of code block
    #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list / matrix / table]
    file = csv.reader(csvfile)


    #print for headers, NEEDS TO BE OUTSIDE OF THE LOOP
    print (f"{'NAME':11}   {'NUM':11}   {'COLOR'}")
    print ("--------------------------------------------")


    #Step 3: process through every record (row) in the file
    for record in file:
        #add +1 to totalRecords to keep accurate count of records
        totalRecords += 1

        #print(record) #entire record/row data as a list

        name = record[0]     #name field
        number = record[1]     #number field
        color = record[2]     #color field


        print(f"{name:10}    {number:10}    {color.title():10}") #*:10* designates the field width so the spacing looks good no matter the length of the words     +++++    *.title()* makes the first character of the chosen variable (?) capitalized


#----disconnected from file--------------------------
print(f"\nTOTAL RECORDS: {totalRecords}\n") #the f lets you call totalRecords and have it show up in the print statement