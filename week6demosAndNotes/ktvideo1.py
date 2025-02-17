#Week 7: Bubble Sort

#Bubble sort is a method of sorting (ordering) lists
#REMINDER: Binary Search can only be performed on ORDERED LISTS
#lists can be ordered numerically or alphabetically (aka ALPHA mina)
#       increasing (ascending)
#       low -> high ... where lower values are stored in index [0] or earlier part of the list
#       A -> Z
#       1 -> 100
#       decreasing (descending)
#       high -> low ... where higher values are stored in index [0] or earlier part of the list
#       Z -> A
#       100 -> 1

name = ["Mary", "Cathy", "Tom", "Whitney", "Adam", "Sam", "Betty", "Ed"]
age = [21, 33, 24, 28, 30, 31, 40, 68]
#we have index [0] - [7] for both lists

numRec = len(name) #len() returns the length of the list passed to it

print("BEFORE SORTING---------------------------------------------")

for index in range(0, numRec):

    print("INDEX: {0} \t {1:10} \t {2}".format(index, name[index], age[index]))


#BUBBLE SORT----------------------------------------------------------
for index in range(0, numRec - 1): #outter loop

    print("OUTTER LOOP! index = ", index) #not necessary for algorithm

    for k in range(0, numRec - 1): #inner loop
        print("\tINNER! k = ", k)

        #below if statement determines the sort
        if (name[k] > name[k + 1]):
            #the if controls which values will swap
            #SWAP
            temp = name[k]
            name[k] = name[k + 1]
            name[k + 1] = temp

            #if other data exists within original record (spread among other lists) swap those values too
            tempA = age[k]
            age[k] = age[k + 1]
            age[k + 1] = tempA

print("\n\nBubble sort complete")

print("AFTER SORTING-----------ALPHA INCREASING-----------------------")

for index in range(0,numRec):
    print("INDEX: {0}\t {1:10} \t {2}".format(index, name[index], age[index]))