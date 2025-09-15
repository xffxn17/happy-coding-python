# what are data types in python
# data types are the classification or categorization of data items. it tells what type of value a variable is holding
# in python data types are dynamic which means we don't need to declare the data type of a variable while assigning a value to it. python interpreter will automatically assign the data type based on the value assigned to the variable
# there are several built-in data types in python some of them are
# 1. int - integer data type which holds whole numbers
# 2. float - floating point data type which holds decimal numbers
# 3. str - string data type which holds sequence of characters
# 4. bool - boolean data type which holds either True or False value
# 5. list - list data type which holds a collection of items in a particular order
# 6. tuple - tuple data type which holds a collection of items in a particular order and is immutable
# 7. dict - dictionary data type which holds a collection of key-value pairs
# 8. set - set data type which holds a collection of unique items
# 9. NoneType - NoneType data type which holds a special value None
# we can use type() function to check the data type of a variable
# we can use id() function to check the memory address of a variable

# let's see some examples of data types in python

# integer data type
num = 10
print(num)  # it will print 10
print(type(num))  # it will print <class 'int'>
# lets convert int to float
print(float(num))  # it will print 10.0
print(type(num))  # it will still print <class 'int'> because type of num is still int
# it will print <class 'float'> because float(num) is a float value
print(type(float(num)))

# float data type
pi = 3.14
print(pi)  # it will print 3.14
print(type(pi))  # it will print <class 'float'>
# now convert float to int
print(int(pi))  # it will print 3

# complex data type
comp = 2 + 3j
print(comp)  # it will print (2+3j)
print(type(comp))  # it will print <class 'complex'>

# now lets make a complex number from two numbers
a = 2  # it will be the real part of complex number
b = 4  # it will be the imaginary part of complex number
c = complex(a, b)  # it will create a complex number from a and b
print(c)  # it will print (2+4j)

# string data type
name = "happy coding"   # string can be defined using single quotes or double quotes

print(name)  # it will print happy coding

print(type(name))  # it will print <class 'str'>

# we can use triple quotes to define a multi-line string
multi_line_str = '''this is a multi-line string it can span multiple lines like this'''

print(multi_line_str)

print(type(multi_line_str))  # it will print <class 'str'>

# boolean data type
# it can hold either True or False value
# it is used to represent truth values
# it is often used in conditional statements and loops
# in python True is represented by 1 and False is represented by 0
# we can use bool() function to convert other data types to boolean
# for example
print(bool(1))  # it will print True
print(bool(0))  # it will print False
print(bool(-1))  # it will print True
print(bool(""))  # it will print False
print(bool("hello"))  # it will print True
print(bool([]))  # it will print False
print(bool([1, 2, 3]))  # it will print True
print(bool(None))  # it will print False
print(bool({}))  # it will print False
print(bool({"key": "value"}))  # it will print True
print(bool(()))  # it will print False
print(bool((1, 2)))  # it will print True
print(bool(set()))  # it will print False
print(bool({1, 2, 3}))  # it will print True
print(type(True))  # it will print <class 'bool'>
print(type(False))  # it will print <class 'bool'>
print(int(True))  # it will print 1
print(int(False))  # it will print 0
print(float(True))  # it will print 1.0
print(float(False))  # it will print 0.0
print(str(True))  # it will print 'True'
print(str(False))  # it will print 'False'
print(complex(True))  # it will print (1+0j)
print(complex(False))  # it will print 0j
print(type(bool(1)))  # it will print <class 'bool'>
print(type(bool(0)))  # it will print <class 'bool'>
print(type(bool("hello")))  # it will print <class 'bool'>
print(type(bool("")))  # it will print <class 'bool'>
# etc...

# for example

# lets define two boolean variables
a = 15  # integer variable
b = 17  # integer variable

print(a < b)  # it will print True because 15 is less than 17

print(a > b)  # it will print False because 15 is not greater than 17

print(a <= b)  # it will print True because 15 is less than or equal to 17

print(a >= b)  # it will print False because 15 is not greater than or equal to 17

print(a == b)  # it will print False because 15 is not equal to

print(a != b)  # it will print True because 15 is not equal to 17

# range in python
# range is a built-in function in python that is used to generate a sequence of numbers
# it is often used in for loops to iterate over a sequence of numbers
# range(stop) - it will generate numbers from 0 to stop-1
# range(start, stop) - it will generate numbers from start to stop-1
# range(10) it can also neglected  # it will generate numbers from 0 to 9
print(range(10))  # it will print range(0, 10)

print(list(range(10)))  # it will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# convert range to list to see the numbers
print(list(range(5, 15)))  # it will print [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# range(start, stop, difference) - it will generate numbers from start to stop-1 with a difference value means ex.
# range(0, 10, 2) - it will generate numbers from 0 to 9 with a difference of 2 ex in list it will be [0, 2, 4, 6, 8].

# lets try to print it with the difference value of 3
print(list(range(3, 30, 3)))  # it will print [3, 6, 9, 12, 15, 18, 21, 24, 27]

print(type(range(10)))  # it will print <class 'range'>

# dictionary data type in python
# dictionary is a built-in data type in python that is used to store a collection of key-value pairs
# it is also known as associative array or hash map in other programming languages
# it is unordered, mutable and indexed
# we can use curly braces {} to define a dictionary
# we can use key-value pairs to store data in a dictionary
# we can use keys to access the values in a dictionary
# we can use dict() function to create a dictionary
# in dinctionary keys must be unique and immutable
# for example
dict = {'affan': 'oneplus', 'sadullah': 'samsung', 'sayeed': 'iphone'}

print(dict.keys())  # it will print dict_keys(['affan', 'sadullah', 'sayeed'])

print(dict.values())
# it will print dict_values(['oneplus', 'samsung', 'iphone'])

print(dict.items())
# it will print dict_items([('affan', 'oneplus'), ('sadullah', 'samsung'), ('sayeed', 'iphone')])
# it will print dict_items([('affan', 'oneplus'), ('sadullah', 'samsung'), ('sayeed', 'iphone')])

print(type(dict))  # it will print <class 'dict'>

# it will print {'affan': 'oneplus', 'sadullah': 'samsung', 'sayeed': 'iphone'}
print(dict)

print(dict['affan'])  # it will print oneplus

print(dict['sadullah'])  # it will print samsung

# in dictionary or somewhere else also we can even use square brackets adn get() method to access the values in a dictionary
print(dict.get('sayeed'))  # it will print iphone

# we have different data types in python like int, float, str, bool, list, tuple, dict, set, NoneType etc

# like none, numeric, sequence: list, tuple, set string, range etc, and finally mapping:dictionary
