# Count letters in string
# https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d/python

def letter_count(s):
    new_dict = {}
    for i in s:
        if i not in new_dict:
            print(i)
            new_dict.update({i:1})
        elif i in new_dict:
            new_dict[i] += 1
    return new_dict