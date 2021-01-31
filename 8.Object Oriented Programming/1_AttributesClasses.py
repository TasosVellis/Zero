class Dog:
    # Class object attributes
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # Operations/Actions --> Methods
    # You can use references for methods or for classes. without self and with self
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))


my_dog = Dog('Lab', "Frankie")
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
my_dog.bark(10)


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(15)
my_circle.get_circumference()
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
