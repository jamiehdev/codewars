# The Supermarket Queue
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/python

def queue_time(customers, n):
    l = [0] * n
    for i in customers:
        l.sort()
        l[0] += i
    l.sort()
    return l[-1]