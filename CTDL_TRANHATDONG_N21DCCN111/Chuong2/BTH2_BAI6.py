def Tru(a, b):
    a_int = int(''.join(map(str, a)))
    b_int = int(''.join(map(str, b)))
    result = a_int - b_int

    return result
a = [1, 2, 3]
b = [1, 1, 1]
print(Tru(a, b))
