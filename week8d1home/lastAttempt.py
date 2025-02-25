#W8D1 Collections and Logic
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. 

#IMPORTS------------------------------

#create parallel lists for each seat letter (A-D)
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]
 
#func to print the seating chart
def seatingChart():
    print("\nSeating Chart :] \n")
    for index in range(0,len(seatA)):
        print(f"{index + 1}   {seatA[index]}   {seatB[index]}   {seatC[index]}   {seatD[index]} ")
    print()  #personal preference

#func to update the seat selection
def updateSeat(seatRow, seatLetter):
    if seatLetter == "A":
        seatList = seatA

    elif seatLetter == "B":
        seatList = seatB

    elif seatLetter == "C":
        seatList = seatC

    elif seatLetter == "D":
        seatList = seatD

    #mark the seat as taken with an "X" + let the user know their seat has been reserved
    if seatList[seatRow - 1] != "X":
        seatList[seatRow - 1] = "X"
        print(f"\nSeat {seatRow}{seatLetter} has been successfully reserved! Enjoy your flight ;) \n")

    #if seat is already taken, prompt user to select another seat
    else:
        print(f"\nUnfortunately, seat {seatRow}{seatLetter} is taken. Please select an available option. \n")

#print initial seating chart 2 user
seatingChart()

#start loop using ans variable
ans = "Y"

while ans == "Y":
    #get valid seat row input
    seatRow = (input("\n\tEnter your desired row number: [1-7] "))
    while not seatRow.isdigit() or not (1 <= int(seatRow) <= 7):
        print("\nInvalid entry. Please try again with a number between 1 and 7. ")
        seatRow = input("\n\tEnter your desired row number: [1-7] ")
    seatRow = int(seatRow)

    #get valid seat letter input
    seatLetter = input("\tEnter your desired seat letter: [A-D] ").upper()
    while seatLetter not in ["A", "B", "C", "D"]:
        print("\nInvalid entry. Please try again with a letter between A and D. \n")
        seatLetter = input("\tEnter your desired seat letter: [A-D] ").upper()

    #print what they chose
    print(f"\nYou selected Row {seatRow}, Seat {seatLetter}! ")

    #update the seat selection        
    updateSeat(seatRow, seatLetter)

    #print updated seating chart after selection
    seatingChart()

    #prompt user to pick another seat
    ans = input("\nWould you like to pick another seat? [Y/N] ").upper()
    while ans not in ["Y", "N"]:
        print("\nInvalid entry. Please try again with Y or N. ")
        ans = input("\nWould you like to pick another seat? [Y/N] ").upper()

    #exit program if user chooses "N"
    if ans == "N":
        print("\nExiting program. Have a great day! :) ")