#W3D2 - List Review - 1Dimensional Lists and Parallel Lists

#Prompt: Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1D lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new piece of data for each student: their current average test score.

#this file uses class_grades.csv

#IMPORTS--------------------------------------------------
import csv
#FUNCTIONS------------------------------------------------

#MAIN-EXECUTING CODE--------------------------------------

#initialize a record counting variable
totalRecords = 0

#create an empty list for EVERY!!!! potential field (or hand populate, but this is HORRIBLE if we need to bind several together ----empty is faster and we already have a csv created for our ease) -- here we have FIVE FIELDS/COLUMNS
firstName = []
lastName = []
test1 =[]
test2 = []
test3 = [] #once you make a name for any of the three structures (list, variable, and I forgot the last one), it CANNOT be reutilized


#connecting to the file---------------
with open("week3d2demo/class_grades.csv") as csvfile: #DON'T forget to change the slash to forward, backwards causes issues bc it thinks it's a \n or \t
    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (textfile/2D list)
        totalRecords += 1
        #fname = rec[0] this line would show up JUST the data for the first name, no bracket or single quotes surrounding it 

        #store data from current record to corresponding lists (each field is its own!)
        #.append() -> this puts data at THE END aka next available space in the list

        #parallel lists --> data dispersed across lists, connected by the same index
        firstName.append(rec[0]) #firstName is currently the empty list, here we are making so that everything in rec [0] which is all the first names, goes into the firstName variable 
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file---------------

#processing lists -- USE A FOR LOOP ALWAYS! -they are specifically built for lists--dif from while bc it runs indefinitely whereas here you will know how long it will run (as many records as you got)
for index in range(0, len(firstName)): #it is more scalable to use len and ur variable, versus directly stating 20 for the 20 records we have
    #for every time, index will start at 0 and run up to (NOT INCLUDING) the length (# of items) -> it will NOT iterate with index20 BC there is no 20 in computer terms technically, since we start with zero and that causes us to lose one
    print (f"INDEX {index:2}: {firstName[index]:10}   {lastName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}") #print this and it'll all make sense

#create a new list to hold each students avg test score -> FIRST, you must create the list
avg = []

for i in range(0, len(test1)): #"i" is index in programming, it's just a shorthand Mina
    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a) #avg list WAS empty, but with this, we are populating it with the calculation above to now hold the avg of the three test scores

print(f"\nINDEX #: {'FIRST':11}   {'LAST':11}   {'T1':3}   {'T2':3}   {'T3':3}")
print("--------------------------------------------------------------------------")

for index in range(0, len(firstName)): #it is more scalable to use len and ur variable, versus directly stating 20 for the 20 records we have
    #for every time, index will start at 0 and run up to (NOT INCLUDING) the length (# of items) -> it will NOT iterate with index20 BC there is no 20 in computer terms technically, since we start with zero and that causes us to lose one
    print (f"INDEX {index:3}: {firstName[index]:10}   {lastName[index]:10}   {test1[index]:3}   {test2[index]:3}   {test3[index]:3}   {avg[index]:.2f}") #print this and it'll all make sense
print("--------------------------------------------------------------------------")

#calc the entire class avg using a for loop to add each student's avg to the class total
totalAvg = 0
for i in range(0, len(avg)):
    totalAvg += avg[i]

classAvg = totalAvg / len(avg)

print(f"\nTotal Records: {totalRecords}\nCurrent Class Average: {classAvg:.2f}\n\nGoodbye!")