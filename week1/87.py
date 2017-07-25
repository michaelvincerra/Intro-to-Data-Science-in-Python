#purpose: create a list and convert it to a 'numpy' array.
import numpy as np

mylist = [1, 2, 3, 4, 5, 6]
x = np.array(mylist)
print x

y = np.array([4, 5, 6])
print y

m = ([[ 7, 8, 9], [10, 11, 12]])
print m

#understand how SHAPE works. Currently this is an error. 
#print m.shape

# np.arange(START, STOP, STEP). Syntax for use of creating a specific ARRAY.

n = np.arange(0, 30, 2)
print "This is the np.arange function:", n

x = np.arange(0, 6, 2)
print "This is another np.arange function:", x


# reshape the array to be 3X5
n = n.reshape(3, 5)
print n

#NOTE: figure how to get the following to print...

o = np.linspace(0, 4, 9) #return 9 evenly spaced values from 0 to 4
# USES: np.linspace(START, STOP, HOW MANY NUMBERS SHOULD BE RETURNED).
print "This is 'linspace()': ", o

# resizes 'o' changes the DIMENSIONS and size of array in-place.
# resize LITERALLY DISPLAYS the array as 3 x 3 table.
o.resize(3,3)

# use of 'int' below produces ' whole numbers'.
print np.ones ([2, 3], int)

np.zeros ((2,3))

np.eye(3)

np.diag(y)

np.array([1, 2, 3] * 3)

# within the np.ones(...) in the [], 'rows', 'columns', in that order
p = np.ones([2, 3], int)

np.vstack([p, 2*p])
#print 

np.hstack([p, 2*p])


#OPERATIONS
print (x+y) #elementwise addition 
print (x-y) #elementwise subtraction
print (x * y) #elementwise multiplication
print (x / y) #elementwise power
print "x-squared", (x**2) # ** is the raise-to-power operator in Python, so x**2 means "x squared" in Python -- including numpy.

#dot product 1*4 + 2*5 + 3*6
print x.dot(y)

z = np.array([y, y**2])
print(len(z)) # number of rows of array 

z = np.array([y, y**2])
print z 

print z.shape
print z.T

#unsure??
print z.dtype
# error below: 'invalid syntax'
print z = z.astype('f'), "f stands for 'float32'."
















