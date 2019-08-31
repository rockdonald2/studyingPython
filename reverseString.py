def reverse_string(string):
    new_string = ""

    for x in reversed(string):
        new_string += x

    return new_string


print(reverse_string("reverse this"))

def reverseString(string):
    return string[::-1]


name = input("Enter a string: ")
print(reverseString(name))
