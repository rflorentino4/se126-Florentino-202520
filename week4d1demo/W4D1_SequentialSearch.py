#WD1 - Sequential Searc

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
print (f"{'Fname':12} {'Lname':13} {'T1':5} {'T2':5} {'T3':7} {'# Avg:':7} {'L Avg'}") #header print statements
print("------------------------------------------------------------")

for index in range(0, len(fName)):
    print(f"{fName[index]:10}   {lName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}   {numAvg[index]:8.2f}   {letAvg[index]}")

print("------------------------------------------------------------")

print(f"\nThere are {len(fName)} students in the file.\n")