import re

file = open("row.txt")

row = file.read()

# Task1

result1 = re.findall(r'ab*', row)

# Task2

pattern = r'ab{2,3}'
result2 = re.findall(pattern, row)

# Task3

pattern = r'[a-z]+\_'
result3 = re.findall(pattern, row)

# Task4

pattern = r'[A-Z][a-z]+'
result4 = re.findall(pattern, row)

# Task5

pattern = r'a.+b$'
result5 = re.search(pattern, row)

# Task6

pattern = r'[ ,.]'
replace = ':'
result6 = re.sub(pattern, replace, row)

# Task7

pattern = r'_+(\w)'
def replace(match):
    return match.group(1).upper()
result7 = re.sub(pattern, replace, row)

# Task8

pattern = r'([a-z])([A-Z])'
result8 = re.sub(pattern, r'\1 \2', row)

# Task9

pattern = r'([a-z0-9])([A-Z])'
replace = r'\1 \2'
result9 = re.sub(pattern, replace, row)

# Task10

pattern = r'([a-z0-9])([A-Z])'
replace = r'\1_\2'
result10 = re.sub(pattern, replace, row)
answer10 = result10.lower()


def printing():
    print("Answer for Task 1:\n", result1)

    print("Answer for Task 2:\n", result2)

    print("Answer for Task 3:\n", result3)

    print("Answer for Task 4:\n", result4)

    print("Answer for Task 5:\n", result5)

    print("Answer for Task 6:\n", result6)

    print("Answer for Task 7:\n", result7)

    print("Answer for Task 8:\n", result8)

    print("Answer for Task 9:\n", result9)

    print("Answer for Task 10:\n", result10)

printing()