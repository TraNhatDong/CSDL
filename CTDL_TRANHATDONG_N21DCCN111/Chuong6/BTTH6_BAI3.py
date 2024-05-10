def Giao(a, b):
    set_a = set(a)
    set_b = set(b)
    c = list(set_a & set_b)
    c.sort()
    return c
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)
