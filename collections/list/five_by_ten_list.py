# Write a piece of code that constructs a two-dimensional list of integers named 
# table with 5 rows and 10 columns. Fill the list with a multiplication table, 
# so that list element [i][j] contains the value i * j. Use for loops to build the list.

table = []
for i in range (5):
    a = []
    for j in range (10):
        a.append(i * j)
    table.append(a)
