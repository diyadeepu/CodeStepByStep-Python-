# Write a function named average that accepts a list of integers as its
# parameter and returns the average (arithmetic mean) of all elements in the 
# list as a float. For example, if the list passed contains the values [1, -2, 
# 4, -4, 9, -6, 16, -8, 25, -10], the calculated average should be 2.5. You may 
# assume that the list contains at least one element. Your function should not 
# modify the elements of the list.

def average(list_input: list[int]) -> float:
    sum = 0
    for i in list_input:
        sum += i
    return sum/len(list_input)
