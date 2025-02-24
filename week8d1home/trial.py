#W8D1 Collections and Logic
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows. The program should display the seat pattern, with an ‘X’ making the seats already assigned. 

#create parallel lists for each seat letter
seatA = ["A","A","A","A","A","A","A"]
seatB = ["B","B","B","B","B","B","B"]
seatC = ["C","C","C","C","C","C","C"]
seatD = ["D","D","D","D","D","D","D"]

#I don't like my print statements to be touching the path it prints out automatically
print()

#print seats
print("Seating Chart :] \n")
for index in range(0,len(seatA)):
    print(f"{index + 1}   {seatA[index]}   {seatB[index]}   {seatC[index]}   {seatD[index]} ")

#input from user
seatRow = int(input("\n\tEnter your desired row number: [1-7] "))
seatLetter = input("\tEnter your desired seat letter: [A-D] ").upper()

#personal preference
print()

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

for index in range(0,len(seatA)):
    print(f"{index + 1}   {seatA[index]}   {seatB[index]}   {seatC[index]}   {seatD[index]} ")

#personal preference
print()