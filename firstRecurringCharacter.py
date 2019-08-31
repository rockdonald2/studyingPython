def first_recurring_character(string):
    h = {}

    for letter in string:
        if letter in h:
            return letter
        else:
            h[letter] = 0

    return '\0'


print(first_recurring_character("geeksforgeeks"))
