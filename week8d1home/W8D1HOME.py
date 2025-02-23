#W8D1 Collections and Logic
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. 

#this file uses: airplane_seats.csv

#IMPORTS------------------------------
import csv

#FUNCTIONS----------------------------
def byeKT():
    print(f"\n\t\t\t\tHave a good day KT :]\n")

#MAIN EXECUTING CODE------------------

#create empty lists to hold the file data
rowNumber = []
seatA = []
seatB = []
seatC = []
seatD = []

#open the file and read the data into the lists
with open("week8d1home/airplane_seats.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        rowNumber.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])

#display the seat pattern
print()
for index in range(len(rowNumber)):
    print(f"\t\t\t\t\t\t\t\t\t{rowNumber[index]} {seatA[index]} {seatB[index]} {seatC[index]} {seatD[index]}\n")
print()   
#disconnected from file-----------------------
ans = "y"

while ans == "y":
    promptUser = input("Would you like to pick a seat? [y/n] :) ").lower()

    if promptUser == "y":
        seatRow = input("Enter your desired row number: ")
        seatLetter = input("Enter the seat letter [A, B, C,  or D]: ").upper()

        if seatLetter == "A":
            seatA(seatRow) == "X"
            
        elif seatLetter == "B":
            seatC[int(seatRow)] = "X"
        elif seatLetter == "C":
            seatD[int(seatRow)] = "X"
        elif seatLetter == "D":
            seatA[int(seatRow)] = "X"
        else:
            print("Invalid seat letter")

        #display the seat pattern
        for index in range(len(rowNumber)):
            print(f"\n{rowNumber[index]} {seatA[index]} {seatB[index]} {seatC[index]} {seatD[index]}\n")
    
    elif promptUser == "n":
        print("\n*Exiting program*")
        byeKT()
        ans = "n"
    
    else:
        print("\n\t**INVALID INPUT**\n")
        ans = input("Would you like to pick a seat? [y/n] :) ").lower()
