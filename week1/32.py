# Dictionary sets an equivalency; uses {} as container, uses 'key: value' pairs.

x = {'Christopher Brooks': 'brooks@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] #Retrieve a value by using the indexing operator
 
x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']
 
#in for loops note how the name variable occurs before it's defined.  
for name in x: 
 	print (x[name])
 	
#in for loops note how the email variable occurs before it's defined. 
# yet items is universal as a way to call items from a list. 	
for email in x.items():
	print(email)
	
	

	