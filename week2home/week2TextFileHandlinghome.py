#W2D2 - Text File Handling Review

#PROGRAM PROMPT: Produce a report that lists all the computers in the provided csv file. It must look like the provided sample output. The last line should print the number of computers in the file.


#VARIABLE DICTIONARY:


#--IMPORTS-----------------------------------------------------------
import csv
#--FUNCTIONS---------------------------------------------------------
#def difference(people, maxCap):
#    "'This function is passed two values and returns the difference between them'"
#    diff = maxCap - people
#    return diff #this value will replace the difference() call in the main code
#--MAIN EXECUTING CODE-----------------------------------------------

#initialize needed counting vars
totalRec = 0




#--connected to file-------------------------------------------------
with open("week2home/filehandling.csv") as csvfile: #we need to manually change the forward slash to backslash -- we want it to process a file and not run it as \c like we would for \n or \t

    file = csv.reader(csvfile) #you can call the csvfile anything, it's just a variable here

    print(f"{"Type":9} {"Brand":7} {"CPU":4} {"RAM":4} {"1st Disk":8} {"No HDD":4} {"2nd Disk":6} {"OS":4} {"YR"}") #this can be wherever you want, as long as it's NOT in the FOR LOOP
    
    for rec in file:
        #below code occurs for every record (row) in the file (textfile/2D list)
        if rec[0] == "D":
                type = "Desktop"
        elif rec[0] == "L":
                type = "Laptop"
        else:
                type = "ERROR --" + str(rec[0])
        #print(type)
        if rec [1] == "DL":
                brand = "Dell"
        elif rec[1] == "GW":
                brand = "Gateway"
        elif rec[1] == "HP":
                brand = rec[1]
        else:
                brand = "ERROR --" + str(rec[1])
        
        cpu = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        nohdd = rec[5]
        
        if rec[5] == "1":
                secondDisk = "" #this will be empty
                os = rec[6]
                yr = rec[7]
        elif rec[5] == "2":
                secondDisk = rec[6]
                os = rec[7]
                yr = rec[8]
             

        print(f"{type:3} {brand:5} {cpu:5} {ram:5} {firstDisk:5}{nohdd:5} {secondDisk:5} {os:5} {yr:5} ")

#         name = rec[0]
#         max = int(rec[1]) #ALL TEXT DATA is always seen as strings unless otherwise stated, aka casting it as a number
#         ppl = int(rec[2])

#         #call the difference() to find people over/under capacity
#         remaining = difference(ppl, max)

#         #count and display the rooms that are over capacity (remaining is negative)
#         if remaining < 0:
#             roomsOver += 1
            
#             print(f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}") 

#         #count ALL rooms!
#         totalRec += 1 

# #--disconnected from file--------------------------------------------

# #display final data (counting vars)
# print(f"\nTotal rooms in the file: {totalRec}")