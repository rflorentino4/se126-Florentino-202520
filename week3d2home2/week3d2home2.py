#W3D2 Text File Handling PT 2 + lists
#Romina Florentino 
#SE126-2025.20
#---------------------------------------------


#DIRECTIONS: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.
#---------------------------------------------


#PROGRAM PROMPT: Construct a program that will analyze potential voters. The program should generate the following totals: -1 Number of individuals not eligible to register. -2 Number of individuals who are old enough to vote but have not registered. -3 Number of individuals who are eligible to vote but did not vote. -4 Number of individuals who did vote. -5 Number of records processed.
#---------------------------------------------


#imports-----------------
import csv


#functions---------------
def byeKT():
    print(f"\n{'Have a good day KT :]' : ^65}\n")


#main executing code-----
ids = []
age = []
registered = []
voted = []


#connected to file-------
with open("week3d2home2/voters_202040.csv") as csvfile: #don't forget to CHANGE the SLASH, you'll see a weird color if not
    print(f'\n{"Type":9} {"Brand":8} {"CPU":4} {"RAM":4} {"1st Disk":10} {"No HDD":7} {"2nd Disk":9} {"OS":6} {"YR"}') #this can be wherever you want, as long as it's NOT in the FOR LOOP ++++ be care of how you use single & double quotes, must use both to differentiate (I think? this works tho)

    file = csv.reader(csvfile)

    for rec in file: #occurs for every record/row in the textfile/2D list 
        #index 0 = voter ID
        ids.append(rec[0])

        #index 1 = age
        if int(rec[1]) < 18:
            notEligible.append(rec[1])

        elif int(rec[1]) >= 18 and rec[2] == "N":
            oldNotReg.append(rec[1])

        elif int(rec[1]) >= 18 and rec[2] == "Y" and rec[3] == "N":
            eligibleNotVote.append(rec[1])
        
#index 0 = voter ID
#index 1 = age
#index 2 = registered
#index 3 = voted