źclass Dog():
	
	#CLASS OBJECT ATTRIBUTE
	#SAME FOR ANY INSTANCE OF THE CLASS
	species = 'mammal'


	def __init__(self, breed, name, spots):
		#attributes
		self.breed = breed
		self.name = name
		#expect a boolean
		self.spots = spots

	#number is without self because it is not referencing anything in the instance of the class
	#you dont need to provide name in bark() because it's already defined in the clas	
	def bark(self, number):
		print("WOOF! My name is {} and the number is {}".format(self.name,number))




#instance of my class:
my_dog = Dog(breed='Lab', name='Lusia', spots=False)

print(my_dog.name)
print(my_dog.species)
my_dog.bark(number=8)
