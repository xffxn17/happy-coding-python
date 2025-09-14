# continuation of dictionary in this file
prog = {'js': 'Atom', 'cs': 'vs', 'python': [
    "pycharm", "sublime"], 'java': {"jse": "netbeans", 'jee': 'eclipse'}}
# in this dictionary we have a list and another dictionary as values

print(prog)  # it will print the whole dictionary

print(prog["python"])  # it will print the list of python ide

print(prog["java"])  # it will print the dictionary of java ide

# it will print the value of key jse in the dictionary of java
print(prog["java"]["jse"])
# it will print the value of key python in the list of python ide
print(prog["python"][0])
# we can have any data type as value in the dictionary
# we can have list, dictionary, tuple, set, integer, float, string etc as value in the dictionary
# but keys must be immutable data type like string, integer, float, tuple etc
# we cannot have list or dictionary or set as key in the dictionary because they are mutable data type
# because mutable data type can be changed but immutable data type cannot be changed
# therefore we can have only immutable data type as key in the dictionary
# also keys must be unique in the dictionary because if we have duplicate keys then only the last key will be considered
