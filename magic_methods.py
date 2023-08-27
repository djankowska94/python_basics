class Book():

	def __init__(self,title,author,pages):
		
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}"

	def __len__(self):
		return self.pages

	#extra things happening when deleting using del
	def __del__(self):
		print("A book object has been deleted")
	

b = Book('Gioconda Smile', 'Aldous Huxley', 100)

print(b)


