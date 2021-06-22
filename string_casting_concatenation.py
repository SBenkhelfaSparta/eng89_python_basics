# using and managing strings
#  strings casting
# string concatenation
#  Casting methods

#  Single and double quotes
single_quotes = 'These are single quotes and working perfectly fine!'
double_quotes = "These are double quotes also working fine"

# print(single_quotes)
# print(double_quotes)

#  concatenation
# first_name = "James"
# last_name = "Bond"
# age = 22

# print(type(age))
# print(type(str(age)))


# create a variable called ge with int val and display age on the same line as james bond

# print(first_name + ' ' + last_name + ' ' + str(age))
#           01234567891011
# greetings = "Hello World"
                        #-1
# in python indexing start with 0
# print(greetings)
# to confrirm the length of the string as a method is len()
# print(len(greetings))
# print(greetings[0:5]) # slicing# the string from index 0 - 4 upto but not including 5
# print(greetings[-1]) # slicing string from the last index position

# print(greetings[6:])
# print(greetings[-5:])


# white_spaces = "Lots of white spaces            "
# we have strip() tgat removes all the whire spaces
#print(str(len(white_spaces)) + 'including white spaces')


# some more built in methods that we can use with strings

example_text = " here's some text with lots of text"

print(example_text.count('text')) #count() method count the word in string
print(example_text.lower()) # brings everything to lower case
print(example_text.upper()) #brings everything to upper case
print(example_text.capitalize()) #capatilsises the first letter
print(example_text.replace('with', ','))