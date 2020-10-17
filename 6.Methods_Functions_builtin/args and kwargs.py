def my_func(*args):
    return sum(args) * 0.05
    # Return 5% of the sum of a and b

# *args
# When a function parameter starts with an asterisk, it
# allows for an arbitrary number of arguments,
# and the function takes them in as a tuple of values


print(my_func(40, 60, 50, 100))


# *kwargs
# Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments.
# Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs.
# For example:
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(
            f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")


myfunc(fruit='pineapple')


# *args and **kwargs combined
# You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')
