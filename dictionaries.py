phonebook = {
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["John"] = 938477566

print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Remove an item
del phonebook["John"]

