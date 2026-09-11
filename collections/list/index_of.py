# Write a function named index_of that returns the index of a particular value 
# in a list of integers. The function should return the index of the first occurrence 
# of the target value in the list. If the value is not in the list, it should return -1. 
# For example, if a list called list stores the following values:

# list = [42, 7, -9, 14, 8, 39, 42, 8, 19, 0]
# Then the call index_of(list, 8) should return 4 because the index of the first 
# occurrence of value 8 in the list is at index 4. The call index_of(list, 2) 
# should return -1 because value 2 is not in the list.

def index_of(a, b):
    count = 0
    for i in a:
        if (i == b):
            return count
        count += 1
    return -1
