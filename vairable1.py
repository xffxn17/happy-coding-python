# now adding a vairable with plus for example
name = "celebrate"
# now lets print it
print("lets's " + name)  # never forget to add space in the string
# now lets change the value of name
name = "party"
print("lets's " + name)  # plus symbol is mandotory to concatenate two strings
# now lets try to fetch one character from the string
print(name[0])  # never forgot that the name is of the last value assigned to it
# it is starting from 0 index to upto n-1 index
# so in this case it will be 0 to 4 index
# so if i try to fetch 5th index it will give error
# print(name[5])  # Uncommenting this will give IndexError because 'party' has only 5 characters (0-4)
# now lets try negative numbers to fetch the characters
print(name[-1])  # it will give the last character of the string
# now for the first one it will be -5 index
print(name[-5])  # it will give the first character of the string
# now lets try to fetch the 2 characters from the string
print(name[0:2])  # it will give the first two characters of the string
# the last index is not included
print(name[1:4])  # it will give the characters from index 1 to 3
# now if i don't give the ending index it will go upto the last index
print(name[0:])  # it will give the characters from index 0 to last index
# what if i don't give the starting index
# it will give the characters from index 0 to the index 3 as 4 is not included
print(name[:4])
# what if i don't give both the starting and ending index
print(name[:])  # it will give the whole string
# what if i start from the middle of the string and go upto beyond the last index
print(name[2:10])  # it will give the characters from index 2 to last index
# it will not give error
# now lets try to change one character of the string
# name[0:3] = "fun"  # Uncommenting this will give TypeError because strings are immutable in Python
# It will give error because string is immutable
# For single character also it will give error
# name[0] = "F"  # Uncommenting this will give TypeError because strings are immutable
# to add something with the string we can use + with it depends on starting or ending you want to add
print("fun " + name)  # it will add fun at the starting of the string. here you got to add space after fun