def do_stuff_with_number(n):
    print(n)

try:
    do_stuff_with_number(the_list[i])
except IndexError: # Raised when accessing a non-existing index of a list
    do_stuff_with_number(0)

