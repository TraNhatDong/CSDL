def Nhan(a, b):
    a_int = int(''.join(map(str, a)))
    b_int = int(''.join(map(str, b)))
    result = a_int * b_int
    if result > 2147483647 or result < -2147483648:
        return [-1]

    return result
a = [1, 2, 3]
b = [4, 5, 6]
print(Nhan(a, b))
