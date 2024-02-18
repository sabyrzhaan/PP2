n = int(input())
def func(n):
    for x in range(n, -1, -1):
        yield x
for i in func(n):
    print(i)