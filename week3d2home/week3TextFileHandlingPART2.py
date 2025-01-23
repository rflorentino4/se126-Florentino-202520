#W3D2 Text File Handling PT 2 + lists
#Romina Florentino 
#SE126-2025.20
#---------------------------------------------

#DIRECTIONS: This in-class lab is a continuation of Lab #2, where instead of processing the data directly from the file, you will first store the data to lists (one list for every possible field in the text file records) and then use for loops to complete your printing and computing for cost.
#---------------------------------------------

#PROGRAM PROMPT: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.
#---------------------------------------------

#imports-----------------
import csv

#functions---------------

#main executing code-----

#initialize my counting variable
totalRec = 0

#connected to file-------
with open("week3d2home/filehandling.csv") as csvfile: #don't forget to CHANGE the SLASH, you'll see a weird color if not
    file = csv.reader(csvfile)

    for rec in file: #occurs for every record/row in the textfile/2D list
        totalRec += 1
        
