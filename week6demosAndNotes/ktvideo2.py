#WEEK 8: BUBBLE SORT with a text file and MULTIPLE RETURN VALUES

#This demo uses the file: "GOT_bubble_sort.txt"


def swap(n, j):
    #this function receives two arguments to fulfill its parameters
    # a list (n) and a current index (j)

    #swap values
    t = n[j]
    n[j] = n[j + 1]
    n[j + 1] = t

    return n[j], n[j + 1]

#THE CALL TO THE ABOVE FUNCTION ON LINEs 78, 86, 88: 
#         _1stReturn_ , _2ndReturn_= swap(_list_, _index_)



import csv

num_records = 0

last_name = []
first_name = []
age = []



with open("week6demosAndNotes\GOT_bubble_sort.txt") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file:
        #print(rec)

        num_records += 1

        last_name.append(rec[0])
        first_name.append(rec[1])
        age.append(int(rec[2]))
print("Finished Processing File.\n\n")


print("{0:15} \t {1:15} \t {2:3}".format("LASTNAME", "FIRSTNAME", "AGE"))
print("--------------------------------------------------------------------")
for i in range(0, num_records): #print original lists to console

    print("{0:15} \t {1:15} \t {2:3}".format(last_name[i], first_name[i], age[i]))


#if we wanted to search for 1 person in the list (binary search!) we could NOT use lastname (there are multiples!) SO ... sort by FIRST NAME

#BUBBLE SORT --- Sort FIRSTNAMES in INCREASING ALPHA

for i in range(0, num_records - 1):

    for k in range(0, num_records - 1):
    
        if (first_name[k] > first_name[k + 1]): #Sorted by --> FIRSTNAME, INCREASING (>)

            #if above is true, perform the SWAP
            #temp_name = first_name[k]
            #first_name[k] = first_name[k + 1]
            #first_name[k + 1] = temp_name
            
            first_name[k], first_name[k + 1] = swap(first_name, k)
            #when passing a list to a function, you just pass the list name AND 
            #you must also pass ... the INDEX value! 
            #(1 current value if swapping, num_records value is processing)
            

            #SWAP REMAINING VALUES ASSOCIATED WITH NAME!

            last_name[k], last_name[k + 1] = swap(last_name, k)

            age[k], age[k + 1] = swap(age, k)


print("\n\nSORTED BY FIRST NAME--------------------------------------------\n")            
print("{0:15} \t {1:15} \t {2:3}".format("LASTNAME", "FIRSTNAME", "AGE"))
print("--------------------------------------------------------------------")
for i in range(0, num_records): #print original lists to console

    print("{0:15} \t {1:15} \t {2:3}".format(last_name[i], first_name[i], age[i]))



#BUBBLE SORT IN DECREASING ORDER

#sorted by age, decreasing

for i in range(0, num_records - 1):

    for k in range(0, num_records - 1):

        if (age[k] < age[k + 1]):#SORTED BY --> AGE, DECREASING (<)


            age[k], age[k + 1] = swap(age, k)

            first_name[k], first_name[k + 1] = swap(first_name, k)

            last_name[k], last_name[k + 1] = swap(last_name, k)
 

print("\n\nSORTED BY AGE-------------------------------------------------\n")            
print("{0:15} \t {1:15} \t {2:3}".format("LASTNAME", "FIRSTNAME", "AGE"))
print("--------------------------------------------------------------------")
for i in range(0, num_records): #print original lists to console

    print("{0:15} \t {1:15} \t {2:3}".format(last_name[i], first_name[i], age[i]))
