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
def byeKT():
    print(f"\n{'Have a good day KT :]' : ^65}\n")


#main executing code-----


#create lists for each POSSIBLE field in the text file records
type = []
brand = []
cpu = []
ram = []
firstDisk = []
nohdd = []
secondDisk = []
os = []
yr = []


#connected to file-------
with open("week3d2home/filehandling.csv") as csvfile: #don't forget to CHANGE the SLASH, you'll see a weird color if not
    print(f'\n{"Type":9} {"Brand":8} {"CPU":4} {"RAM":4} {"1st Disk":10} {"No HDD":7} {"2nd Disk":9} {"OS":6} {"YR"}') #this can be wherever you want, as long as it's NOT in the FOR LOOP ++++ be care of how you use single & double quotes, must use both to differentiate (I think? this works tho)

    file = csv.reader(csvfile)

    for rec in file: #occurs for every record/row in the textfile/2D list 
        #send type to list
        if rec[0] == "D":
            type.append("Desktop")

        elif rec[0] == "L":
            type.append("Laptop")

        #send brand to list
        if rec [1] == "DL":
            brand.append("Dell")

        elif rec[1] == "GW":
            brand.append("Gateway")

        elif rec[1] == "HP":
            brand.append("HP")
        
        #send 2-5 to list
        cpu.append(rec[2])
        ram.append(rec[3])
        firstDisk.append(rec[4])
        nohdd.append(int(rec[5]))
        
        #send the rest to list if no hdd is 1
        if int(rec[5]) == 1:
            secondDisk.append("-----") #this will be empty because 1's don't have a second disk
            os.append(rec[6])
            yr.append(rec[7])

        #send the rest to list if no hdd is 2
        else:
            secondDisk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
             

#--disconnected from file--------------------------------------------
      
#processing data from lists using FOR loop to print all of the file information
for index in range(0, len(type)): #this will run for as many i's/indexes there are in the list --incrementing by 1 each time
    print(f"{type[index]:9} {brand[index]:8} {cpu[index]:4} {ram[index]:4} {firstDisk[index]:10} {str(nohdd[index]):7} {secondDisk[index]:9} {os[index]:6} {yr[index]}")


#initialize counting variables
oldDesktop = 0
oldLaptop = 0


#processing data from lists using FOR loop
for index in range(0, len(yr)):
    if int(yr[index]) <= 16: #old
        if type[index] == "Desktop":
            oldDesktop += 1
        elif type[index] == "Laptop":
            oldLaptop += 1


#end report
print("---------------------------------------------------------------------------")
print(f"\nNumber of desktops that need to be replaced: {oldDesktop}. This will cost you ${oldDesktop * 2000:.2f}")
print(f"\nNumber of laptops that need to be replaced: {oldLaptop}. This will cost you ${oldLaptop * 1500:9.2f}")
print(f"\n**At a minimum, you will need ${oldDesktop * 2000 + oldLaptop * 1500:.2f} to replace all machines from 2016 and earlier.**")
print("---------------------------------------------------------------------------")
print(f"\nTotal records in the file: {len(type)}")

#my goodbye func
byeKT()