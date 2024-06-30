my_str = "Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers."

# split words by space charahter and put them into the new_str var as a list
new_str  = my_str.split( )
my_words = {}
counter = 1
for item in new_str:
    my_words[counter] = item
    counter = counter + 1

print(my_words)


# print(new_str)
# print(len(new_str))
