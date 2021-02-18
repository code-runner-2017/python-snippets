x = lambda a : a + 10
print(x(5))   # 15

x = lambda a, b : a * b
print(x(5, 6))  # 30

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))  # 33