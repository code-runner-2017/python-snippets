thisset = {"apple", "banana", "cherry"}

# The value already exists => won't be added to the set
thisset.add("apple")
print(thisset) # {'cherry', 'banana', 'apple'}
print(len(thisset))   # 3