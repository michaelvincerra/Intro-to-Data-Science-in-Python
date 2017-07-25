import numpy as np

#I added this from prev. exercise, 125.py
r = np.arange(36)
r.resize((6, 6))
print r

r2 = r[:3, :3]
print  r2

r2[:] = 0
print r2

print r

r_copy = r.copy()
print r_copy

r_copy[:] = 10
print (r_copy, 'n')
print (r)

#ITERATING OVER ARRAYS

test = np.random.randint(0, 10, (4, 3))
print test

for row in test:
	print (row)
	
#Iterate by index:
for i in range(len(test)):
	print(test[i])
	
#Iterate by row and index:
for i, row in enumerate(test):
	print('row', i, 'is', row)
	
test2 = test**2
print test2

for i, j in zip(test, test2):
	print(i, '+', j, '=', i+j)
		
print

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print x
x[1:7:2]
print "x[1:7:2]"
print "SLICE[1-START, 7-STOP, 2-STEP (EXCLUDE LAST)])", x[1:7:2]
# array([1, 3, 5])
