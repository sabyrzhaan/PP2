s = input()

def func(str):
    cnt = 0
    for i in str:
        if(i.isupper()):
            cnt += 1

    return cnt
uppercase_letters = func(s)
lowercase_letters = len(s) - uppercase_letters
print(uppercase_letters, lowercase_letters)