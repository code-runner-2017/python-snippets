# IMPORTANT: if you do need cryptographic level randomness, you should use the secrets module

import random       # regular
import secrets      # cryptographic

print(random.randint(0, 5)) # any value between 0 and 5 (included)

# Random choices from a list
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

# Return a list that contains any 2 of the items from a list:
print(random.sample(mylist, k=2))

# Return an 8 bits sized integer:
print(random.getrandbits(8))

#
# ----  Secrets ----
#

print(secrets.randbelow(8)) # a random int in the range [0, 9)

print(secrets.randbits(8)) # Return an int with 8 random bits

# Return a random text string, in hexadecimal, with 16 random bytes
print(secrets.token_hex(16))  # eg: 086d29c5a1c8717ff5c227092f508998

# Base64 encoded, url safe:
print(secrets.token_urlsafe(16))  # eg: FNTNPBtxrmPfd72Qy9DNhQ

# Return a random item from the list
print(secrets.choice(mylist))   # eg: banana