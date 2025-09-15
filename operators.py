'''# operators in python
# arithmetic operators
# +, -, *, /, %, //, **
# comparison operators
# ==, !=, >, <, >=, <=
# assignment operators
# =, +=, -=, *=, /=, %=, //=, **=
# logical operators
# and, or, not
# bitwise operators
# &, |, ^, ~, <<, >>
# membership operators
# in, not in
# identity operators
# is, is not
# operator precedence
# parentheses, exponentiation, multiplication/division, addition/subtraction, comparison, logical, assignment
# operator associativity
# left to right, right to left
# operator overloading
# custom behavior for operators based on operand types
# examples(multiple line of comments can be written using triple quotes in starting and ending)'''

# lets goooooo
x = 10
y = 3
print("Arithmetic Operators")
print("x + y =", x + y)  # addition
print("x - y =", x - y)  # subtraction
print("x * y =", x * y)  # multiplication
print("x / y =", x / y)  # division
print("x % y =", x % y)  # modulus
print("x // y =", x // y)  # floor division
print("x ** y =", x ** y)  # exponentiation

# now arithmetic shortcuts

# x = x + 2 making it comment because it will change the value of x
# print(x)  # it will print 12

# now
x += 2
print(x)  # it will print 12

# now same we can do for other arithmetic operators like subtraction, multiplication, division, modulus, floor division, exponentiation

x -= 2
print(x)  # it will print 10

x *= 2
print(x)  # it will print 20

x /= 2
print(x)  # it will print 10.0

x %= 3
print(x)  # it will print 1.0

x //= 2
print(x)  # it will print 0.0

x **= 2
print(x)  # it will print 0.0
# the x values are changing at every arithmetic operation from above

# we can assign values in one line also like this

a, b = 4, 6  # assigning 4 to a and 6 to b in one line

print("a =", a)  # like other languages ex c or c++ we dont need to give space after = in printing area like above and below python automatically gives space

print('b =', b)

'''now'''
n = 7
print(-n)  # it will print -7

# now if we print n it will print 7 because -n is not changing the value of n
print(n)  # it will print 7

# now doing something crazy
n = -n
print(n)  # it will print -7

# now we are checking the bool and comparison
a = 4
b = 7
print(a < b)  # it will print true
print(a > b)  # it will print false

# now for comparison we use == symbol
print(a == b)  # it will print false

# now for not equal to we use != symbol
print(a != b)  # it will print true

# now lets check logical operators

print(a < 5 and b > 6)  # it will print false

print(a < 5 and b < 6)  # it will print true

print(a < 5 or b > 6)  # it will print true

print(a < 5 or b < 6)  # it will print true

# now not operators in python
x = True
print(x)  # it will print true
print(not x)  # it will print false

# like that only lets make x false
x = False
print(x)  # it will print false now
print(not x)  # it will print true
