def Cong(a_sign, a_digits, b_sign, b_digits):
    a_int = int(''.join(map(str, a_digits))) * (-1 if a_sign == 1 else 1)
    b_int = int(''.join(map(str, b_digits))) * (-1 if b_sign == 1 else 1)
    result = a_int + b_int
    if result > 2147483647 or result < -2147483648:
        return [-1]

    return result
a_sign = 0
a_digits = [1, 2, 3]
b_sign = 1  # Số âm
b_digits = [4, 5, 6]
print(Cong(a_sign, a_digits, b_sign, b_digits))  # Kết quả sẽ là 123 + (-456)
