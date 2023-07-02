#!/usr/bin/env python3

class Foo():

	def __enter__(self):
		print("Enter...")

	def __exit__(self, type, value, traceback):
		print("...and exit.")

with Foo():
	print("Hello world!")

# often used case is with open('/path/to/file.txt', 'w') as wr which open a file for writing
# then use wr.write('something') to write to the file
