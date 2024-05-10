def Hieu(a, b):
    set_b = set(b)
    c = [x for x in a if x not in set_b]
    c = list(set(c))
    c.sort()
    return c
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b)
print(c)
