s = input()

def func(s):
    y = ""
    for i in (reversed(s)):
        y += i

    if(s == y):
        return 1
    return 0

if(func(s)):
    print("Yes, it is palindrome")
else:
    print("No, it is NOT palindrome")