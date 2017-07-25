import csv

#%precision 2

#where is the file mpg.csv!!!
with open('mpg.csv') as csvfile:
    # converting to a list of dictionaries
	mpg = list(csv.DictReader(csvfile))
	
print mpg[:3] # The first three dictionaries in our list.


#60
print len(mpg)

print mpg[0].keys

#find the city fuel economy standard across cars
print sum(float(d['cty']) for d in mpg / len(mpg)

# find the average hwy fuel economy across all cars. 
print sum(float(d['hwy']) for d in mpg / len(mpg)



#understand this lesson and the use of 'lambda' function. 
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

