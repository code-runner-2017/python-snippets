for x in range(5):
    print(x)

count = 0

while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

