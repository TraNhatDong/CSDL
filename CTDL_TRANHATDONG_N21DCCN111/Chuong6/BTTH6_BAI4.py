def Hop(a, b):
    c = list(set(a).union(set(b)))
    c.sort()
    return c
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hop(a, b)
print(c)
