n = int(input())
def func(n):
    for x in range(1, n+1):
        if x**2>n:
            break
        yield x**2

for i in func(n):
    print(i)