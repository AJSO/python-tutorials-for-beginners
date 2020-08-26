# The bubble sort takes an unordered list and orders it in ascending values. 
# This is done by comparing two values at any given time.
def bubbleSort(unsorted_list):
    # setting the range of values
    indexing_length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            # if item to the left is greater than item to the right
            if unsorted_list[i] > unsorted_list[i+1]:
                # the sorted variable it false
                sorted = False
                # flipping the two values in the list in comparison
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

    return unsorted_list

print(bubbleSort([7,5,2,13,6,7,4,3,2,7,1,34,64,23]))