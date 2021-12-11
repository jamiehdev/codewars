def queue_time(customers, n):
    l = [0] * n
    for i in customers:
        l.sort()
        l[0] += i
    l.sort()
    return l[-1]