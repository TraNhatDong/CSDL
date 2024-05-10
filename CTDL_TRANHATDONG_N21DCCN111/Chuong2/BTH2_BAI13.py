def Nhan(a_sign, a_digits, b_sign, b_digits):
    a_str = ''.join(map(str, a_digits))
    b_str = ''.join(map(str, b_digits))
    result = int(a_str) * int(b_str)
    result_sign = a_sign ^ b_sign
    if result > 2147483647 or result < -2147483648:
        return [-1]
    if result_sign == 1:
        result = -result

    return result
a_sign = 0
a_digits = [1, 2, 3]
b_sign = 1
b_digits = [4, 5, 6]
print(Nhan(a_sign, a_digits, b_sign, b_digits))
