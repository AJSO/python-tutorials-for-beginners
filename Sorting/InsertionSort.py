# Insertion sort takes unsorted sequence and divides it into sublist.

def InsertionSort(itemlist):

    indexing_length = range(1, len(itemlist))
    for i in indexing_length:
        value_to_sort = itemlist[i]

        # check if the value to the left is higher than the value that we're trying to sort
        while itemlist[i-1] > value_to_sort and i > 0:
            itemlist[i], itemlist[i-1] = itemlist[i-1], itemlist[i]
            # incrementing through the list
            i= i - 1

    return itemlist

print(InsertionSort([7,5,2,13,6,7,4,3,2,7,1,34,64,23]))

# InsertionSort is faster than the bubble and selection Sort