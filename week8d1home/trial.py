#W8D1 Collections and Logic
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. 



#this never worked for me....****************************************************************************************************************************************************************************************************************************************



#FUNCTIONS======
def seatingChart ():
    #print seats
    print("Seating Chart :] \n")

    for index in range(0,len(seatA)):
        print(f"{index + 1}   {seatA[index]}   {seatB[index]}   {seatC[index]}   {seatD[index]} ")
    print()


#create parallel lists for each seat letter
seatA = ["A","A","A","A","A","A","A"]
seatB = ["B","B","B","B","B","B","B"]
seatC = ["C","C","C","C","C","C","C"]
seatD = ["D","D","D","D","D","D","D"]

#call seatingChart function to print for user
seatingChart()

#begin while loop
ans = "Y"

while ans == "Y":
    ans = input("Would you like to select a seat? [Y/N] ").upper()

    if ans == "Y":

        #input from user
        seatRow = int(input("\n\tEnter your desired row number: [1-7] "))
        if not seatRow.isdigit() or seatRow < 1 or seatRow > 7:
            print("\nInvalid entry. Please try again with a number between 1 and 7. ")            

        seatLetter = input("\tEnter your desired seat letter: [A-D] ").upper()
        if seatLetter not in ["A","B","C","D"]:
            print("\nInvalid entry. Please try again with a letter between A and D. ")


        #code for specific seat letter
        if seatLetter == "A":
            if seatA[seatRow - 1] != "X":
                seatA[seatRow - 1] = "X"
            
            else:
                print(f"\nUnfortunately, seat {seatRow} {seatLetter} is taken. Please select an available option. ")

        if seatLetter == "B":
            if seatB[seatRow - 1] != "X":
                seatB[seatRow - 1] = "X"
            
            else:
                print(f"\nUnfortunately, seat {seatRow} {seatLetter} is taken. Please select an available option. ")

        if seatLetter == "C":
            if seatC[seatRow - 1] != "X":
                seatC[seatRow - 1] = "X"
            
            else:
                print(f"\nUnfortunately, seat {seatRow} {seatLetter} is taken. Please select an available option. ")

        if seatLetter == "D":
            if seatD[seatRow - 1] != "X":
                seatD[seatRow - 1] = "X"
            
            else:
                print(f"\nUnfortunately, seat {seatRow} {seatLetter} is taken. Please select an available option. ")
    elif choice == "N":
        print("You have chosen to exit the program. Goodbye!" )
        ans = "N"
    
    else:
        print("Invalid entry. Please try again with either 'Y' or 'N' ")




for index in range(0,len(seatA)):
    print(f"{index + 1}   {seatA[index]}   {seatB[index]}   {seatC[index]}   {seatD[index]} ")

#personal preference
print()