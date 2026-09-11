# Write a function named is_sorted that accepts a list of real numbers as a 
#parameter and returns True if the list is in sorted (nondecreasing) order and 
# False otherwise. For example, if lists named list1 and list2 store 
#[16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the 
# calls is_sorted(list1) and is_sorted(list2) should return False and True respectively. 
# Assume the list has at least one element. A one-element list is considered to be sorted.

def is_sorted(nums):
    for i in range (len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
