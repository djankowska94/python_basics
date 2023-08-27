#inheritance = a way to form new classes with the classes that have already been defined

#base class
class Animal():
	def __init__(self):
		print("ANIMAL CREATED")

	def who_am_i(self):
		print("I am an animal")

	def eat(self):
		print("I am eating")



class Dog(Animal):
	def __init__(self):
		#create an instance of an animal class when creating an instance of a dog class
		Animal.__init__(self)
		print("DOG CREATED")

	def who_am_i(self):
		print("I am a dog")
	

	def bark(self):
		print("WOOF!")


my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()



my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()






#polymorphism
class Dog():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says woof!"



class Cat():
	
	def __init__(self, name):
		self.name = name

	def speak(self):
		return self.name + " says meow!"


my_dog = Dog("Lusia")
my_cat = Cat("Lalek")


print(my_dog.speak())


for pet in [my_dog, my_cat]:
	print(type(pet))
	print(pet.speak())


def pet_speak(pet):
	print(pet.speak())


pet_speak(my_dog)
pet_speak(my_cat)

class Animal():
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")


my_animal = Animal("Fred")
#my_animal.speak()


class Dog(Animal):

	def speak(self):
		return self.name + " says woof!"

my_dog = Dog("Yogi")
my_dog.speak()
