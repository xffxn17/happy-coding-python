# now learning tuple and sets in python
# for list we use [] but for tuple we use () and for sets we use {}
# tuples are immutable means we cannot change the values of tuple once it is created
# let's go for tuple
tup = (25, 9, 5, 66, 52, 4, 6)
print(tup)  # it will print entire tuple

# now lets access the tuple index
print(tup[0])  # it will print first element of tuple
print(tup[3])  # it will print 4th element of

# tup[0] = 45  # it will give error because tuple is immutable
# now lets go for sets
# print(tup[0])

# here tuple are faster than list because tuple are immutable

# now lets go for sets
sets = {25, 9, 5, 66, 52, 4, 6}  # for sets we use {}
print(sets)  # it will print entire sets

# now lets access the sets index
# print(sets[0])  # it will give error because sets are unordered

sets.add(45)  # it will add 45 to the sets
print(sets)  # it will print entire sets

sets.remove(5)  # it will remove 5 from the sets
print(sets)  # it will print entire sets tuple

# sets are unordered means we cannot access the elements of sets by index
# sets are mutable means we can change the values of sets once it is created
# sets are faster than list and tuple because sets are unordered
# sets do not allow duplicate values
# it will not add 25 to the sets because sets do not allow duplicate values
sets.add(25)
print(sets)  # it will print entire sets tuple

# sets are used to store multiple items in a single variable
# sets are used to perform mathematical set operations like union, intersection, difference, etc.
# sets are used to remove duplicate values from a list
# sets are used to check membership of an item in a collection
# sets are used to store unique values
# sets are used to store items that are not in a specific order
# sets are used to store items that are not indexed
# sets are used to store items that are not mutable
# sets are used to store items that are not hashable
# sets are used to store items that are not iterable
# sets are used to store items that are not comparable
# sets are used to store items that are not sortable
# sets are used to store items that are not searchable
# sets are used to store items that are not filterable
# sets are used to store items that are not groupable
# sets are used to store items that are not aggregatable
# sets are used to store items that are not joinable
# sets are used to store items that are not unionable
# sets are used to store items that are not intersectable
# sets are used to store items that are not differenciable
# sets are used to store items that are not symmetric differenciable
# sets are used to store items that are not reflexive
# sets are used to store items that are not transitive
# sets are used to store items that are not antisymmetric
# sets are used to store items that are not equivalence relation
# sets are used to store items that are not partial order
# sets are used to store items that are not total order
# sets are used to store items that are not well order
# sets are used to store items that are not dense order
# sets are used to store items that are not linear order
# sets are used to store items that are not lattice
