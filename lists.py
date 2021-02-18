# See also https://www.w3schools.com/python/python_lists_methods.asp

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# length
print(len(fruits))  # 5

# access 3rd element
print(fruits[3])  # kiwi

# position of an element
print(fruits.index("cherry")) # 2

# count occurrences
print(fruits.count("apple")) # 1

# List comprehension
# create a new list with all the fruits containing the letter 'a'
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']

# with upper()
newlist = [x.upper() for x in fruits]
print(newlist)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# if .. else: replace banana with orange
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# sorting
fruits.sort(reverse = True)
print(fruits) # ['mango', 'kiwi', 'cherry', 'banana', 'apple']

# list 0..9
newlist = [x for x in range(5)]
print(newlist)  # [0, 1, 2, 3, 4]

# Copy a list
fruits = ["apple", "banana", "cherry"]
mylist = fruits.copy()  # or mylist = list(fruits)

# Join lists
joinList = fruits + newlist
print(joinList) # ['apple', 'banana', 'cherry', 0, 1, 2, 3, 4]

# Extend an existing list
mylist.extend(newlist)
print(mylist) # ['apple', 'banana', 'cherry', 0, 1, 2, 3, 4]

# Remove an element
mylist.remove("banana")

# Remove all elements
mylist.clear()