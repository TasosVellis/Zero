# WARMUP SECTION

def lesser_of_two_evens(a, b):
    """
     a function that returns the lesser of two given numbers if both numbers are even,
    but returns the greater if one or both numbers are odd
    :param a: int
    :param b: int
    :return: int
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
    """
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

def animal_crackers(text):
    """
    a function takes a two-word string and returns True if both words begin with same letter
    :param text: str
    :return: bool
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    """
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


def makes_twenty(n1, n2):
    """
    Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
    If not, return False
    :param n1: int
    :param n2: int
    :return: bool
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False
    """
    return n1 == 20 or n2 == 20 or (n1 + n2) == 20


# LEVEL 1


def old_macdonald(name):
    """
    Write a function that capitalizes the first and fourth letters of a name¶
    :param name: str
    :return:str
    old_macdonald('macdonald') --> MacDonald
    """
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short!"

def master_yoda(text):
    """
    Given a sentence, return a sentence with the words reversed
    :param text: str
    :return: str
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    """
    return " ".join(text.split()[::-1])

def almost_there(n):
    """
    Given an integer n, return True if n is within 10 of either 100 or 200
    :param n:int
    :return: bool
    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    """
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# LEVEL 2

def has_33(nums):
    """
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
    :param nums:list of ints
    :return:bool
    """
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def paper_doll(text):
    """
    Given a string, return a string where for every character in the original there are three characters
    :param text:str
    :return:str
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    """
    new_text = ""
    for ch in text:
        new_text += ch * 3
    return new_text


def blackjack(a, b, c):
    """
    Given three integers between 1 and 11, if their sum is less than or equal to 21,
    return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    :param a: int
    :param b: int
    :param c: int
    :return: int or str
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    """
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'

def summer_69(arr):
    """
    Return the sum of the numbers in the array,
    except ignore sections of numbers starting
    with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
    Return 0 for no numbers.
    :param arr: list of integers
    :return: int
    """
    get_result = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                get_result += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return get_result


# CHALLENGING PROBLEMS

def spy_game(nums):
    """
    Write a function that takes in a list of integers and returns True if it contains 007 in order
    :param nums: array
    :return: bool
    """
    code = [0, 0, 7, "x"]

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works
    return len(code) == 1

