# Write a function named double_list that takes a list of strings as 
# a parameter and that replaces every string with two of that string. 
# For example, if the list stores the values ["how", "are", "you?"] 
# before the function is called, it should store the values 
# ["how", "how", "are", "are", "you?", "you?"] after the function finishes executing.

def double_list(str_list):
    for i in range(len(str_list) - 1, -1, -1):
        str_list.insert(i + 1, str_list[i])
