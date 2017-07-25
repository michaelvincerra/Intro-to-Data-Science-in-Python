import numpy as np


s = np.arange(13)
print s

#Use bracket notation to get the value at a specific index. 
#Remember that indexing starts at 0.
print s[0], s[4], s[-1]

#Use : to indicate a range. array[start:stop]
#Leaving start or stop empty will default to the beginning/end of the array.

print s[1:5]


#Use negatives to count from the back.

print s[-4]

#Let's look at a multidimensional array.
r = np.arange(36)
r.resize((6, 6))
print r


# use bracket notation to slice: array[row, column]
# define what slice means in this case!!!???
print r[2,2]

print r[3, 3:6]



# use ":" to select a range of rows or columns
#Here we are selecting all the rows up to (and not including) row 2, and 
#all the columns up to (and not including) the last column.
print r[:2, :-1]

#This is a slice of the last row and only every other element
print r[-1, ::2]

print r[r >30]

r[r > 30] = 30
print r





