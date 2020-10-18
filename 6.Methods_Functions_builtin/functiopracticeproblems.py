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

# Test
# there is a conflict here