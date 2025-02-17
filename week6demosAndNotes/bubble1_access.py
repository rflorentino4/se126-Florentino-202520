#WEEK 8: BUBBLE SORT

#BUBBLE SORT is a method of sorting (ordering) lists
#REMINDER: Binary Search only works on ORDERED lists
#list can be ordered alpha/numeric:
#                   *INCREASING [ascending]
#                       low --> high ... where lower values are stored in earlier part of list [0]
#                         A --> Z
#                         1 --> 100
#                   *DECREASING [descending]
#                       high --> low ... where higher values are stored in earlier part of list [0]
#                         Z --> A
#                       100 --> 1










name = ["Mary", "Cathy", "Tom", "Whitney", "Adam", "Sam", "Betty", "Ed"]
age = [21, 33, 24, 28, 30, 31, 40, 68]

num_rec = len(name)

print("BEFORE SORTING----------------------------------")

for i in range(0,num_rec):
    print("INDEX: {0}\t {1:10} \t {2}".format(i, name[i], age[i]))








#BUBBLE SORT--------------------------------------------------------------------------------------
#this is an algorithm, so don't change it! it works just as it is!
#only piece that changes --> the list you are sorting by



#sorting NAME in INCREASING ORDER
for i in range(0, num_rec - 1):#outer loop -- shifts through list

    #not part of algorithm, for console display during demo
    #print("OUTER LOOP! i = ", i)

    for k in range(0, num_rec - 1):#inner loop -- performs the swap

        #not part of algorithm, for console display during demo
        #print("\tINNER LOOP! k = ", k)
        
        if (name[k] > name[k - 1]): #ordered by NAME, INCREASING {> for increasing, < for decreasing}

            #"if value in position 0 is greater than value in position 1 (after it), they must swap places because list is being ordered in increasing order"

            #if above is true, SWAP (below)

            #SWAP!
            temp = name[k]
            name[k] = name[k + 1]
            name[k + 1] = temp



            #If other data exists within original record (spread amongst other lists) 
            #make sure to swap them too!
            temp_a = age[k]
            age[k] = age[k + 1]
            age[k + 1] = temp_a



print("\n\nBubble Sort complete.")


print("AFTER SORTING-----------ALPHA INCREASING-----------------------")
for i in range(0,num_rec):
    print("INDEX: {0}\t {1:10} \t {2}".format(i, name[i], age[i]))
