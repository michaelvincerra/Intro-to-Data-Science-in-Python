#x = (1, 'a', 2, 'b')

# 'type' is calling out the object type only; no other function.
#print type(x)


x = [1, 'a', 2, 'b']
# 'type' is calling out the object type only; no other function.
print type(x)

x.append(3.3)
print(x)


for item in x:
	print(item)
	
	i=0		
	#using the index operator. ask Brooks how this works. 
	while( i != len(x)):
		print(x[i])	
		i = i +1

	