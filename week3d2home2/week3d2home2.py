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


#initializations
notEligible = 0
oldNotReg = 0
eligibleNotVote = 0
didVote = 0


#connected to file-------
with open("week3d2home2/voters_202040.csv") as csvfile: #don't forget to CHANGE the SLASH, you'll see a weird color if not
    print(f'\n{"ID #:":7} {"Age":7} {"Registered":12} {"Voted":8}') #this can be wherever you want, as long as it's NOT in the FOR LOOP ++++ be care of how you use single & double quotes, must use both to differentiate (I think? this works tho)

    file = csv.reader(csvfile)

    for rec in file: #occurs for every record/row in the textfile/2D list 
        ids.append(rec[0])

        age.append(int(rec[1]))

        registered.append(rec[2])

        voted.append(rec[3])

    



    #     if int(rec[1]) < 18:
    #         notEligible += 1
    #         age.append(rec[1])
        
    # for index in range (0,len(age)):
    #     print(f"{ids[index]}  {age[index]} {registered[index]}  {voted[index]}")

for index in range(0, len(ids)): #this will run for as many i's/indexes there are in the list --incrementing by 1 each time
    print(f"\n{ids[index]}   {age[index]}   {registered[index]}   {voted[index]}")

print(f"\nTotal records in the file: {len(ids)}\n")











        # #index 0 = voter ID
        # ids.append(rec[0])

        # #index 1 = age
        # if int(rec[1]) < 18:
        #     age.append("Not eligible")
        #     notEligible += 1

        # elif int(rec[1]) >= 18 and rec[2] == "N":
        #     age.append("Old enough, not registered")
        #     oldNotReg += 1

        # elif int(rec[1]) >= 18 and rec[2] == "Y" and rec[3] == "N":
        #     age.append("Eligible, not voted")
        #     eligibleNotVote += 1

        # elif int(rec[1]) >= 18 and rec[2] == "Y" and rec[3] == "Y":
        #     age.append("Voted")
        #     didVote += 1
        
        
#index 0 = voter ID
#index 1 = age
#index 2 = registered
#index 3 = voted