#Working with Data Structures: In and Not In Keywords

#In and Not In Keywords

#In -> Returns True if a sequence with the specified value is present in the object ======== ex: x in y

#Not In -> Returns True if a sequence with the specified value is not present in the object ======== ex: x not in y

available = ["A", "B", "C", "D"]

seat = input("Which seat? [A/B/C/D]: ").upper()

while seat not in available:    #while the "seat" value input by the user is not in the "available" list, run the following sequence of code

    print("---Only A/B/C/D accepted---")

    seat = input("Which seat? [A/B/C/D]: ").upper()

print(f"Thank you for providing a valid seat.\nYou have chosen seat: {seat}.")      #so this runs when the user enters a valid seat choice (A/B/C/D)