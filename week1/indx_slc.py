# indexing and slicing of arrays; think of pulling cards from the deck.
# indexing starts at 0 (positional)
# use ":" to indicate a range. array[start:stop]
# Leaving start or stop empty will default to the beginning/end of array.

 
x = [0, 1, 2, 3, 4]

print "REPEAT AFTER ME: THERE ARE FIVE ITEMS IN THIS LIST/ARRAY"

print "The [:] alone shows everything in the array %s" % x[:]
print
print "The [1:] STARTS at the 2nd item, and shows the remainder of the array %s" % x[1:]

print
# It's starting and ending in the same place; therefore, it shows nothing. 
print "The 1:1 begins where it ends, thus shows nothing: %s"  % x[1:1]
print
print "The [1:-1]shows '1' as 2nd item, and '-1', the last item, is ALWAYS excluded: %s." % x[1:-1]

print
# two colons can be used to indicate a step-size. array[start:stop:stepsize]
print "The [1::2] starts index at '1' and 'steps' by 2: %s" % x[1::2]
print
# array[start:stop:stepsize]
# step-size: go to the end and step backwards by two(-2)
print "The [-1::-2] shows last item of the list, then steps back by two: %s" % x[-1::-2]

print
print "The [:2] shows the list, %s, up to the 2nd item, EXCLUDING the second item." % x[:2]

print
print "The [::] shows.....%s. It's the same as [:]" % x[::]

print
print " This starts the index and then shows the rest of the list [-1:] %s" % x[:-1]
print

print "REMEMBER: [start:step:end]. Step is optional. SET THE INDEX. END CHAR IS OMITTED."