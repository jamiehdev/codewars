# Array.diff
# https://www.codewars.com/kata/523f5d21c841566fde000009/python

def array_diff(a, b):
    occurences = []
    for i in a:
        if i not in b:
            occurences.append(i)
    return occurences


print(array_diff([1, 2], [1]))