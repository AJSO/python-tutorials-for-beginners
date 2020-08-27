# The goal of the binary search algorithm is to look through an already sorted sequence and 
# determine whether or not the item we're looking for is in the sequence.
# Takes the mid-point as the starting point for the search.
# if Search < Mid-point = check Left
# if Search == Mid-point = return Position#
# binary search complexity: nx1/2x1/2x1/2 = n/2^k
# where n = len(sequence) 
#       k = number of steps

def BinarySearch(sequence, item):
    # we need to know the beginning and the end of the sequence
    begin_index = 0 #first element
    end_index = len(sequence)-1 #last Element

    while begin_index <= end_index:
        #the midpoint should be the middle position btn the begining index and the 
        # rest of the item in our sequence
        midpoint = begin_index + (end_index - begin_index) // 2
        # comparing the midpoint to the value that we are searching for.
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            #return the position
            return midpoint

        elif item < midpoint_value:
            # we change our ending position
            end_index = midpoint-1
        else:
            # if the item is greater than the midpoint_value
            begin_index = midpoint + 1

    return None

sequence_a = [1,2,4,5,6,7,8,9,9]
item_a = 9

print(BinarySearch(sequence_a, item_a))
