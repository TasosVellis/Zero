#!/usr/bin/env python
x = 25


def printer():
    x = 50
    return x


print(x)

print(printer())

# LEGB Rule
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

# lambda num: num ** 2


# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

# GLOBAL
name = "This is a global string"


def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'I AM A LOCAL'
        print('Hello ' + name)
    hello()


greet()
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
y = 50


def func(y):
    print(f'Y is {y}')

    # LOCAL REASSIGNMENT on a global variable
    y = "NEW VALUE"
    print(f'I JUST LOCALLY CHANGED global Y to {y}')
    return y


y = func(y)

# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
