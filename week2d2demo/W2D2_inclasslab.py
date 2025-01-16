#W2D2 - Text File Handling Review

#PROGRAM PROMP:


#VARIABLE DICTIONARY:


#--IMPORTS-----------------------------------------------------------
import csv
#--FUNCTIONS---------------------------------------------------------
def difference(people, maxCap):
    "'This function is passed two values and returns the difference between them'"
    diff = maxCap - people
    return diff #this value will replace the difference() call in the main code
#--MAIN EXECUTING CODE-----------------------------------------------

#initialize needed counting vars
totalRec = 0
roomsOver = 0

#--connected to file-------------------------------------------------
with open("week2d2demo/classLab2-1.csv") as csvfile: #we need to manually change the forward slash to backslash -- we want it to process a file and not run it as \c like we would for \n or \t

    file = csv.reader(csvfile) #you can call the csvfile anything, it's just a variable here

    print(f"{"NAME":22}  {"MAX":5}   {"PPL":3}   {"OVER"}") #this can be wherever you want, as long as it's NOT in the FOR LOOP
    print("------------------------------------------")

    for rec in file:
        #below code occurs for every record (row) in the file (textfile/2D list)
        
        #assign each field data value to a friendly variable name
        name = rec[0]
        max = int(rec[1]) #ALL TEXT DATA is always seen as strings unless otherwise stated, aka casting it as a number
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the rooms that are over capacity (remaining is negative)
        if remaining < 0:
            roomsOver += 1
            
            print(f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}") #the spaces in between your print statement ARE LITERAL, so make sure you're spacing it evenly because it will mess up your field width +++++ good rule of thumb is always give out EXTRA SPACE in field width ======== abs() makes whatever variable inside, postive -> absolute value ------- or could you do {remaining * -1:5} since we're not storing that value anyway

        #count ALL rooms!
        totalRec += 1 #be conscious of your indents, this needs to be in line of the if statement so that it ALWAYS goes up by one

#--disconnected from file--------------------------------------------

#display final data (counting vars)
print(f"\nRooms currently OVER capacity: {roomsOver}")
print(f"\nTotal rooms in the file: {totalRec}")