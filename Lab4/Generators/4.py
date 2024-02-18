a = int(input())
b = int(input())
def func(a, b):
    for x in range(a, b+1):
        yield x**2

for i in func(a, b):
    print(i)