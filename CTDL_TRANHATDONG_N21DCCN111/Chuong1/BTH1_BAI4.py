from math import factorial
n=int(input("Nhập n"))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(int(factorial(i)/((factorial(j))*factorial(i-j))),end=" ")
    print()
