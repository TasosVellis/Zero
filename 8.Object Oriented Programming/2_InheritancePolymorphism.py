# Inheritance is way to form new classes using classes that already have been defined
#
# class Animal:
#
#     def __init__(self):
#         print('Animal Created')
#
#     def who_am_i(self):
#         print('I am an animal')
#
#     def eat(self):
#         print("I am eating")
# Because I added Animal in Dog class, Dog is a derived class, Animal is a base class
# Derived classes override or extend the functionality of base classes

# class Dog(Animal):
#
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     # We can override as chosen
#     def who_am_i(self):
#         print("I am a dog")
#
#     def eat(self):
#         print("I am a dog and eating")
#
#     def bark(self):
#         print("WOOF!!")

#
# myanimal = Animal()
# myanimal.eat()
# myanimal.who_am_i()
# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()

# Polymorphism
# Refers to the way different object classes can share the same method name
# Example
# Real life polymorphism examples
# - opening different file types- pdf, excel, word
# - adding different objects - the + operator performs arithmetic and concatenation


class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

# Iterate through classes 1st option
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


# Abstract Classes
# An abstract is one that never expects to be instantiated
# Example we will never have an Animal object, only cat and dog object which are derived from Animal
#
class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


myanimal = Animal('fred')
myanimal.speak()