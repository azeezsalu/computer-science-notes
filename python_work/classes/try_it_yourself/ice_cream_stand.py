class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} sells {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'cherry', 'galato']

	def describe_flavors(self):
		print("This are the flavors:")
		for flavor in self.flavors:
			print(flavor.title())

IceCreamStand = IceCreamStand('popeyes', 'chichen sandwich')
IceCreamStand.describe_flavors()