def name_of_function(name):
	"""this is a doc string"""
	print("Hello " + name)


name_of_function("Jose")


def say_hello(name="Tasos"):
	print(f'Hello {name}')


say_hello('Angie')


def sum_numbers(num1, num2):
	return num1 + num2

# Return True if any number is even in a list

def check_even_list(num_list):
	"""

	return all the even numbers in a list
	"""

	even_numbers = []
	for number in num_list:
		if number % 2 == 0:
			even_numbers.append(number)
		else:
			pass
	return even_numbers


print(check_even_list([3, 5, 7, 10, 14]))

