def Tru(a_sign, a_digits, b_sign, b_digits):
    a_str = ''.join(map(str, a_digits))
    b_str = ''.join(map(str, b_digits))
    a_int = int(a_str) if a_sign == 0 else -int(a_str)
    b_int = int(b_str) if b_sign == 0 else -int(b_str)
    result = a_int - b_int
    if result > 2147483647 or result < -2147483648:
        return [-1]

    return result


a_sign = 0
a_digits = [1, 2, 3]
b_sign = 1
b_digits = [4, 5, 6]
print(Tru(a_sign, a_digits, b_sign, b_digits))
