n = int(input())
def func(n):
    for x in range(n+1):
        if x%3==0 and x%4==0:
            yield x
for i in func(n):
    print(i)