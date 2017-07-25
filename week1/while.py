

x = [1, 'a', 2, 'b']


print "EXAMPLE 1"

i = 0
# while "i" does NOT equal length of x, or 4 items, continue.
while (i !=len(x)):
	#print/repeat loop as long as the product of (x[i]) remains true (or < 4)
	print (x[i])
	# where i += 1 continues until false, at which point loop is exited
	i = i +1

#The value so far, with each iteration, is 1, 2, 3 and 4 times, (1, a , 2, b) because there are 4 items in the list)
#i = int(0)

#while (i <=len(x)-1):
#	print (x[i])
#	i = i +1

print "EXAMPLE 2"

i = 0
#in an array, does the -1 include the final character?
while (i <=len(x)-1):
	print (x[i])
	i = i +1
	
print "EXAMPLE 3"
	
i = 0
while (i < len(x)):
	print (x[i])
	i = i +1
	
	