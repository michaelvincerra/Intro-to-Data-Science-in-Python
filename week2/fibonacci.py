#x = 1
#y = 1

#def fib():
#	x, y = 1, 1
#	while y<x:
#		result.append(y)
#		x, y = x, x+y
#	return result 

#print fib



def fib(n):
 a, b = 1, 1
 for i in range(n - 1):
  a, b = b, a + b
 return a


print(fib(100))
