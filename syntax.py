if 5 > 2:
    print("Five is greater than two")

x = 5
y = "Hello, world!"

# comment

# python variables can change data type after assignment

john = "john"  # typeof str
john = 2  # typeof int

patrick = 'patrick'
# is the same as
patrick = "patrick"

w, u, i = 1, 2, 3  # allows you to assign values to multiple variables in one line
o = p = n = 4  # this is allowed too

b = "awesome"
print("Python is " + b)

# three types of numbers: int, float, complex
x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(z))
# type conversion with the int(), float() and complex() methods, except for the complex numbers
# random number with the random() function

# casting int(), float(), str()
x = int("1")

b = "Hello, world!"
print(b[2:5])

# string len() - length, strip() - rm whitespaces, lower() - lowercaseing, upper() - uppercasing
# replace(), split() - splits it into separate substrings
# in, not in - similar to js match()
# concat with + operator

age = 36
text = "My name is John Doe and I'm {} years old"
print(text.format(age))  # utilizes the placeholder {} to insert the int into the str

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# list: append(), insert(), remove(), pop()
# del deletes the whole list
# listName.copy(), or list()
# join with + operator or append() - one by one, extend() - whole
# sort()

# array types: list, tuple, set and dictionary
# list: ordered and changeable []
# tuple: ordered and unchangeable (), but there's a workaround, convert it into a list, modify, then convert back
# set: unordered and unindexed {}, you cannot refer to it with indeces, cannot change its items, but can add new
    # add() - one item, update() - two or more
    # remove(), discard() - difference is if the item is not present the remove will throw, but the discard will
        # not throw an error
    # pop()
    # clear() - empties the set
    # del
# dictionary: unordered, changeable and indexed {} but with keys and values, such like the js objects
    # you access items by its key
    # you add new item by making a new key and assigning a value to it, syntax: dict["newKey"] = newValue
