# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
test = st.split()
for i in test:
    if i.startswith("s"):
        print(i)

print("------------------------------------------")
# Use range() to print all the even numbers from 0 to 10.
for i in range(11):
    if i % 2 != 0:
        print(i)



print("------------------------------------------")
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
new_list = [i for i in range(1,51) if i % 3 ==0]
print(new_list)


print("------------------------------------------")

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
splitted_list = st.split()
print(splitted_list)
for word in splitted_list:
	if len(word) % 2 == 0:
		print("even!")



print("------------------------------------------")
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0:
		print("Fizz")



print("------------------------------------------")
# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

character_list = [word[0] for word in st.split()]
print(character_list)

