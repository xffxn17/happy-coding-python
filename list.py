nums = [25, 9, 5, 66, 52, 4, 6]
print(nums)  # print entire list
print(nums[0])  # print first element
print(nums[-1])  # print last element
print(nums[0:5])  # print elements from index 0 to 4
print(nums[2:])  # print elements from index 2 to end
# now names
names = ["Affan", "Amman", "Tuba Firdous", "Obaid ur Rahman"]
print(names)  # it will prints names
both = [nums, names]  # list inside list
print(both)  # it will print both lists
print(both[0])  # it will print first list
print(both[1])  # it will print second list
print(both[0][1])  # it will print second element of first list
print(both[1][2])  # it will print third element of second list
# list methods
nums.append(45)  # it will add 45 at the end of list
print(nums)  # it will print updated list

nums.insert(4, 18)  # it will add 18 at index 4
print(nums)  # it will print updated list

nums.remove(9)  # it will remove 9 from list without giving index value
print(nums)  # it will print updated list

nums.pop(1)  # it will remove element at index 1, here value is not given
print(nums)  # it will print updated list

nums.pop()  # it will remove last element of list
print(nums)  # it will print updated list

del nums[2]  # it will delete element at index 2
print(nums)  # it will print updated list

del nums[3:]  # it will delete elements from index 2 to end
print(nums)  # it will print updated list

nums.extend([45, 18, 17, 333])  # it will add multiple elements at end of list
print(nums)  # it will print updated list

print(nums.index(66))  # it will print index no. of 66 from the list

min(nums)  # it will print minimum value from the list
print(min(nums))  # it will print the minimum of the nums

max(nums)  # it will print maximum value from the list
print(max(nums))  # it will print the maximum value of the nums

# print(sum(nums))  # it will print sum of all elements of the list

nums.sort()  # it will sort the list in ascending order
# always first we have to sort it first than only we can print it in nums as nums will going to modify
print(nums)  # it will print updated list