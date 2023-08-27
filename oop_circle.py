class Circle():
	
	#class object attribute
	pi = 3.14
	#we can reference class object attributes with Circle.pi instead of self.pi, may be more readable

	#we set default radius = 1
	def __init__(self, radius=1):
		self.radius = radius
		self.area = self.pi * radius ** 2

	def get_circumference(self):
		return 2 * self.pi * self.radius


my_circle = Circle()
print(my_circle.get_circumference())

second_circle = Circle(radius=10)
print(second_circle.get_circumference())
