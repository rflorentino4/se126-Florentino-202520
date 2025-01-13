def difference(roomCap, roomRequest): #<--FUNCTION HEADER
    diff = roomCap - roomRequest

    if diff == 0:
        print(f"\n\t\t***perfect even**)    ")
        promptUser()

    elif diff < 0:
        newDiff = diff * -1
        print(f"\n\t\t***VIOLATION***\n\t\tThe meeting cannot be held as planned due to fire regulations. {newDiff} people must be excluded in order to meet the fire regulations.")
        promptUser()

    elif diff < roomCap:
        print(f"\n\t\t***LEGAL***\n\t\tIt is legal to hold the meeting. {diff} additional people may legally attend.")
        promptUser()

    else:
        print("Invalid input. Please try again baby.")
        promptUser() 
    return diff, roomCap


def promptUser():  # <-- FUNCTION HEADER
    print("three")  # Debugging line to track when the function is called
    userResponse = input("Would you like to enter a room capacity? [y/n]: ").lower()

    # Keep asking for a valid response if the input is neither "y" nor "n"
    while userResponse != "y" and userResponse != "n":
        print("Invalid input. Please enter a valid response of [y/n].")
        userResponse = input("Would you like to enter a room capacity? [y/n]: ").lower()

    return userResponse  # Return the user input

# --------MAIN CODE--------------------------------------------
#beginPrompt = promptUser()  # First prompt when the program starts
beginPrompt = "y"  #
print("one")  # Debugging line

# Only enter this loop if the user responds with "y"
while beginPrompt == "y": #try using the func maybe ??? -> or (promptUser() == "y")   
    promptName = input("Hello! Please enter the meeting name (ex: Ctrl Alt Elite): ")

    print(f"\n\t\tWelcome to the *{promptName}* meeting room capacity program!\n")

    # Room capacity and request (attendees)

    roomCap = int(input(f"\t\tEnter the maximum room capacity for *{promptName}* as an integer (ex: 500): "))
    roomRequest = int(input(f"\t\tEnter the number of attendees for *{promptName}* as an integer (ex: 250): "))

    # Assuming difference is another function that adjusts roomCap
    diff, roomCap = difference(roomCap, roomRequest)  # <-- Function call to adjust room capacity

    # Ask again if the user wants to continue after completing the room input
    beginPrompt = promptUser()  # This will ask again after the logic
    print("two")  # Debugging line

# If the user chooses "n", exit the program gracefully
if beginPrompt == "n":
    print("You have chosen to exit the program. Goodbye!")
    exit()