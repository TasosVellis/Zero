# def square(num):
#    return num ** 2


# my_nums = [1, 2, 3, 4]

# print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


numbers = [1, 2, 3, 4, 5, 6]
# print(list(filter(check_even, numbers)))


print(list(map(lambda num: num ** 2, numbers)))

print(list(filter(lambda num: num % 2 == 0, numbers)))

print(list(map(lambda name: name[::-1], names)))
