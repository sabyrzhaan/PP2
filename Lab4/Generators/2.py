n = int(input())
def func(n):
    for x in range(0, n+1, 2):
            yield x
for i in func(n):
    print(i, end = ' ')