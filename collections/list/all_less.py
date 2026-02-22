# Write a function named all_less that accepts two lists of integers and returns
# True if each element in the first list is less than the element at the same 
# index in the second list. Your function should return false if the lists are 
# not the same length. For example, if the two lists passed are [45, 20, 300] 
# and [50, 41, 600], your function should return True. If the lists are not the 
# same length, you should always return False.

def all_less(a: list[int], b: list[int]) -> bool:
    if (len(a) != len(b)):
        return False
    w = True
    for i in range (len(a)):
        if (a[i] > b[i]):
            return False
    return True
