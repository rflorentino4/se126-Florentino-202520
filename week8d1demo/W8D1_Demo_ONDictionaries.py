#W8D1 Collections and Logic
#Romina Florentino 
#SE126.04 - 2025
#---------------------------------------------
#PROGRAM PROMPT: Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. The keys are reffered to as properties and the values can be any data type.

#IMPORTS------------------------------

#FUNCTIONS----------------------------
def byeKT():
    print(f"\n\t\t\t\tHave a good day KT :]\n")

#MAIN EXECUTING CODE------------------

#start by creating a populated dictionary
myCar = {
    #'key' (string) : value,
    "make" : "Ford" ,
    "model" : "Focus SE Hatchback" ,
    "year" : 2014 , 
    "name" : "Gwendoline" , 
    "color" : "black" ,
    #key names CANNOT BE repeated / no duplicates of keys!!!!
    #if you run a duplicate command, it will just print the latest value you set equal to a key
}

#view the entire dictionary and all of its data ----->> it shows you both the key and the value exactly as entered, not pretty...
print(myCar)
#OUTPUT:
#{'make': 'Ford', 'model': 'Focus SE Hatchback', 'year': 2014, 'name': 'Gwendoline', 'color': 'black'}

#view a specific value from the dictionary --> name[key] --> value
print(f"\nMy car is a {myCar["make"]} {myCar["model"]}. \n") 
#OUTPUT:
#My car is a Ford Focus SE Hatchback.

#everything is stored UNDER the dictionary name

#new dictionary
yourCar = {
    #'key' (string) : value,
    "make" : "Ford" ,
    "model" : "F-150" ,
    "year" : 2024 , 
    "name" : "Gandalf" , 
    "color" : "gray" ,
    "friends" : ["Tyler", "Tony", "Steve"]
    #these are STRINGS, capitalization + spelling MATTERS !!!!
}

#print yourCar dict
print(f"My car is a {yourCar["make"]} {yourCar["model"]}. It is {yourCar["color"]}. ")
#OUTPUT:
#My car is a Ford F-150. It is gray.

#add some data to a dict once created
yourCar["plate"] = "12345"

#or use the .update({key:value}) method --> way easier to edit in the actual dict, but if you're working across files or thousands of lines in, use this or the previous method to save the hassle
yourCar.update({"wheels" : "4"})


for key in yourCar:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():10}\t{yourCar[key]}")
    #OUTPUT is the following:
    #MAKE            Ford
    #MODEL           F-150
    #YEAR            2024
    #NAME            Gandalf
    #COLOR           gray    