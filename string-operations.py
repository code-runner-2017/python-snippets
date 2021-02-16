astring = "Hello world!"
print(astring.index("o"))   # 4

print(astring[1])  # e

# slice of the string, starting at index 3, and ending at index 6
print(astring[3:7]) # lo w

# prints the characters of string from 3 to 7 skipping one character
# [start:stop:step]
print(astring[3:7:1])  # el

print(astring.upper())
print(astring.lower())

afewwords = astring.split(" ")
print(afewwords)    # ['Hello', 'world!']

