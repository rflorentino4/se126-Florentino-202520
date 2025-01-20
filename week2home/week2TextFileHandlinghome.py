#W2D2 - LAB #2: Text File Handling Review
#Romina Florentino 
#SE126-2025.20


#PROGRAM PROMPT: Produce a report that lists all the computers in the provided csv file. It must look like the provided sample output. The last line should print the number of computers in the file.


#VARIABLE DICTIONARY:
#totalRec = counting variable for the total records in file (must be 29)
#csvfile = variable that calls our csv file ----ask KT Thursday
#file = variable that stores the csvfile and lets us use it, I think? ----ask KT Thursday
#rec = variable that works for every record/row in the textfile/2D list
#type = variable that displays the type of computer
#brand = variable that displays the brand of the computer
#cpu = variable that displays the cpu of the computer
#ram = variable that displays the ram of the computer
#firstDisk = variable that displays the first disk amount of space
#nohdd = variable that displays if there is a second disk on the computer (1=no, 2=yes)
#secondDisk = variable that displays the second disk amount of space
#os = variable that displays the OS of the computer
#year = variable that displays the year the computer came out


#--IMPORTS-----------------------------------------------------------
import csv


#--FUNCTIONS---------------------------------------------------------


#--MAIN EXECUTING CODE-----------------------------------------------


#initialize needed counting vars
totalRec = 0


#--connected to file-------------------------------------------------
with open("week2home/filehandling.csv") as csvfile: #we need to manually change the forward slash to backslash -- we want it to process a file and not run it as \c like we would for \n or \t

        #below is the print for my titles, NOT the data Mina
        print(f'\n{"Type":9} {"Brand":8} {"CPU":4} {"RAM":4} {"1st Disk":10} {"No HDD":7} {"2nd Disk":9} {"OS":4} {"YR"}') #this can be wherever you want, as long as it's NOT in the FOR LOOP ++++ be care of how you use single & double quotes, must use both to differentiate (I think? this works tho)
      
        file = csv.reader(csvfile) #you can call the csvfile anything, it's just a variable here

        for rec in file:
        #below code occurs for every record (row) in the file (textfile/2D list)
                totalRec += 1
                
                #print type
                if rec[0] == "D":
                        type = "Desktop"

                elif rec[0] == "L":
                        type = "Laptop"

                #print brand
                if rec [1] == "DL":
                        brand = "Dell"

                elif rec[1] == "GW":
                        brand = "Gateway"

                elif rec[1] == "HP":
                        brand = rec[1]
        
                #print 2-5
                cpu = rec[2]
                ram = rec[3]
                firstDisk = rec[4]
                nohdd = rec[5]
        
                #print rest if no hdd is 1
                if rec[5] == "1":
                        secondDisk = "" #this will be empty because 1's don't have a second
                        os = rec[6]
                        yr = rec[7]

                #print rest if no hdd is 2
                elif rec[5] == "2":
                        secondDisk = rec[6]
                        os = rec[7]
                        yr = rec[8]
             
                #this is the print for the actual DATA held in the csv
                print(f"{type:9} {brand:8} {cpu:4} {ram:4} {firstDisk:10} {nohdd:7} {secondDisk:9} {os:4} {yr:} ")


# #--disconnected from file--------------------------------------------


# #display final data (counting var)
#print(f"\n{'Total records in the file: ' str{totalRec} : ^30}") #this didn't work bc of the curly braces Mina
print(f"\n{'Total records in the file: ' + str(totalRec): ^65}") #use this instead
print(f"{'Have a good day KT :]' : ^65}\n")