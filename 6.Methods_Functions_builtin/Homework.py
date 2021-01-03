#!/usr/bin/env python
import collections
import string


def vol(rad):
    """
    Write a function that computes the volume of a sphere given its radius.

    The volume of a sphere is given as 4/3 πr^3
    vol(2) -> 33.49333333333333
    """
    p = 3.14
    return 4 / 3 * p * pow(rad, 3)


print(vol(2))


def ran_check(num, low, high):
    """
    Write a function that checks whether a number is in a given range
    (inclusive of high and low)
    ran_check(5,2,7)-> 5 is in the range between 2 and 7
    """
    if num in range(low, high + 1):
        return '{} is in the range between {} and {}'.format(num, low, high)
    else:
        return 'The number is outside the range'


print(ran_check(8, 2, 7))


def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(5, 2, 7))


def up_low(s):
    """
    Write a Python function that accepts a string and calculates the number of upper
    case letters and lower case letters.
    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33
    """
    countlower = 0
    countupper = 0
    for ch in s:
        if ch.islower():
            countlower += 1
        elif ch.isupper():
            countupper += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : " + str(countupper))
    print("No. of Lower case Characters : " + str(countlower))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Collections example


def high_low(t):
    c = collections.Counter("upper" if x.isupper(
    ) else "lower" if x.islower() else "empty" for x in t)
    return c


t = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(high_low(t))


def unique_list(lst):
    """
    Write a Python function that takes a list and returns a new list with unique
    elements of the first list.
    unique_list([1,1,1,1,2,2,3,3,3,3,4,5])=> [1, 2, 3, 4, 5]
    """
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numbers):
    """
    Write a Python function to multiply all the numbers in a list.
    multiply([1,2,3,-4]) -> -24
    """
    cummulator = 1
    for i in numbers:
        cummulator *= i
    return cummulator


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    """
    Write a Python function that checks whether a passed in string is palindrome or not.
    Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
    palindrome('helleh')-> True
    """
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('nurses run'))


# HARD

def ispangram(str1, alphabet=string.ascii_lowercase):
    """
    Write a Python function to check whether a string is pangram or not.
    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"
    ispangram("The quick brown fox jumps over the lazy dog")->True
    """
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


text = "The quick brown fox jumps over the lazy dog"
text.replace(" ", "")
print(set(text.lower()))
print(ispangram(text, alphabet=string.ascii_lowercase))
