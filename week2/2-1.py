import pandas as pd
# pd.Series? Use the latter command to see the default settings for pd.Series?


animals = ['Tiger', 'Bear', 'Moose']
print pd.Series(animals)

numbers = [ 1, 2, 3]
print pd.Series(numbers)


animals = ['Tiger', 'Bear', None]
print pd.Series(animals)

numbers = [1, 2, None]
print pd.Series(numbers)
#NaN = Not_a_Number; 
#Similar to None, but a numeric value, more efficient


import numpy as np
#np.nan == None
#False

original_sports = pd.Series({'Archery': 'Bhutan',
					'Golf': 'Scotland',
					'Sumo':	'Japan',
					'Taekwondo': 'South Korea'})

cricket_loving_countries = pd.Series(['Austrialia',
									'Barbados',
									'Pakistan',
									'England'],
									index=['Cricket',
											'Cricket',
											'Cricket',
											'Cricket'])
# note that the append call is made below AFTER original


# SEE APPEND method below, which allows creates of new, all_countries, without changing the original Data Series.
all_countries = original_sports.append(cricket_loving_countries)

print
print  "all_countries"
print pd.Series(all_countries)
print
print "cricket_loving_countries"
print cricket_loving_countries

# iloc/loc are ATTRIBUTES not methods

# Use iloc to see 4th country (remember: 0,1,2,3)


s= pd.Series([100.00, 120.00, 101.00, 3.00])
# iloc Uses index to search for the LABEL to which the index number corresponds.
print s.iloc[3]

# loc Uses label to searches for the INDEX to which label corresponds.
#s.loc['Golf']


total = 0
for item in s:
	total += item #iterate... see also the #while loop
print(total)



# Produces same result as above formula
import numpy as np
total = np.sum(s)
print(total)


s = pd.Series(np.random.randint(0, 1000, 10000))
print s.head()
#limits results to first five elements


print "Ex.`"
# %%timeit


#%%timeit -n 100
#summary = 0
#for item in s:
#	summary += item

#%%timeit -n 100
#summary = np.sum(s)

s+=2 #add 2 to each item using broadcasting
print s.head()

#if iterating thru a series, are you doing it in the most efficient way?
#alternative, slower, way:

for label, value in s.iteritems():
	s.set_value(label, value+2)
print s.head()

#compare processing speed of EX. 2

print "Ex.2"

#%%timeit -n 100
#for label, value in s.iteritems():
#	s.loc[label] = value+2


#%%timeit -n 100
#a = pd.Series(np.random.randint(0,1000, 10000))
#s += 2



s = pd.Series([1, 2, 3])
#s.loc['Animal'] = Bears
print s


