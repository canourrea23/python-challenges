# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# string_empty = []
# string_forward = "This_is_a_string"
# string_forward.split(" ")
# string_empty[:] = string_forward
# rev_string = " "
# for i in range(len(string_empty)):
#     rev_string += string_empty[len(string_empty) - 1 - i]
 
    
# print(rev_string)    


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

while True:
    string = input("Enter string: ")
  
    print ("The original string is : ", string) 
    
    print ("The reversed string is: ", (reverse(string)))
