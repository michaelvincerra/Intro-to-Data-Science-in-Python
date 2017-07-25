import numpy as np


a = np.array([-4, -2, 1, 3, 5])

b = np.array([0, 1, 2, 3, 4])

print a.sum()
 
print a.max()

print a.min()

print a.mean()

print a.std()


# to find the INDEX (?) of the maximum and minimum values in an array
# argmax returns index of first occurrence of maximum over requested axis.
# NA/null values are excluded. In both cases below, the index of the max value is 4, index starts at zero

a, maximum value is 5, index is 4. -4 index is zero

b, maximum value is 4, index is 4. o index is zero


print "a.argmax()", a.argmax()

print "b.argmax()",  b.argmax()


print a.argmin()



