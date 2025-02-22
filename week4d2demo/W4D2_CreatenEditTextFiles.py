#WD1 - Create and Edit Text Files + List and Sequential Search Review

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#this file uses: dragons.csv

#IMPORTS---------------------------
import csv

#FUNCTIONS-------------------------


#MAIN EXECUTING CODE---------------

#create an empty list 4 every potential field in the file (here it's 5, last, last name, dragon, dragon color 1, dragon color 2)
dragons = []        #field0 - dragon names
riders = []         #field1 - rider names
counts = []         #field2 - 1 or 2, count of colors
color1 = []         #field3 - first primary color
color2 = []         #field4 - second color, ONLY when count IS TWO (2)


with open("week4d2demo/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        counts.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":       #either CAST as an integer, or declare it EQUAL to a STRING
            color2.append(rec[4])
        elif rec[2] == "1":
            color2.append("---")
        else:
            color2.append("ERROR")

#disconnected from file-----------

#process lists 2 display data to the console
print(f"{'\nDRAGONS':15}   {'RIDERS':30}   {'#':3}   {'COLOR1':8}   {'COLOR2':8}")
print("-----------------------------------------------------------------------------")

for index in range(0, len(dragons)):
    print(f"{dragons[index]:15}   {riders[index]:30}   {counts[index]:3}   {color1[index]:8}   {color2[index]:8}")

print("-----------------------------------------------------------------------------\n")

#SEARCH FOR A SPECIFIC DRAGON------------

#STEP ONE: set up and gain of search
found = "x"
search = input("Which dragon are you looking for:")

#STEP TWO: perform search --> for loop ALWAYS with an if statement attached -for=sequence -if=search
for index in range(0, len(dragons)):
    if search.lower() in dragons[index].lower():        #lower is a METHOD, the child of a FUNCTION, you NEED the PARENTHESIS 
        #the second lower is white bc the comp doesn't KNOW that it can perform the method bc it's not aware of all the data types within the list ++++ if you use "in" instead of "==" it will return ONLY THE LAST VALUE with what you searched
        #hold onto the found location (index) of our searched-for value
        found = index

#STEP THREE: filter and display results --doesn't matter if u use a string or number as long as it's not POSITIVE INT (I think)
if found != "x":
    print(f"Your search for {search} has been FOUND! :]")
    print(f"{dragons[found]:15}   {riders[found]:30}   {counts[found]:3}   {color1[found]:8}   {color2[found]:8}")
    #this needs to be FOUND now, not INDEX bc it is the new location -these r parallel lists
else:
    print(f"Your search for {search} was NOT FOUND... :[")


#SEARCH FOR A COLOR SET
found = []
search = input("Enter the color you are looking for:")

for index in range(0, len(color1)):
    if search.lower() in color1[index] or search.lower() in color2[index]:
        found.append(index)

print("Here is what the found list contains:")
for index in range(0, len(found)):
    print(f"\t{found[index]}")

if not found:       #this runs only IF the list is EMPTY
    print(f"Your search for {search} was NOT FOUND... :[")
else:
    for index in range(0, len(found)):
        print(f"{dragons[found[index]]:15}   {riders[found[index]]:30}   {counts[found[index]]:3}   {color1[found[index]]:8}   {color2[found[index]]:8}")

#CAREFULLY RUN THIS LAST SECTION
#WRITE SOME DATA TO A NEW FILE
#create and write dragons and riders of the data to a new text file:
file = open('targs.csv', 'w')

for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}\n")

file.close()