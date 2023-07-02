#!/usr/bin/env

class DreamCake:
	# Measurements are defined in grams or units
	eggs = 4
	sugar = 300
	milk = 200
	butter = 50
	flour = 250
	baking_soda = 20
	vanilla = 10

	topping = None
	garnish = None

	is_baked = False

	def __init__(self, topping='No topping', garnish='No garnish'):
		self.topping = topping
		self.garnish = garnish

	def bake(self):
		self.is_baked = True

	def is_cake_ready(self):
		return self.is_baked

# A plain cake
plain_cake = DreamCake()
# A chocolate cake
chocolate_cake = DreamCake(topping='Chocolate frosting')
# A luxury cake (using named parameters)
luxury_strawberry_cake = DreamCake(topping='Strawberry frosting', garnish='Chocolate bits')
# A luxury cake (using positional parameters)
luxury_strawberry_cake = DreamCake('Strawberry frosting', 'Chocolate bits')

chocolate_cake.bake() # Call the function
is_cake_done = chocolate_cake.is_cake_ready()

print(is_cake_done) # Prints "True" because we called "bake" earlier
