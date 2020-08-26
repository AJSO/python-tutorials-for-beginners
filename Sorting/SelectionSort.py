# Selection sort tries to find the minimum value in a list.
# it sets the first number as the minimum and compares to every number in the list. 
# As soon as it comes accross the number lower than the firt number selected, it is assigned as the new minimum and the process continues.
# the minimum value will be moved to the left, and the select a new minimum value.

def Selection_Sort(list_item):
    # setting the range of the values.
    # -1 because once we have the last item in our unsorted list we don't need to do a comparison on it. 
    # instead we can assume it's the highest value in our list
    indexing_length = range(0,len(list_item)-1)
    # for every element(i)
    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_item)):
            if list_item[j] < list_item[min_value]:
                # replace the minimum value
                min_value = j

        # switching values
        if min_value != i:
            list_item[min_value], list_item[i] = list_item[i],list_item[min_value]

    return list_item

print(Selection_Sort([7,5,2,13,6,7,4,3,2,7,1,34,64,23]))

# The selection sort is better than the bubble sort. 
# coz it cuts down the number of item switches we need to do. that's we switch once or not at all.
# while in the bubble sort we switch through all items in the list each time we iterate