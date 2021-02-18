import pathlib
import os

# writes a new file (use "a" for append)
f = open("output/sample-output.txt", "w")
f.write("Now the file has more content!\n")
f.write("and more...\n")
f.write("and more!\n")
f.close()

# open and read the file after the appending:
f = open("output/sample-output.txt", "r")
print(f.read())
f.close()

# loop for each line
f = open("output/sample-output.txt", "r")
for line in f:
  print("line: "+ line, end='')     # end='' to not print an additional newline. Default is env='\n'


f = pathlib.Path('output/example.txt')

f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print('read from open(): {!r}'.format(handle.read()))

print('read_text(): {!r}'.format(f.read_text('utf-8')))

# Delete a file

if os.path.exists("output/sample-output.txt"):
  os.remove("output/sample-output.txt")
else:
  print("The file does not exist")