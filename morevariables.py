# lets learn more variables in python

num = 10  # integer variable

print(num)  # it will print the value of the variable num
print(id(num))  # it will print the memory address of the variable num
print(type(num))  # it will print the data type of the variable num

# now lets assign a a value to b

a = 10  # assigning value 10 to a
b = a  # assigning value of a to b

print(a)  # it will print the value of a
print(id(a))  # it will print the memory address of a

print(b)  # it will print the value of b
print(id(b))  # it will print the memory address of b

# both a and b have same value and same memory address because both are pointing to same value in memory. as in python both same values assigned to different variables will point to same memory location to save memory

# in our program there is a,b,num all pointing to same value 10 in memory so all have same memory address.

print(id(10))  # it will print the memory address of value 10 in memory
# it will be same as memory address of a,b,num because all are pointing to same value 10 in memory

# now lets change the value of a

a = 20  # changing the value of a to 20

print(a)  # it will print the value of a

print(id(a))  # it will print the memory address of a

# lets se the id of b right now
print(b)  # it will print the value of b
print(id(b))  # it will print the memory address of b
# it will be same as before because we have not changed the value of b

# now lets assign the value of a to b again which is now a=20
b = a  # assigning value of a to b

print(b)  # it will print the value of b

print(id(b))  # it will print the memory address of b
