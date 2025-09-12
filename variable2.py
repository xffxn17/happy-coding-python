# Assign a value to the variable 'name'
name = "celebrate"

# Print a message by joining two strings using +
# The space after "let's" ensures words don't run together
print("let's " + name)

# Change the value of 'name' to something else
name = "party"

# Print the new message with the updated value
print("let's " + name)

# Access the first character of the string using its index (starts at 0)
print(name[0])  # Output: 'p'

# Indexing starts at 0 and goes up to length-1
# For 'party', valid indexes are 0 to 4

# Trying to access an index outside the range will cause an error
# print(name[5])  # Uncommenting this line will cause IndexError

# Negative indexes count from the end of the string
print(name[-1])  # Output: 'y' (last character)
print(name[-5])  # Output: 'p' (first character)

# Slicing: Get a part of the string using [start:end]
print(name[0:2])  # Output: 'pa' (characters at index 0 and 1)
print(name[1:4])  # Output: 'art' (characters at index 1, 2, 3)

# If you leave out the end index, it goes to the end of the string
print(name[0:])   # Output: 'party'

# If you leave out the start index, it starts from the beginning
print(name[:4])   # Output: 'part' (index 0 to 3)

# Leaving out both gives the whole string
print(name[:])    # Output: 'party'

# If the end index is beyond the string length, it just goes to the end
print(name[2:10]) # Output: 'rty' (index 2 to end)

# Strings are immutable: you can't change characters directly
# The following lines would cause errors if uncommented:
# name[0:3] = "fun"
# name[0] = "F"

# To add something to a string, use + to join them
print("fun " + name)  # Output: 'fun party'