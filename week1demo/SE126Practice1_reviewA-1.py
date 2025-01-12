#Romina Florentino
#SE126.04
#W1D2 Lab Demo: SE126 Review
#1-9-2025 [W1D2]

#PROGRAM PROMPT: This is a temperature conversion program, it allows a user to enter as many Fahrenheit temps as they'd like and then shows the Celsius conversion for each. It also counts the number of temps and determines the average of all temps entered. 

#VARIABLE DICTIONARY
#temp_count     the total number of all temps entered
#temp_total     the sum total of all temps entered
#avg_temp       the avg temp entered (avg_temp = temp_total / temp_count)
#tempF          the temp in Fahrenheit, entered by the user
#tempC          the temp in Celsius (tempC = (tempF - 32) * (5 / 9))
#answer         loop control; value determines if loop repeats, entered by the user

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
def again(): #<--FUNCTION HEADER
    '''this function asks a user if they would like to enter another temp, checks the response for validity, and then returns a valid response back to the main program'''

    ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower() #ans only exists within this function (local var)

    #user error trap loop - ensures user provides valid value ---don't use if
    while ans != "y" and ans != "n":
        print ("***INVALID ENTRY!***")
        ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower() #ans only exists within this function (local var)
    return ans #this value will replace the function call in the main code, MUST match indent of user error start/while loop

def converter(f): #f just means its waiting for a value -> it's just a parameter
    c = (f - 32) * (5 / 9) #after we give the parameter a value, it now becomes an argument (?)
    return c

#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
temp_count = 0
temp_total = 0

answer = "y" #loop control var

#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y" or answer == "Y": #this could also work as just again() and calling the value of the func
    #funcs that end in a return are just bringing back a value or values which is why this would work

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    #necessary calculations
    tempC = converter(tempF)

    #math processes needed later for average calculation
    temp_count = temp_count + 1 #temp_count += 1
    temp_total += tempF

    #display data to user = both show the same output
    print("\n\t\tTEMP# {0}\tTEMP {1:.1f}F = TEMP {2:.1f}C\n".format(temp_count, tempF, tempC))
    #print(f"\n\t\tTEMP# {temp_count}\tTEMP {tempF:.1f}F = TEMP {tempC:.1f}C\n")

    #loop control! allowing a way back in or out of the loop based on the value of answer
    answer = again() #return value will replace this function call and store to "answer" 
    #input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

#out of loop

#average calculation and conversion
avg_tempF = temp_total / temp_count 

avg_tempC = converter(avg_tempF)


#final displays
print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVGERAGE TEMP {0:.1f}F  |  {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThank you for using the program. Goodbye.\n\n")