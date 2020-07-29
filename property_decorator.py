# @property is a built-in decorator for the property()
# function in Python. It is used to give "special"
# functionality to certain methods to make them act as
# getters, setters, or deleters when we define properties in a class. 


class Product:
	def __init__(self, init_price):
		self.price = init_price # note that we are calling our setter

	@property # this is the getter
	def price(self):
		return self.__price

	@price.setter
	def price(self, new_price):
		if new_price<0:
			raise ValueError("A product cannot have a negative value")
		else:
			self.__price = new_price
			print(f"The price has been updated succesfuly with {new_price}")
	
	@price.deleter
	def price(self):
		del self.__price
		print("The attribute has been deleted")


carrot = Product(12)
print(carrot.price) # accessing (getter)
carrot.price = 1000 # updating the value (setter)
print(carrot.price) # accessing (getter)
del carrot.price # deleting the attribute (deleter)
#print(carrot.price) # accessing (getter), this will raise an error

	