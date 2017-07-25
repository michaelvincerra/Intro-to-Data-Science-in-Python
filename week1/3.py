def add_numbers(x,y,z=None):
	if (z==None):
		return x+y
	else:
		return x+y+z


# Purpose: 'add_numbers' becomes the argument that executes the math x + y, etc.

print(add_numbers(1,2))
print(add_numbers(1,2,3))