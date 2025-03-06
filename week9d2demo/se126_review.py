#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp
#the greater value is put inside of a temp variable while the first two variables are equal to one, then that second variable is made equal to the third temp variable which is what needed 2 be second bc it is greater


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists --hand populated here
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list[len(names_list) - 1])       #last value OR see below
print(names_list) #remind her that she said there's another method we haven't done here to cover this

#creation & population of dictionaries
people_dictionary ={
    #"key" : value (if string, then you use "")
    "fname" : "George",
    "mname" : "Bullet",
    "lname" : "Wayne",
    "age" : 12, #NO key name duplicates, it won't tell you but it will only take the last added value pairing of that duplicate key

}

print(people_dictionary) #displays ALL keys & values in the dict
print(people_dictionary["fname"]) #this is how you print out specific indexes, using the KEY=INDEX STRING
#better to have mixed data types in dicts, than in lists -> but the best method 4 mixed data is objects

#create an empty list 4 each potential field (even the uneven field ---only a few have a red value at the end) --these allow us 2 make parallel lists
#these MUST remain the same length in order 2 be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#create an empty dictioanry
dragons = {} #store data to file

#gaining data from a text file 
with open("week9d2demo\dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #take all of the data in csv, and store every row/record
        print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0]) #always add to the end, which here is 0 index/first value
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
            tempColor = rec[4]

        else:
            color2.append("---") #we need this 2 make both lists parallel
            tempColor = ("---")

        #adding data to a dictionary
        dragons.update({ rec[0] : [rec[1], rec[2], rec[3], tempColor] }) #store a key to a techical list, making a dict somewhat like a 2d list --> used when we want to store multiple values to a key when typically it's 1 key equals 1 value


#processing data from collections
#lists --> standard: for index in range():
#headers must go outside of for loop
print(f"{'NAMES':12}   {'RIDERS':30}   {'NIMS':4}   {'COLOR1':8}   {'COLOR2'}")
print("-" * 75)

for index in range(0,len(names)):
    print(f"{names[index]:12}   {riders[index]:30}   {nums[index]:4}   {color1[index]:8}   {color2[index]}")

#dictionaries --> for key in collections
for key in dragons:
    print(f"{key.upper()} : {dragons[key]}") #this will show the values as a 1D list to the console
    #if we wanted to look at individual values, need 2 build another for loop(above is outer, this list below is called inner)
    for value in dragons[key]:
        #loops thru each value in the list found at the current key
        print(f"{key} - {value}", end="") #the end part just means that the two values will continue to print on the same lines, instead of separate
    print()

    for index in range(0,len(dragons[key])):
        print(f"{key} / {dragons[key][index]}")
    print("\n")


#searching & sorting
#sequential!!! best for duplicates, unordered data, etc.
#here we're doing it in a dict that resembles a 2d list
search = input("\nEnter the Dragon RIDER'S name you wish to find: ")

found = [] #best 2 use a list when there's going to be multiple returns or if you're using non exact matches/"in"

for key in dragons:
    if search.lower() in dragons[key][0].lower():
        found.append(key)

if not found: #found is still an empty list
    print(f"\n Sorry, we couldn't find {search} :[ ")
else:
    print(f"We have found your search for {search} !!!! Here are the results: ")
    
    for index in range(0,len(found)): #found is a list of keys
        print(f"{found[index].upper():12} {dragons[found[index]][0]:30} {dragons[found[index]][1]:3} {dragons[found[index]][2]:8} {dragons[found[index]][3]}")



#binary search ----> requires a set of ORDERED + UNIQUE data (here, ONLY the names are unique) -- SO NO DUPLICATES in BINARY
#must bubble sort first tho, bc it is NOT ordered, but it is also just good practice to always do it b4 binary search
#bubble is the same algorithm across languages, there's actually a built-in py func but we write it to understand it
for index in range(0,len(names) - 1):
    for j in range(0,len(names) - 1): #HAS to be a DIFFERENT iterator, NOT INDEX
        if names[j] > names[j+1]:
            #things now need to swap places!
            swap(j, names) #current index, and the list get swapped
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2) #everything must be swapped so EVERYTHING is moved together, not just one part of a person/item on the csv

#binary -> bi means 2 --> we create a high and low half of the list
search = input("\nPlease enter the DRAGON NAME you wish to find: ")

#must set up three values b4 going into a loop
min = 0 #represents first index
max = len(names) - 1 #last index 
mid = int((min + max) / 2)

#now we go into searching algorithm
while min < max and search.lower() != names[mid].lower(): #don't forget that BOTH need to be capital or lower
    if search.lower() < names[mid].lower(): #if what we're looking for is less than the middle, we don't need anything above that so disregard and continue with the lower half
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"\nWe found your search for {search} in record {mid}: ")
    print(f"{names[mid]:12}   {riders[mid]:30}   {nums[mid]:4}   {color1[mid]:8}   {color2[mid]}")
else:
    print(f"\nWe were NOT able to find your search for {search} :[ ")



#2D lists - lists of lists! 
letters = [
    ["A","B","C"],
    ["D","E","F"],
    ["G","H","I"]
]

print(letters)  #whole 2d list (you will see multiple []s)
print(letters[0])   #first list inside of 2d letters list
print(letters[0][0])    #first value of first list in 2d letters
print(letters[0][len(letters[0] - 1)])      #last value in first list in 2d

#negative indexing, index splicing