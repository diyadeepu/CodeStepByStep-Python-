# Write a function named get_percent_even that accepts a list of integers as a 
# parameter and returns the percentage of the integers in the list that are even numbers. 
# For example, if a list a stores [6, 4, 9, 11, 5], then your function should 
# return 40.0 representing 40% even numbers. If the list contains no even elements 
# or is empty, return 0.0. Do not modify the list passed in.

def get_percent_even (array):
    evenCount = 0.0
    if (len(array) == 0):
        return 0.0
    for i in array:
        if (i % 2 == 0):
            evenCount += 1.0
    percent = evenCount/len(array)
    totalPercent = percent * 100
    return totalPercent
