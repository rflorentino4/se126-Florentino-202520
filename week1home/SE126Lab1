#Romina Florentino
#SE126.04
#W1D2 Lab #1: SE126 Room Capacity
#1-11-2025 start, due 1-13-2025

#PROGRAM PROMPT: This is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program. 
#--------------------------------------------------

#VARIABLE DICTIONARY
#roomCap -                  maximum room capacity (in assignment, labled as "max_cap")
#roomRequest -              number of people attending the meeting (in assignment, labled as "people")
#diff - FUNCTION*           function that calculates the difference between roomCap and roomRequest
#promptUser - FUNCTION*     function that prompts the user [y/n] if they want to add room details (in assignment, labeled as "decision")
#userResponse -             asks user if they want to begin the program (in assignment, labeled as "response")
#beginPrompt -              starts the room details main program/loop
#promptName -               asks user to enter meeting name
#newDiff -                  used to make "diff" a positive number *for display purposes* when roomCap < roomRequest

#MINA'S NOTES
#

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
def difference(roomCap, roomRequest): #<--FUNCTION FOR DIFFERENCE CALCULATIONS
    diff = roomCap - roomRequest
    return diff


def promptUser(): #<--FUNCTION TO PROMPT USER TO ENTER ROOM DETAILS
    userResponse = input("Hello! :] Would you like to enter a room capacity? [y/n]: ").lower()

    while userResponse != "y" and userResponse != "n":
        print("Invalid input. Please enter a valid response of [y/n]. ")
        userResponse = input("Would you like to enter a room capacity? [y/n]: ").lower()
    return userResponse


#--------MAIN CODE--------------------------------------------
#start of program
beginPrompt = promptUser()


#while loop for room details, including calculations for under, over, and exact
while beginPrompt == "y":
    promptName = input("\n\t\tHello KT! Please enter the meeting name (ex: Ctrl Alt Elite): ")

    print(f"\n\t\tWelcome to the *{promptName}* meeting room capacity program!\n")

    roomCap = int(input(f"\t\tEnter the maximum room capacity for *{promptName}* as an integer (ex: 500): "))
    roomRequest = int(input(f"\t\tEnter the number of attendees for *{promptName}* as an integer (ex: 250): "))

    diff = difference(roomCap, roomRequest) #calling the function
    
    #exact/LEGAL if statement
    if diff == 0:
        print(f"\n\t\t***PERFECT!***\n\t\tIt is legal to hold the meeting. NO additional people may legally attend. ")

    #over/ILLEGAL elif statement
    elif diff < 0:
        newDiff = diff * -1
        print(f"\n\t\t***VIOLATION!***\n\t\tThe meeting cannot be held as planned due to fire regulations. {newDiff} people must be excluded in order to meet the fire regulations.")

    #under/LEGAL elif statement
    elif diff < roomCap:
        print(f"\n\t\t***LEGAL!***\n\t\tIt is legal to hold the meeting. {diff} additional people may legally attend. ")

    #invalid characters get sent here to resend the prompt
    else:
        print("\nInvalid input. Please try again. ")
    

    #prompt user to start again after entering all details
    beginPrompt = promptUser()


    #if user enters "n" to initial prompt to start program, they get sent here
    if beginPrompt == "n":
        print("\n\t\tYou have chosen to exit the program. Goodbye! ")