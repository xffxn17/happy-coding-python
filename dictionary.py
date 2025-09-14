# Dictionary is a collection of key-value pairs
data = {1: "Affan", 2: "Amman", 4: "Obaid ur Rahman", 5: "Tuba"}

print(data)  # it will print whole dictionary

print(data[2])  # it will print value of key 2

# print(data[3])  # it will give error because 3 is not a key in the dictionary

print(data.get(5))  # it will print value of key 5

print(data.get(3))  # it will give None because 3 is not a key in the dictionary

# it will give Not Found because 3 is not a key in the dictionary
# therefore whenever for any key we can print our message for it if the key does not exist
print(data.get(3, "Not Found"))

print(data.keys())  # it will print all the keys of the dictionary

print(data.values())  # it will print all the values of the dictionary

# now lets merge two dictionaries
keys = ['affan', 'amman', 'obaid', 'tuba']  # list of keys
values = ['python', 'java', 'c++', 'c#']  # list of values
merged = dict(zip(keys, values))  # merging two lists into dictionary
# zip function will merge two lists into tuples and then dict function will convert those tuples into dictionary
print(merged)  # it will print the merged dictionary

print(merged['affan'])  # it will print value of key 'affan'
print(merged.get('amman'))  # it will print value of key 'amman'
# we can either use [] or get() to get the value of a key in the dictionary
# but if the key does not exist then [] will give error while get() will give None or our message

# now lets see how to add new key-value pair in the dictionary
merged['hammad'] = 'js'  # adding new key-value pair in the dictionary
print(merged)  # it will print the dictionary with new key-value pair

# now lets see how to remove key-value pair from the dictionary
# removing key-value pair from the dictionary using del keyword
del merged['hammad']

print(merged)  # it will print the dictionary without the removed key-value pair

# removing key-value pair from the dictionary using pop() method
# it will remove the key-value pair and return the value of the removed key
merged.pop('tuba')  # it will remove the key tuna from the merged.

print(merged)
