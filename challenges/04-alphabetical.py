# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = "jdslkfjoiawsdifadslkfjabu"
def alphabet(string):
    alphabetical = [ ]
    for i in string:
        alphabetical.append(i)
    alphabetical.sort()
    sorted = "".join(alphabetical)
    print(sorted)

alphabet(string)


# string = input('Give me a string to alphabetize: \n')

# sorted_list = sorted(string)

# sorted_string = ''.join(sorted_list)

# print("The original string is:", string)
# print('Sorted alphabetically, the string is:', sorted_string)
