def add_nunbers(x,y,z=None, flag=False):
	if(flag):
		print ('flag is true!')
	if (z==None):
		return x+y
	else:
		return x+y+z
		
print(add_nunbers(1,2, flag=True))
