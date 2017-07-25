class Person:
	department = 'School of Information' # a class variable
	
	def set_name(self, new_name): # a method
		self.name = new_name
	def set_location(self, new_location):
		self.location = new_location
		
person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} lives in {} and works in the department {}'.format(person.name, person.location, 
		person.department))
		
	