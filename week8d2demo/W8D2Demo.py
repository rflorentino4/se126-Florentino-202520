#W8D2 Dictionary Review + Gaining Data from Text Files
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------

#this file uses: dictionary_file.csv

#IMPORTS------------------------------
import csv

#FUNCTIONS----------------------------


#MAIN EXECUTING CODE------------------
library = {              #flat bracket=list , curl braces=dictionary
    #'key' : value
    "1230" : "Red Rising",   #both go in quotation marks tho !
    "1231" : "The Little Prince",

}

with open("week8d2demo\dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following
        #file --> 2D list; rec --> 1 record's data also a list!
        library.update({rec[0] : rec[1]})  #similar to .append in lists + but follows same key value pairing to denote it's a dict (so curl braces)
        #libraryNum --> rec[0], a string
        #title --> rec[1], also a string

#disconnected from file-----------------
print(f"\n{'KEY':4} : {'TITLE'}")
print("-" * 50) #this works????

for key in library: 
    #for every key found in the library dictionary
    print(f"{key:4} : {library[key]}")
print("-" * 50)

#Sequential Search with Dictionaries --> only way to search through multiple search returns/strings
search = input("\nEnter the TITLE you are looking for: ")

found = 0 #use anything that you are sure IS NOT a key in your dict

for key in library:
    if search.lower() == library[key].lower():
        found = key

#if there were multiple return values: 1. found would equal a list = [] 2. change "==" to "in" 3. "found=key" becomes "found.append(key)" 4. for loop would change to "for index in range(0,len(found)): print (f"{found[index].upper:4} : {library[found[index]]}")

if found != 0:
    print(f"\nWe have found your search for {search}, here is the info: ")
    print("-" * 50)
    print(f"{found.upper():4} : {library[found]} ")
    print("-" * 50)

else:
    print(f"\nWe could not find your search for {search} :[ ")


#Sequential Search with Dictionaries --> only way to search through multiple search returns/strings
search = input("\nEnter the LIBRARY NUMBER you are looking for: ")

found = 0 #use anything that you are sure IS NOT a key in your dict

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"\nWe have found your search for {search}, here is the info: ")
    print("-" * 50)
    print(f"{found.upper():4} : {library[found]} ")
    print("-" * 50)

else:
    print(f"\nWe could not find your search for {search} :[ ")