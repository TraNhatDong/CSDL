def Duynhat(a):
    b = list(set(a))
    b.sort()
    return b
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print(b)
